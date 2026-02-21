from models.task import Task
import pytest

def test_task_creation():
    task = Task(
        id=1,
        project_id=1,
        assigned_to_id=1,
        title="Create classes",
        status="Completed"
    )

    assert task.id == 1
    assert task.project_id == 1
    assert task.assigned_to_id == 1
    assert task.title == "Create classes"
    assert task.status == "Completed"

def test_task_default_status():
    task = Task(
        id=2,
        project_id=1,
        assigned_to_id=1,
        title="Write tests"
    )

    assert task.status == "Not Started"

def test_task_invalid_status():
    with pytest.raises(ValueError):
        Task(
            id=3,
            project_id=1,
            assigned_to_id=1,
            title="Invalid status test",
            status="Done"
        )

def test_to_dict():

    task = Task(
        id=1,
        project_id=1,
        assigned_to_id=1,
        title="Create classes",
        status="Completed"
    )

    assert task.to_dict() == {
        "id": 1,
        "project_id": 1,
        "assigned_to_id": 1,
        "title": "Create classes",
        "status": "Completed"
    }

def test_from_dict():

    task_dict = {
        "id": 1,
        "project_id": 1,
        "assigned_to_id": 1,
        "title": "Create classes",
        "status": "Completed"
    }

    task = Task.from_dict(task_dict)

    assert task.id == 1
    assert task.project_id == 1
    assert task.assigned_to_id == 1
    assert task.title == "Create classes"
    assert task.status == "Completed"

def test_status_update():

    task = Task(
        id=1,
        project_id=1,
        assigned_to_id=1,
        title="Create classes"
    )

    task.status = "In Progress"

    assert task.status == "In Progress"

def test_invalid_id():
    with pytest.raises(ValueError):
        Task(0, 1, 1, "Title")


def test_invalid_project_id():
    with pytest.raises(ValueError):
        Task(1, 0, 1, "Title")


def test_invalid_assigned_to_id():
    with pytest.raises(ValueError):
        Task(1, 1, 0, "Title")


def test_invalid_title():
    with pytest.raises(ValueError):
        Task(1, 1, 1, "")