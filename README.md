
## Introduction

Many times when writing classes, there is a well known order in which
methods can be called. Finite state machines provide an excellent way
to enforce the ordering.

This library provides two decorators: one for a class and another for
a method. They defined a class's state machine and the valid
transitions after a method invocation, respectively.

## Sample

```python
from fsm import StateMachine, state_machine, next_state

@state_machine(["appears"])
class Mouse:

    @next_state(["runs_away", "enters_mouse_trap"])
    def appears(self):
        print("In appears()")

    @next_state(["escapes"])
    def runs_away(self):
        print("In runs_away()")

    @next_state(["appears"])
    def escapes(self):
        print("In escapes()")

    @next_state(["trapped"])
    def enters_mouse_trap(self):
        print("In enters_mouse_trap()")

    @next_state(["removed"])
    def trapped(self):
        print("In trapped()")

    @next_state([])
    def removed(self):
        print("In removed()")

mouse = Mouse()
mouse.appears()
mouse.runs_away()
mouse.enters_mouse_trap() # fsm.TransitionError: Invalid state transition:
                          #  runs away -> enters mouse trap
    
```
