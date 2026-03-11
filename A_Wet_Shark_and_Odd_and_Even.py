size = int(input())
lst = list(map(int, input().split()))

ans = sum(lst)
lst.sort()
minOdd = 10**18
for num in lst:
    if num % 2:
        minOdd = num
        break

ans = ans - minOdd if ans % 2 else ans
print(ans)





size = int(input())
lst = list(map(int, input().split()))

minOdd = min((x for x in lst if x % 2), default=-1)
ans = sum(lst)
ans = ans - minOdd if ans % 2 else ans
print(ans)