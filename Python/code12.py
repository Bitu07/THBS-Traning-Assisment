# class OverLoad():
#     def add(self,datatype, *a1 ):
#         if datatype =='int':
#             answer = 0
#         if datatype =='float':
#             answer =0.0
#         if datatype =='str':
#             answer =''
#
#         for x in a1 :
#             answer = answer + x
#         print(answer)
#
#
# cla=OverLoad()
#
# cla.add('int', 10, 20) # Int
# cla.add('int', 10, 20,30,40)
# cla.add('float', 10.25, 20.25) # Float
# cla.add('str', 'This ', ' is ',' Sample',' program') # String


# class Overload:
#     def sum1(self,a,b,c):
#         print(a+b+c)
#
#     def sum2(self,a,b):
#         print(a+b)
#
# ole = Overload()
# ole.sum1(10,20,30)
# ole.sum2(10,20)

# class Emp:
#     def __init__(self,name,empno,email):
#         self.name=name  #public
#         self._empno=empno   #protected
#         self.__email=email  #private
#
#     def display(self):
#         print(self.__email)
#
# # class Manager(Emp):
#
# # cal = Manager()
# em = Emp("Sam","1001","sam@gmail.com")
# print(em.name)
# print(em._empno)
# # print(em.__email)
# em.display()

#
# class Emp():
#     name='sam'  #public
#     _empno=1001   #protected
#     __email='sam@gmail.com'  #private
#
#     def display(self):
#         print(self.__email)
#
# class Manager(Emp):
#     pass
#
# class Project:
#     pass
#
#
# cal = Manager()
# em = Emp()
# pj = Project()
#
# print(em.name)
# print(em._empno)
# em.display()
# print()
#
# print(cal.name)
# print(cal._empno)
# cal.display()
#
# print(pj.name)
# print(pj._empno)
# pj.display()



# class Emp:
#     pub = None
#     _pro = None
#     __pri = None
#
#     def __init__(self, pub, pro, pri):
#         self.pub = pub
#         self._pro = pro
#         self.__pri = pri
#
#     def displayPublic(self):
#         print("Public Data Member: ", self.pub)
#
#     def _displayProtected(self):
#         print("Protected Data Member: ", self._pro)
#
#     def __displayPrivate(self):
#         print("Private Data Member: ", self.__pri)
#
#     def accessBaseMembers(self):
#         self.displayPublic()
#         self._displayProtected()
#         self.__displayPrivate()
#
# class Manager(Emp):
#     def __init__(self, pub, pro, pri):
#         Emp.__init__(self, pub, pro, pri)
#
#     def accessSubMembers(self):
#         self.displayPublic()
#         self._displayProtected()
#         # self.__displayPrivate() # Error
#
# obj = Manager(input("Enter Name 1 :"),input("Enter Name 2 :"),input("Enter Name 3 :"))
# obj.accessBaseMembers()
# obj.accessSubMembers()



#
# class Employee:
#
#     def __init__(self, sal):
#         self.sal = sal
#
# # def setage(self, inc):
# # self.inc = inc
#
#     def __add__(self, obj):
#         return Employee(self.sal + obj.sal)
#
#     def __gt__(self, obj):
#         return self.sal > obj.sal
#
#     def __lt__(self, obj):
#         return self.sal < obj.sal
#
#     def __str__(self):
#         return "Highest Salary " + str(self.sal)
#
#
# emp_1 = Employee(5000)
# print(emp_1.sal)
#
# emp_2 = Employee(10000)
# print(emp_2.sal)
#
# emp_3= emp_1 + emp_2
# print(emp_3.sal)
#
# print(emp_3 > emp_2)
#
# print(emp_1 < emp_2)
#
# print(emp_3)
import calendar
# import datetime
# print(datetime.time.min)
# print(datetime.time.max)
#
# import calendar
# print(calendar.monthrange())
#
# import os.path, time
# print("created: %s" % time.ctime(os.path.getmtime("F1.txt")))
# print("Last Modified: %s" % time.ctime(os.path.getctime("F1.txt")))


import datetime

# for i in range(0,5):
#     print(datetime.datetime.today() + datetime.timedelta(days=i))

cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2022,2,1,1,3
                     ))