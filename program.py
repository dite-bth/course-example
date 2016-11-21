class Program():


    def __init__(self, name, points, courseList):
        self.name = name
        self.points = points
        self.courseList = courseList


    def getStudentsInCourses(self):
        programStudents = list()

        for course in self.courseList:
           for student in course.studentList:
               programStudents.append(student)

        return programStudents