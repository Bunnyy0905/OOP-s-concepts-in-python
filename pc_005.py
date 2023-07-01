# #Accessing(Creating, Modifying and deleting) an instance variables outside the class(main)
# #Note: Modification in one object won't affecting other objects
# class Student:
#     def __init__(self,sid,sname): 
#         self.id=sid      #Acessing(creating) an instance variables(id,name) using constructor
#         self.name=sname    
# s1=Student("C01","Bunny")    
# s2=Student("C06","Bhumita")     
# print(s1.__dict__)
# s1.gender="Male" #creating an instance variable(name) for object s1 (outside the class)
# print(s1.__dict__)
# s1.name="Bhaskar Singh" #modifying an instance variable(name) for object s1 (outside the class)
# print(s1.__dict__)
# print(s2.__dict__) 
# del s2.id #deleting an instance variable(id) for object s2 (outside the class)
# print(s2.__dict__)

# Method 2 : #Accessing(Creating, Modifying and deleting) an instance variable using instance method
class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    
    def display(self):
        print(self.name, self.salary)


    def change_data(self):
        self.name="Bhaskar Singh"
        self.salary="250000"

# for using input
    def user_input(self):
        self.name=input("Enter new name:")
        self.salary=int(input("Enter new salary:"))
e1=Employee('Ankit',150000)
e2=Employee('Bunny', 200000)

e2.display()
e1.change_data()
print(e1.__dict__)
e1.user_input()
print(e1.__dict__)
# print(e1.__dict__)
