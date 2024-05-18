from nicegui import ui
from datetime import datetime

from runner import Runner
from my_button import MyButton

timer_label = ui.label()
ui.timer(1.0, lambda: timer_label.set_text(f"{datetime.now():%X}"))

setup_button = ui.button("Setup runner")
button = MyButton()
label = ui.label("My label!")
# button.on_click(lambda: label.set_text('Hello, world!'))


def setup_runner(arg):
    # label.update()
    ui.notify(f"Starting task with {arg=}")
    runner = Runner(button, label)
    button.click_callback = runner.handle_callback


setup_button.on_click(lambda _: setup_runner("my_arg"))

# TODO: Not a fix! This is a workaround!
ui.run(reconnect_timeout=60)
