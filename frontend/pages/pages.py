import math
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from typing import Dict, List, Optional, Tuple, Union

from backend.JarvisManager import JarvisManager
from custom_types import MotorInfo
from frontend.custom_classes import EntryWithPlaceholder, ReorderableListbox
from frontend.custom_classes.style import Style


class BasePage(Toplevel, ABC):

    destroy_others: bool = True
    raw_title: str
    style: Style

    def __init__(self, manager: JarvisManager, master: Union[Misc, None] = None, **kwargs):
        Toplevel.__init__(self, master, **kwargs)
        ABC.__init__(self)
        self.manager = manager

        self.title(type(self).raw_title)
        self.style = Style(self)
        self.style.configure("basicFrame.TFrame",
                             foreground="white", background="#26343E")
        self.style.configure("basicFrame.TLabel",
                             foreground="white", background="#26343E")
        
        if type(self).destroy_others:
            self.destroy_all_but_self()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    @abstractmethod
    def setup(self, **kwargs):
        return

    @classmethod
    def deploy(cls, manager, parent, **kwargs):
        return cls(manager, parent).setup(**kwargs)

    @classmethod
    def destroy_all(cls, root):
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == cls.raw_title:
                widget.destroy()

    def destroy_all_but_self(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == self.raw_title and widget != self:
                widget.destroy()

    def display_error(self, msg: Union[Exception, str]):
        if type(msg) == Exception:
            msg = str(msg) 
            
        tmp = Toplevel(self)
        tmp.title("Error!")
        tmp.bind("<Return>", lambda event: tmp.destroy())

        frame = ttk.Frame(tmp, style="basicFrame.TFrame")
        frame.grid(column=0, row=0, sticky="nsew")

        ttk.Label(frame, text=msg, style="basicFrame.TLabel").grid(column=0, row=0) # type: ignore
        ttk.Button(frame, text="Close", command= lambda: tmp.destroy()).grid(column=0, row=1)

        for iame in frame.winfo_children():
            iame.grid_configure(padx=5, pady=5)


def _find_container(name: str, frame_to_search: ttk.Frame):
    containers: List[Frame] = []
    for child_frame in frame_to_search.winfo_children():
        for widget in child_frame.winfo_children():
            if type(widget) == ttk.Label:
                nme = widget.cget("text")
                if nme == name:
                    containers.append(child_frame)  # type: ignore

    return containers



class AdminPromptPage(BasePage):
    raw_title = "Admin Prompt Page"

    def setup(self, **kwargs):
        self.password = "InMoov"

        self.style.configure("adminPromptPage.TFrame", background="#26343E")
        top_frame = ttk.Frame(self, style="basicFrame.TFrame")
        top_frame.grid(column=0, row=0, sticky="nsew")

        
        label = ttk.Label(top_frame, text="Enter admin password", style="basicFrame.TLabel").grid(column=0, row=0)
        entry = ttk.Entry(top_frame)
        entry.bind("<Return>", lambda event: self.check_entry(entry, entry.get()))
        entry.grid(column=0, row=1)

        for iame in top_frame.winfo_children():
            iame.grid_configure(padx=5, pady=5)


    def check_entry(self, entry: ttk.Entry, pas: str):
        entry.delete(0, END)
        if pas == self.password:
            AdminPromptPage.destroy_all(self.master)
            AdminPage.deploy(self.manager, self.master)
        else:
            self.display_error("Invalid password!")
   


        


        




class AdminPage(BasePage):
    raw_title = "Admin Page"

    def setup(self, **kwargs):
        top_frame = ttk.Frame(self, style="basicFrame.TFrame")
        top_frame.grid(column=0, row=0, sticky="nsew")

        
        # top_frame.grid_columnconfigure(5, weight=1)
        self.build_shit(top_frame)

        children = top_frame.winfo_children()
        for iame in children:
            iame.grid_configure(padx=5, pady=(5, 0))

        children[-1].grid_configure(pady=5)

        

    def build_button(self, parent_frame: ttk.Frame, index: int, name: str, info: MotorInfo):
        ttk.Label(parent_frame, text=info[4], style="basicFrame.TLabel").grid(column=0, row=index + 1)
        l1 = ttk.Entry(parent_frame)
        l1.insert(0, str(info[1]))
        l1.grid(column=1, row=index + 1)
        l1.bind("<Return>", lambda event: self.manager.motors.set_motor_config(name, "min", int(l1.get())))

        l2 = ttk.Entry(parent_frame)
        l2.insert(0, str(info[2]))
        l2.grid(column=2, row=index + 1)
        l2.bind("<Return>", lambda event: self.manager.motors.set_motor_config(name, "max", int(l2.get())))

        l3 = ttk.Entry(parent_frame)
        l3.insert(0, str(info[3]))
        l3.grid(column=3, row=index + 1)
        l3.bind("<Return>", lambda event: self.manager.motors.set_motor_config(name, "home", int(l3.get())))

                 
    def build_lock(self, parent_frame: ttk.Frame, index: int, name: str):


        def lock_func():
            new_bool = not locked_str.get() == 'True'
            locked_str.set(str(new_bool))

            self.manager.motors.lock_motor(name, new_bool)


        locked_str = StringVar(parent_frame, value=str(self.manager.motors.get_motor_locked(name)))

        ttk.Button(parent_frame, text="Lockout", command=lock_func) \
            .grid(column=4, row = index + 1)
        
        ttk.Label(parent_frame, textvariable=locked_str, style="basicFrame.TLabel") \
            .grid(column=5, row = index + 1)
        
 
    def build_shit(self, parent_frame: ttk.Frame):

        ttk.Label(parent_frame, text="Minimums", style="basicFrame.TLabel") \
                .grid(column=1, row=0)
        ttk.Label(parent_frame, text="Maximums", style="basicFrame.TLabel") \
                .grid(column=2, row=0)
        ttk.Label(parent_frame, text="Home Values", style="basicFrame.TLabel") \
                .grid(column=3, row=0)

        ttk.Label(parent_frame, text="Maintence Lockouts", style="basicFrame.TLabel") \
                .grid(column=4, row=0, columnspan=2)
        

        for index, (name, info) in enumerate(self.manager.motors.get_motor_info().items()):
            self.build_button(parent_frame, index, name, info)
            self.build_lock(parent_frame, index, name)
           



   
            
     
         



class MoveListPage(BasePage):
    raw_title = "Move List Page"
    displaymovebox: Listbox
    movelistlist: Dict[str, List[Label]]

    def setup(self, **kwargs):
        top_frame = ttk.Frame(self, style="basicFrame.TFrame")
        top_frame.grid(row=0, column=0, sticky="nsew")

        for i in range(3):
            top_frame.grid_rowconfigure(i, weight=1)
            top_frame.grid_columnconfigure(i, weight=1)

        leftside_f = ttk.Frame(top_frame, style="basicFrame.TFrame")
        leftside_f.grid(column=0, row=0)

        self.populate_leftside(leftside_f)

        middle_f = ttk.Frame(top_frame)
        middle_f.grid(column=1, row=0)

        self.populate_middle(middle_f)

        rightside_f = ttk.Frame(top_frame)
        rightside_f.grid(column=2, row=0)

        self.populate_rightside(rightside_f, middle_f)


        for iame in top_frame.winfo_children():
            iame.grid_configure(padx=10, pady=10)

    def _calc_col_and_row(self, index: int):
        return (math.floor(index / 3), index % 3)
    

    def add_move(self, name: str):
        if not any(nme == name for nme in self.displaymovebox.get(0, END)):
            self.displaymovebox.insert(END, name)


    def _delete_movelist(self, wanted_del: str, frame_to_search: ttk.Frame, entry: Optional[Entry] = None):
        containers = _find_container(wanted_del, frame_to_search)

        if (len(containers) == 0):
            if entry:
                entry.delete(0, END)
            self.display_error(f"Couldn't find movelist \"{wanted_del}\".")
   
        for con in containers: 
            col_con = con.grid_info()
            col_ind = col_con["column"] * 3 + col_con["row"]
            for child in con.winfo_children():
                child.destroy()
            con.grid_remove()
            con.destroy()

            frames = [(frame, frame.grid_info()) for frame in frame_to_search.winfo_children()]
            for (frame, frame_info) in frames:
                index = frame_info["column"] * 3 + frame_info["row"]
                c, r = self._calc_col_and_row(index - 1)
                if index > col_ind:
                    frame.grid(column=c, row=r)

        if (len(containers) > 0):
            self.manager.brain.forget_movelist(wanted_del)

    def _add_movelist(self, wanted_added: str, frame_to_search: ttk.Frame, entry: Optional[Entry] = None):
        containers = _find_container(wanted_added, frame_to_search)

        if len(containers) > 0:
            self.display_error("Move already exists")
            if entry:
                entry.delete(0, END)
            return


        if len(frame_to_search.winfo_children()) > 0:
            index = max([frame.grid_info()["column"] * 3 + frame.grid_info()["row"]
                        for frame in frame_to_search.winfo_children()])
        else:
            index = -1
        c, r = self._calc_col_and_row(index + 1)
        ml_frame = self.construct_movelist_frame(wanted_added, [], frame_to_search)
        ml_frame.grid(column=c, row=r)
        ml_frame.grid_configure(padx=5, pady=5)

        try:
            self.manager.brain.teach_movelist(wanted_added, [])
        except Exception as e:
            self.display_error(e)


    def construct_movelist_frame(self, name: str, moves: List[str], parent_frame: ttk.Frame):
        
        def save_moveset(event, box: Optional[Listbox] = None):
            items: List[str] = movebox.get(0, END)
            for mov in items:
                if not self.manager.brain.has_move(mov):
                    self.manager.brain.remove_move_from_movelist(name, mov)
                    if box:
                        box.delete(box.get(0, END).index(mov))
            try:
                self.manager.brain.teach_movelist(name, items)
            except Exception as e:
                self.display_error(e)

                        
 
        def add_to_moveset(event: Event, entry: Entry):
            tmp = insert.get()
            entry.delete(0, END)
            if not self.manager.brain.has_move(tmp):
                self.display_error("Invalid move.")
            else:
                movebox.insert(END, tmp)
                save_moveset(event)

        def delete_selected(event):
            items = movebox.curselection()
            for item in items:
                movebox.delete(item)
            save_moveset(event)
        
        movelist_frame = ttk.Frame(parent_frame)

        ttk.Label(movelist_frame, text=name) \
            .grid(column=0, row=0)
        

        val = StringVar()
        insert = EntryWithPlaceholder(movelist_frame, placeholder="Add move", textvariable=val)

        insert.grid(column=0, row=1, columnspan=2, sticky="nsew")
        insert.grid_configure(pady=(0, 5))

        insert.bind("<Return>", func=lambda event: add_to_moveset(event, insert))
        insert.bind
 
        movebox = ReorderableListbox(movelist_frame)
        movebox.grid(column=0, row=2, columnspan=2, sticky="nsew")

        for mov in moves:
            movebox.insert(END, mov)

        movebox.bind("<Leave>", func=lambda event: save_moveset(event, movebox))
        movebox.bind("<BackSpace>", func=delete_selected)


        button_ml_f = ttk.Frame(movelist_frame)
        button_ml_f.grid(column=1, row=0)

        but = ttk.Button(button_ml_f, text="Perform",
                         command=lambda: self.manager.perform_movelist(name))
        but.grid(column=0, row=0)

        but1 = ttk.Button(button_ml_f, text="Delete", command = lambda: self._delete_movelist(name, parent_frame))
        but1.grid(column=1, row=0)

        return movelist_frame
    

    def populate_leftside(self, frame: ttk.Frame):

        def get_moves(event):
            self.displaymovebox.delete(0, END)
            for mov in self.manager.brain.get_move_names():
                self.displaymovebox.insert(END, mov)

        move_label = ttk.Label(frame, text="Available moves")
        move_label.grid(column=0, row=0, sticky="nsew")
        move_label.bind("<Leave>", get_moves)
        move_label.bind("<Enter>", get_moves)

        self.displaymovebox = Listbox(frame, bg="grey")
        self.displaymovebox.grid(column=0, row=1, sticky="nsew")

        for mov in self.manager.brain.get_move_names():
            self.displaymovebox.insert(END, mov)

        add_moves = ttk.Button(frame, text="Add new moves",
                               command=lambda: ControlPage.deploy(self.manager, self.master))
        add_moves.grid(column=0, row=2, sticky="nsew")

        view_moves = ttk.Button(frame, text="View all moves",
                                command=lambda: PointsPage.deploy(self.manager, self.master))
        view_moves.grid(column=0, row=3, sticky="nsew")

        close_moves = ttk.Button(frame, text="Hide moves",
                                 command=lambda: PointsPage.destroy_all(self.master))
        close_moves.grid(column=0, row=4, sticky="nsew")

        for iame in frame.winfo_children():
            iame.grid_configure(pady=5)

    def populate_middle(self, frame: ttk.Frame):
        c = 0
        r = 0
        for index, (key, val) in enumerate(self.manager.brain.get_movelists().items()):
            c, r = self._calc_col_and_row(index)
            child_frame = self.construct_movelist_frame(key, val, frame)
            child_frame.grid(column=c, row=r)
            child_frame.grid_configure(padx=5, pady=5)
    

    def populate_rightside(self, frame: ttk.Frame, frame_to_search: ttk.Frame):
        del_label = ttk.Label(frame, text="Delete movelist")
        del_label.grid(column=0, row=0, sticky="nsew")

        val = StringVar()
        del_entry = EntryWithPlaceholder(
            frame, placeholder="Movelist name", textvariable=val)
        del_entry.grid(column=0, row=1, sticky="nsew")

        del_entry.bind("<Return>", func=lambda event: self._delete_movelist(val.get(), frame_to_search, del_entry))

        add_label = ttk.Label(frame, text="Add movelist")
        add_label.grid(column=0, row=2, sticky="nsew")

        val1 = StringVar()
        add_entry = EntryWithPlaceholder(
            frame, placeholder="Movelist name", textvariable=val1)
        add_entry.grid(column=0, row=3)

        add_entry.bind("<Return>", func=lambda event: self._add_movelist(val1.get(), frame_to_search, add_entry))


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

    def build_motor_button_set(self, frame_canvas: ttk.Frame, info: Tuple[str, MotorInfo],  c: int, r: int):
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
            try:
                self.manager.motors.move_motor(info[0], tmp)
            except Exception as e:
                self.display_error(e)

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

    def _set_all_slides_to_point(self, point_name: str, entry: Entry):
        pts = self.manager.brain.get_moves()

        if not pts.get(point_name):
            self.display_error(f"Point \"{point_name}\" doesn't exist.")
            return
        
        pt = pts[point_name]
        for index, name in enumerate(self.manager.motors.get_motor_names()):
            assert self.slides.get(name)
            self.slides[name].set(pt[index])

        entry.delete(0, END)

    def _teach_point(self, point_name: str, entry: Entry):
        if (point_name == "Teach point"):
            return

        pts = []
        for slide in self.slides.values():
            pts.append(int(slide.get()))

        self.manager.brain.teach_movement(point_name, pts)

        entry.delete(0, END)

    def _del_point(self, point_name: str, entry: Entry):
        if (point_name == "Delete point"):
            return

        pts = self.manager.brain.get_moves().get(point_name)
        if pts:
            self.manager.brain.forget_move(point_name)
        else:
            self.display_error(f"Point \"{point_name}\" doesn't exist.")
        cur = [g.get() for g in self.slides.values()]

        if pts == cur:
            self._return_all_slides_home()

        entry.delete(0, END)

    def build_other_buttons(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame, style="basicFrame.TFrame")
        child_frame.grid(row=0, column=2, sticky='ne')

        send_all_button = ttk.Button(
            child_frame, text="Send all motors", command=self._send_all_motors)
        send_all_button.grid(column=0, row=0, sticky="nsew")
        send_all_button.grid_configure(pady=10)

        goto_button = ttk.Button(child_frame, text="Goto point",
                                 command=lambda: self._set_all_slides_to_point(val.get(), goto_entry))
        goto_button.grid(column=0, row=1, sticky="nsew")
        goto_button.grid_configure(pady=(10, 0))

        val = StringVar()
        goto_entry = EntryWithPlaceholder(
            child_frame, placeholder="Goto point", textvariable=val)
        goto_entry.grid(column=0, row=2, sticky="nsew")
        goto_entry.grid_configure(pady=(0, 5))
        goto_entry.bind(
            "<Return>", func=lambda event: self._set_all_slides_to_point(val.get(), goto_entry))

        teach_button = ttk.Button(child_frame, text="Teach point",
                                  command=lambda: self._teach_point(val1.get(), teach_entry))
        teach_button.grid(column=0, row=3, sticky="nsew")
        teach_button.grid_configure(pady=(5, 0))

        val1 = StringVar()
        teach_entry = EntryWithPlaceholder(
            child_frame, placeholder="Teach point", textvariable=val1)
        teach_entry.grid(column=0, row=4, sticky="nsew")
        teach_entry.grid_configure(pady=(0, 5))
        teach_entry.bind(
            "<Return>", func=lambda event: self._teach_point(val1.get(), teach_entry))

        del_button = ttk.Button(child_frame, text="Delete point",
                                command=lambda: self._del_point(val2.get(), del_entry))
        del_button.grid(column=0, row=5, sticky="nsew")
        del_button.grid_configure(pady=(5, 0))

        val2 = StringVar()
        del_entry = EntryWithPlaceholder(
            child_frame, placeholder="Delete point", textvariable=val2)
        del_entry.grid(column=0, row=6, sticky="nsew")
        del_entry.grid_configure(pady=(0, 5))
        del_entry.bind(
            "<Return>", func=lambda event: self._del_point(val2.get(), del_entry))

        points_button = ttk.Button(child_frame, text="View all points",
                                   command=lambda: PointsPage.deploy(self.manager, self.master))
        points_button.grid(column=0, row=7, sticky="nsew")
        points_button.grid_configure(pady=(5, 10))

        reset_button = ttk.Button(
            child_frame, text="Return all to home", command=self._return_all_slides_home)
        reset_button.grid(column=0, row=8, sticky="nsew")
        reset_button.grid_configure(pady=(10, 0))

        return child_frame

    

class PointsPage(BasePage):

    raw_title = "Points Page"

    points: List[Tuple[StringVar, StringVar]]
    button_frame: ttk.Frame

    def setup(self, **kwargs):
        self.points = []
        points = self.manager.brain.get_moves()

        top_frame = ttk.Frame(self, style="basicFrame.TFrame")
        top_frame.grid(column=0, row=0)

        canvas=Canvas(top_frame, background="#26343E", width=800,height=200)
        canvas.grid(column=0, row=0)
 
    
        
        def build_thing(name: str, info: List[int], x: int, y: int):
            def click_pt(event):
                PointPage.deploy(self.manager, self, name=name, point=info)
            id1= canvas.create_text(0, y, text=name, activefill="red", fill="white")
            id2= canvas.create_text(400, y, text=str(info), activefill="red", fill="white")
            canvas.tag_bind(id1, "<Button-1>", click_pt)
            canvas.tag_bind(id2, "<Button-1>", click_pt)
            ids.append((id1, id2))

        
     
        y = 0
        ids = []
        for index, (name, info) in enumerate(points.items()):
            build_thing(name, info, index, y)
            y+= 30

        # canvas.update_idletasks()

        bar = ttk.Scrollbar(top_frame)
        bar.config(command=canvas.yview)
        bar.grid(column=1, row=0, sticky="nsew")


        maxwidth = max([canvas.bbox(child[1])[2] - canvas.bbox(child[0])[0] for child in ids])

        canvas.config(width=maxwidth + 20, yscrollcommand=bar.set, scrollregion=canvas.bbox("all"))


    def _delete_move(self, name: str):
        try:
            self.manager.brain.forget_move(name)
        except Exception as e:
            self.display_error(e)


class PointPage(BasePage):

    raw_title = "Single Point Details"

    def setup(self, name: str, point: List[int], **kwargs):
        top_frame = ttk.Frame(self, style="basicFrame.TFrame")
        top_frame.grid(column=0, row=0, sticky="nsew")
        top_frame.grid_columnconfigure(0, weight=1)

        self.style.configure("pointPage.TLabel", font=(None, 22), extends="basicFrame.TLabel")

        
        ttk.Label(top_frame, text=name, style="pointPage.TLabel") \
            .grid(column=0, row=0, columnspan=2, sticky="we")
        
        ttk.Button(top_frame, text="Close", command = lambda: self.destroy()) \
            .grid(column=0, row=1, columnspan=2, sticky="we")
        
        for index, (pt, name) in enumerate(zip(point, self.manager.motors.get_motor_full_names()), 2):

            ttk.Label(top_frame, text=name, style="basicFrame.TLabel") \
                    .grid(column=0, row=index, sticky="w")
            
            ttk.Label(top_frame, text=pt, style="basicFrame.TLabel") \
                    .grid(column=1, row=index, sticky="e")
            
        for iame in top_frame.winfo_children():
            iame.grid_configure(padx=5, pady=5)




        



