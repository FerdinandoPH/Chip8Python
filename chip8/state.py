class State():
    def __init__(self,cpu,screen_state):
        self.cpu=cpu
        self.scale_factor=screen_state[0]
        self.width=screen_state[1]
        self.height=screen_state[2]
        self.screen_array=screen_state[3]
        #self.screen_array=screen_array
