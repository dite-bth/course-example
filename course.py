class Course():

    def __init__(self, name, code, points, students):
        self.name = name
        self.code = code
        self.points = points

        self.studentList = list()
        self.studentList = students
        self.studentList.sort()


    def addStudent(self, studentObj):
        self.studentList.append(studentObj)
        self.studentList.sort()


    def removeStudent(self, studentObj):
        self.studentList.remove(studentObj)

    def __str__(self):
        s = self.name + "\n" + self.code + " " + self.points + "HP\n"

        for student in self.studentList:
            s += student + "\n"