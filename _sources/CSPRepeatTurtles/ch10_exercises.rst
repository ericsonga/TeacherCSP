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
	:prefix: 10-6-

Chapter 10 Exercises
---------------------

#.

    .. tabbed:: ch10ex1t

        .. tab:: Question

            Fix 4 syntax errors in the code below to correctly draw a square

            .. activecode:: ch10ex1q
                :nocodelens:

                from turtle import 	    # use the turtle library
                space = screen()   		# create a turtle space
                alisha = Turtle  		# create a turtle named alisha
                alisha.setheading(90)  	# point due north
                for sides in [1,2,3]:	# repeat the indented lines 4 times
    	            alisha.forward(100)        	# move forward by 100 units
      	            alisha.right(90)           	# turn by 90 degrees

        .. tab:: Answer

            Add a ``*`` at the end of line 1.  Change ``screen`` to ``Screen`` in line 2.  Add ``()`` at the end of line 3.  Change line 5 to ``[1,2,3,4]``.

            .. activecode:: ch10ex1a
                :nocodelens:

                from turtle import *	# use the turtle library
                space = Screen()   		# create a turtle space
                alisha = Turtle()  		# create a turtle named alisha
                alisha.setheading(90)  	# point due north
                for sides in [1,2,3,4]:	# repeat the indented lines 4 times
    	            alisha.forward(100)        	# move forward by 100 units
      	            alisha.right(90)           	# turn by 90 degrees

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch10ex1q

#.

    .. tabbed:: ch10ex2t

        .. tab:: Question

            The code currently draws a square. Change it so that it draws a triangle.

            .. activecode::  ch10ex2q
                :nocodelens:

                from turtle import *      # use the turtle library
                space = Screen()          # create a turtle space
                alisha = Turtle()         # create a turtle named alisha
                alisha.setheading(90)     # point due north
                for sides in [1,2,3,4]:   # repeat the indented lines 4 times
                    alisha.forward(100)
                    alisha.right(90)

        .. tab:: Answer

            Change the list to only have 3 items in it and change the angle to be 120.

            .. activecode::  ch10ex2a
                :nocodelens:

                from turtle import *      # use the turtle library
                space = Screen()          # create a turtle space
                alisha = Turtle()         # create a turtle named alisha
                alisha.setheading(90)     # point due north
                for sides in [1,2,3]:     # repeat the indented lines 3 times
                    alisha.forward(100)
                    alisha.right(120)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex2q

#.

    .. tabbed:: ch10ex3t

        .. tab:: Question

           Fix the code below to draw a rectangle. You will need to fix the indention on 3 lines.

           .. activecode::  ch10ex3q
                :nocodelens:

                from turtle import *
                    space = Screen()
                carlos = Turtle()

                # repeat 2 times
                for i in [1,2]:
                    carlos.forward(175)
                    carlos.right(90)
                carlos.forward(150)
                carlos.right(90)



        .. tab:: Answer

            Change the indention on lines 2, 9 and 10 as shown below.

            .. activecode::  ch10ex3a
                :nocodelens:

                from turtle import *
                space = Screen()
                carlos = Turtle()

                # repeat 2 times
                for i in [1,2]:
                    carlos.forward(175)
                    carlos.right(90)
                    carlos.forward(150)
                    carlos.right(90)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex3q

#.

    .. tabbed:: ch10ex4t

        .. tab:: Question

            Fix the errors in the code so that it draws a square.

            .. activecode::  ch10ex4q
                :nocodelens:

                from turtle import *
                space = Screen()
                liz = Turtle()
                liz.setheading(90)
                for sides in range(5)
                    liz.forward(90)
                liz.right(100)

        .. tab:: Answer

            It should be range(4) and add a colon afterwards. Fix the indentation on the last line to be in the for loop, and switch the two numbers in the ``forward`` and ``right`` methods.

            .. activecode::  ch10ex4a
                :nocodelens:

                from turtle import *
                space = Screen()
                liz = Turtle()
                liz.setheading(90)
                for sides in range(4):
                    liz.forward(100)
                    liz.right(90)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex4q

#.

    .. tabbed:: ch10ex5t

        .. tab:: Question

           Fill in values for ``x`` on line 5 and ``y`` on line 7 to allow the code below to correctly draw a pentagon.

           .. activecode::  ch10ex5q
                :nocodelens:

                from turtle import *   	# use the turtle library
                space = Screen()    	# create a turtle space
                will = Turtle()   		# create a turtle named will
                will.setheading(90)    	# point due north
                for sides in range(x):	# repeat the indented lines
      	            will.forward(100)      	# move forward by 100 units
      	            will.right(y)


        .. tab:: Answer

            Change ``x`` to ``5`` and ``y`` to ``72``.

            .. activecode::  ch10ex5a
                :nocodelens:

                from turtle import *   	# use the turtle library
                space = Screen()    	# create a turtle space
                will = Turtle()   		# create a turtle named will
                will.setheading(90)    	# point due north
                for sides in range(5):	# repeat the indented lines 5 times
      	            will.forward(100)      	# move forward by 100 units
      	            will.right(72)          	# turn by 72 degrees


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch10ex5q

#.

    .. tabbed:: ch10ex6t

        .. tab:: Question

            Complete the code on lines 5 and 7 to draw a hexagon.

            .. activecode::  ch10ex6q
                :nocodelens:

                from turtle import *
                space = Screen()
                mia = Turtle()
                mia.setheading(90)
                for sides in
                    mia.forward(40)
                    mia.

        .. tab:: Answer

            Line 5 needs to say "for sides in range(6)" and line 7 has to have the turtle turning right by 60.

            .. activecode::  ch10ex6a
                :nocodelens:

                from turtle import *
                space = Screen()
                mia = Turtle()
                mia.setheading(90)
                for sides in range(6):
                    mia.forward(40)
                    mia.right(60)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex6q

#.

    .. tabbed:: ch10ex7t

        .. tab:: Question

           Finish the code on lines 1, 2, 3, 6 and 8 below to correctly draw a triangle.

           .. activecode::  ch10ex7q
                :nocodelens:

                from
                space =
                marie =

                # repeat
                for i in range():
                    marie.forward(100)
                    marie.left()

        .. tab:: Answer

            Add ``turtle import *`` to the end of line 1.  Add ``Screen()`` to the end of line 2.  Add ``Turtle()`` at the end of line 3.  Set line 6 to repeat 3 times.  Set line 8 to turn left 120 degrees.

            .. activecode::  ch10ex7a
                :nocodelens:

                from turtle import *
                space = Screen()
                marie = Turtle()

                # repeat 3 times
                for i in range(3):
                    marie.forward(100)
                    marie.left(120)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex7q

#.

    .. tabbed:: ch10ex8t

        .. tab:: Question

            Finish the code to draw a 15 sided figure with each side having a length of 40.

            .. activecode::  ch10ex8q
                :nocodelens:

                from turtle import *
                space = Screen()
                hi = Turtle()


        .. tab:: Answer

            You need a for loop that iterates through 15 elements. In the body of the loop, the turtle must go forward 40 and turn left 24.

            .. activecode::  ch10ex8a
                :nocodelens:

                from turtle import *
                space = Screen()
                hi = Turtle()

                for i in range(15):
                    hi.forward(40)
                    hi.left(24)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex8q

#.

    .. tabbed:: ch10ex9t

        .. tab:: Question

           Fix the indention in the code below to correctly draw 20 pentagons.

           .. activecode::  ch10ex9q
                :nocodelens:

                from turtle import *     # use the turtle library
                from sys import *        # use the system library
                setExecutionLimit(50000) # let this take up to 50 seconds
                space = Screen()         # create a turtle space
                zoe = Turtle()           # create a turtle named zoe
                zoe.setheading(90)       # point due north

                for repeats in range(20):   # draw the pattern 20 times
      	            zoe.forward(10)         	# Offset the shapes a bit
      	            zoe.right(18)             	# And turn each one a bit

      	        # This part makes a pentagon
      	        for sides in range(5):    # repeat 5 times
      	            zoe.forward(50)         # move forward by 50 unit
      	            zoe.right(72)           # turn by 72 degrees

        .. tab:: Answer

            Indent lines 13-15 as shown below.

            .. activecode::  ch10ex9a
                :nocodelens:

                from turtle import *     # use the turtle library
                from sys import *        # use the system library
                setExecutionLimit(50000) # let this take up to 50 seconds
                space = Screen()         # create a turtle space
                zoe = Turtle()           # create a turtle named zoe
                zoe.setheading(90)       # point due north

                for repeats in range(20):   # draw the pattern 20 times
      	            zoe.forward(10)         	# Offset the shapes a bit
      	            zoe.right(18)             	# And turn each one a bit

      	            # This part makes a pentagon
      	            for sides in range(5):    # repeat 5 times
      	                zoe.forward(50)         # move forward by 50 unit
                        zoe.right(72)           # turn by 72 degrees

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex9q

#.

    .. tabbed:: ch10ex10t

        .. tab:: Question

            The procedure below draws a square. Write code that uses the procedure to draw two squares connected by a line 10 units in length.

            .. activecode::  ch10ex10q
                :nocodelens:

                def square(aTurtle):
                    for sides in range(4):
                        aTurtle.forward(100)
                        aTurtle.right(90)

        .. tab:: Answer

            Call the statements needed to create a turtle. Then use a for loop with a range of 2 and call the function inside the for loop with a turtle right and forward method in there too.

            .. activecode::  ch10ex10a
                :nocodelens:

                from turtle import *
                space = Screen()
                t = Turtle()

                def square(aTurtle):
                    for sides in range(4):
                        aTurtle.forward(100)
                        aTurtle.right(90)

                for i in range(2):
                    square(t)
                    t.right(90)
                    t.forward(100)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex10q

#.

    .. tabbed:: ch10ex11t

        .. tab:: Question

           Fix the following code below to draw a circle of turtles using the ``stamp`` procedure.  You will need to change 3 lines.

           .. activecode::  ch10ex11q
                :nocodelens:

                from turtle import *
                space = Screen()
                jose = Turtle()
                jose.shape("turtle")
                jose.
                for size in range():
                    jose.forward(50)
                    jose.stamp()
                    jose.forward()
                    jose.right(36)

        .. tab:: Answer

            On line 5 add ``penup()``.  On line 6 change it to ``(10)``.  On line 9 change it to ``(-50)``.

            .. activecode::  ch10ex11a
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

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex11q

#.

    .. tabbed:: ch10ex12t

        .. tab:: Question

                Complete the code where the ``x's`` are in order to draw 20 triangles.

            .. activecode::  ch10ex12q
                :nocodelens:

                from turtle import *
                for sys import *              # use the system library
                setExecutionLimit(50000)      # let this take up to 50 seconds
                space = Screen()
                t = x
                t.setHeading(90)
                for repeats in range(x):
                    t.color("blue")
                    t.forward(10)
                    t.left(18)
                    for sides in range(x):
                        t.color("green")
                        t.forward(x)
                        t.right(x)

        .. tab:: Answer

            You need to call the Turtle() and then set the range to 20, then the next range to 3 and make the turtle go foward 60 and right 120.

            .. activecode::  ch10ex12a
                :nocodelens:

                from turtle import *
                for sys import *              # use the system library
                setExecutionLimit(50000)      # let this take up to 50 seconds
                space = Screen()
                t = Turtle()
                t.setHeading(90)
                for repeats in range(20):
                    t.color("blue")
                    t.forward(10)
                    t.left(18)
                    for sides in range(3):
                        t.color("green")
                        t.forward(60)
                        t.right(120)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex12q

#.

    .. tabbed:: ch10ex13t

        .. tab:: Question

           Rewrite the following code to create a procedure to draw a square with a turtle.  Pass the turtle and the size of the square as input (parameters) to the procedure.

           .. activecode::  ch10ex13q
                :nocodelens:

                from turtle import *	# use the turtle library
                space = Screen()   		# create a turtle space
                alisha = Turtle()  		# create a turtle named alisha
                alisha.setheading(90)  	# point due north
                for sides in [1,2,3,4]:	# repeat the indented lines 4 times
    	            alisha.forward(100)        	# move forward by 100 units
      	            alisha.right(90)           	# turn by 90 degrees


        .. tab:: Answer

            Define the procedure as shown below.  Create a turtle and do all set-up before calling the procedure.

            .. activecode::  ch10ex13a
                :nocodelens

                def drawSquare(turtle,size):
                    for sides in [1,2,3,4]:	# repeat the indented lines 4 times
    	                turtle.forward(size)    # move forward by 100 units
      	                turtle.right(90)        # turn by 90 degrees

      	        from turtle import *	# use the turtle library
                space = Screen()   		# create a turtle space
                alisha = Turtle()  		# create a turtle named alisha
                drawSquare(alisha,50)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex13q

#.

    .. tabbed:: ch10ex14t

        .. tab:: Question

            Currently, the code has a turtle drawing a straight line. Add 2 lines of code (1 before the loop and 1 in the loop) to make the turtle stamp in the line.

            .. activecode::  ch10ex14q
                :nocodelens:

                from turtle import *
                space = Screen()
                tess = Turtle()
                tess.color("blue")
                tess.shape("turtle")


                for size in range(5, 60, 2):

                    tess.forward(size)

        .. tab:: Answer

            You have to add a penup statement before the loop and a stamp statement in the loop.

            .. activecode::  ch10ex14a
                :nocodelens:

                from turtle import *
                space = Screen()
                tess = Turtle()
                tess.color("blue")
                tess.shape("turtle")

                tess.penup()
                for size in range(5, 60, 2):
                    tess.stamp()
                    tess.forward(size)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex14q

#.

    .. tabbed:: ch10ex15t

        .. tab:: Question

           Rewrite the following code to create a procedure to draw a rectangle with a turtle.  Pass the turtle and the length and width of the rectangle as parameters to the procedure.

           .. activecode::  ch10ex15q
                :nocodelens:

                from turtle import *
                space = Screen()
                carlos = Turtle()

                # repeat 2 times
                for i in [1,2]:
                    carlos.forward(175)
                    carlos.right(90)
                    carlos.forward(150)
                    carlos.right(90)

        .. tab:: Answer

            Define the procedure to draw a rectangle given a turtle, the length, and the width.  Call the procedure to test it.

            .. activecode::  ch10ex15a
                :nocodelens:

                def drawRectangle(turtle,length,width):
                    for i in [1,2]:
                        turtle.forward(length)
                        turtle.right(90)
                        turtle.forward(width)
                        turtle.right(90)

                from turtle import *
                space = Screen()
                carlos = Turtle()
                drawRectangle(carlos,50,100)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex15q

#.

    .. tabbed:: ch10ex16t

        .. tab:: Question

            Complete the code so that the turtle stamps a square pattern 20 times (it should look like a circle enclosing a couple of circles if you use a turn angle of 18)

            .. activecode::  ch10ex16q
                :nocodelens:

                from turtle import *
                from sys import *               # use the system library
                setExecutionLimit(50000)        # let this take up to 50 seconds
                space = Screen()
                zoe = Turtle()

        .. tab:: Answer

            Make sure to use penup before the loop. Inside the loop, there should be another loop, and you should call the stamp method inside both loops.

            .. activecode::  ch10ex16a
                :nocodelens:

                from turtle import *
                from sys import *               # use the system library
                setExecutionLimit(50000)        #let this take up to 50 seconds
                space = Screen()
                zoe = Turtle()
                zoe.setheading(90)
                zoe.penup()

                for repeats in range(20):
                    zoe.stamp()
                    zoe.forward(10)
                    zoe.right(18)
                    for sides in range(4):
                      zoe.stamp()
                      zoe.forward(50)
                      zoe.right(90)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex16q

#.

    .. tabbed:: ch10ex17t

        .. tab:: Question

           Create a procedure to draw 4 turtles at the 4 corners of a square using the ``stamp`` procedure.

           .. activecode::  ch10ex17q
                :nocodelens:

        .. tab:: Answer

            Define the procedure as shown below.

            .. activecode::  ch10ex17a
                :nocodelens:

                def drawStampSquare(turtle,size):
                    turtle.penup()
                    turtle.shape("turtle")
                    for sides in range(4):	# repeat the indented lines 4 times
    	                turtle.forward(size)    # move forward by 100 units
    	                turtle.stamp()
      	                turtle.right(90)        # turn by 90 degrees

      	        from turtle import *
                space = Screen()
                carlos = Turtle()
                drawStampSquare(carlos,50)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex17q

#.

    .. tabbed:: ch10ex18t

        .. tab:: Question

            Create a procedure that takes in a turtle and integer parameter. The procedure should stamp a turtle shape into a circle in 20 steps with the forward number being equal to the parameter.

            .. activecode::  ch10ex18q
                :nocodelens:


        .. tab:: Answer

            In the procedure, have the two parameters. Change the turtle shape to "turtle" and use penup. Then have a loop for range of 20. Inside the loop make the turtle go forward by the int parameter value. Use the stamp method and then the turn right by 18.

            .. activecode::  ch10ex18a
                :nocodelens:

                def circle(turt, num):
                    turt.shape("turtle")
                    turt.penup()
                    for size in range(20):
                        turt.forward(num)
                        turt.stamp()
                        turt.right(18)

                from turtle import *
                space = Screen()
                tess = Turtle()

                circle(turt, 20)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex18q

#.

    .. tabbed:: ch10ex19t

        .. tab:: Question

           Write a procedure that takes a turtle and a number of sides as parameters and draws a polygon with that number of sides.

           .. activecode::  ch10ex19q
               :nocodelens:

        .. tab:: Answer

            Create a procedure as shown below.  Call it to test it.

            .. activecode::  ch10ex19a
                :nocodelens:

                def drawPolygon(turtle,numSides):
                    angle = 360 / numSides
                    for x in range(numSides):
                        turtle.forward(25)
                        turtle.right(angle)

                from turtle import *
                space = Screen()
                carlos = Turtle()
                drawPolygon(carlos,7)
                carlos.forward(100)
                drawPolygon(carlos,9)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex19q

#.

    .. tabbed:: ch10ex20t

        .. tab:: Question

            Write a procedure that takes a turtle, an int for the number of sides for a polygon, and an int for the number of times to draw that polygon. The procedure should draw that polygon that number of times in a circular path.

            .. activecode::  ch10ex20q
                :nocodelens:


        .. tab:: Answer

            .. activecode::  ch10ex20a
                :nocodelens:

                def drawShape(turtle, numSides, numTimes):
                    anglePolygon = 360 / numSides
                    circleShape = 360 / numTimes
                    for x in range(numTimes):
                        turtle.forward(20)
                        turtle.right(circleShape)
                        for y in range(numSides):
                            turtle.forward(30)
                            turtle.right(anglePolygon)

                from turtle import *
                space = Screen()
                t = Turtle()
                drawShape(t, 3, 20)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch10ex20q
