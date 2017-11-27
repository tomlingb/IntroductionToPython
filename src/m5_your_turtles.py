"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Geoffrey Tomlinson.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow

Bob = rg.SimpleTurtle('turtle')
Jack = rg.SimpleTurtle('turtle')

Bob.pen = rg.Pen('purple', 2)
Jack.pen = rg.Pen('red', 2)

Bob.speed = 10
Jack.speed = 10

size1 = 50
size2 = 100

for k in range(10):
    Bob.draw_circle(size1)
    Jack.draw_circle(size1)
    Bob.pen_up()
    Bob.right(45)
    Bob.forward(10)
    Bob.left(45)
    Bob.pen_down()
    Jack.pen_up()
    Jack.right(45)
    Jack.forward(15)
    Jack.left(45)
    Jack.pen_down()
