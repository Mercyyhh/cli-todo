#!/usr/bin/env python3

import argparse
import json

json_path = "json/tasks.json"

parser = argparse.ArgumentParser(
    prog="ToDo CLI App",
    description="Simple CLI TODO Application for personal use",
    epilog="ToDo App by Mercyh"
    )

# [DEFINE COMMANDS, ARGUMENTS, FLAGS]

parser.add_argument("action", choices=["add", "remove", "list", "complete"], help="Decide what action you want to do!")
parser.add_argument("task", nargs="*", help="Task description or number") # whatever that comes after the action command will be passed on to tasks command
parser.add_argument("-r", "--removed",action="store_true", help="List removed tasks")
parser.add_argument("-c", "--completed",action="store_true", help="List completed tasks")

# [TEMP LIST & DICTIONARY]

task_details = {
    "task": None
}

# [TODO LIST FUNCTIONS]

def add_task(json_file, task_dict, user_args):
    task_dict["task"] = user_args 
    with open(json_file, "r") as f:
        existing_tasks = json.load(f)
    
    existing_tasks["tasks"].append(task_dict)
    with open(json_file, "w") as f:
        json.dump(existing_tasks, f, indent=2)

def list_tasks(json_file, task_catagory):
    with open(json_file, "r") as f:
        tasks = json.load(f)
    
    for i, item in enumerate(tasks[task_catagory], start=1):
        print(f"{i}. {item["task"]}")

def move_task(json_file, task_index, dest_list): # move task will delete and complete task as it all is just moving the task to another list
    with open(json_file, "r") as f:
        tasks = json.load(f)

    task_index -=1
    task_to_dlt = tasks["tasks"].pop(task_index)
    tasks[dest_list].append(task_to_dlt)

    with open(json_file, "w") as f:
        json.dump(tasks, f, indent=2)

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
    active_list = None
    if args.removed:
        active_list = "deleted"
    elif args.completed:
        active_list = "completed"
    else:
        active_list = "tasks"
        
    list_tasks(json_path, active_list)

if args.action == "remove":     
    if not args.task:           
        print("'remove' Command takes an argument!")
    else:
        try:
            move_index = int(args.task[0])
            move_task(json_path, move_index, "deleted")
        except ValueError:
            print("'remove' Command takes an int argument!")    
        except IndexError:
            print(f"Task {args.task} does not exist")

if args.action == "complete":
    if not args.task:
        print("'complete' Command takes an argument!")
    else:
        try:
            move_index = int(args.task[0])
            move_task(json_path, move_index, "completed")
        except ValueError:
            print("'complete' Command takes an int argument!")    
        except IndexError:
            print(f"Task {args.task} does not exist")
    
