..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

..  shortname:: Chapter: What You Can Do with a Computer
..  description:: Some tidbits of what you can do with a computer

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-1-4-


.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |teachernote| image:: Figures/apple.jpg
    :width: 26px
    :align: bottom
    :alt: teacher note



Compute with Turtles
=====================

A turtle here is not an animal.  
We are working with a virtual turtle, an idea that dates back to the 1960's.  The original robot turtle had a physical pen in it.  The student-programmers would steer the robot around using programs, and create drawings with the pen.

.. figure:: Figures/mindstorms_turtle.jpg 
    :width: 200px
    :align: center
    :alt: Children playing with a Logo turtle robot that can draw with a pen
    :figclass: align-center
    
    Figure 3: Children playing with a Logo turtle robot that could draw with a pen
    
..	index::
	single: comment
	single: library
	single: screen
	pair: turtle; screen
	pair: turtle; library
	pair: programming; comment
	pair: program; comment
    
Today, we can play with virtual turtles in a fully-graphical and non-robotic way. Below is a Python program that first reads in a **library** that contains the code to let us work with turtles (``from turtle import *``). Then it creates a **Screen**, a space on the page for the turtle to move in and draw on (``space = Screen()``).  Next it creates a turtle named ``alex`` (``alex = Turtle()``), then has ``alex`` move around on the screen (``alex.forward(150)``) and when it moves it will draw. The part of any line that starts with a  ``#`` character is called a **comment**.  Python and the computer ignores everything from the ``#`` character to the end of the line.   **Comments** explain what we're doing in the programs and are intended to be read by people, not computers.

Try clicking the |runbutton| button below to see what the following program does.

.. activecode:: Turtle_1
    :tour_1: "Line-by-line Tour"; 1: first-turtle-line-1; 2: first-turtle-line-2; 3: first-turtle-line-3; 4: first-turtle-line-4; 5: first-turtle-line-5; 6: first-turtle-line-6;
    :nocodelens:
	
    from turtle import *	# use the turtle library
    space = Screen()		# create a turtle space
    alex = Turtle()   		# create a turtle named alex
    alex.forward(150)		# move forward by 150 units
    alex.left(90)   		# turn by 90 degrees
    alex.forward(75)		# move forward by 75 units 
   
   
..	index::
	single: dot notation
	
.. Note::
   Notice that we tell ``alex`` what to do in the code above using **dot notation**: ``alex.forward(150)``, 	``alex.left(90)``, and ``alex.forward(75)``.  That is how you communicate with a turtle.  You use the name of the turtle followed by a ``.`` and then what you want it to do.  

.. mchoicemf:: 1_4_1_Turtle_Q1
   :answer_a: North
   :answer_b: West
   :answer_c: South
   :answer_d: East
   :correct: d
   :feedback_a: Check which way alex moved first
   :feedback_b: Check which way alex moved first
   :feedback_c: Check which way alex moved first
   :feedback_d: Turtles start off facing east by default
   
   Which direction will alex move when the code below executes? 
   
   :: 
   
      from turtle import *       
      space = Screen()    		  
      alex = Turtle()   		
      alex.forward(100)  

Just by going forward, backward, left, and right, we can have a turtle draw a shape.  

.. fillintheblank:: 1_4_2_Shape
   :correct: ^square$|^Square$|^SQUARE$
   :feedback1: ('.*','Did you actually run the program?')
   :blankid: shapeBlank

   What shape will the program below draw when you click on the *Run* button? :textfield:`shapeBlank::medium`

.. activecode:: Turtle_2
    :tour_1: "Line-by-line Tour"; 1: t1-line1; 2: t1-line2; 3: t1-line3; 4: t1-line4; 5: t1-line5; 6: t1-line6; 7: t1-for100-1; 8: t1-right90-1; 9: t1-for100-2; 10: t1-right90-2; 11: t1-for100-3; 12: t1-right90-3; 
    :nocodelens:
	
    from turtle import *	# use the turtle library
    space = Screen()    	# create a turtle screen (space)
    zari = Turtle()   		# create a turtle named zari
    zari.setheading(90) 	# Point due north
    zari.forward(100)   	# tell zari to move forward by 100 units
    zari.right(90)       	# turn by 90 degrees
    zari.forward(100)   	# tell zari to move forward by 100 units
    zari.right(90)       	# turn by 90 degrees
    zari.forward(100)   	# tell zari to move forward by 100 units
    zari.right(90)      	# turn by 90 degrees
    zari.forward(100)    	# tell zari to move forward by 100 units
    zari.right(90)       	# turn by 90 degrees
   
