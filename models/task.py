class Task:

    # init
    def __init__(self, id, project_id, assigned_to_id, title, status="Not Started"):
        self.id = id
        self.project_id = project_id
        self.assigned_to_id = assigned_to_id
        self.title = title
        self.status = status

    # convert from class to dict (instance)
    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "assigned_to_id": self.assigned_to_id,
            "title": self.title,
            "status": self.status,
        }
    
    # convert from dict to class (class)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            project_id=data["project_id"],
            assigned_to_id=data["assigned_to_id"],
            title=data["title"],
            status=data.get("status"),
        )

    # representation function
    def __repr__(self):
        return f"Task(id={self.id}, project_id={self.project_id}, assigned_to_id={self.assigned_to_id}, title={self.title}, status={self.status})"
    
    # project_id getter
    @property
    def project_id(self):
        return self._project_id
    
    # project_id setter
    @project_id.setter
    def project_id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            print(f"{value} is not a valid value for project_id")
            raise ValueError
        self._project_id = value

    # assigned_to_id getter
    @property
    def assigned_to_id(self):
        return self._assigned_to_id
    
    # assigned_to_id setter
    @assigned_to_id.setter
    def assigned_to_id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            print(f"{value} is not a valid value for assigned_to_id")
            raise ValueError
        self._assigned_to_id = value

    # status getter
    @property
    def status(self):
        return self._status
    
    # status setter
    @status.setter
    def status(self, value):

        # check for valid value
        if not isinstance(value, str) or value not in ('Not Started', 'In Progress', 'Completed'):
            print(f"{value} is not a valid status value.")
            raise ValueError
        self._status = value