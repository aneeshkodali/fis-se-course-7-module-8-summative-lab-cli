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
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
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

    # name getter
    @property
    def name(self):
        return self._name
    
    # name setter
    @name.setter
    def name(self, value):
        # check for valid value
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{value} is not a valid name")
        self._name = value

    # email getter
    @property
    def email(self):
        return self._email
    
    # email setter
    @email.setter
    def email(self, value):
        # check for valid value
        if not isinstance(value, str) or '@' not in value or '.' not in value.split('@')[-1]:
            raise ValueError(f"{value} is not a valid email.")
        self._email = value 