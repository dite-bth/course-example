from course import Course
from student import Student


s1 = Student("Nils", "nile16", 15)
s2 = Student("Tommi", "tosv15", 105)
sList = [s1, s2, Student("Fredrik", "frfr14", 2)]

c = Course("KURSEN", "ME1572", 15, sList)



c.addStudent(Student("Jesper", "jetr16", 15))

print(c)