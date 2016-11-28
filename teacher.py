from person import Person

class Teacher(Person):


    def __init__(self, name):
        super().__init__(name)
        self.email = self.name.lower() + "@bth.se"


    def __str__(self):
        return self.name + " " + self.email