
# Problem Link : https://codeforces.com/problemset/problem/381/A
sereja = 0
dima =  0
n = int(input())
a = list(map(int,input().split()))
while a:
    b = [a[0], a[-1]]
    m = max(b)
    sereja += m
    a.remove(m)
    if a:
        c = [a[0], a[-1]]
        n = max(c)
        dima += n
        a.remove(n)

print(sereja, dima)
