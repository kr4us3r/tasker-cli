from datetime import datetime

def add(text: str, data: dict) -> None:
    id = int(max(data.keys(), default=0)) + 1
    time_fmt = datetime.now().strftime("%Y-%m-%d %H:%M")
    data[id] = {"description": text,
                 "status": "to-do",
                 "createdAt": time_fmt,
                 "updatedAt": time_fmt}
    print("Entry added successfully.")

def remove(id: int, data: dict) -> None:
    if str(id) not in data:
        print("No such entry.")
        return
    del data[str(id)]
    print("The entry has been removed.")

def update(id: int, text: str, data: dict) -> None:
    if str(id) not in data:
        print("No such entry.")
        return
    data[str(id)]["description"] = text
    print("Description updated successfully.")
            
def set_status(id: int, status: str, data: dict) -> None:
    if str(id) not in data:
        print("No such entry.")
        return
    data[str(id)]["status"] = status
    data[str(id)]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Status has been updated.")

def list_entries(status: str | None, data: dict) -> None:
    if not data:
        print("There are no entries.")
        return

    match status:
        case None:
            for k, v in data.items():
                print(f"{k}: \"{v["description"]}\"\nStatus: {v["status"]}\
                    \nCreated at {v["createdAt"]}. Last modified at {v["updatedAt"]}\n")
        case _:
            for k, v in data.items():
                if v["status"] == status:
                    print(f"{k}: \"{v["description"]}\"\nStatus: {v["status"]}\
                    \nCreated at {v["createdAt"]}. Last modified at {v["updatedAt"]}\n")
            

    
