
# Problem link : https://codeforces.com/contest/2036/problem/A

t = int(input().strip())

for _ in range(t):

    n = int(input().strip())

    notes = list(map(int, input().strip().split()))
    is_perfect = True
    for i in range(1, n):
        interval = abs(notes[i] - notes[i - 1])
        if interval != 5 and interval != 7:
            is_perfect = False
            break
    if is_perfect:
        print("YES")
    else:
        print("NO")


