from person import Person

class Student(Person):


    def __init__(self, name, acronym, points=0):
        super().__init__(name)
        self.points = points
        self.acronym = acronym
        self.email = acronym + "@bth.se"

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def addPoints(self, p):
        self.points += p

    def __str__(self):
        return self.name + " " + self.acronym + " " + str(self.points)
