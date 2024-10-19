# Problem_link : https://vjudge.net/contest/664316#problem/K


def main():

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0

        while True:
            flag = 0
            for i in range(n - 1):
                if arr[i] < arr[i + 1]:
                    differ = arr[i + 1] - arr[i]
                    arr[i] += differ
                    count += 1
                    break
                if arr[i] > arr[i + 1]:
                    differ = arr[i] - arr[i + 1]
                    arr[i + 1] += differ
                    count += 1
                    break
            else:  # No break occurred
                break

            for i in range(n - 1):
                if arr[i] != arr[i + 1]:
                    flag = 1
                    break

            if flag == 0:
                break

        print(count)


if __name__ == "__main__":
    main()
