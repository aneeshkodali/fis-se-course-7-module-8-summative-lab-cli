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