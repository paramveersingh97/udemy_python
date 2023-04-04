def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

result = multiply(1,2,3,4,5)  
print(result)


# unpacking keyword arguments

def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    print(kwargs)
    # print(**kwargs)
    named(**kwargs)
    print(kwargs.items())
    for i in kwargs.items():
        print(i)
    for name, passw in  kwargs.items():
        print(f"{name} and {passw}")


print_nicely(name="Bob", age=25)