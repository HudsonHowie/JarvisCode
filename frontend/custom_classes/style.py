import tkinter as tk
import tkinter.ttk as ttk


class Style(ttk.Style):
    EXTENDS = 'extends'

    def __init__(self, parent):
        super().__init__(parent)
        self._style = {}

    def configure(self, cls, **kwargs):
        self._style.setdefault(cls, {}).update(kwargs)

        extends = self._style.get(kwargs.get(Style.EXTENDS), {})
        super().configure(cls, **extends)

        super().configure(cls, **kwargs)