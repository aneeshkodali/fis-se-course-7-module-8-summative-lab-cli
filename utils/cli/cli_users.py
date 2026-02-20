from models.user import User
from utils.storage import load_data, save_data
from utils.common import generate_next_id

USER_FILE = "data/users.json"

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
            print(f"User with email `{user.email}` already exists.")
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

    print(f"User added: {new_user}")

def find_user(args):

    # load data
    data = load_data(file_path=USER_FILE)
    users = [User.from_dict(record) for record in data]

    # apply filters to data (matches if ANY criteria matches)
    users_filtered = [
        user
        for user in users
        if (
            (args.id and user.id == args.id) or
            (args.name and user.name == args.name) or
            (args.email and user.email == args.email)
        )
    ]

    if not users_filtered:
        print(f"No users found.")
        return
    
    print("Users found.")
    for user in users_filtered:
        print(user)
        
def list_users(args):

    # load data
    data = load_data(file_path=USER_FILE)
    users = [
        User.from_dict(record)
        for record in data
    ]

    if not users:
        print("No users found.")
        return

    for user in users:
        print(user)

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
