..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-14-2-

Using Decisions with Turtles
==============================

Here's an example of conditional execution (using an ``if`` statement) with a turtle.  We can make the turtle do some action when a condition is true.  In this example if the turtle gets to right side of the space (drawing area), pick it up and move it back to the left side of the space further down so that it can draw more.

.. activecode:: td_pattern
    :tour_1: "Structural Tour"; 1-4: td1a-line1-4; 6-8: td1a-line6-8; 10-15: td1a-line10-15; 17: td1a-line17; 18: td1a-line18; 19: td1a-line19; 20: td1a-line20; 21: td1a-line21; 22: td1a-line22; 23: td1a-line23; 24: td1a-line24; 25: td1a-line25; 
    :nocodelens:

    from turtle import *      # use the turtle library
    from sys import *         # use the system library
    setExecutionLimit(50000)  # let this take up to 50 seconds
    space = Screen()          # create a turtle screen (space)
    
    width = 400               # set the desired width
    space.setup(width,width)  # set the space width and height
    maxX = width / 2          # set the max x value to half the width
    
    jaz = Turtle()            # create a turtle named jaz
    jaz.shape('turtle')       # set the shape for jaz to turtle
    jaz.penup()               # pick up the pen (don't draw)
    jaz.goto(-1 * maxX,100)   # go to the left side of the space
    jaz.pendown()             # put the pen down to draw with
    jaz.left(60)              # turn the turtle left 60 degrees
    
    for x in range(10):       # repeat the body 10 times
    	jaz.forward(100)           # go forward 100
      	jaz.right(120)             # turn right 120 degrees
      	jaz.forward(100)           # go forward 100
      	jaz.left(120)              # turn left 120 degrees
      	if (jaz.xcor() >= maxX):   # if at right edge of space
      	    jaz.penup()                # pick up the pen
      	    jaz.goto(-1 * maxX,jaz.ycor() - 100)  # move left & down
      	    jaz.pendown()              # put the pen down
      	    
This code calculates ``maxX`` as half the ``width`` since the drawing area uses the cartesian coordinate system with (0,0) as the center.  Since the ``width`` is 400 the ``maxX`` is 200.  We move the turtle to ``-1 * maxX`` which is -200.  When the turtle's x coordinate is greater than or equal to the maxX, which means it is at the right edge, then we move the turtle back to the left edge and down 100.

For more information on what this code does listen to the audio tour.  
  
.. mchoice:: 14_2_1_finish_pattern
   :answer_a: 12
   :answer_b: 14
   :answer_c: 16
   :answer_d: 18
   :correct: c
   :feedback_a: Using a range of 12 will complete the pattern on this line, but what should it be to finish the pattern in the space?
   :feedback_b: This will stop in the middle of the last line of the pattern.  How many would fill the last row?
   :feedback_c: Each iteration of the loop draws one peak and there are 4 peaks per row.  There is room for 4 rows so the answer is 4 * 4 = 16.
   :feedback_d: This would try to draw on the line below the end of the drawing area.  

   What value should you use for range in line 17 in the program above (td_pattern) to complete the pattern to fill the drawing space?  
   
Modify the code above to draw a different pattern.  Try turning changing the direction of every turn, what does that do?
   
  
