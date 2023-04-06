# First class functions means that the functions are just variables, and you can pass them as a variable in the other function

def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend / divisor

def calculate(*values,operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)



def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}")

friends= [
    {"name": "Smith","age":36},
    {"name": "Rolf","age":38},
    {"name": "Matin","age":30}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Smith", get_friend_name))
