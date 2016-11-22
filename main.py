from course import Course
from student import Student
from program import Program
from teacher import Teacher
from school_nile16 import School

s1 = Student("Nils", "nile16", 15)
s2 = Student("Tommi", "tosv15", 105)
sList = [s1, s2, Student("Fredrik", "frfr14", 2)]

t = Teacher("Hasse", "haha@hej.com")

c = Course("KURSEN", "ME1572", 15, t)

p = Program("Kalops", 180, [c], sList, t)

p.addStudent(Student("Jesper", "jetr16", 15))

ss = p.getStudents()

school = School("Ulan-Bator High", "Ulan-Bator", [p])

p.studentList[2].name = "Nilz"
print(school)
#print(p)