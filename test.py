try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *




# create the world and bob
world = TurtleWorld()
bob = Turtle()

bob.delay = 0

bob.fd(100)
bob.lt(-220)
bob.fd(100)

wait_for_user()