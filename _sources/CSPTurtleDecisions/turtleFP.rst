..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-14-1-

Turtle Functions and Procedures
=================================

*Learning Objectives:*

- Introduce more turtle functions and procedures.
- Show examples using conditionals with turtles.
- Use the modulus function to detect odd and even
- Show how to generate random numbers in Python
- Use conditionals to avoid a collision

..	index::
    pair: turtle; procedures
    pair: turtle; functions
    pair: turtle; documentation
    pair: turtle; backward
    pair: turtle; forward
    pair: turtle; color
    pair: turtle; goto
    pair: turtle; left
    pair: turtle; pendown
    pair: turtle; penup
    pair: turtle; pensize
    pair: turtle; shape
    pair: turtle; stamp
    pair: turtle; xcor
    pair: turtle; ycor
    pair: turtle; Turtle

Turtles can do more than go forward, turn left, and turn right.  The table below lists turtle functions and procedures.

==========  ==========  =========================
Name        Parameters  Description
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
shape       shapename     Should be 'arrow', 'classic', 'turtle', or 'circle'
stamp       None          Leaves an impression of a turtle shape at the current location
Turtle      None          Creates and returns a new turtle object
xcor        None          Returns the x value of the turtle's position
ycor        None          Returns the y values of the turtle's position
==========  ==========  =========================

.. mchoicemf:: 14_1_1_change_size
   :answer_a: shape
   :answer_b: xcor
   :answer_c: pensize
   :answer_d: color
   :correct: c
   :feedback_a: Use shape to set the shape used for the turtle.  It doesn't affect the line that is drawn.  
   :feedback_b: Use this function to get the x value of the turtle's position
   :feedback_c: This changes the width of the line that the turtle draws as it moves.
   :feedback_d: Use color to change the line color and the turtle color.

   What procedure would you use to change the size of the line the turtle leaves when it moves?
   
.. mchoicemf:: 14_1_2_goto
   :answer_a: stamp
   :answer_b: xcor
   :answer_c: penup
   :answer_d: goto
   :correct: d
   :feedback_a: Use stamp to leave a copy of turtle shape at the current position. 
   :feedback_b: Use xcor to get the x value of the turtle's position.
   :feedback_c: Use penup to pick up the pen (stop drawing as you move).
   :feedback_d: Use goto to move to the given x and y position.

   What procedure would you use move the turtle to a given x and y position?

Once you are comfortable with the basics of turtle graphics you can read about even
more options on the `Python Docs Website <http://docs.python.org/dev/py3k/library/turtle.html>`_. 



  
