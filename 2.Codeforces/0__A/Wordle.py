# Problem link: https://www.codechef.com/practice/course/strings/STRINGS/problems/WORDLE


for _ in range(int(input())):
    result = ""
    S_String = str(input())
    T_String = str(input())
    for i in range(len(S_String)):
        if S_String[i] == T_String[i]:
            result += "G"
        else:
            result += "B"
    print(result)
