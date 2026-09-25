# square of numbers

num = [1, 2, 3, 4, 5]
squares = [x*x for x in num]
print("Squares: ", squares)


# even numbers

num = [1, 2, 3, 4, 5]
even = [x for x in num if x % 2 == 0]
print("Even numbers: ", even)


# multiply by 2


num = [1, 2, 3, 4, 5]
ans = [x*2 for x in num]
print("Ans: ", ans)



# Positive numbers

num = [1, 2, 3, 4, 5, -1, -2]
positive = [x for x in num if x > 0]
print("Positive num: ", positive)


# length of words

words = ["apple", "panda", "cat"]
length = [len(x) for x in words]
print("Lengths: ", length)
