# Problem Link: https://codeforces.com/contest/2019/submission/283364173



def getMaxscore(a,n,start):
    max_val = 0
    count = 0
    for i in range(start,n,2):
        max_val = max(max_val,a[i])
        count +=1
    return max_val + count
def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        first_from_0 = getMaxscore(a,n,0)
        second_from_1 = getMaxscore(a,n,1)
        print(max(first_from_0,second_from_1))
if __name__ == '__main__':
    main()


