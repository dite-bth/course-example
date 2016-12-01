from teacher import Teacher



from bth import program as prog
from student import Student
from course import Course

s = Student("Sven", "sasa")
c = Course("MIntro", "ME1571", 15)
cl = [c]
sl = [s]
t = Teacher("Arne")

p = prog.Program("IW", 180, cl, sl, t)

print(p)