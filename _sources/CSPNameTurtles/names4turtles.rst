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

- Use assignment to name objects like turtles.
- Ask turtle objects to perform actions.
- Understand that using the right object at the right time, in order, is critical to success.

..	index::
	single: objects
	
Names can be more than numbers and strings.  They can also be turtles or "screens" (a space on the page where a turtle can draw).  You can also call things like turtles and screens **objects**.  **Objects** in programming are things that do the action in a program.  

We have seen this example once before.

.. activecode:: Turtle_Names1
    :tour_1: "Line-by-line Tour"; 1: t1-line1; 2: t1-line2; 3: t1-line3; 4: t1-line4; 5: t1-line5; 6: t1-line6; 7: t1-for100-1; 8: t1-right90-1; 9: t1-for100-2; 10: t1-right90-2; 11: t1-for100-3; 12: t1-right90-3;
    :nocodelens:
	
    from turtle import *	# use the turtle library
    space = Screen()		# create a turtle screen (space)
    zari = Turtle() 		# create a turtle named zari
    zari.setheading(90)		# Point due north
    zari.forward(100)		# tell zari to move forward by 100 units
    zari.right(90)   		# turn by 90 degrees
    zari.forward(100)		# tell zari to move forward by 100 units
    zari.right(90)   		# turn by 90 degrees
    zari.forward(100)		# tell zari to move forward by 100 units
    zari.right(90)   		# turn by 90 degrees
    zari.forward(100)		# tell zari to move forward by 100 units
    zari.right(90)    		# turn by 90 degrees

Now try this one.  

.. activecode:: Turtle_Names2
    :tour_1: "Line-by-line Tour"; 1: tri-line1; 2: tri-line2; 3: tri-line3; 4: tri-line4; 5: tri-line5; 6: tri-line6; 7: tri-line7; 8: tri-line8; 9: tri-line9; 10: tri-line10;
    :nocodelens:
	
    from turtle import *   	# use the turtle library
    space = Screen()     	# create a turtle screen (space)
    zari = Turtle()      	# create a turtle named zari
    zari.setheading(90) 	# Point due north
    zari.forward(100)  		# tell zari to move forward by 100 units
    zari.right(120) 		# turn right by 120 degrees
    zari.forward(100)		# tell zari to move forward by 100 units
    zari.right(120)   		# turn right by 120 degrees
    zari.forward(100) 		# tell zari to move forward by 100 units
    zari.right(120)   		# turn right by 120 degrees

.. mchoicemf:: 5_1_1_Turtle_Names2_Q1
   :answer_a: A square
   :answer_b: A triangle
   :answer_c: A rectangle
   :correct: b
   :feedback_a: That was the first program, but not the second program.
   :feedback_b: Now, what if you did one more forward and right.  Would it still be a triangle? Try it!
   :feedback_c: But, we could change the first program to make a rectangle.  Can you change two lines in the first program to draw a rectangle?

   What shape did that draw?

This works because ``zari`` is a turtle, and each statement gets executed, one right after the other.  If we introduce another turtle and another name, it doesn't work the same

.. activecode:: Two_Turtles
    :tour_1: "Line-by-line Tour"; 1: tt-line1; 2: tt-line2; 3: tt-line3; 4: tt-line4; 5: tt-line5; 6: tt-line6; 7: tt-line7; 8: tt-line8; 9: tt-line9; 10: tt-line10; 11: tt-line11; 12: tt-line12;
    :nocodelens:
	
    from turtle import * 	# use the turtle library
    space = Screen()     	# create a turtle screen (space)
    zari = Turtle()     	# create a turtle named zari
    zari.setheading(90) 	# Point due north
    zari.forward(100)   	# tell zari to move forward by 100 units
    zari.right(120)     	# turn right by 120 degrees
    zari.forward(100)     	# tell zari to move forward by 100 units
    zari.right(120)      	# turn right by 120 degrees
    chad = Turtle()     	# create a new turtle named chad
    chad.color("orange")  	# change the color chad's draws with
    chad.forward(100)     	# tell chad to move forward by 100 units
    chad.right(120)     	# turn chad by 120 degrees
    
.. mchoicemf:: 5_1_2_Turtle_Dir_Q1
   :answer_a: North
   :answer_b: South
   :answer_c: East
   :answer_d: West
   :correct: c
   :feedback_a: The turtles in some of the examples faced north because of the <code>setheading(90)</code> instruction. Which way does chad move first?
   :feedback_b: Which way does chad first move in the example above?  North is at the top of the page.
   :feedback_c: Turtles start off facing east which is toward the right side of the page.
   :feedback_d: Which way does chad first move in the example above?   North is at the top of the page.

   Which way does a turtle face when first created?
    
**Mixed up programs**

.. parsonsprob:: 5_1_3_Turtle_L

   The following program uses a turtle to draw a capital L as shown in the picture to the left of this text, <img src="../_static/TurtleL4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   ella = Turtle()
   =====
   ella.right(90)
   ella.forward(150)
   =====
   ella.left(90)
   =====
   ella.forward(75)
   
.. parsonsprob:: 5_1_4_Turtle_Check

   The following program uses a turtle to draw a checkmark as shown to the left, <img src="../_static/TurtleCheckmark4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle.  The turtle should turn to face southeast, draw a line that is 75 pixels long, then turn to face northeast, and draw a line that is 150 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  Northeast is between north and east. Southeast is between south and east. <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   =====
   space = turtle.Screen()
   maria = turtle.Turtle()
   =====
   maria.right(45)
   =====
   maria.forward(75)
   =====
   maria.left(90)
   =====
   maria.forward(150)
   



