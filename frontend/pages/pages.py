import functools
from abc import ABC, abstractmethod
from copy import deepcopy
from tkinter import *
from tkinter import ttk
from turtle import back
from typing import Dict, overload

from backend.JarvisManager import JarvisManager
from frontend.custom_classes.entries import EntryWithPlaceholder


class BasePage(Toplevel, ABC):

    def __init__(self, manager: JarvisManager, master, **kwargs):
        self.manager = manager
        super().__init__(master, **kwargs)
        # self.grid(column=0, row=0, sticky="nsew")

    @abstractmethod
    def setup(self, **kwargs):
        return

    @classmethod
    def deploy(cls, manager, parent, **kwargs):
        return cls(manager, parent, **kwargs).setup(**kwargs)


class ControlPage(BasePage):

    slides: dict[str, Scale]

    def setup(self, **kwargs):
        self.slides = dict()
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, stick="nsew")
        self.build_motor_contol_panel(frame)
        self.build_other_buttons(frame)

        
    def build_motor_button_set(self, frame_canvas: ttk.Frame, info: tuple[str, list[float]],  c: int, r: int):
            slide = Scale(frame_canvas, fg='white', bg='#26343E', label=info[0] +' Control',
                          width=20, length=300, from_=info[1][1], to=info[1][2], orient="horizontal")
            slide.grid(column=c, row=r, sticky="we")
            slide.set(info[1][3])

            def go_func():
                tmp = slide.get()
                return self.manager.motors.move_motor(info[0], tmp)

            self.slides[info[0]] = slide
            go_button = Button(frame_canvas, text="Go",command = go_func)
            go_button.grid(column=c + 1, row=r, sticky="we")

            
    def build_motor_contol_panel(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame)
        child_frame.grid(row=0, column=0, pady=(5, 0), sticky='nw')
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
            assert self.slides.get(info[0]), "Weird."
            self.slides[info[0]].set(info[1][3])

                
    def _set_all_slides_to_point(self, point_name: str):
        pts = self.manager.brain.get_moves()
        assert pts.get(point_name), "Weird."

        pt = pts[point_name]
        for index, name in enumerate(self.manager.motors.get_motor_names()):
            assert self.slides.get(name)
            self.slides[name].set(pt[index])
                


    def build_other_buttons(self, frame: ttk.Frame):
        child_frame = ttk.Frame(frame)
        child_frame.grid(row=0, column=1, pady=(0, 0), sticky='n')
        child_frame.grid_rowconfigure(0, weight=1)
        child_frame.grid_columnconfigure(0, weight=1)

        
        send_all_button = Button(child_frame, text = "Send all motors", command=self._send_all_motors)
        send_all_button.grid(column=0, row=0, sticky="nsew")
     
        val = StringVar()
        goto_entry = EntryWithPlaceholder(child_frame, placeholder="goto point", textvariable=val)
        goto_entry.grid(column=0, row=1, sticky="nsew")
        goto_entry.bind("<Return>", func = lambda test: self._set_all_slides_to_point(val.get()))

        goto_button = Button(child_frame, text = "Goto point", command=lambda: self._set_all_slides_to_point(val.get()))
        goto_button.grid(column=0, row=2, sticky="nsew")

        reset_button = Button(child_frame, text = "Return all to home", command=self._return_all_slides_home)
        reset_button.grid(column=0, row=3, sticky="nsew")

        for child in child_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


 



class ProgramPage(BasePage):

    def setup(self, **kwargs):
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, stick="nsew")
        Button(frame, text="Program").grid(column=0, row=0, sticky="we")


class PointsPage(BasePage):

    points: list[tuple[StringVar, StringVar]]
    button_frame: Frame

    def setup(self, **kwargs):
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
        frame_canvas = Frame(frame_main)
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
                            height=col_h + 50 * len(self.points))

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))
