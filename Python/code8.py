class sample:
     def reversewords(self,word):
         return " ".join(reversed(word.split()))


x = input("-> ")
c1 = sample()
print(c1.reversewords(x))
a=c1.reversewords(x)

s1=""
for i in a:
    s1=i+s1

print(s1)
data = a.split()
print(data)

for li in data:
    print("".join(reversed(li)),end=" ")
