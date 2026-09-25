def cal(num):
    sum = 0
    for x in num:
        sum += x

    average = sum / len(num)

    maximum = max(num)
    return average, maximum

num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])

average, maximum = cal(num)
print("Average: ", average)
print("Maximum: ", maximum)