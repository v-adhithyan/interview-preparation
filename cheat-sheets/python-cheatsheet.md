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

## Python oops convention

- Names beginning with single underscore are protected
  - example : ```self._protected = "I am protected"```
- Names beginning with double underscore are private.
  - example: ```self.__private = "I am private. I am not accessible by child classes."```

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

## array (compact arrays)

  - Similar to list in Python. Sample usage
  ```primes = array('i', [2, 3, 5, 7])```
  
  - The first argument represents the type of array, whether it is int or char etc.
  
  - The array module does not provide support for making compact arrays of user- defined data types. Compact arrays of such structures can be created with the lower- level support of a module named ctypes. (See Section 5.3.1 for more discussion of the ctypes module.)
 
## metaclass

-  A metaclass is different from a superclass, in that it provides a template for the class definition itself. Specifically, the ABCMeta declaration (from abc module) assures that the constructor for the class raises an error.

## namespaces

- A namespace is an abstraction that manages all of the identifiers that are defined in a particular scope, mapping each name to its associated value. In Python, functions, classes, and modules are all first-class objects, and so the “value” associated with an identifier in a namespace may in fact be a function, class, or module.
- A first class object is an entity that can be dynamically created, destroyed, passed to a function, returned as a value, and have all the rights as other variables in the programming language have.
- In Java, for example, there are primitive types (int, bool, double, char) that aren't proper objects. That's why Java has to introduce Integer, Boolean, Double and Character as first-class types. This can be hard to teach to beginners -- it isn't obvious why both a primitive type and an class have to exist side-by-side.It also means that an object's class is -- itself -- an object. This is different from C++, where the classes don't always have a distinct existence at run-time.
- [Reference](https://stackoverflow.com/questions/245192/what-are-first-class-objects)

## types of namespaces

### instance namespace
- Every instance of a python class will have a dedicated namespace to  manage such values.
- The use of self will in an assignment will make the member to be in instance namespace.

### class namespace
- There is a separate class namespace for each class that has been defined. This namespace is used to manage members that are to be shared by all instances of a class, or used without reference to any particular instance.
- When something is to be shared by all instance of a class, it will be stored in class namespace.

## dictionaries and __slots__ declaration
- By default, Python represents each namespace with an instance of the built-in dict class (see Section 1.2.3) that maps identifying names in that scope to the associated objects.
- While a dictionary structure supports relatively efficient name lookups, it requires additional memory usage beyond the raw data that it stores.
- Python provides a more direct mechanism for representing instance namespaces that avoids the use of an auxiliary dictionary. To use the streamlined representation for all instances of a class, that class definition must provide a class-level member named     slots     that is assigned to a fixed sequence of strings that serve as names for instance variables.
- example 
```
class CreditCard:
slots = '_customer' , '_bank' , '_account' , '_balance' , '_limit'
```
## name resolution

1. The instance namespace is searched; if the desired name is found, its associ- ated value is used.
2. Otherwise the class namespace, for the class to which the instance belongs, is searched; if the name is found, its associated value is used.
3. If the name was not found in the immediate class namespace, the search con- tinues upward through the inheritance hierarchy, checking the class name- space for each ancestor (commonly by checking the superclass class, then its superclass class, and so on). The first time the name is found, its associate value is used.
4. If the name has still not been found, an AttributeError is raised.

## dynamic dispatch

Python uses what is known as dynamic dispatch (or dynamic binding) to determine, at run-time, which implementation of a function to call based upon the type of the object upon which it is invoked.

## shallow copy
```
  frameworks = ["struts", "angular"]
  latest_frameworks = list(frameworks)
```
This causes a new list to be created, as shown in Figure however, it is what is known as a ***shallow copy***. The new list is initialized so that its contents are precisely the same as the original sequence. However, Python’s lists are referential and so the new list represents a sequence of references to the same elements as in the first. This can be solved by using deep copy from python copy module.

## deep copy
```
import copy
frameworks = ["struts", "angular"]
latest_frameworks = copy.deepcopy(frameworks)
```
## methods in random package

|Syntax|Description|
|:----:|:----------|
|<b><i>random.seed(a)</b></i>|Initiate random number generator based on seed value|
|<b><i>random.random()</b><i>|returns random number in range 0.0 - 0.1|
|<b><i>random.randint(a,b)</b><i>|generate a random number within a and b|
|<b><i>random.randrange(start, stop, step)</b><i>|Returns the random number from the range provided.|
|<b><i>random.choice(array)</b><i>|Returns a random value from the array passed.|
|<b><i>random.shuffle(array)</b><i>|Shuffles the array randomly.|

## python memory management

- https://rushter.com/blog/python-memory-managment/
- https://rushter.com/blog/python-garbage-collector/
- https://www.slideshare.net/nnja/memory-management-in-python-the-basics
- https://www.slideshare.net/jmgimeno/objectoriented-programming-in-python
- https://www.slideshare.net/MattHarrison4/learn-90

## python static method vs classmethod

- https://www.programiz.com/python-programming/methods/built-in/classmethod
