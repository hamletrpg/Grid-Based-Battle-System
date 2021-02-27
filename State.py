from transitions import Machine 

class GameState():
    STATES = ['moving', 'attacking', 'idle']

    def __init__(self):

        transitions = [
            {'trigger': 'stop', "source": "*", "dest": "idle"},
            {"trigger": "walk", "source": "idle", "dest": "moving"},
            {"trigger": "fight", "source": "idle", "dest": "attacking"}
        ]

        self.machine = Machine(model=self, states=GameState.STATES, initial="idle", transitions=transitions)

    def __str__(self):
        return self.state