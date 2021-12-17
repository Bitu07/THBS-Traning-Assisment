# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
# total = (x * y) + (y * z) + (x * z)
# l = []
# for i in range(total):

# 1

# count = 0
# n = int(input())
# l1 = list(map(int, input().split(" ")))
#
# for i in range(1, len(l1)):
#     if l1[i] % 2 == 0 and l1[i] == l1[i - 1]:
#         count = count + 1
# print(count)


# 1

# count = 0
# n = int(input())
# l1 = input().split(" ")
#
# for i in range(1, n):
#     if int(l1[i]) % 2 == 0 and int(l1[i]) == int(l1[i-1]):
#         count = count + 1
# print(count)


# 2

# import math
# n = int(input())
# l1 = list(map(int, input().split(" ")))
# for i in range(n):
#     sq = int(math.sqrt(l1[i]))
#     print(sq)
#     if l1[i] != sq * sq:
#         l1.remove(l1[i])
#         l1.insert(i, 0)
#
# print(l1)



# 3

# count = 1
# def rec(n):
#     global count
#     if n<=1:
#         return count
#     else:
#         count = count + n * 5 - 5
#         return rec(n-1)
#
# n=int(input())
# print(rec(n))
