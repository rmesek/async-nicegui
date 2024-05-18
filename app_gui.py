from nicegui import ui
from datetime import datetime
from typing import Literal

from runner import Runner
from my_button import MyButton

timer_label = ui.label()
ui.timer(1.0, lambda: timer_label.set_text(f"{datetime.now():%X}"))

setup_button = ui.button("Setup runner")
button = MyButton()
label = ui.label("My label!")


def setup_runner(arg: Literal["loop", "sleep"]):
    # label.update()
    ui.notify(f"Starting task with {arg=}")
    runner = Runner(button, label)
    button.click_callback = lambda: runner.handle_callback(arg)


setup_button.on_click(lambda: setup_runner("sleep"))

# TODO: Not a fix! This is a workaround!
ui.run(reconnect_timeout=60)
