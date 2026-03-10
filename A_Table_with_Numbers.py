test = int(input())
for _ in range(test):
    size, h, w = map(int, input().split())
    lst = list(map(int, input().split()))

    h, w = min(h, w), max(h, w)
    cntH = sum(1 for num in lst if num <= h)
    cntW = sum(1 for num in lst if num <= w)
    print(min(cntH, cntW // 2))
