from datetime import timedelta
from dataclasses import dataclass


@dataclass
class TimerMode:
    name: str
    duration: int
    color: str

WORKMODE = TimerMode("Stint", 2 * 60, "green")
RESTMODE = TimerMode("RestLap", 1 * 60, "yellow")


class Timer:

    def __init__(self):
        self.modes = [WORKMODE, RESTMODE] 
        self.current_mode_index = 0
        self.remaining_seconds = self.current_mode().duration
        self.running = False

    def current_mode(self) -> TimerMode:
        return self.modes[self.current_mode_index]
    
    def toggle(self) -> None:
        self.running = not self.running

    def tick(self) -> bool:
        if self.running:
            self.remaining_seconds -= 1
            if self.remaining_seconds <= 0:
                self.switch_mode()
                return True
        return False

    def switch_mode(self):
        self.current_mode_index = (self.current_mode_index + 1) % len(self.modes)
        self.remaining_seconds = self.current_mode().duration

    def reset(self):
        self.remaining_seconds = self.current_mode().duration
        self.running = False
