# class Emp():
#     def display(self):
#         print("This is from Base class")

    # def display1(self):
    #     print("display1 from base class")

# class Manager(Emp):
#     def display1(self):
#         print("This is from Sub class")

# class Third(Manager,Emp):
#     pass

# cla = Manager()
# cla.display()
# cla.display1()
# print(help(Third))


# class Emp():
#     def display(self):
#         print("This is from Base class")
#
#
# class Manager(Emp):
#     def display(self):
#         print ("This is from Sub class")
#
# cla = Manager()
# cla.display()


# class Emp():
#     def display(self):
#         print("This is from Base class")
#
#
# class Manager(Emp):
#     def display1(self):
#         print("This is from Sub/Parent class method")
#
#
# class Project(Manager):
#     def display2(self):
#         print("This is from project Sub class Method")
#
# class Salary(Project):
#     def display3(self):
#         print("This is from salary Sub class Method")
#
#
# cla = Salary()
# cla.display()
# cla.display1()
# cla.display2()
# cla.display3()
# print(help(Salary))



# class Emp():
#     def display(self):
#         print("This is from Emp Base class")
#
#
# class Manager(Emp):
#     def display1(self):
#         print("This is from Manager class method")
#
#
# class Project(Emp):
#     def display1(self):
#         print("This is from Project class Method")
#
# cla = Manager()
# cla.display()
# cla.display1()
#
# cla = Project()
# cla.display()
# cla.display1()
# print(help(Project))



# class Emp():
#     def display(self):
#         print("This is from Emp class")
#
# class Manager():
#     def display1(self):
#         print("This is from Manager class method")
#
# class Project(Emp,Manager):
#     def display2(self):
#         print("This is from Project class Method")
#
# cla = Project()
# cla.display()
# cla.display1()
# cla.display2()
# print(help(Project))


# class Emp():
#     def display(self):
#         print("This is from Emp class")
#
# class Manager():
#     def display1(self):
#         print("This is from Manager class method")
#
# class Project(Emp):
#     def display2(self):
#         print("This is from Project class Method")
#
# class Salary(Manager,Project):
#     def display3(self):
#         print("This is from salary class method")
#
#
# sal = Salary()
# sal.display()
# sal.display1()
# sal.display2()
# sal.display3()


#
# class Emp:
#     def display(self,name=None,salary=None): # parameter
#         if name ==None and salary ==None:
#             print("This is default method")
#         elif name!=None and salary ==None :
#             print("Name is : " , name)
#         else:
#             print("Name is : " , name)
#             print("Salary is : " , salary)
#
# cla = Emp()
# cla.display()
# print()
# cla.display(input("Enter Name : ")) # argu
# print()
# cla.display(input("Enter Name : "),int(input("Enter Salary : ")))

# def display(a,b=30):
#     print(a,b)
#
# display(10,20)
# display(10)



