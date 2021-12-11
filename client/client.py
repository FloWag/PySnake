from typing import Tuple
from client.gui_manager import GUIManager
import random

from client.snake import Snake

class Client:

    _gui_manager: GUIManager
    _snake: Snake
    _apple: Tuple[int, int]
    _max_x: int = 20
    _max_y: int = 20

    _score: int = 3

    def __init__(self) -> None:
        pass

    def start(self) -> None:
        print("starting client ...")
        self._snake = Snake(10,10,self._score)

        self._apple = (8,8)

        self._gui_manager = GUIManager(40,self._max_x, self._max_y)
        self._gui_manager.add_keyboard_listener(self.on_key_press)

        
        self._gui_manager.render(self._snake.get_part_positions(), self._apple)
        print(self._snake.get_part_positions())

        from client.game_loop import GameLoop
        self.game_loop = GameLoop(speed= 0.3, client=self)
        self.game_loop.start()
        self._gui_manager.mainloop()
        self.game_loop.running = False

    def update(self) -> None:
        self._snake.move()
        grow:bool = self._snake._head.x == self._apple[0] and self._snake._head.y == self._apple[1]
        if(grow):
            self._snake.move(grow=True)
            self._apple = (random.randint(1,self._max_x),random.randint(1,self._max_y))
            self._score += 1
        
        if(len(self._snake.get_part_positions()) > len(set(self._snake.get_part_positions()))):
            print(f"Game Over: Du hast dich selbt gegessen")
            print(f"Dein Score: {self._score}")
            self.game_loop.running = False
        if(self._snake._head.x < 1 or self._snake._head.x > self._max_x):
            self.game_loop.running = False
            print(f"Game Over: out of bounds")
            print(f"Dein Score: {self._score}")
        if(self._snake._head.y < 1 or self._snake._head.y > self._max_y):
            self.game_loop.running = False
            print(f"Game Over: out of bounds")
            print(f"Dein Score: {self._score}")



    def render(self) -> None:
        self._gui_manager.render(self._snake.get_part_positions(), self._apple)

    def on_key_press(self,event) -> None:
        if(event.keysym == "Up" and self._snake.direction != 2):
            self._snake.direction = 0
        elif(event.keysym == "Right" and self._snake.direction != 3):
            self._snake.direction = 1
        elif(event.keysym == "Down" and self._snake.direction != 0):
            self._snake.direction = 2
        elif(event.keysym == "Left" and self._snake.direction != 1):
            self._snake.direction = 3
