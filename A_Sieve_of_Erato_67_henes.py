test = int(input())
for _ in range(test):
    size = int(input())
    lst = list(map(int, input().split()))
    print("YES" if 67 in lst else "NO")