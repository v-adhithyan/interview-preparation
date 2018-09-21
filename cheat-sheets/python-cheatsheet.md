# Python Cheat sheet

## Common builtin functions

|Syntax   |Description    |
|:-------:|:-------------:|
|abs(x)   |Returns the absolute value of a number|
|chr(int) |Returns the character for the given ascii value|
|divmod(x,y)|Returns x//y, x%y as a tuple|
|isintance(obj, class)| Checks if the object is instance of given class|
|max| Returns the maximum element|
|min| Returns the minimum element|
|ord(char) | Returns the ascii value of the character|
|pow(x,y)|Raises x to the power y. Equivalent to x**y|
|range(n)|Construct an iteratble of value 0 to n-1|
|range(start, n)|Construct an iterable fo values from start to start+n-1|
|range(start, n, step)| Construct an iterable like [start, start+step, start + (2 x step) ... start+(n-1 x step) ]|
|reversed(sequence)|Reverse the given sequence|
|round(x)|Round the given number|
|round(x, k)|Round the given number to k points.|
|sorted()|sorts the given sequence|

## Python modules

- array 
- collections
- copy (object copying support)
- heapq (provides heap based priority queue functions)
- math
- os
- random
- re (regular expression support)
- sys
- time

## random modules

|Syntax|Description|
|:----:|:----------|
|<b><i>random.seed(a)</b></i>|Initiate random number generator based on seed value|
|<b><i>random.random()</b><i>|returns random number in range 0.0 - 0.1|
|<b><i>random.randint(a,b)</b><i>|generate a random number within a and b|
|<b><i>random.randrange(start, stop, step)</b><i>|Returns the random number from the range provided.|
|<b><i>random.choice(array)</b><i>|Returns a random value from the array passed.|
|<b><i>random.shuffle(array)</b><i>|Shuffles the array randomly.|
