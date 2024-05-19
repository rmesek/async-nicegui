from nicegui import ui


class MyButton:
    def __init__(self) -> None:
        self.click_callback = None
        self.button = ui.button("Click me")
        self.button.on_click(self.handle_click)

    def set_callback(self, callback):
        self.click_callback = callback

    def handle_click(self):
        # ui.notify('Button clicked!')
        if self.click_callback is not None:
            self.click_callback()
        else:
            ui.notify("No callback set!")
