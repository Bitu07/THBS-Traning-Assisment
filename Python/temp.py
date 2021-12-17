def xor(arr):
    ans = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            ans = (arr[i]^arr[j])
    return ans

n=int(input())
arr = list(map(int,input().split()))
out = xor(arr)
print(out)