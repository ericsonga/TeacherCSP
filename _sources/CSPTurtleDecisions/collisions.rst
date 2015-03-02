..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-14-5-
     
Avoiding Collisions
======================

You can use conditionals to detect when two turtles are getting close to each other and then have the turtles take evasive action. In the code below they try both try to turn right just as ships do if they are heading straight for each other.    
   
.. activecode:: td_avoid_collision
    :tour_1: "Structural Tour"; 1-2: td4-line1-2; 3-6: td4-line3-6; 7: td4-line7; 8-11: td4-line8-11; 12: td4-line12; 13-14: td4-line13-14; 15-17: td4-line15-17;
    :nocodelens:

    from turtle import *      # use the turtle library
    space = Screen()          # create a turtle screen (space)
    jaz = Turtle()            # create a turtle named jaz
    jaz.shape('turtle')       # set the shape for jaz to turtle
    mia = Turtle()            # create a turtle named mia
    mia.shape('turtle')       # set the shape for mia to turtle
    mia.color('red')          # set the color for mia to red
    mia.penup()               # pick up the pen (don't draw)
    mia.goto(100,0)           # move to the right 100
    mia.pendown()             # put down the pen
    mia.right(180)            # turn 180 degrees (face jaz)
    for x in range(20):       # repeat the body 20 times
    	jaz.forward(10)            # go forward 10
    	mia.forward(10)             # go forward 10
    	if (mia.xcor() - jaz.xcor() < 40):  # if they get close
        	jaz.right(45)                       # turn jaz left
        	mia.right(45)                       # turn mia left
  
Notice that this code doesn't quite work as intended.  Both ``jaz`` and ``mia`` turn completely around.  How could you modify the code to fix it so that they turn to avoid each other, but don't end up turning completely around?  You might want to check the distance between the y values as well.