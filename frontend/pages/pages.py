import math
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from typing import Dict, List, Tuple, Type, Union

from typing_extensions import Self

from backend.JarvisManager import JarvisManager
from frontend.custom_classes import EntryWithPlaceholder, ReorderableListbox


class BasePage(Toplevel, ABC):

    raw_title: str
    style: ttk.Style

    def __init__(self, manager: JarvisManager, master, **kwargs):
        Toplevel.__init__(self, master, **kwargs)
        ABC.__init__(self)
        self.manager = manager
        self.title(type(self).raw_title)
        self.style = ttk.Style(self)
        self.style.configure("basicFrame.TFrame",
                             foreground="white", background="#26343E")

        self.destroy_all_but_self()

    @abstractmethod
    def setup(self, **kwargs):
        return

    @classmethod
    def deploy(cls, manager, parent, **kwargs):
        return cls(manager, parent, **kwargs).setup(**kwargs)

    @classmethod
    def destroy_all(cls, root):
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == cls.raw_title:
                widget.destroy()

    



    def destroy_all_but_self(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == self.raw_title and widget != self:
                widget.destroy()


class MoveListPage(BasePage):

    raw_title = "Move List Page"
    displaymovebox: Listbox
    movelistlist: Dict[str, List[Label]]

    def setup(self, **kwargs):
        frame = ttk.Frame(self, style="basicFrame.TFrame")
        frame.grid(row=0, column=0, stick="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        m_frame = self.build_move_display(frame)

        m1_frame = self.build_list_display(frame)

        m2_frame= self.build_movelist_handler(frame, m1_frame)

        for iame in frame.winfo_children():
            iame.grid_configure(padx=10, pady=10)

    def add_move(self, name: str):
        if not any(nme == name for nme in self.displaymovebox.get(0, END)):
            self.displaymovebox.insert(END, name)
            
         

    def build_move_display(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame, style= "basicFrame.TFrame")
        child_frame.grid(column=0, row=0, sticky="nsew")

        move_label = ttk.Label(child_frame, text="Available moves")
        move_label.grid(column=0, row=0, sticky="nsew")

        self.displaymovebox = Listbox(child_frame, bg="grey")
        self.displaymovebox.grid(column=0, row=1, sticky="nsew")

        for mov in self.manager.brain.get_move_names():
            self.displaymovebox.insert(END, mov)

            
        add_moves = ttk.Button(child_frame, text="Add new moves",
                                command=lambda: ControlPage.deploy(self.manager, self.master))
        add_moves.grid(column=0, row=2, sticky="nsew")

        view_moves = ttk.Button(child_frame, text="View all moves",
                                command=lambda: PointsPage.deploy(self.manager, self.master))
        view_moves.grid(column=0, row=3, sticky="nsew")

        close_moves = ttk.Button(child_frame, text="Hide moves",
                                 command=lambda: PointsPage.destroy_all(self.master))
        close_moves.grid(column=0, row=4, sticky="nsew")

        for iame in child_frame.winfo_children():
            iame.grid_configure(pady=5)

        return child_frame

    def build_moveset_frame(self, name: str, moves: List[str], frame: ttk.Frame):
        child_frame = ttk.Frame(frame)
        child_frame.grid_rowconfigure(0, weight=1)
        child_frame.grid_columnconfigure(0, weight=1)

        little_frame = ttk.Frame(child_frame)
        little_frame.grid_rowconfigure(0, weight=1)
        little_frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(little_frame, text=name)
        label.grid(column=0, row=0, sticky="nsew")

        but = ttk.Button(little_frame, text="Perform",
                         command=lambda: self.manager.perform_movelist(name))
        but.grid(column=1, row=0, sticky="nsew")

        little_frame.grid(column=0, row=0, sticky="nsew")

        val = StringVar()
        submit_move_entry = EntryWithPlaceholder(
            child_frame, placeholder="Add point", textvariable=val)
        submit_move_entry.grid(column=0, row=1, sticky="nsew")
        submit_move_entry.grid_configure(pady=(0, 5))

        listbox = ReorderableListbox(child_frame,
                                     bg="grey")

        listbox.grid(column=0, row=2, sticky="nsew")

        for mov in moves:
            listbox.insert(END, mov)
        
        for iame in child_frame.winfo_children():
            iame.grid_configure(padx=5, pady=3)

        def add_to_moveset(event):
            tmp = submit_move_entry.get()
            assert self.manager.brain.has_move(
                tmp), "Unknown move: \"%s\". Cannot teach unknown moves." % tmp
            listbox.insert(0, tmp)
            save_moveset(event)

        def save_moveset(event):
            items: List[str] = listbox.get(0, END)
            self.manager.brain.teach_movelist(name, items)

        def delete_selected(event):
            items = listbox.curselection()
            for item in items:
                listbox.delete(item)
            save_moveset(event)

        submit_move_entry.bind("<Return>", func=add_to_moveset)
        listbox.bind("<Leave>", func=save_moveset)
        listbox.bind("<BackSpace>", func=delete_selected)
        return child_frame

    def _calc_col_and_row(self, index: int):
        return (math.floor(index / 3), index % 3)

    def build_list_display(self, frame: ttk.Frame):
        movelists_frame = ttk.Frame(frame, style="basicFrame.TFrame")
        movelists_frame.grid(column=1, row=0, sticky="nsew")
        movelists_frame.grid_rowconfigure(0, weight=1)
        movelists_frame.grid_columnconfigure(0, weight=1)

        c = 0
        r = 0
        for index, (key, val) in enumerate(self.manager.brain.get_movelists().items()):
            c, r = self._calc_col_and_row(index)
            child_frame = self.build_moveset_frame(key, val, movelists_frame)
            child_frame.grid(column=c, row=r, sticky='ns')
            child_frame.grid_configure(padx=5, pady=5)

        return movelists_frame

    def build_movelist_handler(self, master_frame: ttk.Frame, movelist_frame: ttk.Frame):
        child_frame = ttk.Frame(master_frame, style="basicFrame.TFrame")
        child_frame.grid(column=2, row=0, sticky="nsew")
        # child_frame.grid_rowconfigure(0, weight=1)
        # child_frame.grid_columnconfigure(0, weight=1)

        del_label = ttk.Label(child_frame, text="Delete movelist")
        del_label.grid(column=0, row=0, sticky="nsew")

        val = StringVar()
        del_entry = EntryWithPlaceholder(
            child_frame, placeholder="Movelist name", textvariable=val)
        del_entry.grid(column=0, row=1, sticky="nsew")

        def _find_container(event, name: str):
            containers: List[Frame] = []
            for child_frame in movelist_frame.winfo_children():
                for widget in child_frame.winfo_children():
                    if type(widget) == ttk.Frame:
                        for child_widgets in widget.winfo_children():
                            if type(child_widgets) == ttk.Label:
                                nme = child_widgets.cget("text")
                                if nme == name:
                                    containers.append(child_frame)  # type: ignore
            return containers

        def remove_movelist(event):
            wanted_del = val.get()

            containers = _find_container(event, wanted_del)

            for con in containers:
                col_con = con.grid_info()
                col_ind = col_con["column"] * 3 + col_con["row"]
                for child in con.winfo_children():
                    child.destroy()
                con.destroy()

                frames = [(frame, frame.grid_info())
                          for frame in movelist_frame.winfo_children()]
                for (frame, frame_info) in frames:
                    index = frame_info["column"] * 3 + frame_info["row"]
                    c, r = self._calc_col_and_row(index - 1)
                    if index > col_ind:
                        frame.grid(column=c, row=r)

            if (len(containers) > 0):
                self.manager.brain.forget_movelist(wanted_del)

        del_entry.bind("<Return>", func=remove_movelist)

        add_label = ttk.Label(child_frame, text="Add movelist")
        add_label.grid(column=0, row=2, sticky="nsew")

        val1 = StringVar()
        add_entry = EntryWithPlaceholder(
            child_frame, placeholder="Movelist name", textvariable=val1)
        add_entry.grid(column=0, row=3)

        def add_movelist(event):
            wanted_added = val1.get()
            containers = _find_container(event, wanted_added)

            if len(containers) > 0:
                raise AssertionError("fuck")

            index = max([frame.grid_info()["column"] * 3 + frame.grid_info()["row"]
                        for frame in movelist_frame.winfo_children()])
            c, r = self._calc_col_and_row(index + 1)
            ml_frame = self.build_moveset_frame(
                wanted_added, [], movelist_frame)
            ml_frame.grid(column=c, row=r)
            ml_frame.grid_configure(padx=5, pady=5)


            self.manager.brain.teach_movelist(wanted_added, [])

        add_entry.bind("<Return>", func=add_movelist)

        return child_frame


class ControlPage(BasePage):

    raw_title = "Control Page"
    slides: Dict[str, Scale]

    def setup(self, **kwargs):
        self.style.configure("sliderFrame.TFrame",
                             foreground="white", background="#26343E")
        self.style.configure("sliderFrame.TLabel",
                             foreground="white", background="#26343E")
        self.style.configure("sliderFrame.TButton", background="lime")
        self.style.configure("sliderFrame.Horizontal.TScale",
                             foreground="white", background="#26343E")

        self.slides = dict()
        frame = ttk.Frame(self, style="basicFrame.TFrame")
        frame.grid(row=0, column=0, stick="nsew")

        frame1 = self.build_motor_contol_panel(frame)

        frame2 = self.build_other_buttons(frame)

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def build_motor_button_set(self, frame_canvas: ttk.Frame, info: Tuple[str, List[float]],  c: int, r: int):
        val = IntVar()
        mini_frame = ttk.Frame(frame_canvas, style="sliderFrame.TFrame")
        mini_frame.grid(column=c, row=r, sticky="nsew")
        mini_frame.grid_columnconfigure(1, weight=1)

        lab = ttk.Label(mini_frame, style="sliderFrame.TLabel",
                        text=info[0] + ' Control')
        lab.grid(column=0, row=0, sticky="ns")

        display = ttk.Label(
            mini_frame, style="sliderFrame.TLabel", textvariable=val)
        display.grid(column=1, row=0, sticky="ns")

        def go_func():
            tmp = val.get()
            return self.manager.motors.move_motor(info[0], tmp)

        go_button = ttk.Button(
            mini_frame, style="sliderFrame.TButton", text="Go", command=go_func)
        go_button.grid(column=2, row=0, sticky="ns")

        def only_whole(e):
            value = slide.get()
            if int(value) != value:
                slide.set(round(value))

        slide = ttk.Scale(frame_canvas, style="sliderFrame.Horizontal.TScale",
                          length=300, from_=info[1][1], to=info[1][2], orient="horizontal", variable=val, command=only_whole)
        slide.set(info[1][3])
        slide.grid(column=c, row=r + 1, sticky="we", pady=(0, 10))
        self.slides[info[0]] = slide

    def build_motor_contol_panel(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame, style="basicFrame.TFrame")
        child_frame.grid(row=0, column=0, sticky='nw')
        child_frame.grid_rowconfigure(0, weight=1)
        child_frame.grid_columnconfigure(0, weight=1)

        col_count = 0
        row_count = 0
        index = 0

        for info in self.manager.motors.get_motor_info().items():
            if (index != 0 and index % 8 == 0):
                col_count += 3
                row_count = 0

            self.build_motor_button_set(
                child_frame, info, col_count, row_count)
            row_count += 2
            index += 1

        for irame in child_frame.winfo_children():
            irame.grid_configure(padx=5)

        return child_frame

    def _send_all_motors(self):
        for name in self.manager.motors.get_motor_names():
            assert self.slides[name]
            self.manager.motors.move_motor(name, int(self.slides[name].get()))

    def _return_all_slides_home(self):
        for info in self.manager.motors.get_motor_info().items():
            assert self.slides.get(
                info[0]), "The motor didn't have a respective slide."
            self.slides[info[0]].set(info[1][3])

    def _set_all_slides_to_point(self, point_name: str):
        pts = self.manager.brain.get_moves()
        assert pts.get(point_name), "The move requested doesn't exist."

        pt = pts[point_name]
        for index, name in enumerate(self.manager.motors.get_motor_names()):
            assert self.slides.get(name)
            self.slides[name].set(pt[index])

    def _teach_point(self, point_name: str):
        if (point_name == "Teach point"):
            return

        pts = []
        for slide in self.slides.values():
            pts.append(int(slide.get()))

        self.manager.brain.teach_movement(point_name, pts)

     
    def _del_point(self, point_name: str):
        if (point_name == "Delete point"):
            return
        
        pts = self.manager.brain.get_moves().get(point_name)
        if pts:  
            self.manager.brain.forget_move(point_name)
        cur = [g.get() for g in self.slides.values()]

        if pts == cur:
            self._return_all_slides_home()

    def build_other_buttons(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame, style="basicFrame.TFrame")
        child_frame.grid(row=0, column=2, sticky='ne')

        send_all_button = ttk.Button(
            child_frame, text="Send all motors", command=self._send_all_motors)
        send_all_button.grid(column=0, row=0, sticky="nsew")
        send_all_button.grid_configure(pady=10)

        goto_button = ttk.Button(child_frame, text="Goto point",
                                 command=lambda: self._set_all_slides_to_point(val.get()))
        goto_button.grid(column=0, row=1, sticky="nsew")
        goto_button.grid_configure(pady=(10, 0))

        val = StringVar()
        goto_entry = EntryWithPlaceholder(
            child_frame, placeholder="Goto point", textvariable=val)
        goto_entry.grid(column=0, row=2, sticky="nsew")
        goto_entry.grid_configure(pady=(0, 5))
        goto_entry.bind(
            "<Return>", func=lambda event: self._set_all_slides_to_point(val.get()))

        teach_button = ttk.Button(child_frame, text="Teach point",
                                  command=lambda: self._teach_point(val1.get()))
        teach_button.grid(column=0, row=3, sticky="nsew")
        teach_button.grid_configure(pady=(5, 0))

        val1 = StringVar()
        teach_entry = EntryWithPlaceholder(
            child_frame, placeholder="Teach point", textvariable=val1)
        teach_entry.grid(column=0, row=4, sticky="nsew")
        teach_entry.grid_configure(pady=(0, 5))
        teach_entry.bind(
            "<Return>", func=lambda event: self._teach_point(val1.get()))
        

        del_button = ttk.Button(child_frame, text="Delete point",
                                  command=lambda: self._del_point(val2.get()))
        del_button.grid(column=0, row=5, sticky="nsew")
        del_button.grid_configure(pady=(5, 0))


        val2 = StringVar()
        del_entry = EntryWithPlaceholder(
            child_frame, placeholder="Delete point", textvariable=val2)
        del_entry.grid(column=0, row=6, sticky="nsew")
        del_entry.grid_configure(pady=(0, 5))
        del_entry.bind(
            "<Return>", func=lambda event: self._del_point(val2.get()))


        points_button = ttk.Button(child_frame, text="View all points",
                                   command=lambda: PointsPage.deploy(self.manager, self.master))
        points_button.grid(column=0, row=7, sticky="nsew")
        points_button.grid_configure(pady=(5, 10))

        reset_button = ttk.Button(
            child_frame, text="Return all to home", command=self._return_all_slides_home)
        reset_button.grid(column=0, row=8, sticky="nsew")
        reset_button.grid_configure(pady=(10, 0))

        return child_frame


class ProgramPage(BasePage):

    raw_title = "Program Page"

    def setup(self, **kwargs):
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, stick="nsew")
        ttk.Button(frame, text="Program").grid(column=0, row=0, sticky="we")


class PointsPage(BasePage):

    raw_title = "Points Page"

    points: List[Tuple[StringVar, StringVar]]
    button_frame: ttk.Frame

    def setup(self, **kwargs):
        self.points = []
        points = self.manager.brain.get_moves()

        for (key, val) in points.items():
            self.points.append(
                (StringVar(value=key), StringVar(value=str(val))))

        # frame = ttk.Frame(self)
        # frame.grid(row=0, column=0, stick="nsew")

        frame_main = ttk.Frame(self)
        frame_main.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = ttk.Frame(frame_main)
        frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        button_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=button_frame, anchor='nw')
        buttons = []
        for index, (key, val) in enumerate(self.points):
            buttons.append([ttk.Label(button_frame, textvariable=key),
                           ttk.Label(button_frame, textvariable=val)])
            buttons[index][0].grid(row=index, column=0, sticky='news')
            buttons[index][1].grid(row=index, column=1, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        button_frame.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        col_w = max([buttons[index][0].winfo_width() + buttons[index]
                    [1].winfo_width() for index in range(len(self.points))])
        col_h = sum([max([buttons[index][0].winfo_height(), buttons[index]
                    [1].winfo_height()]) for index in range(len(self.points))])

        for child in button_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        frame_canvas.config(width=col_w + vsb.winfo_width() + 15,
                            height=col_h + 10 * len(self.points))

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))
