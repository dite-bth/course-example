class Program():


    def __init__(self, name, points, courseList, students):
        self.name = name
        self.points = points
        self.courseList = courseList

        self.studentList = list()
        self.studentList = students


    def getStudents(self):
        return self.studentList


    def addStudent(self, studentObj):
        self.studentList.append(studentObj)


    def removeStudent(self, studentObj):
        self.studentList.remove(studentObj)