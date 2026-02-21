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
- [`tests/`](./tests/): contains data and logic tests

## Project Use

To use this repository:

### Installation

Clone the repository:
```sh
git clone https://github.com/aneeshkodali/fis-se-course-7-module-8-summative-lab-cli.git
```

Make sure you are in the repository folder:
```sh
cd fis-se-course-7-module-8-summative-lab-cli
```

Create virtual environment:
```sh
python -m venv venv
```

Activate virtual environment (for Windows):
```sh
source venv/Scripts/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

### Running the CLI

All commands are run through `main.py`

### Users

**Add a user**
```sh
python main.py add-user --name "Bob Smith" --email "bob.smith@aol.com"
```

**List all users**:
```sh
python main.py list-users
```

**Find a user**:

By ID:
```sh
python main.py find-user --id 1
```

By Name:
```sh
python main.py find-user --name "Bob Smith"
```

By Email:
```sh
python main.py find-user --email "bob.smith@aol.com"
```

Can combine attributes on which to perform search
- Pass multiple args/values to the CLI command
- Returns results if user is matched to ANY criteria

```sh
python main.py find-user --name "Bob Smith" --email "anne.johnson@google.com"
```
--> Will return 2 users

### Projects

**Add a project**
```sh
python main.py add-project --owner-id 1 --title "PM CLI" --description "Project management CLI tool" --due-date "2026-02-20"
```

**List all projects**:
```sh
python main.py list-projects
```

**List all projects for an owner**:
```sh
python main.py list-owner-projects --owner-id 1
```

### Task

**Add a task**:
```sh
python main.py add-task --project-id 1 --assigned-to-id 1 --title "Create classes"
```

**Update a task status**:
```sh
python main.py update-task-status --id 1 --status "Completed"
```

**List tasks for a project**:
```sh
python main.py list-project-tasks --project-id 1
```

**List tasks for a user**:
```sh
python main.py list-assigned-tasks --assigned-to-id 1
```

### Data persistance

Data is stored locally within the `data/` folder.

The application automatically:
- Created IDs incrementally
- Prevents duplicate data
- Loads and saves data between runs