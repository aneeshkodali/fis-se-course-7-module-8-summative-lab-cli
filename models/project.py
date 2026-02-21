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
        return f"Project(id={self.id}, owner_id={self.owner_id}, title='{self.title}', description='{self.description}', due_date='{self.due_date}')"
    
    # id getter
    @property
    def id(self):
        return self._id
    
    # id setter
    @id.setter
    def id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{value} is not a valid value for id")
        self._id = value

    # owner_id getter
    @property
    def owner_id(self):
        return self._owner_id
    
    # owner_id setter
    @owner_id.setter
    def owner_id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{value} is not a valid value for owner_id")
        self._owner_id = value

    # title getter
    @property
    def title(self):
        return self._title

    # title stter
    @title.setter
    def title(self, value):
        # check for valid value
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{value} is not a valid title")
        self._title = value

    # description getter
    @property
    def description(self):
        return self._description

    # description stter
    @description.setter
    def description(self, value):
        # check for valid value
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{value} is not a valid description")
        self._description = value
    
    # due_date getter
    @property
    def due_date(self):
        return self._due_date
    

    # due_date stter
    @due_date.setter
    def due_date(self, value):
        # check for valid value
        if value is None:
            self._due_date = None
        elif not isinstance(value, str):
            raise ValueError(f"{value} is not a valid due_date")
        else:
            self._due_date = value