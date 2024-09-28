

# Problem link : https://www.codechef.com/practice/course/strings/STRINGS/problems/DNASTORAGE

for _ in range(int(input())):
    size = int(input())
    binary_String = str(input())

    new_list = []
    result = ""
    for i in range(0,size,2):
        new_list.append(binary_String[i: i+2])
    for j in new_list:
        if j == "00":
            result += "A"
        elif j == "01":
            result += "T"
        elif j == "10":
            result += "C"
        elif j == "11":
            result +="G"
    print(result)



'''import re

a = "010101"

# Use regex to find all pairs of digits
output = tuple(re.findall('..', a))

print(output)'''
