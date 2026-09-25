n = int(input())
count = 0

for x in range(n):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])

    if a + b + c >= 2:
        count += 1

print(count)
