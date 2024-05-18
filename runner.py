from nicegui import ui
import asyncio
from engine import Engine


class Runner:
    def __init__(self, button, label):
        self.button = button
        self.label: ui.label = label
        self.my_task = Engine()
        self.task_running = False

    async def run_loop(self):
        result = await asyncio.to_thread(self.my_task.my_task_loop)
        self.label.set_text(result)

    async def run_sleep(self):
        result = await asyncio.to_thread(self.my_task.my_task_sleep, 10)
        self.label.set_text(result)

    def stop(self): ...

    async def handle_callback(self, task_type: str):
        if self.task_running:
            ui.notify("Task already running!")
            return
        ui.notify("Handling callback!")
        self.label.set_text("Handling click!")

        self.task_running = True
        try:
            if task_type == "loop":
                await self.run_loop()
            else:
                await self.run_sleep()
        finally:
            self.task_running = False
