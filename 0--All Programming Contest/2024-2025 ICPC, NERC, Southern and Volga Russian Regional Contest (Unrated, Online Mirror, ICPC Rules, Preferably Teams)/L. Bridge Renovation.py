# Problem link: https://codeforces.com/contest/2038/problem/L

def calculate_min_planks(N):
    plank_length = 60

    _total18 = N
    total21 = N
    total25 = N
    total_planks = 0

    while _total18 > 0 or total21 > 0 or total25 > 0:
        used18 = 0
        used21 = 0
        used25 = 0
        remaining_length = plank_length

        while remaining_length >= 25 and total25 > 0:
            remaining_length -= 25
            used25 += 1
            total25 -= 1

        while remaining_length >= 21 and total21 > 0:
            remaining_length -= 21
            used21 += 1
            total21 -= 1

        while remaining_length >= 18 and _total18 > 0:
            remaining_length -= 18
            used18 += 1
            _total18 -= 1

        total_planks += 1

    return total_planks


N = int(input())
result = calculate_min_planks(N)
print(result)
