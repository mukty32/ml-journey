a = input().split()
n = int(a[0])
h = int(a[1])
height = input().split()

width = 0
for x in height:
    x = int(x)
    if x > h:
        width = width + 2
    else:
        width = width + 1
print(width)