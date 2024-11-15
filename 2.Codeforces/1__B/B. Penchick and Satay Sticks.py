
# https://codeforces.com/contest/2031/problem/B

def solve():
    n = int(input())

    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] != i + 1 and a[i] != i and a[i] != i + 2:
            print("no")
            return

    print("yes")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
