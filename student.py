import uuid


class Student:

    def __init__(self, firstname, lastname, department):
        self.id = uuid.uuid4().hex
        self.firstname = firstname
        self.lastname = lastname
        self.department = department

    def __str__(self):
        return f"id: {self.id} " \
               f"firstname: {self.firstname} " \
               f"lastname: {self.lastname} " \
               f"department: {self.department} "