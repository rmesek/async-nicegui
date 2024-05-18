from engine import Engine
from typing import TYPE_CHECKING

# if TYPE_CHECKING:
from nicegui import ui


class Runner:
    def __init__(self, button, label):
        self.button = button
        self.label: ui.label = label
        self.my_task = Engine()

    def run_loop(self):
        result = self.my_task.my_task_loop()
        self.label.set_text(result)

    def run_sleep(self) -> str:
        result = self.my_task.my_task_sleep(10)
        self.label.set_text(result)

    def stop(self): ...

    def handle_callback(self):
        ui.notify("Handling callback!")
        self.run_sleep()
