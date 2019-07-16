# Singleton pattern

- When we want only one object to be created for a class we use this pattern. 

- The created object can passed or accessed from a global variable or from a private member of class. It can then be passed to places where it is required. (Dependency injection)

- It is used to provide global point of access to the object. In terms of practical use Singleton patterns are used in logging, caches, thread pools, configuration settings, device driver objects

## Example

```python
class Logger:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, *kwargs)
        
        return cls._logger
```

## Alternatives to singleton pattern in python

- Use a module.

- Create one instance somewhere at the top-level of your application, perhaps in the config file.

- Pass the instance to every object that needs it. That’s a dependency injection and it’s a powerful and easily mastered mechanism.

## References

- https://www.toptal.com/python/python-design-patterns