# imports
from utils.cli.cli_projects import register_project_commands
from utils.cli.cli_task import register_task_commands
from utils.cli.cli_users import register_user_commands
import argparse



def main():

    # initialize parser
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    
    # initialize subparsers
    subparsers = parser.add_subparsers()

    # register commands
    register_project_commands(subparsers=subparsers)
    register_task_commands(subparsers=subparsers)
    register_user_commands(subparsers=subparsers)


    # parse args from command line
    args = parser.parse_args()
    # check if func/subcommand passed
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()