class Descriptor:
    def __get__(self, obj, objtype):
        return "Getting value"

class MyClass:
    attr = Descriptor()

print(MyClass().attr)