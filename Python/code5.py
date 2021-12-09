# # name="Abhishek"
# # print(name[:4])
# # print(name[:-4])
# # print(name[::-1])
# # for i in name:
# #     print(i)
# #
# # print(name.lower())
# # print(name.upper())
# # print(name.isupper())
# # print(name.islower())
# # print(name.isalnum())
# # print(name.count("h"))
# # print(name.find("i"))
# # str="hello world world"
# # str2 = str.replace("world","Abhi",1)
# # print(str2)
# # print(name.capitalize())
# fname="Abhi"
# lname="Yadav"
# loc="Guj"
# print("this is ",fname+lname)
# print("this is ",fname+" "+lname)
# print("this is ",fname,lname)
# print(fname+ " " +lname+" is from "+loc)
# str2 = "{} {} is from {}"
# print(str2.format("Abhi","yadav","Guj"))
# print(str2.format("Nitin","Gour","UP"))
# msg="{} {} is from {}".format("Aman","chandel","delhi")
# msg2="{str_fname} {str_lname} is from {str_loc}".format(str_fname="ABhi",str_lname="Yadav",str_loc="India")
# print(msg)
# print(msg2)
# msg3="<{tag_val}>monthly sales report</{tag_val}>".format(tag_val="h1")
# print(msg3)
# msg4=f"{fname} {lname} is from {loc}"
# print(msg4)
# biodata={"fname":"Abhi","lname":"yadav","loc":"Guj"}
# print("{} {} is from {}".format(biodata["fname"],biodata["lname"],biodata["loc"]))
# print(".. {0[fname]} {0[lname]} is from {0[loc]}".format(biodata))
#
#
# import datetime
# x=datetime.datetime.now()
# print(x)
# dat = "{:%B %d,%Y}".format(x);
# print(dat)

# sen = input("--> ")
# c=0
# d=0
# for i in range(len(sen)):
#     if sen[i].isdigit():
#         d+=1
#     elif sen[i].isalpha():
#         c+=1
#
# print("total letter count: ",c)
# print("total digit count: ",d)

# u=0
# l=0
# for i in sen:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
# print("total Upper Case count: ", u)
# print("total Lower Case count: ", l)

# str="python"
# print(str[1:6:2])
# print(round(2.5))
# print(round(5.6))
# print(round(5.4))
#
# sal = 100000
# print("{:,}".format(sal))
# print(abs(-4))
# print(bool(1))
# print(bool(0))
# print(bin(8))
# print(ord("a"))
# print(chr(97))
# for i in range(2211,2222):
#     print(chr(i),end=" ")
#
# txt = "{0:X}"
# print(txt.format(255))
#
# txt = "{0:o}"
# print(txt.format(255))
#
# print(divmod(9,2))

# def fun():
#     print("function called")
#
# fun()
#
# def sum():
#     a=10
#     b=20
#     print("sum: ",a+b)
#
# def sub():
#     a = 10
#     b = 20
#     print("sub: ", b-a)
#
# sum()
# sub()

# def sum_num(num1,num2):
#     print(num1+num2)
#
# a=20
# b=10
# sum_num(a,b)
#
# def sqr_fun(x):
#     c=x*x
#     print(c)
# sqr_fun(10)
#
# print(sqr_fun(10))
# sqr_fun=lambda x:x*x

# def cal_tax(sal,tax ):
#     tx_amnt = sal*tax
#     th_tax=sal-tx_amnt
#     return th_tax
#
# cal_tax = lambda sal,tax :sal-sal*tax
#
# emp1={"name":"Abhi","sal":10000,"tax":0.03,"th_sal":None}
# emp2={"name":"Aman","sal":15000,"tax":0.04,"th_sal":None}
# emp1["th_sal"]=cal_tax(emp1["sal"],emp1["tax"])
# emp2["th_sal"]=cal_tax(emp2["sal"],emp2["tax"])
# print(emp1["th_sal"])

# num = [1,2,3,4,5,6,7,8,9,10]
# l2 = list(filter(lambda x:(x%2==0),num))
# print(l2)
#
# l3=list(map(lambda x:x*x,num))
# print(l3)
#
# num = [1,2,3,4,5,6,7,8,9,10]
# l4 = list(map(lambda x:(x%2==0),num))
# print(l4)
#
# l5=list(filter(lambda x:x*x,num))
# print(l5)


credit = lambda amount, credit: amount + credit
debit = lambda amount, debit: amount - debit

# ac = {"name":"Abhi","amount":0}
# msg = "{} you have ${} in your AC"


# while(True):
#     print("!! Welcome !!")
#     i = int(input("1. Credit \n2. Debit \n\n-->"))
#
#     if(i == 1):
#         cr = int(input("Enter Amount: "))
#         ac["amount"] = credit(ac["amount"],cr)
#         print(f"{cr} is added in your AC")
#
#         print()
#
#     elif(i == 2):
#         db = int(input("Enter Amount: "))
#         ac["amount"] = debit(ac["amount"], db)
#         print(f"{db} is debited from your AC")
#         print()
#
#     print(msg.format(ac["name"], ac["amount"]))

# def account(l):


# l = [("D",200),("D",300),("W",100)]