import sys

var=200
dec_var=22.6
str_var="Apple"
print(var)
print(dec_var)
print(str_var)
print(type(var))
print(type(dec_var))
print(type(str_var))
print(sys.getsizeof(var))
print(sys.getsizeof(dec_var))
print(sys.getsizeof(str_var))

str_var="hello, how are you doing today"
print(sys.getsizeof(str_var))

a, b = 3, 6
print(a)
print(b)

i=1,2,3
print(i)
i=(1,2,3)
print(i)

num1="10"
num2="20"
print(num1+num2)
print(int(num1) + int(num2))

var1 = eval(input("Enter the value 1: "))
var2 = eval(input("Enter the value 2: "))
var3 = eval(input("Enter the value 3: "))
print(type(var1))
print(type(var2))
print(type(var3))

x,y,z = input("Enter the value: ").split(",")
print(x)
print(y)
print(z)

# Arithematic Operators --> + - * / % ** //

import sys
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Relational Operator --> > < >= <= != ==
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

# Assignment Operator +=, -=, *=, /=, =
# bitwise operator

x=4
y=5
print(x&y)
print(x|y)
print(~y)
print(10<<2)
print(5>>3)
print(x^y)

#Logical operator and,or,not

# print(sep=" ",end="\n",file=sys.stdout,flush=false)
a,b,c = 10,20,30
print(a,end="**")
print(a,b)
print(a,b,c,sep=", ",end="@")
print("12")
