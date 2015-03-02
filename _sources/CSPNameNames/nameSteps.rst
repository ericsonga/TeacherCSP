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
	:prefix: csp-6-3-
	
.. highlight:: java
   :linenothreshold: 4

Naming Sets of Steps
=====================

How did `abs` and `int` get defined?  By *defining* new procedures and functions, we can associate a name with a sequence of steps.  Look at the program below.  What do you think it will do when you press the *Run* button?  Click *Run* and see what happens. 

.. activecode:: First_Function
  :tour_1: "Line by line tour"; 1: dsq-line1; 2: dsq-line2; 3: dsq-line3; 4: dsq-line4; 5: dsq-line5; 6: dsq-line6; 7: dsq-line7; 8: dsq-line8; 9: dsq-line9;
  :nocodelens:

  def square(turtle):
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)

If you are wondering why the *Run* button didn't seem to do anything, all that the program did was define the procedure ``square`` which takes a ``turtle`` as input.  If we want to actually execute the program we need to create a turtle and *call* the procedure as shown in the next example.

..	index::
	single: def
	single: functions
	single: calling functions

.. activecode:: First_Function_Call
  :tour_1: "Important lines tour"; 1-9: dsq2-line1-9; 11-13: dsq2-line11-13; 14: dsq2-line14;
  :nocodelens:

  def square(turtle):
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)

  from turtle import * 	# use the turtle library
  space = Screen()     	# create a turtle screen
  malik = Turtle()    	# create a turtle named malik
  square(malik)       	# draw a square with malik
  
..	index::
	single: parameter
	pair: programming; parameter    

In the above program, we *DEFine* the word ``square`` to represent the Python statements that draw a square with a turtle.  The ``square`` procedure takes as input a ``turtle`` that will be used to draw the square. Notice that the sequence of statements that are part of the ``square`` procedure are indented.  Python uses indention to show what statements belong to the procedure.  When the indention stops with ``from turtle import *`` it means that the new statements are not part of the procedure.  

.. Note::
   Notice that we defined the turtle procedure ``def square (turtle):`` in the code above before we tried to call it ``square(malik)``.  This is required in Python, but not in some other programming languages.

.. mchoicemf:: 6_3_1_Functions_Q2
   :answer_a: Procedure
   :answer_b: Function
   :correct: b
   :feedback_a: It returns a value so it is a function
   :feedback_b: It returns a value so it can't be a procedure

   Is ``abs`` a procedure or a function?
   
.. mchoicemf:: 6_3_2_Functions_Q3
   :answer_a: Procedure
   :answer_b: Function
   :correct: a
   :feedback_a: It doesn't return a value so it is a procedure
   :feedback_b: It doesn't return a value so it can't be a function

   Is ``square`` a procedure or a function?
   
See the video below for a hint on how to solve the next mixed up code problem. 

.. video:: indentVideo
		   :controls:
		   :thumb: ../_static/video-mixedUpCodeIndent.png

		   http://ice-web.cc.gatech.edu/ce21/1/static/video/IndentVideo.mov
		   http://ice-web.cc.gatech.edu/ce21/1/static/video/IndentVideo.webm
   
.. parsonsprob:: 6_3_3_Triangle_Procedure

   The following code should define a procedure that draws a triangle, but it may be mixed up and contains extra code.  Drag the needed code to the right side in the correct order.  <b>Remember that the statements in the procedure must be indented!</b>  To indent a block drag it further right. 
   -----
   def triangle(turtle):
   =====
       turtle.left(60)
       turtle.forward(100)
       turtle.right(120)
       turtle.forward(100)
       turtle.right(120)
       turtle.forward(100)
       turtle.right(120)  
   ===== 
       endDef #distractor

