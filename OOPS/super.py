class Parent:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print("Parent class display method:",self.name)

class Child(Parent):
    def __init__ (self,name,age):
        super() (name)
        self.age=age
    def display(self):
        super().display()
        print("child class display method: ",self.age)
child=Child("Alice",10)
child.display() 