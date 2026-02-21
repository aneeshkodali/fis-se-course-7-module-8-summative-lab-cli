# imports
from models.user import User
import pytest

def test_user_creation():

    user = User(1, "Bob Smith", "bob.smith@aol.com")

    assert user.id == 1
    assert user.name == "Bob Smith"
    assert user.email == "bob.smith@aol.com"


def test_to_dict():

    user = User(1, "Bob Smith", "bob.smith@aol.com")
    assert user.to_dict() == {
        "id": 1,
        "name": "Bob Smith",
        "email": "bob.smith@aol.com",
    }


def test_from_dict():

    user_dict = {
        "id": 1,
        "name": "Bob Smith",
        "email": "bob.smith@aol.com",
    }

    user = User.from_dict(user_dict)

    assert user.id == 1
    assert user.name == "Bob Smith"
    assert user.email == "bob.smith@aol.com"

def test_invalid_id():
    with pytest.raises(ValueError):
        User(0, "Bob Smith", "bob.smith@aol.com")


def test_invalid_name():
    with pytest.raises(ValueError):
        User(1, "", "bob.smith@aol.com")


def test_invalid_email():
    with pytest.raises(ValueError):
        User(1, "Bob Smith", "invalid-email")