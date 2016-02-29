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
mouse.enters_mouse_trap() # fsm.Next_StateError: Invalid state next_state: runs away -> enters mouse trap
    
