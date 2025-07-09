from textual.widget import Widget
from textual.reactive import reactive
from textual import events
from rich.text import Text

from ticktask.engine.timer import Timer

from ticktask.ui.custom_bar import CustomProgressBar

class TimerPanel(Widget):

    can_focus = True

    def __init__(self):
        super().__init__(id="timer")
        self.timer = Timer()

    def on_mount(self) -> None:
        self.set_interval(1.0, self._on_tick)

    def _on_tick(self) -> None:
        switched = self.timer.tick()
        self.refresh()

    def render(self):
        bar = CustomProgressBar(
            percent=self.timer.remaining_seconds / self.timer.current_mode().duration,
            color=self.timer.current_mode().color,
            width=70,
            char_full="█",
            char_empty="░",
        ).render()

        text = Text.assemble(bar + '\n', str(self.timer.remaining_seconds) 
            + '/' + str(self.timer.current_mode().duration))
        # TODO: kinda unhandy to assemble progress bar + text like this
        # also should make function to format time (e.g 120 sec = 0:2:00)
        return text

    def on_key(self, event: events.Key) -> None:
        if event.key == "space":
            self.timer.toggle()
            self.refresh()
        elif event.key == "r":
            self.timer.reset()
            self.refresh() 


