..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
    

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: 5-9-

Chapter 5 Exercises
--------------------

#. 

    .. tabbed:: ch5ex1t

        .. tab:: Question
            
            There are 3 syntax errors in the following code.  Fix it to work correctly without errors.  

            .. activecode:: ch5ex1q
                :nocodelens:

                from turtle import *            
                space = screen()     
                alex = Turtle
                alex.Forward(150)                 

        .. tab:: Answer
        
            Change ``screen`` to ``Screen``.  Change ``Turtle`` to ``Turtle()``.  Change ``Forward`` to ``forward``.  

            .. activecode:: ch5ex1a
                :nocodelens:

                from turtle import *             
                space = Screen()     
                alex = Turtle()
                alex.forward(150)

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch5ex1q
                
#. 
   
    .. tabbed:: ch5ex2t

        .. tab:: Question

           The following program is missing things on lines 1, 2, and 3.  Add the missing parts.
           
           .. activecode::  ch5ex2q
                :nocodelens:

                from            
                space =     
                alex = 
                alex.forward(150)

        .. tab:: Answer
        
           Finish the import.  Create the space using ``Screen()``.  Create the turtle using ``Turtle()``.  
            
            .. activecode::  ch5ex2a
                :nocodelens:
                
                from turtle import *             
                space = Screen()     
                alex = Turtle()
                alex.forward(150)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex2q

#. 

    .. tabbed:: ch5ex3t

        .. tab:: Question

           The following code has 3 syntax errors.  Fix the errors so that the code runs. 
        
           .. activecode::  ch5ex3q
                :nocodelens:
                
                from turtle import *              
                space = Screen()     
                alex = turtle()
                alex.Forward(150)
                alex.turn(90)
                alex.forward(75)

        .. tab:: Answer
        
            Change ``turtle()`` to ``Turtle()``.  Change ``Forward`` to ``forward``.  Change ``turn`` to ``left``.  
            
            .. activecode::  ch5ex3a
                :nocodelens:

                from turtle import *              
                space = Screen()     
                alex = Turtle()
                alex.forward(150)
                alex.left(90)
                alex.forward(75)
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch5ex3q
                
#. 

    .. tabbed:: ch5ex4t

        .. tab:: Question

           The following code draws two lines of a rectangle.  Add code to finish drawing the rectangle.  
           
           .. activecode::  ch5ex4q
                :nocodelens:

                from turtle import *           
                space = Screen()     
                alex = Turtle()
                alex.forward(150)
                alex.left(90)
                alex.forward(75)
          

        .. tab:: Answer
        
            Add another ``alex.left(90)`` and then copy and paste lines 4-6 to the end.  
            
            .. activecode::  ch5ex4a
                :nocodelens:

                from turtle import *           
                space = Screen()     
                alex = Turtle()
                alex.forward(150)
                alex.left(90)
                alex.forward(75)
                alex.left(90)
                alex.forward(150)
                alex.left(90)
                alex.forward(75)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex4q
   
#. 

    .. tabbed:: ch5ex5t

        .. tab:: Question

           The following code is missing 3 lines that do the required set-up.  Add them so that the code runs.
           
           .. activecode::  ch5ex5q
                :nocodelens:

                alex.forward(150)
                alex.left(90)
                alex.forward(75)

        .. tab:: Answer
        
            You must import the turtle library, create a drawing space, and create the turtle. 
            
            .. activecode::  ch5ex5a
                :nocodelens:

                from turtle import *           
                space = Screen()     
                alex = Turtle()
                alex.forward(150)
                alex.left(90)
                alex.forward(75)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex5q
                
#. 

    .. tabbed:: ch5ex6t

        .. tab:: Question

           Create a drawing that includes penup, pendown, and pensize.    
           
           .. activecode::  ch5ex6q
                :nocodelens:  

        .. tab:: Answer
        
            Here is one example.
            
            .. activecode::  ch5ex6a
                :nocodelens:
                
                from turtle import *           
                space = Screen()     
                alex = Turtle()
                alex.penup()
                alex.goto(-100,-100)
                alex.pendown()
                alex.forward(100)

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex6q
                
#. 

    .. tabbed:: ch5ex7t

        .. tab:: Question

           Create a drawing with at least 3 colors and using at least 3 turtles.  
           
           .. activecode::  ch5ex7q
                :nocodelens:          

        .. tab:: Answer
        
            Here is one example.
            
            .. activecode::  ch5ex7a
                :nocodelens:
                
                from turtle import *           
                space = Screen()     
                alex = Turtle()
                alex.color('blue')
                alex.forward(100)
                sue = Turtle()
                sue.color('red')
                sue.left(45)
                sue.forward(100)
                gia = Turtle()
                gia.color('green')
                gia.right(45)
                gia.forward(100)

                
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex7q
                
#. 

    .. tabbed:: ch5ex8t

        .. tab:: Question

           Write the code below to draw a diamond shape.
           
           .. activecode::  ch5ex8q
                :nocodelens:

        .. tab:: Answer
        
            Here is one example.
            
            .. activecode::  ch5ex8a
                :nocodelens:
                
                from turtle import *             
                space = Screen()     
                alex = Turtle()
                alex.left(45)
                alex.forward(50)
                alex.right(90)
                alex.forward(50)
                alex.right(90)
                alex.forward(50)
                alex.right(90)
                alex.forward(50)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex8q
                
#. 

    .. tabbed:: ch5ex9t

        .. tab:: Question

           Write the code below to draw a star like this picture.
           
           .. image:: Figures/star.png
           
           .. activecode::  ch5ex9q
                :nocodelens:

        .. tab:: Answer
        
            Here is one example.
            
            .. activecode::  ch5ex9a
                :nocodelens:
                 
                from turtle import *             
                space = Screen()     
                alex = Turtle()
                alex.forward(110)
                alex.left(216)
                alex.forward(110)
                alex.left(216)
                alex.forward(110)
                alex.left(216)
                alex.forward(110)
                alex.left(216)
                alex.forward(110)  
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex9q
                
#. 

    .. tabbed:: ch5ex10t

        .. tab:: Question

           Write the code below to draw at least one of your initials in block style. 
           
           .. activecode::  ch5ex10q
               :nocodelens:

        .. tab:: Answer
        
            Here is one example.
            
            .. activecode::  ch5ex10a
                :nocodelens:
                
                from turtle import *	# use the turtle library
                space = Screen()		# create a turtle space
                t1 = Turtle()   		# create a turtle named t1
                t1.left(180)   		# turn by 90 degrees
                t1.forward(50)		# move forward by 75 units 
                t1.right(90)           # turn right 90 degrees
                t1.forward(50)
                t1.right(90)
                t1.forward(50)
                t1.right(180)
                t1.forward(50)
                t1.right(90)
                t1.forward(50)
                t1.right(90)
                t1.forward(50)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch5ex10q



