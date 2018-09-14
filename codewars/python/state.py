#!/usr/bin/python
class Automaton(object):

    def __init__(self):
        # in-state, data, out-state
        self.states = {'q1' :  {'0': 'q1', '1': 'q2'}, 
                       'q2' :  {'0': 'q3', '1': 'q2'}, 
                       'q3' :  {'0': 'q2', '1': 'q2'}
                       }

    def read_commands(self, commands):
        cur = 'q1'
        for c in commands:
            cur = self.states[cur][c]
        return cur == 'q2'



aut = Automaton()
print aut.read_commands(['1'])
print aut.read_commands(["1", "0", "0", "1"])
            
        
        # Return True if we end in our accept state, False otherwise
