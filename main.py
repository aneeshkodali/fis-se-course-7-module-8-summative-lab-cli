# imports
import argparse

# initialize parser
parser = argparse.ArgumentParser(description="Project Management CLI Tool")

# parse args from command line
args = parser.parse_args()
# check if func/subcommand passed
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()