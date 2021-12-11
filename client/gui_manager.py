from tkinter import *
from typing import List, Tuple

class GUIManager:

    _window: Tk
    _canvas: Canvas

    _grid_pixels: int
    _width: int
    _height: int

    _snake_color: str = "blue"
    _apple_color: str = "green"


    def __init__(self, grid_pixels:int, width:int, height: int) -> None:
        self._width = width
        self._height = height
        self._grid_pixels = grid_pixels
        window_width: int = (grid_pixels * width)
        window_height: int = (grid_pixels * height)
        self._window = Tk(className="Snake", screenName="Snake")
        self._window.geometry(f"{window_width}x{window_height}")
        self._canvas = Canvas(self._window, bg="white", height=window_height, width=window_width)
        self._canvas.pack()
        self._draw_grid()
        self._window.eval("tk::PlaceWindow . center")

    def add_keyboard_listener(self, event_handler) -> None:
        self._window.bind("<KeyPress>", event_handler)

    def _draw_grid(self) -> None:
        # draw vertical grid lines
        for i in range(self._width -1):
            x: int = (i+1) * self._grid_pixels
            y1: int = 0
            y2: int = self._height * self._grid_pixels
            self._canvas.create_line(x,y1,x,y2, fill="silver")
        # draw horizontal grid lines
        for i in range(self._height -1):
            y: int = (i+1) * self._grid_pixels
            x1: int = 0
            x2: int = self._width * self._grid_pixels
            self._canvas.create_line(x1,y, x2,y, fill="silver")

    def render(self, snake: List[Tuple[int, int]], apple: Tuple[int, int]) -> None:
        self._canvas.delete("all")
        self._draw_grid()
        for (x,y) in snake:
            self._fill_field(x,y, self._snake_color)
        self._fill_field(apple[0], apple[1], self._apple_color)

    def _fill_field(self, x: int, y: int, color: str) -> None:
        x1: int = self._grid_pixels * (x-1)
        x2: int = self._grid_pixels * x
        y1: int = self._grid_pixels * (y-1)
        y2: int = self._grid_pixels * y
        self._canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def close(self) -> None:
        self._window.destroy()

    def mainloop(self) -> None:
        self._window.mainloop()