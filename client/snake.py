from typing import List, Tuple

class SnakePart:
    
    def __init__(self, x:int, y:int ) -> None:
        self.x = x
        self.y = y
        self.next_part = None
        self.previous_part = None

class Snake:
    def __init__(self, x: int, y: int, length: int) -> None:
        self._head = SnakePart(x,y)
        self.direction = 0
        self._tail = self._head

        current_part: SnakePart = self._head
        for i in range(1,length):
            prev_part = SnakePart(x-i, y)
            current_part.previous_part = prev_part #type: ignore
            prev_part.next_part = current_part #type: ignore
            current_part = prev_part
            self._tail = prev_part
        
  

    def move(self, grow: bool = False) -> None:
        if(grow):
            part = SnakePart(self._head.x, self._head.y)
            if(self.direction == 0):
                self._head.y -= 1
            elif(self.direction == 1):
                self._head.x += 1
            elif(self.direction == 2):
                self._head.y += 1
            elif(self.direction == 3):
                self._head.x -=1
            part.previous_part = self._head.previous_part
            part.previous_part.next_part = part #type: ignore
            part.next_part = self._head #type: ignore
            self._head.previous_part = part #type: ignore

        current_part: SnakePart = self._tail
        while current_part != None:
            if(current_part.next_part != None):
                current_part.x = current_part.next_part.x
                current_part.y = current_part.next_part.y
            else:
                if(self.direction == 0):
                    current_part.y -= 1
                elif(self.direction == 1):
                    current_part.x += 1
                elif(self.direction == 2):
                    current_part.y += 1
                elif(self.direction == 3):
                    current_part.x -=1
            current_part = current_part.next_part #type: ignore

    def get_part_positions(self) -> List[Tuple[int, int]]:
        positions = []
        current_part: SnakePart = self._tail
        while current_part != None:
            positions.append((current_part.x, current_part.y))
            if current_part.next_part != None:
                current_part = current_part.next_part
            else:
                break
        return positions
