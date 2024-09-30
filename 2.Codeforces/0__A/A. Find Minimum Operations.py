# Problem link :   https://codeforces.com/contest/2020/my

def find_min_oper(n, k):
    if k == 1:
        return n
    result = 0
    while n:
        result += n % k
        n //= k
    return result

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(find_min_oper(n, k))

if __name__ == "__main__":
    main()
