# class Student:
#     roll_no=100
#
#     def __init__(self,name,email,course):
#         self.name = name
#         self.email = email
#         self.course = course
#         Student.roll_no += 1
#         self.roll_no = Student.roll_no
#
#     def display(self):
#         print(self.name)
#         print(self.email)
#         print(self.course)
#         print(self.roll_no)
#
# class PG(Student):
#     def __init__(self,name,email,course,degree):
#         super().__init__(self,name,email,course)
#         self.degree = degree
#
# class Guide(Student):
#     def __init__(self,name,email,specialization,assign_pg=None):
#         super().__init__(self, name, email,specialization)
#         if assign_pg is None:
#             self.assign_pg = []
#         else:
#             self.assign_pg = assign_pg
#
#     def display_stud(self):
#         for stu in self.assign_pg:
#             print(stu.name)
#
#     def add_stu(self,stu):
#         if stu not in self.assign_pg:
#             self.assign_pg.append(stu)
#
#     def remove_stu(self,stu):
#         if stu in self.assign_pg:
#             self.assign_pg.remove(stu)
#
# s1 = Student("Nitin","nitin@gmail.com","CSE")
# s2 = Student("Harsh","harsh@gmail.com","IT")
# s1.display()
# s2.display()
#
# p1 = PG("Amit","amit@gmail.com","M.CSE","Btech")
# p1.display()
# print(p1.degree)
# p2 = PG("Aman","Aman@gmail.com","MBA","MBBS")
# p2.display()
# print(p2.degree)
#
# g1 = Guide("john","")




class User:
    credential = {}
    def __init__(self,name,email,phone,dob,password):
        self.name = name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.password = password

    def display(self):
        print(self.name,self.email,self.phone,self.dob,self.password,sep="\n")

    def signup(self):
        User.credential.update({self.email: self.password})
        print("\nSuccessfully sign up")
        print(User.credential)

    def Signin(self,email,password):
        self.sign_email = email
        self.sign_password = password

        if self.sign_email in User.credential.keys() and self.sign_password in User.credential.values():
            print("\nyou have Successfully Log in")

        else:
            print("\nSorry could not locate your account please Sign up")

user = {}
count = 1
while(True):
    var = int(input("\n1. Sign up \n2. Sign in\n--> "))
    if var == 1:
        key = count
        user[key]=User(input("Enter Name: "),input("Enter Email: "),input("Enter mobile Number: "),input("Enter DOB: "),input("Enter Password: "))
        user[key].signup()
        count+=1

    elif var == 2:
        if len(user) == 0:
            # a=input("Enter Email: ")
            # b=input("Enter password: ")
            print("no user found pls Sign up")
        else:
            # key = int(input("Enter user id: "))
            user[1].Signin(input("Enter Email: "),input("Enter password: "))
