from course import Course
from student import Student
from program import Program
from teacher import Teacher
from school_nile16 import School

import sys




def inputSchool():
    n = input("School name: ")
    c = input("School city: ")

    sc = School(n, c)

def inputStudent():
    n = input("Enter student name: ")

    a = n.split()
    print(a)
    a = ''.join(w[0:2].lower() for w in a)
    s = Student(n, a)

def inputC

while True:
    q = input("Select action 1. Student 2. Course 3. Program 4. School 5. Quit: ")

    if q == "5":
        sys.exit()
    elif q == "1":

    else:
        print("Please enter 1 to 5.")