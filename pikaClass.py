class Pika(object):
    """A class for things that "exist""""
    name = "A new Pika"
    friends = {}                                                #A collection of non-strict relations
    family  = {}                                                #A collection of strict relations
    def __init__(self,*args):
        self.args = args
    def __repr__(self):
        return name
    def makeChirp(self,*args):
        newChirp = new Chirp(self)
    def sendChirp(theChirp, theTarget):
        #Function for sending a chirp
        print name + " just chirped at " + theTarget.name
    def hearChirp(source, theChirp):
        # Hear a chirp
        # - source      = The pika that sent the chirp
        # - theChirp    = An chirp object
        theChirp.mustExecute()                                  #Run the mandatory actions of the chirp, if they exist
        if ("""conditions for optional chirps""")               #Run optional actions of the chirps, if this Pika "wants"
            theChirp.canExecute()
