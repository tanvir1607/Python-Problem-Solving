test = int(input())
for _ in range(test):
    size, s, x  = map(int, input().split())
    lst = map(int, input().split())
    total = sum(lst)
    print("YES" if s >= total and (s - total) % x == 0 else "NO")