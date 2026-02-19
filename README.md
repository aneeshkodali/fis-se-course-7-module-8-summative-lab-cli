# Project Management CLI Tool


## About

This project deals with creating a command-line project management tool for a team of developers. This tool allows administrators to manage users, projects, and tasks through structured CLI commands. The system supports the following (non-exhaustive) tasks:
- Create and list users via the command line.
- Add projects to specific users and display their associated projects.
- Assign tasks to projects and mark them as complete.
- Edit and persist project/task data using file I/O.
- Navigate the tool with clear, user-friendly CLI commands.
- Manage data relationships like one-to-many (users to projects) and many-to-many (projects to tasks with contributors).
- Create and manage users, projects, and tasks.

## File Structure

The following file/folder structure is:
- [`main.py`](./main.py): serves as CLI entry point
- [`models/`](./models/): contains class definitions
- [`data/`](./data/): contains local JSON or CSV file storage
- [`utils/`](./utils/): contains helper functions, custom hooks
- [`requirements.txt`](./requirements.txt): contains external dependencies