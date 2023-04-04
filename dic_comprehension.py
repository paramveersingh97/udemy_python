users = [
    (0,"Bob","pass"),
    (1,"bunty","1234")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_,username,password = username_mapping[username_input]
if password_input == password:
    print("Your are valid user :)")
else:
    print("Your password is not correct :(")