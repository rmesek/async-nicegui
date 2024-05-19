from nicegui import ui
from engine import Engine
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from my_button import MyButton


class Runner:
    def __init__(self, button, label):
        self.my_button: MyButton = button
        self.label: ui.label = label
        self.my_task = Engine()
        self.task_running = False

    def run_loop(self):
        result = self.my_task.my_task_loop()
        with self.label:
            self.label.set_text(result)

    def run_sleep(self):
        result = self.my_task.my_task_sleep(10)
        with self.label:
            self.label.set_text(result)

    def stop(self): ...

    def handle_callback(self, task_type: str):
        with self.my_button.button:
            ui.notify("Handling callback!")
        with self.label:
            self.label.set_text("Handling callback!")

        if task_type == "loop":
            self.run_loop()
        else:
            self.run_sleep()

        with self.my_button.button:
            ui.notify("Callback handled!")
