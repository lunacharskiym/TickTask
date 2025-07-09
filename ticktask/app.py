from textual.app import App, ComposeResult
from textual.widgets import Footer
from ticktask.ui.timer import TimerPanel
from ticktask.ui.task_bar import TaskBar 
from ticktask.ui.notes_area import NotesArea 
from ticktask.ui.dynamic_footer import DynamicFooter 


class TicktaskApp(App):
    
    CSS_PATH = "../assets/ticktask.css"

    BINDINGS = [("tab", "focus_next", "Переключить панель")]

    def __init__(self):
        super().__init__()
        self.focus_index = 0
        self.panels = []

    def compose(self) -> ComposeResult:
        """ """
        timer = TimerPanel()
        task_list = TaskBar()
        notes_area = NotesArea()
        self.footer = DynamicFooter(id="footer")
        self.panels = [timer, task_list, notes_area]
        yield timer 
        yield task_list
        yield notes_area
        yield self.footer 

    def action_focus_next(self):
        self.focus_index = (self.focus_index + 1) % len(self.panels)
        panel = self.panels[self.focus_index]
        self.set_focus(panel)
        self.footer.set_panel(panel.id)

    async def on_mount(self) -> None:
        self.set_focus(self.panels[0])

        self.footer.set_panel(self.panels[0].id)

    



if __name__ == "__main__":
    app = TicktaskApp()
    app.run()
