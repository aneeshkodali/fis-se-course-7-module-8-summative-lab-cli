# imports
from utils.cli.cli_users import register_user_commands
import argparse

# set data file paths
USER_FILE = 'data/users.json'
PROJECT_FILE = 'data/projects.json'


def add_project(args):

    # load data
    user_data = load_data(file_path=USER_FILE)
    users = [User.from_dict(record) for record in user_data]
    project_data = load_data(file_path=PROJECT_FILE)

    # make sure user exists
    user_exists = [
        user
        for user in users
        if user.id == args.owner_id
    ]
    if not user_exists:
        print(f"User with ID {args.owner_id} not found.")
        print(f"Project cannot be added.")
        return
    
    # create new project
    new_project = Project(
        id=generate_next_id(project_data, id_column='id'),
        owner_id = args.owner_id,
        title=args.title,
        description=args.description,
        due_date=args.due_date
    )

    # add project
    project_data.append(new_project.to_dict())
    save_data(file_path=PROJECT_FILE, data=project_data)
    print(f"Project added: {new_project}")

def list_projects(args):

    # load data
    data = load_data(file_path=PROJECT_FILE)
    projects = [
        Project.from_dict(record)
        for record in data
    ]

    if not projects:
        print("No projects found.")
        return

    for project in projects:
        print(project)

def list_owner_projects(args):

    # load data
    data = load_data(file_path=PROJECT_FILE)
    projects = [
        Project.from_dict(record)
        for record in data
    ]

    # filter projects for owner
    owner_projects = [
        project
        for project in projects
        if project.owner_id == args.owner_id
    ]

    if not owner_projects:
        print(f"Now projects found for owner ID: {args.owner_id}.")
        return
    
    for project in owner_projects:
        print(project)

def main():

    # initialize parser
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    
    # initialize subparsers
    subparsers = parser.add_subparsers()

    # register user commands
    register_user_commands(subparsers=subparsers)

    # add-project
    add_project_parser = subparsers.add_parser('add-project')
    add_project_parser.add_argument('--owner-id', type=int, required=True, help='Owner ID of project')
    add_project_parser.add_argument('--title', type=str, required=True, help='Title of project')
    add_project_parser.add_argument('--description', type=str, required=True, help='Description of project')
    add_project_parser.add_argument('--due-date', type=str, required=True, help='Due date of project')
    add_project_parser.set_defaults(func=add_project)

    # list-projects
    list_projects_parser = subparsers.add_parser('list-projects')
    list_projects_parser.set_defaults(func=list_projects)

    # list-owner-projects
    list_owner_projects_parser = subparsers.add_parser('list-owner-projects')
    list_owner_projects_parser.add_argument('--owner-id', type=int, required=True, help='Owner ID of project')
    list_owner_projects_parser.set_defaults(func=list_owner_projects)

    # parse args from command line
    args = parser.parse_args()
    # check if func/subcommand passed
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()