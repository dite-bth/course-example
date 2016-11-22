class Program():


    def __init__(self, name, points, courseList, students, teacherObj=None):
        self.name = name
        self.points = points
        self.courseList = courseList

        self.__admin = teacherObj

        self.studentList = list()
        self.studentList = students


    def setAdmin(self, teacherObj):
        self.__admin = teacherObj


    def getStudents(self):
        return self.studentList


    def addStudent(self, studentObj):
        self.studentList.append(studentObj)


    def removeStudent(self, studentObj):
        self.studentList.remove(studentObj)