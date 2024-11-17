# c Problem link : https://codeforces.com/contest/2037/problem/C

def solve():
    n = int(input())

    if n < 5:
        print(-1)
        return
    result = [1, 3]
    for i in range(7, n + 1, 2):
        result.append(i)
    result.extend([5, 4, 2])
    for i in range(6, n + 1, 2):
        result.append(i)

    print(" ".join(map(str, result)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()