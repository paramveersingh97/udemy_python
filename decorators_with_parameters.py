import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator

user = {"username": "jose", "access_level": "guest"}

# get_admin_passowrd = make_secure(get_admin_password)
# user = {"username": "jose", "access_level": "admin"}
# print(type(get_admin_password))
# print(get_admin_passowrd())

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password.__name__)
print(get_admin_password())
print(get_dashboard_password())

user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())

