# imports
from models.project import Project
import pytest

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

def test_invalid_id():
    with pytest.raises(ValueError):
        Project(0, 1, "Title", "Description", "2026-02-20")


def test_invalid_owner_id():
    with pytest.raises(ValueError):
        Project(1, 0, "Title", "Description", "2026-02-20")


def test_invalid_title():
    with pytest.raises(ValueError):
        Project(1, 1, "", "Description", "2026-02-20")


def test_invalid_description():
    with pytest.raises(ValueError):
        Project(1, 1, "Title", "", "2026-02-20")


def test_invalid_due_date_type():
    with pytest.raises(ValueError):
        Project(1, 1, "Title", "Description", 123)