from nicegui import ui, run
from datetime import datetime
from typing import Literal
import asyncio

from runner import Runner
from my_button import MyButton

SetupArgType = Literal["loop", "sleep"]


async def notify_task_running():
    print("Task already running!")
    with ui_element:
        ui.notify("Task already running!")


def setup_runner(arg: SetupArgType):
    async def handle_click():
        if lock.locked():
            await notify_task_running()
            return
        async with lock:
            await run.io_bound(runner.handle_callback, arg)
            # await asyncio.to_thread(runner.handle_callback, arg)

    ui.notify(f"Runner setup with [{arg=}]!")
    runner = Runner(my_button, label)
    my_button.click_callback = lambda: asyncio.create_task(handle_click())


lock = asyncio.Lock()
ui_element = ui.element()
timer_label = ui.label()
my_button = MyButton()
ui.timer(1.0, lambda: timer_label.set_text(f"{datetime.now():%X}"))
label = ui.label("My label!")
ui.button("Setup runner", on_click=lambda: setup_runner("sleep"))

ui.run(reconnect_timeout=60)


# def single_task(func):
#     """Decorator to prevent multiple tasks from running at the same time."""

#     async def wrapper(*args, **kwargs):
#         if wrapper.task_running:
#             print("Task already running!")
#             with ui_element:
#                 ui.notify("Task already running!")
#             return
#         wrapper.task_running = True
#         try:
#             return await func(*args, **kwargs)
#         finally:
#             wrapper.task_running = False

#     wrapper.task_running = False
#     return wrapper
