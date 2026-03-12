test = int(input())
for _ in range(test):
    size, remove = map(int, input().split())
    txt = input()

    freq = {}
    for char in txt:
        freq[char] = freq.get(char, 0) + 1
    odd_cnt = sum(val % 2 for val in freq.values())
    print("YES" if odd_cnt - remove <= 1 else "NO")
    