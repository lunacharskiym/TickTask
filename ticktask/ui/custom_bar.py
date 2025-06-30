from rich.text import Text

class CustomProgressBar:
    def __init__(
        self,
        percent: float,
        width: int = 30,
        height: int = 1,
        color: str = "green",
        char_full: str = "█",
        char_empty: str = "░",
    ):
        self.percent = max(0.0, min(1.0, percent))
        self.width = width
        self.height = height
        self.color = color
        self.char_full = char_full
        self.char_empty = char_empty

    def render(self) -> Text:
        filled_len = int(self.width * self.percent)
        empty_len = self.width - filled_len

        line = self.char_full * filled_len + self.char_empty * empty_len

        text = Text(line + '\n', style=self.color)

#       for _ in range(self.height):
#           text.append(line + '\n', style=self.color)

        return text

    
