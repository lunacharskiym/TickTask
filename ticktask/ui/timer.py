from datetime import timedelta

from textual.widget import Widget
from rich.text import Text
from rich.progress_bar import ProgressBar

from ticktask.ui.custom_bar import CustomProgressBar

class TimerPanel(Widget):

    can_focus = True

    def __init__(self, work_time=15, rest_time=5):
        self.work_time = work_time
        self.rest_time = rest_time
        self.prev_mode_time = 1
        self.mode = "Stint"
        self.prev_mode = "RestLap"
        self.remaining_seconds = work_time
        self.running = False;
        super().__init__(id="timer")


    def render(self):

        bar = CustomProgressBar(
            percent=self.remaining_seconds / self._get_mode_time(),
            color=self._get_bar_color(),
            width=70,
            char_full="█",
            char_empty="░",
        ).render()

        time_str = str(timedelta(seconds=self.remaining_seconds)) + '/' + str(timedelta(seconds=self._get_mode_time())) 

        return Text.assemble(
            Text(self.mode + '\n', style=self._get_bar_color()),
            bar,
            Text(time_str + '\n', style=self._get_bar_color()),
        )
#       return Text(f"{self.remaining_seconds = }\n{self.mode = }\n{self.running = }")

    def _get_bar_color(self) -> str:

        return {
            "Stint": "green",
            "RestLap": "cyan",
            "Paused": "yellow"
        }.get(self.mode, "white")

    def _get_mode_time(self) -> str:

        return {
            "Stint" : self.work_time ,
            "RestLap" : self.rest_time,
            "Paused" : self.prev_mode_time,
        }.get(self.mode, 0)


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
            self.remaining_seconds = self.rest_time
        else:
            self.mode = "Stint"
            self.remaining_seconds = self.work_time

    def pause_timer(self):
        if self.mode != "Paused":
            self.prev_mode = self.mode
            self.prev_mode_time = self._get_mode_time()
            self.running = False
            self.mode = "Paused"
        else:
            self.running = True
            self.mode = self.prev_mode 

    def reset_timer(self):
        self.running = False
        self.remaining_seconds = self.work_time 
        self.mode = "Stint"
    
    def on_key(self, event):
        if event.key == "space":
            self.pause_timer()
            self.refresh()
        if event.key == 'r':
            self.reset_timer()
            self.refresh()


