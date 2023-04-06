import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function

user = {"username": "jose", "access_level": "admin"}

# get_admin_passowrd = make_secure(get_admin_password)
# user = {"username": "jose", "access_level": "admin"}
# print(type(get_admin_password))
# print(get_admin_passowrd())

@make_secure
def get_password(panel):
    if panel == "admin":
        return 1234
    elif panel == "billing":
        return "super_secure_password"
        
@make_secure
def get_dashboard_passowrd():
    return "user: user_password"

print(get_password.__name__)
print(get_password("billing"))