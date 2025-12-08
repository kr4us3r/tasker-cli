from datetime import datetime

def add(text: str, data: dict) -> None:
    id = int(max(data.keys(), default=0)) + 1
    time_fmt = datetime.now().strftime("%Y-%m-%d %H:%M")
    data[id] = {"description": text,
                 "status": "to-do",
                 "createdAt": time_fmt,
                 "updatedAt": time_fmt}
    print("Entry added successfully.")

def remove(id: str, data: dict) -> None:
    if id not in data:
        print("No such entry.")
        return
    del data[id]
    print("The entry has been removed.")
            
def set_status(status: str, id: str, data: dict) -> None:
    if id not in data:
        print("No such entry.")
        return
    data[id]["status"] = status
    data[id]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Status has been updated.")

def list_entries(data: dict) -> None:
    if not data:
        print("There are no entries.")
        return
    for k, v in data.items():
        print(f"{k}: \"{v["description"]}\"\nStatus: {v["status"]}\
              \nCreated at {v["createdAt"]}. Last modified at {v["updatedAt"]}\n")