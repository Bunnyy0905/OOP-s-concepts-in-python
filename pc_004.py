#Built-in class functions
class Student:
    def __init__(self,sid,sname,gen): 
        self.id=sid     
        self.name=sname   
        self.gender=gen    
s1=Student("C01","Bunny","Male")    
s2=Student("C06","Bhumita","Female")     

print(getattr(s1,'name')) #gets/returns the attribute value of object

setattr(s1,'id','C07') #sets/changes the attribute value of the object
print(s1.__dict__)

delattr(s2,'id') #delete the attribute of the object
print(s2.__dict__)

print(hasattr(s2,'name')) #checks whether the object has following attribute or not. It returns the Boolean value.
print(hasattr(s2,'age'))





# Built-in Class attributes
class Employee:
    '''This is Employee class for maintaining Employee data'''
    # Note: This is the documentation string for class Employee. It tells the purpose of the class.
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag

e1=Employee('Jay',21)
e2=Employee('Bunny',20)


print(Employee.__doc__) # returns the documentation string
print(Employee.__dict__) # returns the namespace. It returns all the contents of the class.
print(Employee.__name__) # returns the name of the class
print(Employee.__module__) # returns the module name where class is defined. If the class is defined in current module, therefore it will return '__main__'
print(Employee.__bases__)  # returns list of base class


print(isinstance(e1,Student))
print(isinstance(e2,Employee))
print(isinstance(s1,Student))
print(isinstance(s2,Employee))