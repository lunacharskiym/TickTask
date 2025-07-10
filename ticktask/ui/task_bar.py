from textual.widget import Widget
from rich.text import Text

from ticktask.engine.task import Task

class TaskBar(Widget):

    can_focus = True

    def __init__(self):
        super().__init__(id="taskbar")
        self.tasks: list[Task] = []
        self.selected_index: int = 0

    def render(self):
        output = Text()

        for task in self.tasks:
            output.append(Text.assemble(task.id, " ", task.title, " ", task.stints))
            output.append(Text("\n__________________\n"))

        return output

    def add_task(self, title: str, stints: int = 1) -> None:
        ...

    def delete_selected(self) -> None:
        ...

    def edit_selected(self, new_title: str) -> None:
        ...

    def toggle_completed(self) -> None:
        ...

    def on_key(self, event: events.key) -> None:
        ...

