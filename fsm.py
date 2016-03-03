

class _StateMachine:
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
                raise _StateMachine.State.TransitionError(
                    "Invalid state transition: %s -> %s" 
                    % (self.__current, name))
            self.__current = name
            self.__states = states
    def __init__(self, states=[]):
        self.__current = _StateMachine.State("__start__", states)
    def next(self, name, states):
        self.__current.next(name, states) 
    def state(self):
        return str(self.__current)


def transition(next):
    def wrap(fn):
        def wrapped_f(*args, **kwargs):
            # Instantiate the FSM after the first method with a
            # transion is invoked.
            cls = args[0]
            if not hasattr(cls, "__machine"):
                setattr(cls, "__machine", _StateMachine(fn.__name__))
            getattr(cls, "__machine").next(fn.__name__, next)
            return fn(*args, **kwargs)
        return wrapped_f
    return wrap
