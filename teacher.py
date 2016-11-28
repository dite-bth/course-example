from person import Person

class Teacher(Person):


    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


    def __str__(self):
        return self.name + " " + self.email