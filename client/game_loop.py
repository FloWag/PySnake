import threading
import time

import client.client as client

class GameLoop (threading.Thread):

    _client: client.Client
    _speed: float
    _running: bool = True

    def __init__(self, speed:float, client: client.Client):
        threading.Thread.__init__(self)
        self._speed = speed
        self._client = client

    def run(self):
        while self._running:
            self._client.update()
            self._client.render()
            time.sleep(self._speed)

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self._running = value