x = 5,11
print(x)
x,y = 5,11
print(x,y)


students = {"param": 91, "paramm": 92, "parammm": 93}
print(list(students.items()))

for name, marks in students.items():
    print(f"{name} got {marks}")


head, *tail = [1,2,3,4]
print(head)
print(tail)


*head, tail = [1,2,3,4]
print(head)
print(tail)

