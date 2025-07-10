from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Task:
    id: str
    title: str
    stints: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def create(title: str, stints: int) -> "Task":
        return Task(id=str(uuid.uuid4()), title=title, stints=stints)

    def toggle_completed(self):
        self.completed = not self.completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "stints": self.stints,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            id=data["id"],
            title=data["title"],
            stints=data["stints"],
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"]),
        )

            



