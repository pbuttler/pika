"""
A chirp is a way for pikas to communicate
This communication includes:
- Waking up other pikas
- Asking other pikas about their status
- Giving other pikas a task
...
"""

class Chirp(object):
    """This is a class whose members are messages It contains info on how to deliver and respond to its contained data"""
    creator = null
    label = "A new chirp"               #A name for this chirp
    data = {}                           #The content of this chirp
    def reverb():
        #Rules on how to react to this chirp
    def __init__(self,creator,*args):
        self.args = args
        self.creator = creator
    def __repr__(self):
        return label

