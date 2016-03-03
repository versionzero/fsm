
## Introduction

Many times when writing classes, there is a well known order in which
methods can be called. Finite state machines provide an excellent way
to enforce the ordering.

This library provides two decorators: one for a class and another for
a method. They defined a class's state machine and the valid
transitions after a method invocation, respectively.

## Sample

```python
from fsm import transition


class Mouse:

    @transition(["runs_away", "enters_mouse_trap"])
    def appears(self):
        print("In appears()")

    @transition(["escapes"])
    def runs_away(self):
        print("In runs_away()")

    @transition(["appears"])
    def escapes(self):
        print("In escapes()")

    @transition(["trapped"])
    def enters_mouse_trap(self):
        print("In enters_mouse_trap()")

    @transition(["removed"])
    def trapped(self):
        print("In trapped()")

    @transition([])
    def removed(self):
        print("In removed()")


mouse = Mouse()
mouse.appears()
mouse.runs_away()
mouse.enters_mouse_trap() # fsm.TransitionError: Invalid state transition:
                          #  runs away -> enters mouse trap    
    
```
