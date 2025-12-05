from datetime import datetime

def add(text: str, data: list) -> None:
    id = data[-1]["id"] + 1 if data else 1
    time_fmt = datetime.now().strftime("%Y-%m-%d %H:%M")
    data.append({"id": id,
                 "description": text,
                 "status": "to-do",
                 "createdAt": time_fmt,
                 "updatedAt": time_fmt})
    print("Entry added successfully.")

def remove(id: int, data: list) -> None:
    if (entry := get_entry_by_id(id, data)) is None:
        return
    data.remove(entry)
    print("The entry has been removed.")
            
def set_status(status: str, id: int, data: list) -> None:
    if (entry := get_entry_by_id(id, data)) is None:
        return
    entry["status"] = status
    entry["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Status has been updated.")

def list_entries(data: list) -> None:
    if not data:
        print("There are no entries.")
        return
    for e in data:
        print(f"{e["id"]}: \"{e["description"]}\"\nStatus: {e["status"]}\
              \nCreated at {e["createdAt"]}. Last modified at {e["updatedAt"]}\n")

def get_entry_by_id(id: int, data: list) -> dict | None:
    if id > 0:
        for item in data:
            if item["id"] == id:
                return item
    print("No such entry.")
    return None