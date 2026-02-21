# imports
from datetime import datetime

class Project:
    
    # init
    def __init__(self, id, owner_id, title, description, due_date):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.due_date = due_date

    # convert from class to dict (instance)
    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
        }
    
    # convert from dict to class (class)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            owner_id=data["owner_id"],
            title=data["title"],
            description=data.get("description"),
            due_date=data.get("due_date"),
        )

    # representation function
    def __repr__(self):
        return f"Project(id={self.id}, owner_id={self.owner_id}, title={self.title}, description={self.description}, due_date={self.due_date})"
    
    # owner_id getter
    @property
    def owner_id(self):
        return self._owner_id
    
    # owner_id setter
    @owner_id.setter
    def owner_id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            print(f"{value} is not a valid value for owner_id")
            raise ValueError
        self._owner_id = value

    # due_date getter
    @property
    def due_date(self):
        return self._due_date
    
    # due_date setter
    @due_date.setter
    def due_date(self, value):

        # convert value to valid date and format
        value_date = datetime.strptime(value, '%Y-%m-%d').date()

        # check for valid value
        if not value_date:
            print(f"Error converting `{value}` to valid date format.")
            raise ValueError
        self._due_date = value_date