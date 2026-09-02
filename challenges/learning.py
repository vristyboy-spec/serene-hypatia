class Cat:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says meow")


my_cat = Cat("Lily", 2)

Cat.bark(my_cat)