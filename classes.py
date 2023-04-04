class Student:
    def __init__(self,name,age):
        self.name = name
        self.grades = (90,88,90)
        self.age = age
    def average(self):
        return sum(self.grades)/len(self.grades)

# student =  Student("Param")  
# print(student.name)
# print(student.grades)
# print(student.average())

bob = Student("Bob",23)
print(bob)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.grades = (90,88,90)
        self.age = age
    # def __str__(self):  
    #     return "hello"
    def __repr__(self): #used for debugging
        return f"this is repr {self.name}"

bob = Student("Bob",23)
print(bob)


