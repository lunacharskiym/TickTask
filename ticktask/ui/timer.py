from textual.widget import Widget
from rich.text import Text

class TimerPanel(Widget):

    can_focus = True

    def __init__(self):
        self.mode = "Stint"
        self.remaining_seconds = 5
        self.running = False;
        super().__init__(id="timer")

    def render(self):
        return Text(f"{self.remaining_seconds = }\n{self.mode = }\n{self.running = }")

    def on_mount(self):
        self.set_interval(1.0, self._tick)

    def _tick(self):
        if self.running:
            self.remaining_seconds -= 1
            self.refresh()
            if self.remaining_seconds == 0:
                self.switch_mode()

    def switch_mode(self):
        if self.mode == "Stint":
            self.mode = "RestLap"
            self.remaining_seconds = 3
        else:
            self.mode = "Stint"
            self.remaining_seconds = 5

    def toggle_timer(self):
        self.running = not self.running
    
    def on_key(self, event):
        if event.key == "space":
            self.toggle_timer()
            self.refresh()


