from student import Student

class Course():

    def __init__(self, name, code, points):
        self.name = name
        self.code = code
        self.points = points







    def __str__(self):
        s = self.name + "\n" + self.code + " " + str(self.points) + "HP"

        return s


