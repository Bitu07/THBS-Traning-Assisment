# num1 = eval(input("enter two num1: "))
# num2 = eval(input("enter two num2: "))
# if(num1==num2):
#     print(num1+num2)
# else:
#     print((num1+num2)*2)

# total = int(input("enter total amount: "))
# a5 = int(input("enter available 5rs coin: "))
# a1 = int(input("enter available 1rs coin: "))
#
# r5 = int(total/5)
# r1 = total%5
# print(r5)
#
# if(((r5*5) + r1)==total and r1<=a1 and r5<=a5):
#     print("total 5 rs coin: ",r5)
#     print("total 1 rs coin: ",r1)
# else:
#     print("-1")

# x=0
# for i in "traning":
#     for j in "aeiou":
#         if(i==j):
#             x=x+1
# print("v: ",x)
# print("c: ",len("traning")-x)

# fruit = ["apple","banana","mango"]
# dish = ["milkshake","salad","juice"]
#
# for i in fruit:
#     for j in dish:
#         print(j,i)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#
# a=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         a=a+1
#         print(a,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
#
# for i in range(4,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()
#
# for i in range(4,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#
# for i in range(4,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# a=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         a=a+1
#         print(a*2,end=" ")
#     print()
# n = int(input("val: "))

# r=5
# for i in range(1,r):
#     n=1
#     for j in range(r,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(n,end=" ")
#             n=n+1
#     print()

# r=5
# for i in range(1,r):
#     n=1
#     for j in range(r,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(j,end=" ")
#             n=n+1
#     print()
#
#
# r=5
# for i in range(1,r):
#     n=1
#     for j in range(r,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(i,end=" ")
#             n=n+1
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()

# l=[]
# for i in "appleeppp":
#     if i not in l:
#         l.append(i)
#     else:
#         print(i,end=" ")

x=3256

a= x//2000
x=x%2000

b= x//500
x=x%500

c=x//200
x=x%200

d=x//50
x=x%50

e=x//5
x=x%5

f=x//1
x=x%1

print("2000 : ",a)
print("500 : ",b)
print("200 : ",c)
print("50 : ",d)
print("5 : ",e)
print("1 : ",f)