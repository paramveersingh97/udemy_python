def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend / divisor


marks = [1,2,3,4,5]

print("Welcome to the grade program")

try:
    average = divide(sum(marks),len(marks))
except ZeroDivisionError as e:
    print("Exception is ", e)
    print("There are no grades yet..")
else: # runs only when try block runs successfully
    print(f"The average grade is {average}")
finally:
    print("Thank You!")