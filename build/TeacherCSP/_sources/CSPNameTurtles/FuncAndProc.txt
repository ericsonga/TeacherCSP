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
	:prefix: csp-5-2-
	
.. highlight:: java
   :linenothreshold: 4

Procedures and Functions
================================

We have seen string **functions** like ``lower()`` which returns a new string with all lowercase characters.  **Functions** return a value.  The ``Screen()`` and ``Turtle()`` in the code below both create objects and return them, so they are functions.   You can also have **procedures** which do some action, but don't return anything.  The ``forward(75)`` and ``left(90)`` below are both procedures since they do an action, but don't return anything. 

.. note::
   Some Python books don't make a distinction between procedures and functions and will call both of these functions.  In this book we are using **function** only for named code that returns a value and **procedure** for named code that doesn't return a value.   
   
.. fillintheblank:: 5_2_1_LetterC_fill

    .. blank:: 5_2_1_LetterC
        :correct: ^c$|^C$
        :feedback1: ('.*','Try to follow the directions as if you are the turtle')

        What letter (like A and D) will the program below draw in block style when you click on the Run button?

.. activecode:: Turtle_C
    :nocodelens:
	
    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle space
    alex = Turtle()         # create a turtle named alex
    alex.left(180)          # turn by 90 degrees
    alex.forward(75)        # move forward by 75 units 
    alex.left(90)           # turn left 90 degrees
    alex.forward(100)       # more forward by 90 units
    alex.left(90)           # turn left 90 degrees
    alex.forward(75)        # move forward by 75 units 

.. note::
   Case matters in Python so ``screen`` is not the same as ``Screen``. Also the open and close parentheses are required after every function and procedure call, even if it doesn't take any input.  
   
The following example has 4 errors.  Can you fix the errors so that the code runs correctly?
    
.. activecode:: Turtle_1_Error
	
    from turtle import *    # use the turtle library
    space = screen()        # create a turtle space
    alisha = Turtle         # create a turtle named alisha
    alisha.forward          # move forward by 150 units
    alisha.left(90)         # turn by 90 degrees
    alisha.Forward(75)      # move forward by 75 units 
    
**Check Your Understanding**

.. mchoice:: 5_2_2_FuncOrProc
   :answer_a: function
   :answer_b: procedure
   :correct: b
   :feedback_a: Does it return a value?
   :feedback_b: The right procedure will cause the turtle to turn right by the specified number of degrees and doesn't return any value so it is a procedure.

   Is right(90) a function or procedure?
    
