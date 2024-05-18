from nicegui import ui, run
from datetime import datetime
from typing import Literal
import time

SetupArgType = Literal["loop", "sleep"]

timer_label = ui.label()
ui.timer(1.0, lambda: timer_label.set_text(f"{datetime.now():%X}"))


def setup_runner(arg: SetupArgType):
    message = f"Starting task with {arg=}"
    print(message)
    ui.notify(message)
    # do some work
    time.sleep(5)
    message = f"Task with {arg=} finished"
    print(message)
    ui.notify(message)


async def setup_runner_async(arg: SetupArgType):
    await run.io_bound(setup_runner, arg)


ui.button("Setup runner", on_click=lambda: setup_runner("sleep"))
ui.button("Setup runner async", on_click=lambda: setup_runner_async("sleep"))

ui.run(reconnect_timeout=60)