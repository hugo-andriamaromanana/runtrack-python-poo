class Student:
    def __init__(self, name, age, credits, student_ID):
        self.name = name
        self.age = age
        self.credits = credits
        self.student_ID = student_ID

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits

    def studentEval(self):
        if self.credits > 89:
            return 'Excellent'
        if self.credits > 79:
            return 'Très Bien'
        if self.credits > 69:
            return 'Bien'
        if self.credits > 59:
            return 'Passable'
        if self.credits < 59:
            return 'Insuffisant'

    def studentInfo(self):
        return f'Nom = {self.name}\nAge = {self.age}\nCrédits = {self.credits}\nÉvaluation = {self.studentEval()}'

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