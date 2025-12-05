import argparse
import json
from .main import add, remove, set_status, list_entries

FILE_PATH = "tasks.json"

def main():
    parser = argparse.ArgumentParser(description="A wondrous tool for task management.")
    sub = parser.add_subparsers(dest="command", help="Available commands.")

    add_p = sub.add_parser("add", help="Adds an entry to the list of tasks.")
    remove_p = sub.add_parser("remove", help="Removes an entry from the list of tasks.")
    status_p = sub.add_parser("set-status", help="Changes the status of a task.")
    sub.add_parser("list", help="Lists all entries.")

    add_p.add_argument("description", type=str, help="Description of the task.")
    remove_p.add_argument("item_id", type=int, help="ID of the entry to be removed.")
    status_p.add_argument("status", choices=["to-do", "in-progress", "done"], type=str,
                          help="Status to set. Available values: 'to-do', 'in-progress', 'done'.")
    status_p.add_argument("item_id", type=int, help="ID of the entry to change the status of.")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        exit(1)

    data = []
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    except:
        with open(FILE_PATH, "w") as f:
            json.dump(data, f)

    if args.command == "add":
        add(args.description, data)
    elif args.command == "remove":
        remove(args.item_id, data)
    elif args.command == "set-status":
        set_status(args.status, args.item_id, data)
    elif args.command == "list":
        list_entries(data)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)
    
if __name__ == "__main__":
    main()