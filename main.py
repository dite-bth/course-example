from course import Course
from student import Student
from program import Program


s1 = Student("Nils", "nile16", 15)
s2 = Student("Tommi", "tosv15", 105)
sList = [s1, s2, Student("Fredrik", "frfr14", 2)]

c = Course("KURSEN", "ME1572", 15)


p = Program("Kalops", 180, [c], sList)


p.addStudent(Student("Jesper", "jetr16", 15))

ss = p.getStudents()
print(ss)

for s in ss:
    print(s)