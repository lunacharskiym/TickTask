from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import Static
from textual import events
from rich.text import Text

class DynamicFooter(Widget):
    active_panel_id = reactive("")

    panel_bindings = {
        "timer": [
            ("space", "Старт/Стоп"),
            ("r", "Сброс"),
            ("m", "Режим"),
        ],
        "tasks": [
            ("a", "Добавить задачу"),
            ("d", "Удалить"),
            ("e", "Редактировать"),
        ],
        "notes": [
            ("s", "Сохранить"),
            ("c", "Очистить"),
        ],
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render(self) -> Text:
        bindings = self.panel_bindings.get(self.active_panel_id, [])
        text = Text()
        for key, desc in bindings:
            text.append(f"[{key.upper()}] {desc}    ", style="bold")
        return text

    def set_panel(self, panel_id: str):
        self.active_panel_id = panel_id
        self.refresh()

