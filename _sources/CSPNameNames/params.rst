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
	:prefix: csp-6-5-
	
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teachers Note: Creating Procedures with Parameters
===================================================================

You probably don't quite feel comfortable with creating procedures with parameters right now.  That's okay.  Our research on how people learn programming says that understanding how *names* can represent *something else* takes alot of practice.  People new to programming will probably prefer:


:: 

   from turtle import *    
   space = Screen()    		
   malik = Turtle()   		
   malik.forward(100)
   malik.right(90)
   malik.forward(100)
   malik.right(90)
   malik.forward(100)
   malik.right(90)
   malik.forward(100)
   malik.right(90)

To creating a ``square`` procedure as shown below

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

and then calling the ``square`` procedure as shown below

:: 

   from turtle import *     # use the turtle library
   space = Screen()    		# create a turtle screen (space)
   malik = Turtle()   		# create a turtle named malik
   square(malik, 100)     	# draw a square with side length 100

When people are first learning programming, they prefer seeing actual values like ``forward(100)`` over ``forward(size)``.  They can probably recognize that having one ``square`` function that can make squares of all kinds of sizes is flexible and thus powerful.  But, they are still trying to understand the baisc turtle commands yet. 

..	index::
	single: abstraction 

Don't worry about creating procedures with parameters yet.  That will come later in the chapter on **abstraction**.  **Abstraction** means focusing on just the important details in a context, just like using an abstract figure to identify female restrooms as shown below.  

.. figure:: Figures/femaleIcon.jpg
    :height: 100px
    :align: center
    :alt: abstract representation of a female 
    :figclass: align-center

    Figure 2: Abstract representation of a female

Right now, it's okay to just be able to read procedures and understand what happens when they are called.  As beginners become more comfortable with basic programming, they will be ready to use the abstraction of using names to represent things like new procedures and functions.

