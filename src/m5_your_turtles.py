"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Caitlin Coverstone.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
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

window = rg.TurtleWindow()

turtle_1 = rg.SimpleTurtle('turtle')
turtle_1.pen = rg.Pen('yellow', 2)
turtle_1.speed = 20

size = 15
for k in range(20):
    turtle_1.draw_circle(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    turtle_1.pen_up()
    turtle_1.right(45)
    turtle_1.forward(10)
    turtle_1.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    turtle_1.pen_down()
    size = size - 12

turtle_2 = rg.SimpleTurtle('turtle')
turtle_2.pen = rg.Pen('blue', 2)
turtle_2.speed = 100

#size = 150
for k in range(25):
    turtle_2.draw_regular_polygon(8,30)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    turtle_2.pen_down()
    turtle_2.right(45)
    turtle_2.forward(10)
    turtle_2.left(45 + k)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    turtle_2.pen_down()
    size = size - 12

window.close_on_mouse_click()

