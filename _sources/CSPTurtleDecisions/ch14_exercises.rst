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
	:prefix: 14-7-

Chapter 14 Exercises
---------------------

#. 

    .. tabbed:: ch14ex1t

        .. tab:: Question
            
            Fix 5 errors in the code below so that it runs correctly. It will draw red and black horizontal stripes.  

            .. activecode:: ch14ex1q
                :nocodelens:

                from turtle import               # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle(                    # create a turtle named sue         
                sue.pensize(10)                  # set the pen width
    
                for y in range(5):               # repeat 5 times
    	            sue.penup()                      # pick up the pen
       	            if y % 2 == 0:                   # if even row
                    sue.color('red')                 # set the color to red
       	            if y % 2 == 1:                   # if odd row
                        sue.color('black')               # set the color to black
       	            sue.goTo(-1 * maxX,y * 10)       # move to the next row
       	            sue.pendown()                    # put the pen down
       	            sue.forward(width)               # move forward by the width
      	            
        .. tab:: Answer
        
            Add ``*`` at the end of line 1.  Change line 4 to ``Screen``.  Add a ``)`` at the end of line 9.  Indent line 15.  Change line 18 to ``goto``.  
            
            .. activecode:: ch14ex1a
                :nocodelens:

                from turtle import *             # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = Screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle()                   # create a turtle named sue         
                sue.pensize(10)                  # set the pen width
    
                for y in range(5):               # repeat 5 times
    	            sue.penup()                      # pick up the pen
       	            if y % 2 == 0:                   # if even row
                        sue.color('red')                 # set the color to red
       	            if y % 2 == 1:                   # if odd row
                        sue.color('black')               # set the color to black
       	            sue.goto(-1 * maxX,y * 10)       # move to the next row
       	            sue.pendown()                    # put the pen down
       	            sue.forward(width)               # move forward by the width

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch14ex1q

#. 

    .. tabbed:: ch14ex2t

        .. tab:: Question

           Indent lines in the code below so that it runs correctly.  It will stamp 4 turtles in two different colors at the corners of a square.  
           
           .. activecode::  ch14ex2q
                :nocodelens:
                
                from turtle import *             # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = Screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle()                   # create a turtle named sue         
                sue.shape("turtle") 
                sue.penup()   
                sue.left(45)          
    
                for y in range(4):               # repeat 4 times
       	        if y % 2 == 0:                   # if even row
                sue.color('red')                 # set the color to red
       	        if y % 2 == 1:                   # if odd row
                sue.color('black')               # set the color to black
                sue.forward(100)
                sue.stamp()
                sue.backward(100)
                sue.left(90)
                
          
        .. tab:: Answer
        
            Indent lines 15 to 22 as shown below.  
            
            .. activecode::  ch14ex2a
                :nocodelens:
                
                from turtle import *             # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = Screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle()                   # create a turtle named sue         
                sue.shape("turtle") 
                sue.penup()   
                sue.left(45)          
    
                for y in range(4):               # repeat 4 times
       	            if y % 2 == 0:                   # if even row
                        sue.color('red')                 # set the color to red
       	            if y % 2 == 1:                   # if odd row
                        sue.color('black')               # set the color to black
                    sue.forward(100)
                    sue.stamp()
                    sue.backward(100)
                    sue.left(90)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex2q

#. 

    .. tabbed:: ch14ex3t

        .. tab:: Question

           Fix 5 errors in the code below so that it runs correctly.  It will draw a repeating pattern from left to right until it hits the width of the window and then will move back to the left side of the window to continue the pattern.
        
           .. activecode::  ch14ex3q
                :nocodelens:
                
                from turtle *             # use the turtle library
                from sys import *         # use the system library
                setExecutionLimit(50000)  # let this take up to 50 seconds
                space = Screen()          # create a turtle screen (space)

                width = 400               # set the desired width
                Space.setup(width,width)  # set the space width and height
                maxX = width / 2          # set the max x value to half the width

                jaz = Turtle()            # create a turtle named jaz
                jaz.shape('turtle')       # set the shape for jaz to turtle
                jaz.penup()               # pick up the pen (don't draw)
                jaz.goto(-1 * maxX,100)   # go to the left side of the space
                jaz.penDown()             # put the pen down to draw with
                jaz.left(60)              # turn the turtle left 60 degrees

                for x in range(10):       # repeat the body 10 times
                    jaz.forward 100)           # go forward 100
                    jaz.right(120)             # turn right 120 degrees
                    jaz.forward(100)           # go forward 100
                    jaz.left(120              # turn left 120 degrees
                    if (jaz.xcor() >= maxX):   # if at right edge of space
                        jaz.penup()                # pick up the pen
                        jaz.goto(-1 * maxX,jaz.ycor() - 100)  # move left & down
                        jaz.pendown()              # put the pen down
         

        .. tab:: Answer
        
            Add ``import`` on line 1.  Change line 7 to ``space``.  Change line 14 to ``pendown``.  Add a ``(`` before the ``100`` on line 18.  Add a ``)`` on line 21.
            
            .. activecode::  ch14ex3a
                :nocodelens:

                from turtle import *      # use the turtle library
                from sys import *         # use the system library
                setExecutionLimit(50000)  # let this take up to 50 seconds
                space = Screen()          # create a turtle screen (space)

                width = 400               # set the desired width
                space.setup(width,width)  # set the space width and height
                maxX = width / 2          # set the max x value to half the width

                jaz = Turtle()            # create a turtle named jaz
                jaz.shape('turtle')       # set the shape for jaz to turtle
                jaz.penup()               # pick up the pen (don't draw)
                jaz.goto(-1 * maxX,100)   # go to the left side of the space
                jaz.pendown()             # put the pen down to draw with
                jaz.left(60)              # turn the turtle left 60 degrees

                for x in range(10):       # repeat the body 10 times
                    jaz.forward(100)           # go forward 100
                    jaz.right(120)             # turn right 120 degrees
                    jaz.forward(100)           # go forward 100
                    jaz.left(120)              # turn left 120 degrees
                    if (jaz.xcor() >= maxX):   # if at right edge of space
                        jaz.penup()                # pick up the pen
                        jaz.goto(-1 * maxX,jaz.ycor() - 100)  # move left & down
                        jaz.pendown()              # put the pen down


        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch14ex3q
                
#. 
                
    .. tabbed:: ch14ex4t

        .. tab:: Question

           Change the code below to use ``if`` and ``else``.  Also fix any errors.   You will need to change 3 lines.  The code will draw random connected lines in alternating colors of red and black.
           
           .. activecode::  ch14ex4q
                :nocodelens:

                from turtle import *      # use the turtle library
                import random
                space = Screen()          # create a turtle screen (space)
                width = space.window_width()
                height = space.window_height()
                maxX = width / 2  # get the max x value
                minX = -1 * maxX
                maxY = height / 2
                minY = -1 * maxY
                jaz = Turtle()            # create a turtle named jaz
                for num in range(10):
                    if num % 2 == 0              # if even row
                        jaz.color('red')          # set the color to red
                    if num % 2 == 1:             # if odd row
                    jaz.color('black')       # set the color to black
                    randX = random.randrange(minX, maxX)
                    randY = random.randrange(minY, maxY)
                    jaz.goto(randX,randY)


        .. tab:: Answer
        
            Add a ``:`` at the end of line 12.  Change line 14 to ``else:``.  Indent line 15.
            
            .. activecode::  ch14ex4a
                :nocodelens:
                
                from turtle import *      # use the turtle library
                import random
                space = Screen()          # create a turtle screen (space)
                width = space.window_width()
                height = space.window_height()
                maxX = width / 2  # get the max x value
                minX = -1 * maxX
                maxY = height / 2
                minY = -1 * maxY
                jaz = Turtle()            # create a turtle named jaz
                for num in range(10):
                    if num % 2 == 0:             # if even row
                        jaz.color('red')          # set the color to red
                    else:
                        jaz.color('black')       # set the color to black
                    randX = random.randrange(minX, maxX)
                    randY = random.randrange(minY, maxY)
                    jaz.goto(randX,randY)

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex4q
                

   
#. 

    .. tabbed:: ch14ex5t

        .. tab:: Question

           Fix the indention so that the code runs correctly.  Two turtles will move towards each other and then turn around and move away from each other.
           
           .. activecode::  ch14ex5q
                :nocodelens:

                from turtle import *
                space = Screen()
                jaz = Turtle()
                mia = Turtle()
                mia.color('red')
                mia.penup()
                mia.goto(100,0)
                mia.pendown()
                mia.right(180)
                for x in range(20):
                jaz.forward(10)
                mia.forward(10)
                if (mia.xcor() - jaz.xcor() < 40):
                jaz.right(45)
                mia.right(45)

        .. tab:: Answer
        
            Indent lines 11-15 as shown below. 
            
            .. activecode::  ch14ex5a
                :nocodelens:

                from turtle import *
                space = Screen()
                jaz = Turtle()
                mia = Turtle()
                mia.color('red')
                mia.penup()
                mia.goto(100,0)
                mia.pendown()
                mia.right(180)
                for x in range(20):
                    jaz.forward(10)
                    mia.forward(10)
                    if (mia.xcor() - jaz.xcor() < 40):
                        jaz.right(45)
                        mia.right(45)

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex5q
                
#. 

    .. tabbed:: ch14ex6t

        .. tab:: Question

           The following code stamps a circle of turtles.  Change the following code to use a different color per stamp and use at least 3 colors.  You can use a counter and reset the counter to 0 after it reaches the number of colors.  Use ``if``, ``elif``, and ``else``. 
           
           .. activecode::  ch14ex6q
                :nocodelens: 
                
                from turtle import *
                space = Screen()
                jose = Turtle()
                jose.shape("turtle")
                jose.penup()               
                for size in range(10):    
                    jose.forward(50)
                    jose.stamp()        
                    jose.forward(-50)
                    jose.right(36)
                
     

        .. tab:: Answer
        
            Add lines 7-12 as shown below.  
            
            .. activecode::  ch14ex6a
                :nocodelens:
                
                from turtle import *
                space = Screen()
                jose = Turtle()
                jose.shape("turtle")
                jose.penup()             
                for size in range(10):   
                    if (size % 3 == 0): 
                        jose.color('blue')
                    elif (size % 3 == 1): 
                        jose.color('yellow')
                    else: 
                        jose.color('gray')
                    jose.forward(50)
                    jose.stamp()        
                    jose.forward(-50)
                    jose.right(36)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex6q
                
#. 

    .. tabbed:: ch14ex7t

        .. tab:: Question

           The following code stamps turtles in a spiral.  Change the code below to cycle through at least 3 colors.  Use ``if``, ``elif``, and ``else``. 
           
           .. activecode::  ch14ex7q
                :nocodelens: 
                
                from turtle import *
                space = Screen()
                tess = Turtle()
                tess.shape("turtle")
                tess.penup()                  # ask tess to pick up her pen
                for size in range(5, 60, 2):  # start with size = 5 and grow by 2
                    tess.stamp()                # leave an impression on the canvas
                    tess.forward(size)          # move tess along
                    tess.right(24)              # and turn her
                
                

        .. tab:: Answer
        
            Add lines 7-12 as shown below. 
            
            .. activecode::  ch14ex7a
                :nocodelens
                
                from turtle import *
                space = Screen()
                tess = Turtle()
                tess.shape("turtle")
                tess.penup()                  # ask tess to pick up her pen
                for size in range(5, 60, 2):  # start with size = 5 and grow by 2
                    if (size % 3 == 0): 
                        tess.color('blue')
                    elif (size % 3 == 1):
                        tess.color('yellow')
                    else: 
                        tess.color('gray')               
                    tess.stamp()                # leave an impression on the canvas
                    tess.forward(size)          # move tess along
                    tess.right(24)              # and turn her
                
                
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex7q
                
#. 

    .. tabbed:: ch14ex8t

        .. tab:: Question

           The following code draws vertical stripes alternating between red and black.  Change the code below to use 5 different colors.  Use ``y % 5`` to get 5 possible values.
           
           .. activecode::  ch14ex8q
                :nocodelens:
                
                from turtle import *             # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = Screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle()                   # create a turtle named sue         
                sue.pensize(10)                  # set the pen width
    
                for y in range(10):               # repeat 10 times
    	            sue.penup()                      # pick up the pen
       	            if y % 2 == 0:                   # if even row
                        sue.color('red')                 # set the color to red
       	            if y % 2 == 1:                   # if odd row
                        sue.color('black')               # set the color to black
       	            sue.goto(-1 * maxX,y * 10)       # move to the next row
       	            sue.pendown()                    # put the pen down
       	            sue.forward(width)               # move forward by the width

        .. tab:: Answer
        
            Modify lines 15 and 17 as shown below.  Add lines 18 to 23.
            
            .. activecode::  ch14ex8a
                :nocodelens:
                
                from turtle import *             # use the turtle library
                from sys import *                # use the system library
                setExecutionLimit(100000)        # let this take up to 100 seconds
                space = Screen()                 # create a turtle screen (space)
    
                width = space.window_width()     # get the width of the screen (space)
                maxX = width / 2                 # set the max x value to half the width
    
                sue = Turtle()                   # create a turtle named sue         
                sue.pensize(10)                  # set the pen width
    
                for y in range(10):              # repeat 10 times
    	            sue.penup()                      # pick up the pen
       	            if y % 5 == 0:               
                        sue.color('red')                 # set the color to red
       	            if y % 5 == 1:                  
                        sue.color('black')  
                    if y % 5 == 2: 
                        sue.color('orange')   
                    if y % 5 == 3:
                        sue.color('green')
                    if y % 5 == 4:
                        sue.color('blue')         
       	            sue.goto(-1 * maxX,y * 10)       # move to the next row
       	            sue.pendown()                    # put the pen down
       	            sue.forward(width)               # move forward by the width

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex8q
                
#. 

    .. tabbed:: ch14ex9t

        .. tab:: Question

           Write a function takes a number and returns a color.  It will return 'yellow' if the number modulus 3 is 0, 'blue' if it is 1, and 'green' if it is 2. 
            
           .. activecode::  ch14ex9q
                :nocodelens:

        .. tab:: Answer
        
            Define the function as shown below and be sure to create tests that try all possible execution paths (all return values).
            
            .. activecode::  ch14ex9a
                :nocodelens:
                
                def getColor(num):
                    if num % 3 == 0:
                        return 'yellow'
                    elif num % 3 == 1:
                        return 'blue'
                    else:
                        return 'green'
                        
                print(getColor(3))
                print(getColor(4))
                print(getColor(5))
                print(getColor(6))
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex9q
                
#. 

    .. tabbed:: ch14ex10t

        .. tab:: Question

           Write code that draws a pattern with the turtle with at least 3 different colors used.  The code must have a ``for`` loop and must have a ``if`` statement inside the for loop that changes the color.    
           
           .. activecode::  ch14ex10q
               :nocodelens:

        .. tab:: Answer
        
            Below is one possible example.  Look for a for loop with an if statment inside of it that changes the color.  
            
            .. activecode::  ch14ex10a
                :nocodelens:
                
                from turtle import *
                space = Screen()
                jose = Turtle()
                for size in range(9):   
                    if (size % 3 == 0): 
                        jose.color('green')
                    elif (size % 3 == 1): 
                        jose.color('blue')
                    else: 
                        jose.color('yellow')
                    jose.forward(50)      
                    jose.forward(-50)
                    jose.right(40)
         
                                 
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch14ex10q



