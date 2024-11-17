# Problem link : https://codeforces.com/contest/2037/problem/A
def maximum_score(test_cases):

    results = []
    for n, array in test_cases:
        freq = {}
        for num in array:
            freq[num] = freq.get(num, 0) + 1
        score = sum(count // 2 for count in freq.values())
        results.append(score)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    test_cases.append((n, array))
results = maximum_score(test_cases)
for result in results:
    print(result)


