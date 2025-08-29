class Foo:
    
    # Class Member Variable
    age = 25
    name = "YC Jung"
    
    # contruct
    def __init__(self, name, age):

        # Instance Member Variable
        self.name = name
        self.age = age

obj = Foo()

print(type(obj))