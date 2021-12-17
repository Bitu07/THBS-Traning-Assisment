l = [10,20,30]

i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
while True:
    try:
        print(next(i))
    except StopIteration:
        break


