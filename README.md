# Tasker CLI

A a simple CLI tool for managing tasks.

## Overview

- Add new tasks with a description.
- Delete tasks by their unique ID.
- Change task status to "to-do", "in-progress", or "done".
- View all tasks with details like status, creation date, and last update.
- Tasks are saved to a local JSON file.

## Installation

Tasker CLI requires Python >=3.9.
```
git clone https://github.com/kr4us3r/tasker-cli.git
cd tasker-cli
pip install .
```
## Usage
Run `tasker-cli` with subcommands. Use `--help` for more details.

### Adding a Task
```
tasker-cli add "Buy groceries"
```
### Listing Tasks
```
tasker-cli list [status]
```
The [status] argument is optional and filters tasks by their status. If omitted, lists all tasks.
```
tasker-cli list
tasker-cli list to-do
tasker-cli list in-progress
tasker-cli list done
```
Example output:
```
1: "Buy groceries"
Status: to-do
Created at 2025-12-09 10:30. Last modified at 2025-12-09 10:30

2: "Finish README"
Status: in-progress
Created at 2025-12-09 11:00. Last modified at 2025-12-09 11:15
```
### Updating Status
```
tasker-cli set-status done 1
```
### Removing a Task
```
tasker-cli remove 2
```
## Data Storage
Tasks are stored in `tasks.json`:
- **Linux/macOS**: `~/.local/share/tasker_cli/tasks.json`
- **Windows**: `%LOCALAPPDATA%\tasker_cli\tasks.json`

