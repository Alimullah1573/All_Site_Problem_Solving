
# Problem_link : https://vjudge.net/contest/664316#status/Alimulla/H/0/


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    score = 0
    arr.sort()
    for i in range(n):
        differ = arr[n - i - 1] - arr[i]
        score += differ

    print(score)

