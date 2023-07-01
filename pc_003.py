# Accessing the attributes and methods outside the class
# Class Members = Class attributes(variables) + Class Methods(functions)
# We can access these variables using objects outside the class
# Syntax: 
# 1. Accessing attribute --> object_name.variable_name
# 2. Accessing method --> object_name.method_name()


class Student:
    # Note: self --> It is a variable which contains the memory address of the current object
    def __init__(self,sid,sname,gen): #Parametrized Constructor-->since parameters such as sid,sname and gen are passed
        self.id=sid     #attribute1 of the CLASS Student
        self.name=sname    #attribute2 of the CLASS Student
        self.gender=gen    #attribute3 of the CLASS Student

    # defining a method/function inside the CLASS Student
    def display(self): #method/function of the CLASS Student
        print(f"Student id = {self.id}, name = {self.name} and gender = {self.gender}")

s1=Student("C01","Bunny","Male")    #object1  of the CLASS Student
s2=Student("C06","Bhumita","Female")     #object2 of the CLASS Student

#accessing/calling the attributes outside the class Student
print(s1.name) #accessing attribute2 of s1 object
print(s2.gender) #accessing attribute3 of s2 object

#updating attributes outside the class
s1.name="Bhaskar Singh" #updating the name attribute from "Bunny" to "Bhaskar Singh"
print(s1.name)


#accessing methods/functions outside the class
print(s2.display()) #accessing the display method/function for s2 object

