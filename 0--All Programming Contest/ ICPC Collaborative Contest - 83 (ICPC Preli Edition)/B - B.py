
# Problem link: https://vjudge.net/contest/669749#problem/B
def check_xor_zero(n ,arr):
    for x in range(n - 3):
        for y in range(x + 1, n - 2):
            for z in range(y + 1, n - 1):
                for w in range(z + 1, n):

                    if arr[x] ^ arr[y] ^ arr[z] ^ arr[w] == 0:
                        return True
    return False
n = int(input())

arr =  list(map(int,input().split()))
if check_xor_zero(n,arr):
    print("Yes")
else:
    print("No")
