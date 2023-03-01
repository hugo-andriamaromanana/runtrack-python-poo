class Student:
    def __init__(self, name, age, credits, student_ID):
        self.__name = name
        self.__age = age
        self.__credits = credits
        self.__student_ID = student_ID

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def studentEval(self):
        if self.__credits > 89:
            return 'Excellent'
        if self.__credits > 79:
            return 'Très Bien'
        if self.__credits > 69:
            return 'Bien'
        if self.__credits > 59:
            return 'Passable'
        if self.__credits < 59:
            return 'Insuffisant'

    def studentInfo(self):
        return f'Nom = {self.__name}\nAge = {self.__age}\nCrédits = {self.__credits}\nÉvaluation = {self.__studentEval()}'

print('------------------')
student = Student("John", 20, 0, 145)
student.add_credits(10)
print(student.credits)
student.add_credits(-10)
print(student.credits)
student.add_credits(10)
print(student.credits)
student.add_credits(10)
print(student.credits)
print('------------------')
print(student.studentInfo())
print('------------------')