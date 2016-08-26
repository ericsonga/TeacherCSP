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

            Fix the errors so it runs and returns the perimeter of a rectangle.

            .. activecode::  ch6ex2q
                :nocodelens:

                def recPerimeter(length, width)
                perimeter = 2 * (length + width)
                Return recPerimeter

                print(recPerimeter(2,4))

        .. tab:: Answer

            Indentation needs to be fixed and there needs to be a colon after the function name.  ``return`` should be lowercase and you should return the variable in the function not the function name.

            .. activecode::  ch6ex2a
                :nocodelens:

                def recPerimeter(length, width):
                	perimeter = 2 * (length + width)
                	return perimeter

                print(recPerimeter(2,4))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex2q

#.

    .. tabbed:: ch6ex3t

        .. tab:: Question

           There are 2 syntax errors in the following code.  Fix the errors so that it runs.

           .. activecode::  ch6ex3q
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

            .. activecode::  ch6ex3a
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
                :identifier: teachercsp_ch6ex3q

#.

    .. tabbed:: ch6ex4t

        .. tab:: Question

            Fix the errors so the code runs and returns the area of a square.

            .. activecode::  ch6ex4q
                :nocodelens:

                x = squareArea(5)

                Def squareArea(sideLength):
                	area = length * length
                	return area
                print(x)

        .. tab:: Answer

            ''def'' should be lowercase. The call to the function should occur after the function is defined.

            .. activecode::  ch6ex4a
                :nocodelens:

                def squareArea(sideLength):
                	area = sideLength * sideLength
                	return area

                x = squareArea(5)
                print(x)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex4q

#.

    .. tabbed:: ch6ex5t

        .. tab:: Question

           The following code has 4 syntax errors.  Fix the errors so that the code runs.

           .. activecode::  ch6ex5q
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

            .. activecode::  ch6ex5a
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
                :identifier: teachercsp_ch6ex5q

#.

    .. tabbed:: ch6ex6t

        .. tab:: Question

            Change the code to take 3 parameters, a turtle, a size that tells it how far to go, and an angle it tells the turtle to turn.

            .. activecode::  ch6ex6q
                :nocodelens:

                def move(turtle):
                    turtle.forward(100)
                    turtle.right(90)
                    turtle.forward(100)
                    turtle.right(90)
                    turtle.forward(100)
                    turtle.right(90)
                    turtle.forward(100)
                    turtle.right(90)

                from turtle import *
                space = Screen()
                t = Turtle()
                move(t, 100, 90)

        .. tab:: Answer

            Add both the ``distance`` and ``angle`` parameters to the function definition.

            .. activecode::  ch6ex6a
                :nocodelens:

                def move(turtle, distance, angle):
                    turtle.forward(distance)
                    turtle.right(angle)
                    turtle.forward(distance)
                    turtle.right(angle)
                    turtle.forward(distance)
                    turtle.right(angle)
                    turtle.forward(distance)
                    turtle.right(angle)

                from turtle import *
                space = Screen()
                t = Turtle()
                move(t, 100, 90)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex6q

#.

    .. tabbed:: ch6ex7t

        .. tab:: Question

           The following code has three lines that need to be changed.  Fix the code to run correctly.

           .. activecode::  ch6ex7q
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

            .. activecode::  ch6ex7a
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
                :identifier: teachercsp_ch6ex7q

#.

    .. tabbed:: ch6ex8t

        .. tab:: Question
        
            Fix the errors so it prints ``"My name is John and I am 18 years old"``.

            .. activecode::  ch6ex8q
                :nocodelens:

                def nameAndAge(nameString, ageInt):
                	print(My name is "nameString" and I am + "str(ageInt)" + years old)

                print(nameAndAge(18, "John"))

        .. tab:: Answer

            It's a function so you need to return not print. Also, fix the errors in returning the values. Then in the call to the function, make sure the string is the first argument and the age the second.

            .. activecode::  ch6ex8a
                :nocodelens:

                def nameAndAge(nameString, ageInt):
	                return("My name is " + nameString + " and I am  " + str(ageInt) + "  years old")

                print(nameAndAge("John", 18))
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex8q

#.

    .. tabbed:: ch6ex9t

        .. tab:: Question

           Change the square procedure below to take a size parameter and have the turtle go forward by the specified size each time.

           .. activecode::  ch6ex9q
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

            .. activecode::  ch6ex9a
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
                :identifier: teachercsp_ch6ex9q

#.

    .. tabbed:: ch6ex10t

        .. tab:: Question

            Change the code so the function takes parameters for the length and base and then call the function and print the result.

            .. activecode::  ch6ex10q
                :nocodelens:

                def areaTriangle():
                   length = 5
                   base = 4
                   return (5 * 4) / 2

        .. tab:: Answer

            Add the parameters for ``length`` and ``base`` and call the function inside the print statement.

            .. activecode::  ch6ex10a
                :nocodelens:

                def areaTriangle(length, base):
                	return (length * base) / 2

                print(areaTriangle(5,4))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex10q

#.

    .. tabbed:: ch6ex11t

        .. tab:: Question

           Change the code below to create a function that calculates the cost of a trip.  It should take the ``miles``, ``milesPerGallon``, and ``pricePerGallon`` as parameters and should return the cost of the trip.

           .. activecode::  ch6ex11q
                :nocodelens:

                miles = 500
                milesPerGallon = 26
                numGallons = miles / milesPerGallon
                pricePerGallon = 3.45
                total = numGallons * pricePerGallon
                print(total)

        .. tab:: Answer

            Add a function definition that takes as parameters ``miles``, ``milesPerGallon``, and ``pricePerGallon``.  Don't forget to call the function to test it.

            .. activecode::  ch6ex11a
                :nocodelens:

                def costOfTrip(miles, milesPerGallon, pricePerGallon):
                    numGallons = miles / milesPerGallon
                    total = numGallons * pricePerGallon
                    return(total)

                print("The cost of the trip is " + str(costOfTrip(500,26,3.45)))


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex11q

#.

    .. tabbed:: ch6ex12t

        .. tab:: Question

            Fix the errors in the procedure and call it.

            .. activecode::  ch6ex12q
                :nocodelens:

                from turtle import *
                space = Screen()
                t = Turtle()
                t2 = Turtle()
                turtleDrawing(t, t2, 100, 45)

                turtleDrawing def(turtle, turtle2, distance, angle)
                	turtle.left(angle)
                	turtle2.right(angle)
                	turtle.forward(turtle2)
                	turtle2.forward(turtle)
                	return distance

        .. tab:: Answer

            The procedure has to be defined before you can call it. Also, in the procedure, make sure the turtle methods are using the ``distance`` and ``angle`` parameters.

            .. activecode::  ch6ex12a
                :nocodelens:

                def turtleDrawing(turtle, turtle2, distance, angle):
                	turtle.left(angle)
                	turtle2.right(angle)
                	turtle.forward(distance)
                	turtle2.forward(distance)

                from turtle import *
                space = Screen()
                t = Turtle()
                t2 = Turtle()
                turtleDrawing(t, t2, 100, 45)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex12q

#.

    .. tabbed:: ch6ex13t

        .. tab:: Question

           Change the code below to create a function to return the number of miles you can drive.  It will take as input (parameters) the ``tankCapacity``, ``theAmountLeft``, and the ``milesPerGallon``.

           .. activecode::  ch6ex13q
                :nocodelens:

                tankCapacity = 10
                amountLeft = 0.25
                numGallons = tankCapacity * amountLeft
                milesPerGallon = 32
                numMiles = numGallons * milesPerGallon
                print(numMiles)

        .. tab:: Answer

            Add a function definition that takes as parameters ``tankCapacity``,``amountLeft``, and ``milesPerGallon``.  Be sure to call the function to test it.

            .. activecode::  ch6ex13a
                :nocodelens:

                def calcNumMiles(tankCapacity,amountLeft, milesPerGallon):
                    numGallons = tankCapacity * amountLeft
                    numMiles = numGallons * milesPerGallon
                    return(numMiles)

                print("The number of miles you can go is " + str(calcNumMiles(10,0.25,32)))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex13q

#.

    .. tabbed:: ch6ex14t

        .. tab:: Question

            Complete and change the code to be a function with 2 parameters that returns the time taken to travel and call the function

            .. activecode::  ch6ex14q
                :nocodelens:

                speed = 5
                distance = 25
                timeTakenToTravel =
                print(timeTakenToTravel)

        .. tab:: Answer

            Take ``speed`` and ``distance`` as parameters and return ``distance / speed``. When calling the function, make sure the arguments are in the right order.

            .. activecode::  ch6ex14a
                :nocodelens:

                def timeTaken(speed, distance):
                	return distance / speed

                print(timeTaken(5,25))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex14q

#.

    .. tabbed:: ch6ex15t

        .. tab:: Question

           Create a procedure to draw a rectangle and call it.  Be sure to take the ``width`` and ``height`` of the rectangle as input to the procedure.

           .. activecode::  ch6ex15q
                :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch6ex15a
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
                :identifier: teachercsp_ch6ex15q

#.

    .. tabbed:: ch6ex16t

        .. tab:: Question

            Create a procedure that takes 2 parameters, a string that you get from a user input and an int. Make the procedure print the string the number of times the int parameter gives and call the procedure.

            .. activecode::  ch6ex16q
                :nocodelens:


        .. tab:: Answer

            Procedure means you want to print not return. Have a string and an int parameter and print the product of the two. When calling the procedure, first get the user input and then pass that input as an argument.

            .. activecode::  ch6ex16a
                :nocodelens:

                def userProcedure(aString, bInt):
                	print(aString * bInt)

                userInput = input("give me a string")
                userProcedure(userInput, 7)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex16q

#.

    .. tabbed:: ch6ex17t

        .. tab:: Question

           Create a procedure to draw a triangle and call it.  Be sure to take the length of each side of the triangle as input to the procedure.

           .. activecode::  ch6ex17q
                :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch6ex17a
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
                :identifier: teachercsp_ch6ex17q

#.

    .. tabbed:: ch6ex18t

        .. tab:: Question

            Create a procedure that takes 7 paramters (turtle, distance, angle, and 4 color strings) and call the procedure to draw a square in 4 different colors.

            .. activecode::  ch6ex18q
                :nocodelens:


        .. tab:: Answer

            Take a parameter for the turtle, distance, and the 4 colors. When you call the procedure make sure the arguments are in the right order.

            .. activecode::  ch6ex18a
                :nocodelens:

                def coloredSquare(turtle, distance, angle, color1, color2, color3, color4):
                	turtle.color(color1)
                	turtle.forward(distance)
                	turtle.left(angle)
                	turtle.color(color2)
                	turtle.forward(distance)
                	turtle.left(angle)
                	turtle.color(color3)
                	turtle.forward(distance)
                	turtle.left(angle)
                	turtle.color(color4)
                	turtle.forward(distance)

                from turtle import *
                space = Screen()
                t = Turtle()
                coloredSquare(t, 100, 90, "blue", "red", "green", "yellow")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex18q

#.

    .. tabbed:: ch6ex19t

        .. tab:: Question

           Write the code below to create a procedure that prints a mad lib.  You can ask the user for input and then pass that input into the procedure.

           .. activecode::  ch6ex19q
               :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch6ex19a
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
                :identifier: teachercsp_ch6ex19q

#.

    .. tabbed:: ch6ex20t

        .. tab:: Question

            Write a function that takes the current hour, current minute, an int to be added to the current hour, and an int to be added to the current minute, and return a string with the new hour and minute (standard 12 hour time; if minutes exceed 60, it should go to the hour) and call the function.

            .. activecode::  ch6ex20q
                :nocodelens:


        .. tab:: Answer

            Make sure the function takes in the 4 parameters. Use the mod function to make sure minutes and hours don't exceed 60 and 12, respectively. The total minutes minus the remaining minutes (from the mod function) gives the number of hours made from the extra minutes.

            .. activecode::  ch6ex20a
                :nocodelens:

                def newTime(currentHour, currentMinute, intHour, intMinute):
                	minutes = currentMinute + intMinute
                	remainingMinutes = minutes % 60
                	hoursFromMinutes = minutes - remainingMinutes
                	newHour = (currentHour + intHour + hoursFromMinutes) % 12
                	return (str(newHour) + " hour(s) and " + str(remainingMinutes) + " minute(s)")

                print(newTime(1, 30, 5, 50))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch6ex20q
