# class Employee:
#         no_emp=0
#         raise_amt=0.05
#
#         def __init__(self,first,last,email,pay):
#             self.first = first
#             self.last=last
#             self.email=email
#             self.pay=pay
#             Employee.no_emp += 1
#
#         def cal_pay(self):
#             self.pay=self.pay+(self.pay+self.raise_amt)
#
#         @classmethod
#         def set_raise_amt(self,amt):
#             self.raise_amt=amt
#
#         @classmethod
#         def from_str_val(self,emp_str):
#             first,last,email,pay = emp_str.split(",")
#             return self(first,last,email,pay)
#
#         def display(self):
#             print(self.first)
#             print(self.last)
#             print(self.email)
#             print(self.pay)
#
# emp1 = Employee("sam","Luke","sam@gmail.com",30000)
# emp2 = Employee("John","Vick","john@gmail.com",40000)
# emp1.display()
# emp2.display()
# print(Employee.raise_amt)
# Employee.set_raise_amt(0.07)
# emp_str1 = input("Enter the fname,lname,email,pay: ")
# emp_str2 = input("Enter the fname,lname,email,pay: ")
# emp3 = Employee(emp_str1)
# emp4 = Employee(emp_str2)
# emp3.display()
# emp4.display()



#
# class Employee:
#     no_emp=0
#     raise_amt=0.05
#     def __init__(self,first,last,email,pay):
#         self.first=first
#         self.last=last
#         self.email=email
#         self.pay=pay
#         Employee.no_emp=+1
#     def display(self):
#         print( self.first)
#         print( self.last)
#         print( self.email)
#         print( self.pay)
#
#
# class Developer:
#
#     def __init__(self,first,last,email,pay,pro_lang):
#         Employee.__init__(self,first,last,email,pay)
#         #super.__init__(self,first,last,email,pay)
#         self.pro_lang=pro_lang
#
# emp1=Employee("manju","sanju","manju1@gmail.com",50000)
# emp2=Employee("raju","ramm","raj1@gmail.com",70000)
#
# Dev1=Developer("manju","joe","manju1@gmail.com",50000,"java")
# Dev2=Developer("raju","joe","manju1@gmail.com",50000,"python")
# Dev1.display()
# print(Dev1.pro_lang)
# Dev2.display()
# print(Dev2.pro_lang)
#
# print(Dev1.raise_amt)
# print(Dev2.raise_amt)




# class Employee:
#     no_emp=0
#     raise_amt=0.05
#     def __init__(self,first,last,email,pay):
#         self.first=first
#         self.last=last
#         self.email=email
#         self.pay=pay
#         Employee.no_emp=+1
#     def display(self):
#         print( self.first)
#         print( self.last)
#         print( self.email)
#         print( self.pay)
#
# class Manager(Employee):
#