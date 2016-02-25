

from fsm import StateMachine
import sys

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
#mouse.enters_mouse_trap() # fsm.TransitionError: Invalid state transition: runs away -> enters mouse trap

def author(author_name):
    def decorator(func):
        func.author_name = author_name
        return func
    return decorator

@author("Lemony Snicket")
def sequenceOf(unfortunate_events):
    pass
#print sequenceOf.author_name    # prints "Lemony Snicket"


def class_decorator(cls):
   for name, method in cls.__dict__.iteritems():
        if hasattr(method, "use_class"):
            # do something with the method and class
            print name, cls
   return cls

def method_decorator(view):
    # mark the method as something that requires view's class
    view.use_class = True
    return view

#@class_decorator
#class ModelA(object):
#    @method_decorator
#    def a_method(self):
#        # do some stuff
#        pass


def state_machine(cls):
    if not hasattr(cls, "__machine"):
        setattr(cls, "__machine", StateMachine("first"))
    machine = getattr(cls, "__machine")
    for name, method in cls.__dict__.iteritems():
        #print("here", name, method)
        if hasattr(method, "__next"):
            # do something with the method and class
            #print name, cls
            #print("ASADSADSADS")
            next_states = getattr(method, "__next")
            #print name
            #print next_states
            machine.next(name, next_states)
    return cls

def state_machine(next):
    print "In state_machine"
    print("next", next)
    def wrap(cls):
        def wrapped_f(*args):
            #setattr(cls, "__machine", StateMachine(next))
            if not hasattr(cls, "__machine"):
                setattr(cls, "__machine", StateMachine("first"))
            machine = getattr(cls, "__machine")
            for name, method in cls.__dict__.iteritems():
                print("here", name, method)
                #if hasattr(method, "__next"):
                if hasattr(method, "__name"):
                    # do something with the method and class
                    #print name, cls
                    #print("ASADSADSADS")
                    next_states = getattr(method, "__next")
                    #print name
                    #print next_states
                    machine.next(name, next_states)
            return cls
        return wrapped_f
    return wrap
    
def next_state(next):
    def wrap(f):
        print "Inside wrap()"
        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", next
            f(*args)
            print "After f(*args)"
            wrapped_f.__name = f.__name__    
        wrapped_f.__next = next
        return wrapped_f
    wrap.use_class = True
    return wrap
    
@state_machine(["one"])
class Foo(object):

    def __init__(self):
        print("In Foo:__init__")

    @next_state(["two"])
    def one(self):
        print("In Foo:one")

    @next_state(["three"])
    def two(self):
        print("In Foo:two")

    @next_state([])
    def three(self):
        print("In Foo:three")

foo = Foo()
foo.one()
foo.two()
foo.three()

sys.exit()

def state_machine(*__args):
    #cls.machine = StateMachine(next)
    print(__args)

def transition(next=[]):
    cls.machine.next(f.__name__, next)
    
class Mouse(object):

    @state_machine(["appears"])
    def __init__(self):
        pass

    @transition(["runs away"])
    def appears(self):
        pass

    @transition(["escapes"])
    def runs_away(self):
        pass

mouse = Mouse()
mouse.appears()
mouse.runs_away()
