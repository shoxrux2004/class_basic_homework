from create_two_attribute import Person
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person=Person("Ali",25)
print(person.name,person.age)
#create an object named "person" whose name is "Ali", age is "25"