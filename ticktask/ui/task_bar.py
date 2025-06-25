from textual.widget import Widget
from rich.text import Text

class TaskBar(Widget):

    can_focus = True

    def __init__(self):
        super().__init__(id="taskbar")

    def render(self):
        return Text(f"taskbar placeholder")
