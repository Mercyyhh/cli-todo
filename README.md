# Python CLI To-Do App
simple to do app written in python using the `argparse` module.

## How to use

`add`, `list`,`remove`,`complete`.

- `add`
    - `add [task name]` will add a task.

- `list`  
    - `list` will list all incomplete tasks.
    - `list -c` will list all completed tasks.

`list` output format:
> 1. Buy milk.
> 2. Finish project.

- `remove`
    - `remove [task number]` will delete a task.
    - `[task number]` should be the task index, for example `remove 2` will remove **"Finish project"** in the above example.

- `complete` works in the same way as `remove`, and it will mark a task as completed.

**Completed tasks and removed(deleted) tasks will not be in the main tasks list, they will have their own dedicated list.**

`list -r` shows all deleted tasks.
`list -c` shows all completed tasks.

## Terminal integration (Linux)

This can be used as is but you will have to run it like, `python3 main.py add buy milk`

in order to run it like a normal terminal command you need to:

1. copy the json file from the json directory to anywhere you
want and change the `json_path` variable in `main.py` to the json file directory.


2. Rename the python file to what you want the command prefix to be, i will choose `todo` for this example. and make sure you remove the file extention. **todo ~~.py~~**

3. Make the file executable with `chmod`.
    - `chmod +x todo`
4. Move the file to `~/.local/bin/`.

5. add the path to bash/zsh if it's not already there. (im not gonna explain, find out yourself)

Now you should be able to run it in the terminal no matter which directory you are in by running:

`todo add buy milk`


