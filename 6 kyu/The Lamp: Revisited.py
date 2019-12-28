class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = 0
        
    def state(self):
        return 'The lamp is {}.'.format(['off', 'on'][self.on])
    
    def toggle_switch(self):
        self.on = not self.on
