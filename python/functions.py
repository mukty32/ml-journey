# simple function

def hello():
    print("Helo python")

hello()


# function with parameters

def add(a, b):
    return a + b
# ans = add(5, 8)
print("Sum: ", add(2, 5))




# *args

# def num(*args):
#     print(args)
# num(1, 2, 3, 4)



def add(*args):
    sum = 0
    for x in args:
        sum += x

    return sum

print("Sum: ", add(1, 2))
print("Sum: ", add(1, 2, 3, 4, 5, 6))



# **kwargs

def student(**kwargs):
    print(kwargs)

student(name= "mukty", id = 321, dept = "CSE")