def get_admin_password():
    return 1234

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
    return secure_function

# user = {"username": "jose", "access_level": "admin"}

get_admin_passowrd = make_secure(get_admin_password)
user = {"username": "jose", "access_level": "admin"}
print(type(get_admin_password))
print(get_admin_passowrd())