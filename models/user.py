class User:
    
    # init
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    # convert from class to dict (instance)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
    
    # convert from dict to class (class)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email']
        )

    # representation function
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    
    # id getter
    @property
    def id(self):
        return self._id
    
    # id setter
    @id.setter
    def id(self, value):
        # check for valid values
        if not isinstance(value, int) or value < 1:
            print(f"{value} is not a valid value for id")
            raise ValueError
        self._id = value