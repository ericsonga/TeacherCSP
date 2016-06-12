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
	:prefix: csp-6-4-
	
.. highlight:: java
   :linenothreshold: 4

Naming Input 
================

What if we want to draw a different size square, like one with a side length of 50?  We could change each of the calls to the ``forward`` procedure as shown below. 

.. activecode:: Function_Change_Size
  :tour_1: "Important lines tour"; 1-9: sq50-line1-9; 2,4,6,8: sq50-line2468; 11-13: sq50-line11-13; 14: sq50-line14; 
  :nocodelens:

  def square(turtle):
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)

  from turtle import * 	# use the turtle library
  space = Screen()    	# create a turtle screen
  malik = Turtle()    	# create a turtle named malik
  square(malik)      	# draw a square with malik
  
But, this means we have to change each of the four ``forward`` statements and we could make a mistake and not set all of them to the same number.  Is there a better way?  What if we create a variable ``size`` and set its value to the amount to move forward?

.. activecode:: Function_Add_Var
  :tour_1: "Important lines tour"; 1-10: sqvar-line1-10; 2: sqvar-line2; 3: sqvar-line3; 4: sqvar-line4; 5-10: sqvar-line5-10; 12-14: sqvar-line12-14; 15: sqvar-line15;
  :nocodelens:

  def square(turtle):
      size = 50
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)

  from turtle import *	# use the turtle library
  space = Screen()    	# create a turtle screen
  malik = Turtle()    	# create a turtle named malik
  square(malik)      	# draw a square with malik
  
.. mchoice:: 6_4_1_Function_Var_Q1
   :answer_a: 100
   :answer_b: 50
   :answer_c: 200
   :answer_d: 90
   :correct: c
   :feedback_a: How much will it go forward?
   :feedback_b: What value is size set to?
   :feedback_c: Size is set to 200 in line 2 so this will draw a square that has a side length of 200.
   :feedback_d: It turns 90 degrees.  It doesn't go forward 90.  

   What is the side length for a square drawn by the following procedure?
   
    :: 
 
     def square(turtle):
         size = 200
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)

Now the program is easier to change since we only have one line to change ``size = 50`` to draw another size square.  But, we still have to change the program in order to draw a different size square.  Is there a better way?

We can add an additional input to the function that specifies the size of the square.  Just separate the names for the inputs with a comma: ``(turtle,size)`` as shown below and be sure to specify the actual size when you call the procedure ``square(malik, 100)`` or ``square(malik, 50)``.

.. activecode:: Function_Call2
  :tour_1: "Important lines tour"; 1-9: dsq3-line1-9; 2: dsq3-line2; 11-13: dsq3-line11-13; 14: dsq3-line14; 15: dsq3-line15; 16: dsq3-line16; 17: dsq3-line17;
  :nocodelens:

  def square(turtle,size):
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)

  from turtle import *	# use the turtle library
  space = Screen()    	# create a turtle screen (space)
  malik = Turtle()    	# create a turtle named malik
  square(malik, 100) 	# draw a square of size 100
  square(malik, 75)   	# draw a square of size 75
  square(malik, 50)    	# draw a square of size 50
  square(malik, 25)   	# draw a square of size 25
  
.. mchoice:: 6_4_2_Name_The_Shape_Q1
   :answer_a: square
   :answer_b: rectangle
   :answer_c: triangle
   :correct: b
   :feedback_a: Check the 2nd and 4th forwards.  How much do they move forward by?
   :feedback_b: This will draw a rectangle with two sides with the specified size and two sides half that size.  Copy this code into the area above and run it.  
   :feedback_c: A triangle has 3 sides.

   What shape would the following code draw? 
   
   :: 
 
     def mystery(turtle,size):
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size / 2)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size / 2)
         turtle.right(90)
      
     from turtle import *	# use the turtle library
     space = Screen()     	# create a turtle screen (space)
     malik = Turtle()     	# create a turtle named malik
     mystery(malik, 100)   	# draw something with size = 100


.. index:: 
	single: arguments
.. index:: 
	single: actual parameters
.. index:: 
	single: parameters
.. index:: 
	single: formal parameters
	pair: parameters; formal
	pair: parameters; actual
  
The inputs that are specified in a function or procedure definition are also called **parameters** or **formal parameters**.  So ``turtle`` and ``size`` are both parameters (formal parameters) in the ``square`` procedure.  Notice that when we call ``square`` we have to specify the actual values for the inputs.  The actual values passed into the function as inputs are called the **arguments** or **actual parameters**. In the call ``square(malik, 50)`` both ``malik`` and ``50`` are arguments (actual parameters) to the ``square`` procedure.  

.. mchoice:: 6_4_3_Name_Args_Q1
   :answer_a: turtle and size
   :answer_b: malik and 25
   :answer_c: imani and 25
   :correct: c
   :feedback_a: These are the names of the parameters (formal parameters).  
   :feedback_b: Look again at the code above.  Is that the name of this turtle?
   :feedback_c: The turtle is named imani and the size is 25 in the code: square(imani, 25). 

   In the following code what are the arguments (actual parameters)?  
   
   :: 
 
     def square(turtle,size):
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
     
     from turtle import * 	# use the turtle library
     space = Screen()      	# create a turtle screen (space)
     imani = Turtle()    	# create a turtle named imani
     square(imani, 25)      # draw a square with size 25
     
.. parsonsprob:: 6_4_4_Draw_Squares

   The following code assumes that a procedure square has been defined that takes a size.  The code should create a turtle and then use it to draw a square, move forward, and draw a second square as shown at left, <img src="../_static/SquareForwardSquare.png" width="150" align="left" hspace="10" vspace="5"/> but the lines are mixed up.  Drag the lines into the correct order on the right.
   -----
   from turtle import *    
   =====
   space = Screen() 
   =====   		
   imani = Turtle()   		
   =====
   square(imani, 75)
   =====
   imani.forward(100)
   =====
   square(imani, 50)

