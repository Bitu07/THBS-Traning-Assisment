# class Convert:
#     def __init__(self): # default constructor
#         self.str1 = ""
#
#     def get(self):
#         self.str1 = input("Enter Name in Lower case : ")
#
#     def printupper(self):
#         print("In Upper Case : " , self.str1.upper())
#
# str1 = Convert()
# str1.get()
# str1.printupper()


# from enum import Enum
#
# class Country(Enum): # Enum is a predefined class
#     Iceland = 354
#     India =91
#     Indonesia = 62
#     Iran =98
#     Iraq =964
#     Ireland =353
#
# print('Member value: {}'.format(Country.India.value))
#
# print()
# for data in Country:
#     print('{:25} = {}'.format(data.name, data.value))



# Class to sort Country name by Country Code and sorted code List
# import enum
#
# class Country(enum.IntEnum):
#     Afghanistan = 93
#     Antarctica = 672
#     Andorra = 376
#     Albania = 355
#     Algeria = 213
#     Angola = 244
#
# print('Country Name ordered by Country Code:')
# print('\n'.join(' ' + c.name for c in sorted(Country)))
#
# print("Original Code List : ", list(map(int, Country)))
# print("Sorted Code List : ", list(map(int, sorted(Country))))



# from collections import Counter, defaultdict
#
# States = (
#     ('TN', 'Chennai'),
#     ('AP', 'Guntur'),
#     ('TN', 'Madurai'),
#     ('KL', 'Cochin'),
#     ('AP', 'Chithoor'),
#     ('TN', 'Coimbatore'),)
#
# citylist = defaultdict(list)
#
# for statename, cityname in States:
#     citylist[statename].append(cityname)
#
# print(citylist)
#
# citycount= Counter(statename for statename, no in States)
# print("Count Citywise : " ,citycount)



