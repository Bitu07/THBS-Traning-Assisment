# num = (1,2,3,5,1)
# print(num)
# print(type(num))
#
# course = ("Mech","CS","IT",["MBA","BBM"])
# print(course)
# print(len(course))
# print(course[0])
# print(course[:])
# print(course[-1])
# print(course[::2])
# for i in course:
#     print(i)

# tup = (5,6,6,2,3,3,1,5,2,2,8,8)
# a=0
#
# for i in range(len(tup)-1):
#     if tup[i]==tup[i+1]:
#         a=a+1
# print(a)

                              #set

# myset = {"apple", "banana", "cherry"}
# for i in myset:
#     print(i)

                            #Add Item

# myset.add("grapse")
# print(myset)
#
# myset.update(["pineapple","fig","mango"])
# print(myset)

                            # Remove item

# myset.remove("fig")
# print(myset)
# # print(myset.remove("fig"))
# print(print(myset))
# print(myset.pop())
# print(myset.clear())
# del myset
# print(myset)
#
#                            JOIN two Set
#
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)
#
# set1.update(set2)
# print(set1)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# lst = [[101,"C1"],[101,"C2"],[102,"C1"],[101,"C2"],[102,"C1"],
#        [102,"C1"],[102,"C1"],[102,"C1"],[103,"C1"]]
# lst_id=[]
# lst_cpn = []
#
# for i in range(len(lst)):
#     for j in range(2):
#         if lst[i][0] not in lst_id:
#             lst_id.append(lst[i][0])
#             lst_cpn.append(lst[i])
#
# print(lst_id)
# print(lst_cpn)
# lst = [[101,"C1"],[101,"C2"],[102,"C1"],[101,"C2"],[102,"C1"],
#        [102,"C1"],[102,"C1"],[102,"C1"],[103,"C1"]]
#
# for i in range(len(lst)):
#     a = i
#     while(a<len(lst)):
#         if lst[i][0]==lst[a][0]:
#             lst.remove(lst[a])
#         a+=1
# print(lst)

# employee={"Name":"Abhi","Exp":1,"Skill":["java","python"]}
# print(employee)
# print(type(employee))
# print(employee.get("email","sorry"))
# employee["email"]="abc@gmail.com"
# print(employee.get("email","sorry"))
# print(employee.keys())
# print(employee.values())
# print(employee.items())
# for i,j in employee.items():
#     print(f"{i} : {j}")

emp = ["ram","shyam","Abhi"]
key = ["Dev","Devops","Tester"]
# project = dict.fromkeys(key,emp)
# print(project)


project = dict.fromkeys(key)
print(project)
j=0
for i in project.keys():
    project[i]=emp[j]
    j+=1
print(project)

project.setdefault("Manager")
print(project)
project.setdefault("It","Aman")
print(project)
