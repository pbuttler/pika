class Chirp(parent):
    """This is a class whose members are messages It contains info on how to deliver and respond to its contained data"""
    creator = object
    label = "A new chirp"
    def __init__(self,*args):
        self.args = args
    def __repr__(self):
        return label

