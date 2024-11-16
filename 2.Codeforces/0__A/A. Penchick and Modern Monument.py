# Division 2
# Problem link: https://codeforces.com/contest/2031/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq_map = {}
    for num in a:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_freq = max(freq_map.values())
    result = n - max_freq
    print(result)
