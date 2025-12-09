from datetime import datetime
from typing import TypedDict
from enum import Enum

class Status(str, Enum):
    TO_DO = "to-do"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class Task(TypedDict):
    description: str
    status: Status
    created_at: str
    updated_at: str

def add(text: str, data: dict[str, Task]) -> str:
    id = int(max(data.keys(), default=0)) + 1
    time_fmt = datetime.now().strftime("%Y-%m-%d %H:%M")
    data[id] = Task(description=text, status=Status.TO_DO,
                    created_at=time_fmt, updated_at=time_fmt)
    return "Entry added successfully."

def remove(id: int, data: dict[str, Task]) -> str:
    if str(id) not in data:
        return "No such entry."
    del data[str(id)]
    return "The entry has been removed."

def update(id: int, text: str, data: dict[str, Task]) -> str:
    if str(id) not in data:
        return "No such entry."
    data[str(id)]["description"] = text
    data[str(id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return "Description updated successfully."

def set_status(id: int, status: Status, data: dict[str, Task]) -> str:
    if str(id) not in data:
        return "No such entry."
    data[str(id)]["status"] = status
    data[str(id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return "Status has been updated."

def list_entries(status: Status | None, data: dict[str, Task]) -> str:
    if not data:
        return "There are no entries."
    entries: list[str] = []
    if status is not None:
        for id, task in data.items():
            if task["status"] == status:
                entries.append(f"{id}: \"{task["description"]}\"\nStatus: {task["status"]}\
                                \nCreated at {task["created_at"]}. Last modified at {task["updated_at"]}")
    else:
        for id, task in data.items():
            entries.append(f"{id}: \"{task["description"]}\"\nStatus: {task["status"]}\
                            \nCreated at {task["created_at"]}. Last modified at {task["updated_at"]}")
    if not entries:
        return "No such entries."
    return "\n\n".join(entries)
