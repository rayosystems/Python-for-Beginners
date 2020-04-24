#!/usr/bin/python

# Understanding Variables in Python 

# Go to the python intrective shell
>>> x = 5			# Here variabe x has been assigned a value 5
>>> x				# Variable can be directly printed by typing just x and hit enter.
5
>>> y = 7
>>> y
7
>>> x+y
12
>>> z=x+y			# Now, a new variable z has been assigned the value - sum of x+y 
>>> z
12
>>> z=z+1			# Now, changing the variable's value  
>>> z
13
>>> z=z+1
>>> z
14
>>> x=y
>>> x
7
>>> y
7
>>> y=9
>>> y
9
>>> x
7
>>> print(x)
7
>>> print(y)
9
>>> print(z)
14
>>>
>>> print(x,y,z)
7 9 14
>>> print(x,y,z,sep=',')
7,9,14
>>> print("x is:", x)				
x is: 7
>>> print("y is:", y)
y is: 9
>>> print("z is:", z)
z is: 14
