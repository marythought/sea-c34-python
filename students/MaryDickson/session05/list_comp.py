# I took the quiz before seeing this assignment, so...

"""
Using a list comprehension, return the number of even ints in the given array.

Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) == 3
count_evens([2, 2, 0]) == 3
count_evens([1, 3, 5]) == 0
def count_evens(nums):
   one_line_comprehension_here

"""

# one way to do it, label and count


def count_evens(nums):
    return[("odd", "even")[i % 2 == 0] for i in nums].count("even")

print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])

# here's another way to do it, positive == 1 and then sum:


def count_evens2(nums):
    return sum([int(i % 2 == 0) for i in nums])

print count_evens2([2, 1, 2, 3, 4])
print count_evens2([2, 2, 0])
print count_evens2([1, 3, 5])
