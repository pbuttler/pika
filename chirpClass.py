class Chirp(object):
    """This is a class whose members are messages It contains info on how to deliver and respond to its contained data"""
    creator = null
    label = "A new chirp"
    def __init__(self,creator,*args):
        self.args = args
        self.creator = creator
    def __repr__(self):
        return label

