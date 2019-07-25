# Command pattern


## Example

```python
import os

class History:
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()
    
    def undo(self):
        self._commands.pop().undo()

class RenameFileCommand:
    def __init__(self, src_file, dest_file):
        self._src = src_file
        self._dest = dest_file
    
    def execute(self):
        os.rename(self._src, self._dest)
    
    def undo(self):
        os.rename(self._dest, self._src)

if __name__ == '__main__':
    history = History()
    history.execute(RenameFileCommand("tmp.txt", "tmp2.txt"))
    history.undo()
```

## References

- https://www.toptal.com/python/python-design-patterns