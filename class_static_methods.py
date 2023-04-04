# Instance method needs an object in order to call them, simply methods has self e.g. instance_method(self):
# In class method intead pf passing self we pass cls which is the class itself


class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Calling static method")

ClassTest.class_method()
ClassTest.static_method()