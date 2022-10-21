import functools
from abc import ABC, abstractclassmethod, abstractmethod
from copy import deepcopy
from tkinter import *
from tkinter import ttk
from turtle import back
from typing import Dict, overload

from backend.JarvisManager import JarvisManager
from frontend.custom_classes.entries import EntryWithPlaceholder


class BasePage(Toplevel, ABC):

    raw_title: str

    def __init__(self, manager: JarvisManager, master, **kwargs):
        super().__init__(master, **kwargs)
        self.manager = manager
        self.destroy_all_but_self()
      
    @abstractmethod
    def setup(self, **kwargs):
        return
    
    @classmethod
    def destroy_all(cls, root):
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == cls.raw_title:
                widget.destroy()


    @classmethod
    def deploy(cls, manager, parent, **kwargs):
        return cls(manager, parent, **kwargs).setup(**kwargs)
    

    def destroy_all_but_self(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, Toplevel) and widget.title() == self.raw_title and widget != self:
                widget.destroy()


class ControlPage(BasePage):

    raw_title = "Control Page"
    slides: dict[str, Scale]

    def setup(self, **kwargs):
        self.wm_title(ControlPage.raw_title)
        self.slides = dict()
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, stick="nsew")
        self.build_motor_contol_panel(frame)
        self.build_other_buttons(frame)

        
 
    def build_motor_button_set(self, frame_canvas: ttk.Frame, info: tuple[str, list[float]],  c: int, r: int):
            slide = Scale(frame_canvas, fg='white', bg='#26343E', label=info[0] + ' Control',
                          width=20, length=300, from_=info[1][1], to=info[1][2], orient="horizontal")
            slide.grid(column=c, row=r, sticky="we")
            slide.set(info[1][3])

            def go_func():
                tmp = slide.get()
                return self.manager.motors.move_motor(info[0], tmp)

            self.slides[info[0]] = slide
            go_button = Button(frame_canvas, text="Go",command = go_func)
            go_button.grid(column=c + 1, row=r, sticky="nsew")

            
    def build_motor_contol_panel(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame)
        child_frame.grid(row=0, column=0, sticky='nw')
        child_frame.grid_rowconfigure(0, weight=1)
        child_frame.grid_columnconfigure(0, weight=1)
 
        col_count = 0
        row_count = 0
        index = 0

        for info in self.manager.motors.get_motor_info().items():
            if (index != 0 and index % 8 == 0):
                col_count += 2
                row_count = 0

            self.build_motor_button_set(child_frame, info, col_count, row_count)
            row_count += 1
            index += 1

    
    def _send_all_motors(self):
        for name in self.manager.motors.get_motor_names():
            assert self.slides[name]
            self.manager.motors.move_motor(name, self.slides[name].get())

            
    def _return_all_slides_home(self):
        for info in self.manager.motors.get_motor_info().items():
            assert self.slides.get(info[0]), "The motor didn't have a respective slide."
            self.slides[info[0]].set(info[1][3])

                
    def _set_all_slides_to_point(self, point_name: str):
        pts = self.manager.brain.get_moves()
        assert pts.get(point_name), "The move requested doesn't exist."

        pt = pts[point_name]
        for index, name in enumerate(self.manager.motors.get_motor_names()):
            assert self.slides.get(name)
            self.slides[name].set(pt[index])

    def _teach_point(self, point_name: str):
        pts = []
        for slide in self.slides.values():
            pts.append(slide.get())
        
        self.manager.brain.teach_movement(point_name, pts)


                


    def build_other_buttons(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame)
        child_frame.grid(row=0, column=2, sticky='ne')
        child_frame.grid_rowconfigure(0, weight=1)
        child_frame.grid_columnconfigure(0, weight=1)

        
        send_all_button = Button(child_frame, text = "Send all motors", command=self._send_all_motors)
        send_all_button.grid(column=0, row=0, sticky="nsew")
        send_all_button.grid_configure(pady=10)

        goto_button = Button(child_frame, text = "Goto point", command=lambda: self._set_all_slides_to_point(val.get()))
        goto_button.grid(column=0, row=1, sticky="nsew")
        goto_button.grid_configure(pady=(10, 0))

        val = StringVar()
        goto_entry = EntryWithPlaceholder(child_frame, placeholder="Goto point", textvariable=val)
        goto_entry.grid(column=0, row=2, sticky="nsew")
        goto_entry.grid_configure(pady=(0, 5))
        goto_entry.bind("<Return>", func = lambda event: self._set_all_slides_to_point(val.get()))

        teach_button = Button(child_frame, text = "Teach point", command=lambda: self._teach_point(val1.get()))
        teach_button.grid(column=0, row=3, sticky="nsew")
        teach_button.grid_configure(pady=(5, 0))

        val1 = StringVar()
        teach_entry = EntryWithPlaceholder(child_frame, placeholder="Teach point", textvariable=val1)
        teach_entry.grid(column=0, row=4, sticky="nsew")
        teach_entry.grid_configure(pady=(0, 5))
        teach_entry.bind("<Return>", func = lambda event: self._teach_point(val1.get()))

        points_button = Button(child_frame, text = "View all points", command=lambda: PointsPage.deploy(self.manager, self.master))
        points_button.grid(column=0, row=5, sticky="nsew")
        points_button.grid_configure(pady=(5, 10))

        
        reset_button = Button(child_frame, text = "Return all to home", command=self._return_all_slides_home)
        reset_button.grid(column=0, row=6, sticky="nsew")
        reset_button.grid_configure(pady=(10, 0))





 



class ProgramPage(BasePage):

    raw_title = "Program Page"

    def setup(self, **kwargs):
        self.wm_title(ProgramPage.raw_title)
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, stick="nsew")
        Button(frame, text="Program").grid(column=0, row=0, sticky="we")


class PointsPage(BasePage):

    raw_title = "Points Page"

    points: list[tuple[StringVar, StringVar]]
    button_frame: Frame

    def setup(self, **kwargs):
        self.wm_title(PointsPage.raw_title)
        self.points = []
        points = self.manager.brain.get_moves()

        for (key, val) in points.items():
            self.points.append(
                (StringVar(value=key), StringVar(value=str(val))))

        # frame = ttk.Frame(self)
        # frame.grid(row=0, column=0, stick="nsew")

        frame_main = Frame(self)
        frame_main.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = Frame(frame_main, bg='#26343E')
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
        button_frame = Frame(canvas)
        canvas.create_window((0, 0), window=button_frame, anchor='nw')
        buttons = []
        for index, (key, val) in enumerate(self.points):
            buttons.append([Label(button_frame, textvariable=key),
                           Label(button_frame, textvariable=val)])
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
