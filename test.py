
n = int(input())
for i in range(n):
    C_name = input()
    NameList = [x[0] for x in C_name.split()]
    print("".join(NameList))