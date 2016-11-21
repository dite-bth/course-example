from student import Student

class Course():

    def __init__(self, name, code, points, students):
        self.name = name
        self.code = code
        self.points = points

        self.studentList = list()
        self.studentList = students


    def addStudent(self, studentObj):
        self.studentList.append(studentObj)


    def removeStudent(self, studentObj):
        self.studentList.remove(studentObj)


    def __str__(self):
        s = self.name + "\n" + self.code + " " + str(self.points) + "HP\n"

        for student in self.studentList:
            s += str(student) + "\n"

        return s



s1 = Student("Nils", "nile16", 15)
s2 = Student("Tommi", "tosv15", 105)
sList = [s1, s2, Student("Fredrik", "frfr14", 2)]

c = Course("KURSEN", "ME1572", 15, sList)



c.addStudent(Student("Jesper", "jetr16", 15))

print(c)