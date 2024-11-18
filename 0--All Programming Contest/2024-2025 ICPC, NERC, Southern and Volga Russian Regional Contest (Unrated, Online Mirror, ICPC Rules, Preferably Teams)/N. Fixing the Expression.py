
# Problem link: https://codeforces.com/contest/2038/problem/N

import sys
DEBUG = False
def debug(x):
    if not DEBUG:
        return
    print(f"DEBUG: {x}", file=sys.stderr)

def solve(s):
    a = s[0]
    b = s[2]
    op = s[1]

    if (op == '<' and a < b) or (op == '>' and a > b) or (op == '=' and a == b):
        return s

    if a < b:
        s = f"{a}<{b}"
    elif a > b:
        s = f"{a}>{b}"
    else:
        s = f"{a}={b}"
    return s

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":


    main()
