# class supermarket:
#     pass
#
# s1 = supermarket()
# s1.pname = input("Enter the Product name: ")
# s1.qnt=int(input("Enter Quantity: "))
# s1.price = eval(input("Enter the price: "))
#
# print(s1.pname,s1.qnt,s1.price,sep=" ")
# print("total ",s1.qnt*s1.price)

# class supermarket:
#     pname = input("Enter the Product name: ")
#     qnt = int(input("Enter Quantity: "))
#     price = eval(input("Enter the price: "))
#
# s1 = supermarket()
# s2 = supermarket()
# print(s1.pname, s1.qnt, s1.price, sep=" ")
# print("total ", s1.qnt * s1.price)

# print(s2.pname, s2.qnt, s2.price, sep=" ")
# print("total ", s2.qnt * s2.price)


# class supermarket:
#
#     def __init__(self,pname,qnt,price):
#         self.pname=pname
#         self.qnt=qnt
#         self.price = price
#
# s1 = supermarket("xyz",3,20)
# s2 = supermarket("abc",2,40)
# print(s1.pname, s1.qnt, s1.price, sep=" ")
# print("total ", s1.qnt * s1.price)
#
# print(s2.pname, s2.qnt, s2.price, sep=" ")
# print("total ", s2.qnt * s2.price)
#
#
# print(s1.pname, s1.qnt, s1.price, sep=" ")
# print("total ", s1.qnt * s1.price)
#
# print(s2.pname, s2.qnt, s2.price, sep=" ")
# print("total ", s2.qnt * s2.price)


class supermarket:

    def __init__(self,pname,qnt,price):
        self.pname=pname
        self.qnt=qnt
        self.price = price

s1 = supermarket(input("Enter the pname: "),int(input("Enter the quantity: ")),eval(input("Enter the price: ")))
# s2 = supermarket("abc",2,40)
print(s1.pname, s1.qnt, s1.price, sep=" ")
print("total ", s1.qnt * s1.price)

# print(s2.pname, s2.qnt, s2.price, sep=" ")
# print("total ", s2.qnt * s2.price)
