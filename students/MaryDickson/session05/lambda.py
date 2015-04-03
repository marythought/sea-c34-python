# lambda

"""
Write a function that returns a list of n functions,
such that each one, when called, will return the input
 value, incremented by an increasing number.

Use a for loop, a lambda, and a keyword argument
"""


def function_builder(num):
    return [(i + num) for i in range(0, num)]

listy = [function_builder]

# well this is odd!  but it does something, anyway.

print listy[0](2)[0]
print listy[0](4)[3]
print listy[0](10)[3]

# below are some uses of lambda I tried (unsuccessfully):

# print (lambda x: x > 2)(3)
# print (lambda x, y: (y + x) for i in range(0, y))
