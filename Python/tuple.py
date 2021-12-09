# a,b= 10,20
# print(a,b)
# a=10,20
# print(a)
# a = input("--> ").split(" ")
# print(a)

# num1 = [10,20,30,50,50,60,70,80,90,100]
# num2=[]
#
# for i in range(0,len(num1),2):
#     num2.append(num1[i:i+2])
#
# print(num2)

# def fun(l):
#     amt=0
#     for i in range(len(l)):
#         if(l[i][0]=="D"):
#             amt = amt + int(l[i][1])
#         else:
#             amt = amt - int(l[i][1])
#     return amt
#
# l3= input("--> ").split(",")
# val = list(map(lambda x:x.split(" "),l3))
#
# print(fun(val))
#
# def elec(ele):
#     return  ele[1]
#
# l =[[2,3],[3,4],[4,5],[5,1],[1,2]]
# l.sort(key=lambda x:x[1])
# print(l)
# l.sort(key=elec)
# print(l)

# def name(employee):
#     return employee.get("Name")
# def exp(employee):
#     return employee.get("exp")
# def sal(employee):
#     return employee.get("sal")
#
# employee = [{"Name":"Abhi","exp":3,"sal":300000},
#             {"Name":"Nitin","exp":4,"sal":400000},
#             {"Name":"Harsh","exp":2,"sal":200000},
#             {"Name":"Bhaggu","exp":5,"sal":500000}]
#
# employee.sort(key=name)
# print(employee)
# employee.sort(key=exp)
# print(employee)
# employee.sort(key=sal)
# print(employee)
# print()
# employee.sort(key=lambda x:x.get("Name"))
# print(employee)
# employee.sort(key=lambda x:x.get("exp"))
# print(employee)
# employee.sort(key=lambda x:x.get("sal"))
# print(employee)
# print()

# def rev(str1):
#     return str1[::-1]
# str1 = "hello"
# print(rev(str1))
#
# def indx(str2 , target):
#     if target in str2:
#         return str2.index(target)
#     else:
#         return -1
#
# str2 = "Hello world"
# print(indx(str2,"world"))

import fun_mod as fm

course=[10,20,30,40,50,60,70,80,90,100]
tgt=50
print(fm.index_find(course,tgt))