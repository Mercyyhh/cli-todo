import argparse
import json
import copy

json_path = "json/trial.json"

parser = argparse.ArgumentParser(
    prog="ToDo CLI App",
    description="Simple CLI TODO Application for personal use",
    epilog="ToDo App by Mercyh"
    )

# [DEFINE COMMANDS, ARGUMENTS, FLAGS]

parser.add_argument("action", choices=["add", "remove", "list"], help="Decide what action you want to do!")
parser.add_argument("task", nargs="*", help="Task description or number") # whatever that comes after the action command will be passed on to tasks command

# [TEMP LIST & DICTIONARY]

task_details = {
    "task": None,
    "completed": False  # Default for incomplete tasks
}

# [TODO LIST FUNCTIONS]

def add_task(json_file, task_dict, user_args): 
    with open(json_file, "r") as f:
        existing_tasks = json.load(f)
    
    task_dict["task"] = user_args
    existing_tasks.append(task_dict)

    with open(json_file, "w") as f:
        json.dump(existing_tasks, f, indent=2)

def list_tasks(json_file):
    with open(json_file, "r") as f:
        tasks = json.load(f)
    
    for i, item in enumerate(tasks, start=1):
        status = "- COMPLETED" if item["completed"] else " "
        print(f"{i}. {item["task"]} {status}")

# [ARGPARSE CONDITIONS]

args = parser.parse_args()

if args.action == "add":
    if not args.task:
        print("'add' Command takes an argument!")
    else:
        new_task = " ".join(args.task)
        add_task(json_path, task_details, new_task)
        print("<<< Task added successfully!!")

if args.action == "list":
    if args.task:
        print("'list' Command takes no argument!")
    else:
        list_tasks(json_path)

if args.action == "remove":     # Remove function
    if not args.task:           # If no task index is provided after command "remove"
        print("'remove' Command takes an argument!")
    else:
        try:
            todo_functions.remove_complete_task(removed_tasks, tasks, args.task)
        except ValueError:
            print("'remove' Command takes an int argument!")    # If user passes a string instead of an int
        except IndexError:
            print(f"Task {args.task} does not exist")   # If user passes in an index that doesn't exist