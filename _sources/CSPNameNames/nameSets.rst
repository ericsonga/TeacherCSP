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
	:prefix: csp-6-6-
	
.. highlight:: java
   :linenothreshold: 4

Naming Sets of Procedures and Functions
=========================================

So far we've seen names for values, like variables that hold strings and numbers.  We've also seen how to name (*define*) functions or procedures and use additional names to store the inputs to those functions or procedures.

Sometimes, you will want to have have a whole group of functions and/or procedures, and you will want to store them somewhere and *name* that *whole set of functions and procedures*.  In fact, you can.  And in fact, you have already used this ability.

.. index::
	single: import, from import

That is what you are doing when you execute a statement like ``from turtle import *``.  That is where the procedures like ``forward`` and ``right`` and functions like ``Screen`` are defined.  We can mix procedures and functions that *we* define with procedures and functions that we *import*.

.. activecode:: Squares_Pattern
  :tour_1: "Important lines tour"; 1-9: sqM-line1-9; 11-13: sqM-line11-13; 14: sqM-line14; 15: sqM-line15; 16: sqM-line16; 17: sqM-line17; 18: sqM-line18; 19: sqM-line19; 20: sqM-line20; 21: sqM-line21; 22: sqM-line22; 23: sqM-line23; 
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

  from turtle import *      # use the turtle library
  space = Screen()          # create a turtle screen (space)
  emily = Turtle()          # create a turtle named emily
  emily.setheading(90)      # Point due north
  emily.forward(10)         # Offset the shapes a bit
  emily.right(18)           # And turn each one a bit
  square(emily,100)   		# draw a square with size 100
  emily.forward(10)         # Offset the shapes a bit
  emily.right(18)           # And turn each one a bit
  square(emily,100) 		# draw a square with size 100
  emily.forward(10)         # Offset the shapes a bit
  emily.right(18)           # And turn each one a bit
  square(emily,100)  		# draw a square with size 100

.. mchoice:: 6_6_1_Function_Use_Q1
   :answer_a: square
   :answer_b: forward
   :answer_c: right
   :answer_d: All of the above
   :correct: d
   :feedback_a: You can use square since you just defined it, but you can also use the others.
   :feedback_b: You can use forward because of the import, but you can also use others.
   :feedback_c: You can use right because of the import, but you can also use others.
   :feedback_d: Yes, you can use all of the turtle stuff from the import, plus the procedure square that was defined.
   
   Imagine that you add one more line to the program above.  Which procedure can you use safely, because it will have been defined?

