# Constructor --> Special method used for initializing objects with attributes. eg. __init__ method
# There are mainly three types of constructor
# 1.Non-Parametrized Constructor
# 2.Parametrized Constructor
# 3.Default Constructor

# Type 1: Non - Parametrized Constructor
class Employee:
    def __init__(self): # Non Parametrized Constructor -->since no parameters are passed
        self.salary=22000
        self.age=21

e1=Employee()
e2=Employee()

print(e1.__dict__) #__dict__ --> special attribute used to see the content of the object 
print(e2.__dict__)



# Type 2: Parametrized Constructor
class Student:
    # Note: self --> It is a variable which contains the memory address of the current object
    def __init__(self,sid,sname,gen): #Parametrized Constructor-->since parameters such as sid,sname and gen are passed
        self.id=sid 
        self.name=sname
        self.gender=gen

# Note:Just by defining the constructor memory allocation is not done. Objects should be created, for Memory allocation for the object. 
s1=Student("C01","Bunny","Male")
s2=Student("C06","Bhumita","Female")

print(s1.__dict__) #__dict__ --> special attribute used to see the content of the object
print(s2.__dict__)



# Type 3: Default Constructor
class Comps:
    pass

stu1=Comps()
stu2=Comps()
# Note: Without constructor, objects cannot be created.
# Since, no constructor is used, therfore default constructor i.e. built-in constructor gets called, which is empty
print(stu1.__dict__)



