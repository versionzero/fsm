
## Introduction

Many times when writing classes, there is a well known order in which
methods can be called. Finite state machines provide an excellent way
to enforce the ordering.

This library provides two decorators: one for a class and another for
a method. They defined a class's state machine and the valid
transitions after a method invocation, respectively.

## Sample

```python
from fsm import state_machine, transition

@state_machine(["appears"])
class Mouse:
    
    def __init__(self):
        pass

    @transition(["runs away", "enters mouse trap"])
    def appears(self):
        pass

    @transition(["escapes"])
    def runs_away(self):
        pass

    @transition(["appears"])
    def escapes(self):
        pass

    @transition(["trapped"])
    def enters_mouse_trap(self):
        pass

    @transition(["removed"])
    def trapped(self):
        
    @transition([])
    def removed(self):
        pass
        
mouse = Mouse()
mouse.appears()
mouse.runs_away()
#mouse.enters_mouse_trap() # fsm.TransitionError: Invalid state
                           # transition:
                           # runs away -> enters mouse trap
```
