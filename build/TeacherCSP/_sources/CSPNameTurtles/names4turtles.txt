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
	:prefix: csp-5-1-
	
.. highlight:: java
   :linenothreshold: 4

Assign a Name to a Turtle
==============================

*Learning Objectives:*

- Use assignment to name objects like turtles and screens.
- Ask turtle objects to perform actions.
- Introduce the concept of a procedure, which does some action, but doesn't return a value.
- Introduce some turtle procedures like ``color``, ``penup``, ``pendown``, and ``pensize``.
- Demonstrate that you can create more than one object of a type.
- Demonstrate that using the right object at the right time, in order, is critical to success.

..	index::
	single: objects
	
Names can be more than numbers and strings.  They can also be turtles or "screens" (a space on the page where a turtle can draw).  You can also call things like turtles and screens **objects**.  **Objects** in programming are the things that do the action in a program.  Objects can have attributes and behavior.  An example of an attribute is a position and an example of a behavior is the ability to go forward.  

We have seen the example below once before.  It allows us to use the ``turtle`` library, creates a ``space`` for a turtle object to draw on, creates a ``turtle`` object and names it ``alex``, asks ``alex`` to go forward by 150 pixels, asks ``alex`` to turn left 90 degrees, and asks ``alex`` to go forward 75 pixels. 

.. activecode:: Turtle_1_Again
    :tour_1: "Line-by-line Tour"; 1: first-turtle-line-1; 2: first-turtle-line-2; 3: first-turtle-line-3; 4: first-turtle-line-4; 5: first-turtle-line-5; 6: first-turtle-line-6;
    :nocodelens:
	
    from turtle import *	# use the turtle library
    space = Screen()		# create a turtle space
    alex = Turtle()   		# create a turtle named alex
    alex.forward(150)		# move forward by 150 units
    alex.left(90)   		# turn by 90 degrees
    alex.forward(75)		# move forward by 75 units 
    
.. mchoice:: 5_1_1_Turtle_Dir_Q1
   :answer_a: North
   :answer_b: South
   :answer_c: East
   :answer_d: West
   :correct: c
   :feedback_a: The turtles in some of the examples faced north because of the <code>setheading(90)</code> instruction. Which way does chad move first?
   :feedback_b: Which way does chad first move in the example above?  North is at the top of the page.
   :feedback_c: Turtles start off facing east which is toward the right side of the page.
   :feedback_d: Which way does chad first move in the example above?   North is at the top of the page.

   Which way does a turtle face when it is first created?
    
What does a left turn of 90 mean? 
----------------------------------
    
When we ask a turtle to turn left, it will turn left based on the direction it is currently heading. A turtle object keeps track of its heading (direction it is facing). Use the figure below to help you understand how much the turtle will turn if asked to turn left 90 degrees and it is currently heading east (0 degrees).

.. figure:: Figures/turnDegrees.png
    :width: 400px
    :align: center
    :alt: shows what a turn of each degrees means for left and right turns
    :figclass: align-center

    Figure 1: The amount of turn for specified degrees for left and right turns
    
**Mixed up programs**

.. parsonsprob:: 5_1_1_Turtle_L

   The following program uses a turtle to draw a capital L as shown in the picture to the left of this text, <img src="../_static/TurtleL4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   ella = Turtle()
   =====
   ella.right(90)
   =====
   ella.forward(150)
   =====
   ella.left(90)
   =====
   ella.forward(75)
   
.. parsonsprob:: 5_1_2_Turtle_Check

   The following program uses a turtle to draw a checkmark as shown to the left, <img src="../_static/TurtleCheckmark4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle.  The turtle should turn to face southeast, draw a line that is 75 pixels long, then turn to face northeast, and draw a line that is 150 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  Northeast is between north and east. Southeast is between south and east. <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   =====
   space = turtle.Screen()
   =====
   maria = turtle.Turtle()
   =====
   maria.right(45)
   =====
   maria.forward(75)
   =====
   maria.left(90)
   =====
   maria.forward(150)


