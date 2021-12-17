# x=10
# try:
#     print(x)
#     b=int(input("Enter value: "))
#     if b==4:
#         raise ValueError
#     c=b/x
#     print(c)
# except ValueError:
#     print("please give value other than 4")
# except NameError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("No Exception")
# finally:
#     print("The 'try except' is finished")

# class MyClass:
#     x=50
#
# p1=MyClass()
# print(p1.x)

# class Employee:
#     pass
#
# emp1 = Employee()
# emp1.fname = "Abhi"
# emp1.lname = "Yadav"
# emp1.email = "abhi@gmail.com"
# emp1.sal = 30000
#
# print(emp1.fname)
# print(emp1.lname)
# print(emp1.email)
# print(emp1.sal)
#
# emp2 = Employee()
# emp2.fname = "Mayank"
# emp2.lname = "Shukla"
# emp2.email = "shukla@gmail.com"
# emp2.sal = 30000
#
# print(emp2.fname)
# print(emp2.lname)
# print(emp2.email)
# print(emp2.sal)

# class Employee:
#
#     def __init__(self,fname,lname,email,sal):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#         self.sal = sal
#
#     def display(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.email)
#         print(self.sal)
#         print()
#
# emp1 = Employee("Abhi","Yadav","abhi@gmail.com",30000)
# emp2 = Employee("Mayank","Shukla","shuklaji@gmail.com",32000)
# emp1.display()
# emp2.display()

# x=50
# def fun():
#     x=10
#     print(x)
# fun()
# print(x)
#
# def fun2():
#     global x
#     x=x+11
#     print(x)
# fun2()
# print(x)

# class Student:
#
#     def __init__(self,fname,lname,rollno,course):
#         self.fname=fname
#         self.lname=lname
#         self.rollno=rollno
#         self.course = course
#
#     def display(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.rollno)
#         print(self.course)
#
#     def subject(self):
#         marks = input("Enter marks: ").split(",")
#         avg = 0
#         sum=0
#         for i in self.marks:
#             sum =sum+int(i)
#         avg=sum/len(self.marks)
#         print(f"{self.fname} Average marks: {avg}")
#         print()
#
# student1 = Student("Abhi","Yadav","85","CSE")
# student1.display()
# student1.subject()
#
# student2 = Student("Mayank","Shukla","74","Mech")
# student2.display()
# student2.subject()

class Employee:
    no_emp=0
    raise_amt=0.05
    def __init__(self,fname,lname,email,sal):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.sal = sal
        Employee.no_emp+=1

    def cal_pay(self):
        self.sal = self.sal + (self.sal * self.raise_amt)

    def display(self):
        print(self.fname)
        print(self.lname)
        print(self.email)
        print(self.sal)
        print()

emp1 = Employee("Abhi","Yadav","abhi@gmail.com",30000)
emp2 = Employee("Mayank","Shukla","shuklaji@gmail.com",32000)

print("No. of Employee: ",Employee.no_emp,"\n")

emp1.display()
Employee.display(emp2)

print(emp1.__dict__,"\n")
print(emp2.__dict__,"\n")

Employee.cal_pay(emp1)
emp1.display()

Employee.cal_pay(emp2)
emp2.display()

emp1.raise_amt =0.07
Employee.cal_pay(emp1)
emp1.display()

