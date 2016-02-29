

class StateMachine:
    """
    Simple (finite) state machine to help guard against improper use
    of class methods.
    
    Many of our classes know apriori the order in which methods should
    be called. In order to enforce this ordering we can use a FSM.
    
    Example:
    
    class Mouse:
        def __init__(self):
            self.machine = StateMachine(["appears"])
        def appears(self):
            self.machine.next("appears", ["runs away", "enters mouse trap"])
        def runs_away(self):
            self.machine.next("runs away", ["escapes"])
        def escapes(self):
            self.machine.next("escapes", ["appears"])
        def enters_mouse_trap(self):
            self.machine.next("enters mouse trap", ["trapped"])
        def trapped(self):
            self.machine.next("trapped", ["removed"])
        def removed(self):
            self.machine.next("removed", [])
        
    mouse = Mouse()
    mouse.appears()
    mouse.runs_away()
    mouse.enters_mouse_trap()
        TransitionError: Invalid state transition: runs away -> enters mouse trap
    
    Explanation:
    
    A mouse appears beside a mouse trap. It has the option to run away or
    enter the trap. In this case it runs away. If we then attempt to say
    that it also entered the mouse trap, then we raise an exception, since
    it is not possible for the mouse to both run away and enter the trap
    at the same time. The only valid step after running away for the mouse
    is that it escapes.
    """
    class State:
        class TransitionError(Exception):
            pass
        def __init__(self, name, next=[]):
            self.__current = name
            self.__states = next
        def __str__(self):
            return self.__current
        def next(self, name, states=[]):
            if not name:
                name = "__end__"
            if name not in self.__states:
                raise StateMachine.State.TransitionError(
                    "Invalid state transition: %s -> %s" 
                    % (self.__current, name))
            self.__current = name
            self.__states = states
    def __init__(self, states=[]):
        self.__current = StateMachine.State("__start__", states)
    def next(self, name, states):
        self.__current.next(name, states) 
    def state(self):
        return str(self.__current)


def state_machine(first):
    def wrap(cls):
        if not hasattr(cls, "__machine"):
            setattr(cls, "__machine", StateMachine(first))
        return cls
    return wrap


def next_state(next):
    def wrap(fn):
        def wrapped_f(*args):
            getattr(args[0], "__machine").next(fn.__name__, next)
            fn(*args)
        return wrapped_f
    return wrap
