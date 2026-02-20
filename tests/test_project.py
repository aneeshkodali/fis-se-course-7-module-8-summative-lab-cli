from models.project import Project


def test_project_creation():

    project = Project(
        id=1,
        owner_id=1,
        title="PM CLI",
        description="Project management CLI tool",
        due_date="2026-02-20"
    )

    assert project.id == 1
    assert project.owner_id == 1
    assert project.title == "PM CLI"
    assert project.description == "Project management CLI tool"
    assert project.due_date == "2026-02-20"


def test_to_dict():

    project = Project(
        id=1,
        owner_id=1,
        title="PM CLI",
        description="Project management CLI tool",
        due_date="2026-02-20"
    )

    assert project.to_dict() == {
        "id": 1,
        "owner_id": 1,
        "title": "PM CLI",
        "description": "Project management CLI tool",
        "due_date": "2026-02-20",
    }


def test_from_dict():

    project_dict = {
        "id": 1,
        "owner_id": 1,
        "title": "PM CLI",
        "description": "Project management CLI tool",
        "due_date": "2026-02-20",
    }

    project = Project.from_dict(project_dict)

    assert project.id == 1
    assert project.owner_id == 1
    assert project.title == "PM CLI"
    assert project.description == "Project management CLI tool"
    assert project.due_date == "2026-02-20"