a, b, c = map(int, input().split())
ans = -1
for i in range(a, b + 1):
    if i % c == 0:
        ans = i
        break

print(ans)





a, b, c = map(int, input().split())
ans = a + c - (a % c) if a % c else a
print(ans if a <= ans <= b else -1)