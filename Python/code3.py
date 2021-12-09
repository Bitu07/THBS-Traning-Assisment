# num = [7,5,3,1,9,6,2,4,8]
# print(len(num))
# print(num)
# print(type(num))
# print(num[0::2])
# print(num[0::3])
# print(num[-1::-3])

# airlines=["AI","SJ","JA","EM","AA"]
#         #  0   1     2    3    4
#         # -5  -4    -3   -2   -1
# print(airlines[1:])
# print(airlines[:2])
# print(airlines[:-2])
# print(airlines[-5:])
#
# print(airlines[1:-2])
# print(airlines[:5])
# print(airlines[-6:])
# print(airlines[-6:2])
# print(airlines[-3:5])

# dum = [1,2,["apple","mango"],33.6]
# print(dum[2][1])
# import copy
#
# course = ["ME","ECE","IT","CSE"]
# for i in course:
#     print(i)
#
# for index,val in enumerate(course):
#     print(f"{index} : {val}")
#
# for index,val in enumerate(course,start=1):
#     print(f"{index} : {val}")
#
# course.append("CE")
# print(course)
# course.insert(2,"AE")
# print(course)
# course2=["MBA","BBM"]
# course.extend(course2)
# print(course)
#
# print(course.remove("ECE"))
# print(course.pop())
#
# course_sort = sorted(course)
# print(course_sort)
#
# print(course.index("IT"))
# print(course.index("IT",0,3))
#
# course.sort()
# print(course)
# course.sort(reverse=True)
# print(course)
#
# course_str = ','.join(course)
# print(course_str)
# course_list = course_str.split(",")
# print(course_list)
#
# import copy
#
# bus = ["BBA","MBA"]
# tech = ["CS","IT"]
# course = bus + tech
# print(course)
# course[len(bus):]=tech
# print(course)
#
# frt=["mango","apple"]
# frt1=frt
# frt2=copy.copy(frt)     # SHALLOW COPY:  the pointer points to the same copy of objects of class
# frt3=copy.deepcopy(frt) # DEEP COPY:  it will create copy of each object inside of the class
# print(frt)
# print(frt1)
# print(frt2)
# print(frt3)
# print()
#
# frt.append("grapse")
# print(frt)
# print(frt1)
# print(frt2)
# print(frt3)
# print()
#
# frt2.insert(0,["mech","tech"])
# print(frt)
# print(frt1)
# print(frt2)
# print(frt3)
# print()
#
# print(id(frt))
# print(id(frt1))
# print(id(frt2))
# print(id(frt3))

# lst = input("--> ").split(",")
# lst2=[]
# lst3 = []
#
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
#
# for index,i in enumerate(lst2):
#     # print(f"{i} : {lst.count(i)}")
#     lst3.append(lst.count(i))
#
# print()
# print(f"{lst2[lst3.index(max(lst3))]} : {max(lst3)}")
# lst = [1,2,3,0,5,0,0,0,0,1,0,2,5,6]
# lst.sort(reverse=True)
# print(lst)

#
# lst = [1,2,3,0,5,0,0,0,0,1,0,2,5,6]
# for i in lst:
#     if i==0:
#         lst.remove(i)
#         lst.append(i)
# print(lst)

# lst = [1,2,5,6,1,2,3]
# l=[]
# # for index,i in enumerate(lst):
# #     if(index%2!=0):
# #         l.append(lst[index-1:index+1])
# #     elif(index>len(lst)-2):
# #         l.append(lst[index])
# # print(l)
#
# for i in range(0,len(lst),2):
#     l.append(lst[i:i+2])
#
# print(l)

# li=[]
# for i in range(6):
#     li.append(i*i)
# print(li)
#
# li=[i*i for i in range(6)]
# print(li)
#
# li = [i for i in range(6) if i%2==0]
# print(li)
#
# li=["even" if i%2==0 else "odd" for i in range(11)]
# print(li)


