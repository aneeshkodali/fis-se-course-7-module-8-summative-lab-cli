from models.project import Project
from models.task import Task
from models.user import User
from rich.console import Console
from utils.storage import load_data, save_data
from utils.common import generate_next_id

PROJECT_FILE = 'data/projects.json'
TASK_FILE = 'data/tasks.json'
USER_FILE = 'data/users.json'
console = Console()

def add_task(args):

    # load data
    user_data = load_data(file_path=USER_FILE)
    users = [User.from_dict(record) for record in user_data]
    project_data = load_data(file_path=PROJECT_FILE)
    projects = [Project.from_dict(record) for record in project_data]
    task_data = load_data(file_path=TASK_FILE)

    # make sure user exists
    user_exists = any(user.id == args.assigned_to_id for user in users)
    if not user_exists:
        console.print(f"User with ID {args.assigned_to_id} not found.")
        console.print(f"Task cannot be added.")
        return
    
    # make sure project exists
    project_exists = any(project.id == args.project_id for project in projects)
    if not project_exists:
        console.print(f"Project with ID {args.project_id} not found.")
        console.print(f"Task cannot be added.")
        return
    
    # create new task
    new_task = Task(
        id=generate_next_id(task_data, id_column='id'),
        project_id=args.project_id,
        assigned_to_id = args.assigned_to_id,
        title=args.title,
        status=args.status if args.status else 'Not Started'
    )

    # add task
    task_data.append(new_task.to_dict())
    save_data(file_path=TASK_FILE, data=task_data)
    console.print(f"Task added: {new_task}")

def list_project_tasks(args):

    # load data
    data = load_data(file_path=TASK_FILE)
    tasks = [
        Task.from_dict(record)
        for record in data
    ]

    # filter tasks for project
    project_tasks = [
        task
        for task in tasks
        if task.project_id == args.project_id
    ]

    if not project_tasks:
        console.print(f"No tasks found for project ID: {args.project_id}.")
        return
    
    for project_task in project_tasks:
        console.print(project_task)

def list_assigned_tasks(args):

    # load data
    data = load_data(file_path=TASK_FILE)
    tasks = [
        Task.from_dict(record)
        for record in data
    ]

    # filter tasks for user
    user_tasks = [
        task
        for task in tasks
        if task.assigned_to_id == args.assigned_to_id
    ]

    if not user_tasks:
        console.print(f"No tasks found for user ID: {args.assigned_to_id}.")
        return
    
    for user_task in user_tasks:
        console.print(user_task)

def update_task_status(args):
    
    # load data
    task_data = load_data(file_path=TASK_FILE)
    tasks = [Task.from_dict(record) for record in task_data]

    # set boolean to indicate if task found/updated
    task_found = False

    # loop through tasks
    for task in tasks:
        if task.id == args.id:
            # try to update task
            try:
                task.status = args.status
                task_found = True
            except ValueError as e:
                console.print(f"Error when updating task {args.id} status: {e}")
            break
    
    # load data back to file
    if task_found:
        new_data = [task.to_dict() for task in tasks]
        save_data(file_path=TASK_FILE, data=new_data)
        console.print(f"Task {args.id} updated with status {args.status}.")
    else:
        console.print(f"Task with ID {args.id} not found.")

def register_task_commands(subparsers):

    # add-task
    add_task_parser = subparsers.add_parser('add-task')
    add_task_parser.add_argument('--project-id', type=int, required=True, help='Project ID of task')
    add_task_parser.add_argument('--assigned-to-id', type=int, required=True, help='Assigned user ID of task')
    add_task_parser.add_argument('--title', type=str, required=True, help='Title of task')
    add_task_parser.add_argument('--status', type=str, choices=['Not Started', 'In Progress', 'Completed'], help='Status of task')
    add_task_parser.set_defaults(func=add_task)

    # list-project-tasks
    list_assigned_tasks_parser = subparsers.add_parser('list-project-tasks')
    list_assigned_tasks_parser.add_argument('--project-id', type=int, required=True, help='Project ID of tasks')
    list_assigned_tasks_parser.set_defaults(func=list_project_tasks)

    # list-assigned-tasks
    list_assigned_tasks_parser = subparsers.add_parser('list-assigned-tasks')
    list_assigned_tasks_parser.add_argument('--assigned-to-id', type=int, required=True, help='Assigned user ID of tasks')
    list_assigned_tasks_parser.set_defaults(func=list_assigned_tasks)

    # update-task-status
    update_task_status_parser = subparsers.add_parser('update-task-status')
    update_task_status_parser.add_argument('--id', type=int, required=True, help='Task ID')
    update_task_status_parser.add_argument('--status', type=str, required=True, choices=['Not Started', 'In Progress', 'Completed'], help='Status of task')
    update_task_status_parser.set_defaults(func=update_task_status)