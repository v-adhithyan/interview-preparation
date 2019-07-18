# Facade pattern

- Facade is an elegant Python design pattern. It's a perfect way of streamlining the interface.
- If we have a system with a considerable number of objects. Every object is offering a rich set of API methods. We can do a lot of things with this system, but how about simplifying the interface? Why not add an interface object exposing a well thought-out subset of all API methods? A Facade!
- Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

## Example

```python
class Car(object):

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level

class Tyre:
    pass

class Tank:
    pass
```
## References
- https://www.toptal.com/python/python-design-patterns
- https://sourcemaking.com/design_patterns/facade/python/1
