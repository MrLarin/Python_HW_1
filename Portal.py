n = (i for i in input().split())
num = [int(i) for i in n]
temp = 0
for i in range(len(num)):
    if num[i] % 2 == 0 and i >= 1:
        temp = num[i]
        num[i] = num[i-1]
        num[i-1] = temp
    elif num[i] % 2 != 0 and i < len(num)-1:
        temp = num[i]
        num[i] = num[i+1]
        num[i+1] = temp
print(*num, sep=" ", end="")
