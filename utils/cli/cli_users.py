from models.user import User
from rich.console import Console
from utils.storage import load_data, save_data
from utils.common import generate_next_id

USER_FILE = "data/users.json"
console = Console()

def add_user(args):

    # load data
    data = load_data(file_path=USER_FILE)
    users = [
        User.from_dict(record)
        for record in data
    ]

    # prevent user from being added if email already exists
    for user in users:
        if user.email == args.email:
            console.print(f"User with email `{user.email}` already exists.")
            return

    # create new user  
    new_user = User(
        id=generate_next_id(data=data, id_column='id'),
        name=args.name,
        email=args.email,
    )

    # add user to data
    users.append(new_user)
    save_data(
        file_path=USER_FILE,
        data=[user.to_dict() for user in users]
    )

    console.print(f"User added: {new_user}")

def find_user(args):

    # end if no filter entered
    if not any([args.id, args.name, args.email]):
        console.print("Please provide at least one search criteria.")
        return

    # load data
    data = load_data(file_path=USER_FILE)
    users = [User.from_dict(record) for record in data]

    # apply filters to data (matches if ANY criteria matches)
    users_filtered = [
        user
        for user in users
        if (
            (args.id is not None and user.id == args.id) or
            (args.name is not None and user.name == args.name) or
            (args.email is not None and user.email == args.email)
        )
    ]

    if not users_filtered:
        console.print(f"No users found.")
        return
    
    console.print("Users found.")
    for user in users_filtered:
        console.print(user)
        
def list_users(args):

    # load data
    data = load_data(file_path=USER_FILE)
    users = [
        User.from_dict(record)
        for record in data
    ]

    if not users:
        console.print("No users found.")
        return

    for user in users:
        console.print(user)

def register_user_commands(subparsers):

    # add-user
    add_user_parser = subparsers.add_parser('add-user')
    add_user_parser.add_argument('--name', type=str, required=True, help='Name of user')
    add_user_parser.add_argument('--email', type=str, required=True, help='Email of user')
    add_user_parser.set_defaults(func=add_user)

    # find-user
    find_user_parser = subparsers.add_parser('find-user')
    find_user_parser.add_argument('--id', type=int, help='ID of user')
    find_user_parser.add_argument('--name', type=str, help='Name of user')
    find_user_parser.add_argument('--email', type=str, help='Email of user')
    find_user_parser.set_defaults(func=find_user)

    # list-users
    list_users_parser = subparsers.add_parser('list-users')
    list_users_parser.set_defaults(func=list_users)
