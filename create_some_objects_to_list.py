from create_one_attribute import Person
class Person:
    def __init__(self,name) -> None:
        self.name=name
p1=Person("Anvar")
p2=Person("Shavkat")
p3=Person("Jasur")
persons=[p1,p2,p3]
print(persons)
#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"

#Add these objects to the "persons" named list