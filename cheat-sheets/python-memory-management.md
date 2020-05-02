# Python memory management
  Python uses reference counting + garabage collection to do memory management.
  
## Basics

- Python has names not variables
- Names contains references to objects.
- An name is just an label for an object. Each object can have lot of names.
- Try the following code, but do not run in a interpreter
  ```
    a = 100
    b = 100
    print(id(a))
    print(id(b))
  ```
  - Both the print statements will print same address / object. So here a and b are just references to int object 100.

- Each object will have an reference count, the number of references to it. When new name points to same object, reference count is increased. On the other hand when del is performed, reference count is decreased.
- Every python object has 3 things
  - type
  - value
  - reference count

## Garbage collection (gc)

A way for program to automatically release memory, when object taking up that space is no longer in use.

## Reference count based gc

When reference count reaches 0, release memory. Sounds simple, actually not. It has space overhead (ref count stored for each object) and execution overhead (count changed on each reference). It is not thread safe and generally does not detect cyclical references. So python uses ref count + generational for gc.

## Generational gc

- Based on assumption that most objects die young.
- Python maintains a list ( 3 lists) of every object created. Newly created objects with ref count > 0 are stored in any generation. For first time they will be placed in generation 0.
  - generation 0
  - generation 1
  - generation 2
- When threshold is reached on any generation, python runs a gc on that generation and younger generations.
  - python makes a list of objects to discard when there are no cyclical references for that object.
  - When the list is prepared, all objects in discard list are discarded.
  - The survived objects will be promoted to next generation. Objects in gen 2 stay there till the program exits.
  - When ref count reaches 0 immediate clean, when there is cycle wait for gc.

## Global interpreter lock (GIL)
- Only one thread can run at any time in a interpreter.

# references

## additional material

- https://www.quora.com/How-does-garbage-collection-in-Python-work
- https://pymotw.com/2/gc/
- http://tech.oyster.com/save-ram-with-python-slots/
- https://realpython.com/python-memory-management/
