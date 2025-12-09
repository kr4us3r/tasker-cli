# Tasker CLI

A simple CLI tool for managing tasks. Idea by https://roadmap.sh/projects/task-tracker.

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
### Removing a Task
```
tasker-cli remove 2
```
### Updating Description
```
tasker cli update 3 "New description"
```
### Updating Status
```
tasker-cli set-status 1 done
```
Supported values are "to-do", "in-progress", and "done".

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
Example:
```
tasker-cli list done
```
Output:
```
1: "Buy groceries"
Status: done
Created at 2025-12-09 10:30. Last modified at 2025-12-09 10:30

2: "Finish README"
Status: done
Created at 2025-12-09 11:00. Last modified at 2025-12-09 11:15
```

## Data Storage
Tasks are stored in `tasks.json`:
- **Linux**: `~/.local/share/tasker_cli/tasks.json`
- **Windows**: `%LOCALAPPDATA%\tasker_cli\tasks.json`





