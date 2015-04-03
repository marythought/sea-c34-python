# lambda

"""
Add the file to your local working repository and commit
 changes frequently while working on the following tasks.
  When you are done, push your changes to GitHub and create
   a pull request titled Task 15 pull request from Your Name
    where you should substitute your name for Your Name.

Write a function that returns a list of n functions,
such that each one, when called, will return the input
 value, incremented by an increasing number.

Use a for loop, a lambda, and a keyword argument

( Extra credit ):

Do it with a list comprehension, instead of a for loop

Not clear? here’s what you should get:

In [96]: the_list = function_builder(4)
### so the_list should contain n functions (callables)
In [97]: the_list[0](2)
Out[97]: 2
## the zeroth element of the list: a function that adds
0 to the input
In [98]: the_list[1](2)
Out[98]: 3
## the 1st element of the list: a function that adds 1
 to the input
In [100]: for f in the_list:
   .....:     print(f(5), end=" ")
   .....:
5
6
7

"""
