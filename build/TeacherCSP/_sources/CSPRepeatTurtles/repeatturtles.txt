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
	:prefix: csp-10-1-

Using Repetition with Turtles
===============================

*Learning Objectives:*

- Use a ``for`` loop to repeat steps with turtles.
- Generalize how to draw a polygon.

..	index::
	pair: statements; for

We already made turtles draw squares.  We told our turtle to go forward and turn right four times, but we don't *explicitly* say "four times."  We can tell the computer to do something explicitly for a certain number of times by using a ``for`` loop.


.. activecode:: Turtle_For
    :tour_1: "Lines of code"; 1: tR1-line1; 2: tR1-line2; 3: tR1-line3; 4: tR1-line4; 5: tR1-line5; 6: tR1-line6; 7: tR1-line7;
    :nocodelens:
	
    from turtle import *	# use the turtle library
    space = Screen()   		# create a turtle space
    alisha = Turtle()  		# create a turtle named alisha
    alisha.setheading(90)  	# point due north
    for sides in [1,2,3,4]:	# repeat the indented lines 4 times
    	alisha.forward(100)        	# move forward by 100 units
      	alisha.right(90)           	# turn by 90 degrees

.. mchoice:: 10_1_1_Turtle_For_Q1
   :answer_a: [0,1,2,3]
   :answer_b: [0,1,2]
   :answer_c: [2,3,4,5]
   :answer_d: [1,2,3,4,5]
   :correct: b
   :feedback_a: This still has four sides -- they are just numbered differently.
   :feedback_b: This would only draw 3 side since there are only 3 items in the list.
   :feedback_c: This still has four sides -- they are just numbered differently.
   :feedback_d: This <i>will</i> draw a square. The turtle will just go on to trace the first side twice.

   The numbers in the list ``[1,2,3,4]`` are not important.  It's the fact that there are *four* items in the list that is important.  Only one of these choices does *not* make a square.  Which one?  (It's not cheating to actually try each of them and run the program each time!)
   
.. parsonsprob:: 10_1_2_Rectangle

   The following program uses a turtle to draw a rectangle as shown to the left, <img src="../_static/TurtleRect.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up and create the turtle.  After that, iterate (loop) 2 times, and each time through the loop the turtle should go forward 175 pixels, turn right 90 degrees, go forward 150 pixels, and turn right 90 degrees.  After the loop, set the window to close when the user clicks in it.<br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order with the correct indention.  Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are incorrectly indented.</p>  
   -----
   from turtle import *      
   =====   
   space = Screen()
   carlos = Turtle()
   =====
   # repeat 2 times
   for i in [1,2]:  
   =====   
       carlos.forward(175)
   =====
       carlos.right(90)
   =====  
       carlos.forward(150)
       carlos.right(90)
   
Since it doesn't matter what's in the list, just as long as there are *four* items, there is a special way of writing that loop.  We use a ``range`` function. 

.. activecode:: Turtle_For_Range
  :tour_1: "Line-by-line tour"; 1: tR2-line1; 2: tR2-line2; 3: tR2-line3; 4: tR2-line4; 7: tR2-line7; 8: tR2-line8; 9: tR2-line9;
  :nocodelens:
 
  from turtle import *		# use the turtle library
  space = Screen()   		# create a turtle space
  marcus = Turtle()  		# create a turtle named marcus
  marcus.setheading(90)		# point due north
  
  # Now make a square
  for sides in range(4):	# repeat the indented lines 4 times
      marcus.forward(100)      		# move forward by 100 units
      marcus.right(90)          		# turn by 90 degrees


The ``range`` function returns a value so that the *for* loop executes that many times.  This makes the turtle go forward and turn right 90 degrees *four* times.

.. |turtlegeometry| image:: Figures/turtle-geometry.jpg
    :width: 200px
    :align: top
    :alt: teachernote




