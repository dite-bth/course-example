class School():

    def __init__(self, name, city, programs):
        self.name = name
        self.city = city
        self.programs = programs

    def getPrograms(self):
        return self.programs

    def addProgram(self,program):
        self.programs.append(program)

    def delProgram(self,program):
        self.programs.remove(program)

    def __str__(self):
        return self.name + " i " + self.city