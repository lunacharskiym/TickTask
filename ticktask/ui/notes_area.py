from textual.widget import Widget
from rich.text import Text

class NotesArea(Widget):

    can_focus = True

    def __init__(self):
        super().__init__(id="notesarea")

    def render(self):
        return Text(f"notes area placeholder")
