..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. 	qnum::
	:start: 1
	:prefix: csp-5-3-
	
.. highlight:: java
   :linenothreshold: 4


    
More Turtle Procedures and Functions 
=======================================

Turtles can do more than go forward, turn left, and turn right.  The table below lists more turtle procedures and functions.

==========  ==========  =========================
Name        Input       Description
==========  ==========  =========================
backward    amount        Moves the turle backward by the specified amount
color       colorname     Sets the color for drawing.  Use 'red', 'black', etc
forward     amount        Moves the turtle forward by the specified amount	  
goto        x,y           Moves the turtle to position x,y
left        angle         Turns the turtle counter clockwise by the specified angle
pendown     None          Puts down the turtles tail so that it draws when it moves
penup       None          Picks up the turtles tail so that it doesn't draw when it moves
pensize     width         Sets the width of the pen for drawing
right       angle         Turns the turtle clockwise by the specified angle
setheading  angle         Turns the turtle to face the given heading.  East is 0, north is 90, west is 180, and south is 270.  
Turtle      None          Creates and returns a new turtle object
==========  ==========  =========================

You can draw a block style C with a turtle.  Can you draw more than one letter?  You would have to use the ``penup()`` procedure to pick up the pen and then move to the new location to draw the second letter and then put the pen down using ``pendown()`` as shown in the example below.  

.. activecode:: Turtle_CandL
    :nocodelens:
	
    from turtle import *  # use the turtle library
    space = Screen()	  # create a turtle space
    ji = Turtle()   	  # create a turtle named ji
    ji.right(180)   	  # turn right by 180 degrees
    ji.forward(75)        # move forward by 75 units 
    ji.right(90)          # turn right 90 degrees
    ji.forward(100)       # more forward by 90 units
    ji.right(90)          # turn right 90 degrees
    ji.forward(75)        # move forward by 75 units 
    ji.penup()            # pick up the pen
    ji.forward(50)        # move forward 50 units
    ji.pendown()          # put the pen down
    ji.right(90)          # turn right 90 degrees
    ji.forward(100)       # go forward 100 units
    ji.left(90)           # turn left 90 degrees
    ji.forward(75)        # go forward 75 units
    
**Mixed up programs**

.. parsonsprob:: 5_3_1_DrawA

   The following program uses a turtle to draw a capital A as shown in the picture to the left of this text, <img src="../_static/DrawA.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   ella = Turtle()
   =====
   ella.left(45)
   ella.forward(100)
   =====
   ella.right(135)
   ella.forward(100)
   =====
   ella.penup()
   ella.goto(100,100)
   =====
   ella.left(45)
   ella.forward(75)
   
.. parsonsprob:: 5_3_2_DrawH
   :adaptive:

   The following program uses a turtle to draw a capital H as shown in the picture to the left of this text, <img src="../_static/DrawH.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   space = Screen()  
   =====    
   anu = Turtle()        
   anu.left(90)
   anu.forward(100)
   =====
   anu.penup()
   anu.goto(0,50)
   anu.pendown()
   =====
   anu.right(90)
   anu.forward(50)
   =====
   anu.penup()
   anu.goto(50,0)
   anu.pendown()
   =====
   anu.left(90)
   anu.forward(100)
    
You can change the color and pensize that you draw with as well.

.. activecode:: Turtle_Color
    :nocodelens:
	
    from turtle import *  # use the turtle library
    space = Screen()	  # create a turtle space
    anu = Turtle()   	  # create a turtle named anu
    anu.color('red')      # set the color to red
    anu.pensize(25)       # set the size of the pen
    anu.right(180)   	  # turn right by 180 degrees
    anu.forward(75)       # move forward by 75 units 
    anu.right(90)         # turn right 90 degrees
    anu.color('blue')     # set the color to blue
    anu.pensize(50)       # set the pen size to 10
    anu.forward(100)      # move forward by 100 units

The space that the turtle draws in is 320 by 320 pixels.  The center of the space is at x=0, y=0.  

.. figure:: Figures/spaceCoord.png
    :width: 400px
    :align: center
    :alt: the space coordinate system
    :figclass: align-center

    Figure 1: The coordinates for the drawing space.  Note that the center is x = 0 and y = 0.
    
The program below uses the ``goto(x,y)`` to move to the top left corner before drawing a square that nearly fills the drawing space.
    
.. activecode:: Turtle_Bounds
    :nocodelens:
	
    from turtle import *  # use the turtle library
    space = Screen()	  # create a turtle space
    anu = Turtle()   	  # create a turtle named anu
    anu.penup()           # pick up the pen (don't draw)
    anu.goto(-150,150)    # go to the top left corner
    anu.pendown()         # put down the pen
    anu.forward(300)      # move forward by 300 pixels
    anu.right(90)         # turn right 90 degrees
    anu.forward(300)      # move forward by 300 pixels
    anu.right(90)         # turn right 90 degrees
    anu.forward(300)      # move forward by 300 pixels
    anu.right(90)         # turn right 90 degrees
    anu.forward(300)      # move forward by 300 pixels
    



