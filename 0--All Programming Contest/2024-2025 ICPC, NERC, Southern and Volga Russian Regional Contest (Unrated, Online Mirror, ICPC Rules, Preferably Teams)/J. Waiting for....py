# Problem link: https://codeforces.com/contest/2038/problem/J

def can_monocarp_board(n, e):

    count = 0
    results = []

    for i in e:
        if i[0] == 'P':
            count += i[1]
        elif i[0] == 'B':
            bi = i[1]
            if bi > count:
                results.append("YES")
            else:
                results.append("NO")
            count = max(0, count - bi)

    return results

n = int(input())
events = []

for _ in range(n):
    line = input().split()
    if line[0] == 'P':
        events.append(('P', int(line[1])))
    elif line[0] == 'B':
        events.append(('B', int(line[1])))

results = can_monocarp_board(n, events)
print("\n".join(results))