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
	:prefix: 6-10-

Chapter 6 Exercises
--------------------

#. 

    .. tabbed:: ch6ex1t

        .. tab:: Question
            
            There are errors in the indention in the following code.  Fix it to work correctly without errors.  

            .. activecode:: ch6ex1q
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

        .. tab:: Answer
        
            The lines following the defintion of the square procedure needed to be indented by 4 spaces as shown below. 

            .. activecode:: ch6ex1a
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

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch6ex1q
                
#. 
   
    .. tabbed:: ch6ex2t

        .. tab:: Question

           There are 2 syntax errors in the following code.  Fix the errors so that it runs.  
           
           .. activecode::  ch6ex2q
                :nocodelens:

                def square(turtle)
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
                square()       	        # draw a square with malik


        .. tab:: Answer
        
            There must be a ``:`` at the end of the procedure definition.  You also have to pass malik to the square procedure as shown below.
            
            .. activecode::  ch6ex2a
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
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex2q

#. 

    .. tabbed:: ch6ex3t

        .. tab:: Question

           The following code has 4 syntax errors.  Fix the errors so that the code runs. 
        
           .. activecode::  ch6ex3q
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
                square(Malik, 100) 	# draw a square of size 100
                square(Malik, 75)   	# draw a square of size 75
                square(Malik, 50)    	# draw a square of size 50
                square(Malik, 25)   	# draw a square of size 25

        .. tab:: Answer
        
            You must change the ``Malik`` to ``malik`` on the calls to square.  Remember that Python is case sensitive.
            
            .. activecode::  ch6ex3a
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
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch6ex3q
                
#. 

    .. tabbed:: ch6ex4t

        .. tab:: Question

           The following code has three lines that need to be changed.  Fix the code to run correctly. 
           
           .. activecode::  ch6ex4q
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
                square(100, malik) 	# draw a square of size 100
                square(malik)   	    # draw a square of size 75
                square(50)    	    # draw a square of size 50
                square(malik, 25)   	# draw a square of size 25
          

        .. tab:: Answer
        
            You have to pass the turtle first and then the size separated by a ``,``.  
            
            .. activecode::  ch6ex4a
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
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex4q
   
#. 

    .. tabbed:: ch6ex5t

        .. tab:: Question

           Change the square procedure below to take a size parameter and have the turtle go forward by the specified size each time.
           
           .. activecode::  ch6ex5q
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

        .. tab:: Answer
        
            Add the ``size`` parameter to the procedure defintion and be sure to add a value for the size when you call the procedure as well.
            
            .. activecode::  ch6ex5a
                :nocodelens:

                def square(turtle, size):
                    turtle.forward(size)
                    turtle.right(90)
                    turtle.forward(size)
                    turtle.right(90)
                    turtle.forward(size)
                    turtle.right(90)
                    turtle.forward(size)
                    turtle.right(90)

                from turtle import * 	# use the turtle library
                space = Screen()     	# create a turtle screen
                malik = Turtle()    	# create a turtle named malik
                square(malik,50)       # draw a square with malik

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex5q
                
#. 

    .. tabbed:: ch6ex6t

        .. tab:: Question

           Change the code below to create a function that calculates the cost of a trip.  It should take the ``miles``, ``milesPerGallon``, and ``pricePerGallon`` as parameters and should return the cost of the trip.  
           
           .. activecode::  ch6ex6q
                :nocodelens: 
                
                miles = 500
                milesPerGallon = 26
                numGallons = miles / milesPerGallon
                pricePerGallon = 3.45
                total = numGallons * pricePerGallon
                print(total)

        .. tab:: Answer
        
            Add a function definition that takes as parameters ``miles``, ``milesPerGallon``, and ``pricePerGallon``.  Don't forget to call the function to test it.  
            
            .. activecode::  ch6ex6a
                :nocodelens:
                
                def costOfTrip(miles, milesPerGallon, pricePerGallon):
                    numGallons = miles / milesPerGallon
                    total = numGallons * pricePerGallon
                    return(total)
                    
                print("The cost of the trip is " + str(costOfTrip(500,26,3.45)))
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex6q
                
#. 

    .. tabbed:: ch6ex7t

        .. tab:: Question

           Change the code below to create a function to return the number of miles you can drive.  It will take as input (parameters) the ``tankCapacity``, ``theAmountLeft``, and the ``milesPerGallon``.  
           
           .. activecode::  ch6ex7q
                :nocodelens: 
                
                tankCapacity = 10
                amountLeft = 0.25
                numGallons = tankCapacity * amountLeft
                milesPerGallon = 32
                numMiles = numGallons * milesPerGallon 
                print(numMiles)         

        .. tab:: Answer
        
            Add a function definition that takes as parameters ``tankCapacity``,``amountLeft``, and ``milesPerGallon``.  Be sure to call the function to test it.
            
            .. activecode::  ch6ex7a
                :nocodelens:
                
                def calcNumMiles(tankCapacity,amountLeft, milesPerGallon):
                    numGallons = tankCapacity * amountLeft
                    numMiles = numGallons * milesPerGallon 
                    return(numMiles) 
                    
                print("The number of miles you can go is " + str(calcNumMiles(10,0.25,32)))
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex7q
                
#. 

    .. tabbed:: ch6ex8t

        .. tab:: Question

           Create a procedure to draw a rectangle and call it.  Be sure to take the ``width`` and ``height`` of the rectangle as input to the procedure.
           
           .. activecode::  ch6ex8q
                :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch6ex8a
                :nocodelens:
                
                def rectangle(turtle, width, height):
                    turtle.forward(width)
                    turtle.right(90)
                    turtle.forward(height)
                    turtle.right(90)
                    turtle.forward(width)
                    turtle.right(90)
                    turtle.forward(height)

                from turtle import * 	# use the turtle library
                space = Screen()     	# create a turtle screen
                malik = Turtle()    	# create a turtle named malik
                rectangle(malik, 100, 80)    # draw a rectangle with malik
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex8q
                
#. 

    .. tabbed:: ch6ex9t

        .. tab:: Question

           Create a procedure to draw a triangle and call it.  Be sure to take the length of each side of the triangle as input to the procedure.
           
           .. activecode::  ch6ex9q
                :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch6ex9a
                :nocodelens:
                
                def triangle(turtle, size):
                    turtle.left(60)
                    turtle.forward(size)
                    turtle.right(120)
                    turtle.forward(size)
                    turtle.right(120)
                    turtle.forward(size)

                from turtle import * 	# use the turtle library
                space = Screen()     	# create a turtle screen
                malik = Turtle()    	# create a turtle named malik
                triangle(malik, 100)    # draw a triangle with malik
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex9q
                
#. 

    .. tabbed:: ch6ex10t

        .. tab:: Question

           Write the code below to create a procedure that prints a mad lib.  You can ask the user for input and then pass that input into the procedure.
           
           .. activecode::  ch6ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch6ex10a
                :nocodelens:
                
                def printMadLib(place,verb,action,color,animal):
                    print("Once upon a time in " + place + ", I was " + 
                          verb + "ing and I " + action + " because a " + 
                          color + " " + animal + " was also " + verb + "ing.")
                          
                place = input("Enter the name of a place.")
                verb = input("Enter a verb.")
                action = input("Enter an action.")
                color = input("Enter your favorite color.")
                animal = input("What is your favorite animal?")
                printMadLib(place,verb,action,color,animal)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex10q



