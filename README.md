
## Introduction

Many times when writing classes, there is a well known order in which
methods can be called. Finite state machines provide an excellent way
to enforce the ordering.

This library provides a decorator for this purpose.

## Mouse Sample

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

## Bank Account Example

A more concrete example is that of a bank account.

```
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    @transition(["deposit", "set_balance"])
    def __init__(self, name):
        """Return a Customer object whose name is *name*.""" 
        self.name = name

    @transition(["deposit", "set_balance", "withdraw"])
    def set_balance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    @transition(["deposit", "set_balance", "withdraw"])
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    @transition(["deposit", "set_balance", "withdraw"])
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
```

Notice that without enforcing that a call to `set_balance` or
`set_balance`, `self.balance` would be underfined before it is used.
