..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".
	



Loops and Patterns with Turtles
=================================

The most famous thing that Seymour invented for kids to do with a computer was *to control a turtle*.  
Not a biological turtle, but a robot turtle that had a pen in it.  The student-programmers would steer the robot around and draw with it.

.. figure:: Figures/mindstorms_turtle.jpg 
    :width: 200px
    :align: center
    :alt: Children playing with a Logo turtle robot
    :figclass: align-center

This is different than most programmed graphics even today.  Most of the time, drawing a line using a programming language requires specifying two points in Cartesian coordinate space.  
You might specify a starting position (like *10,100*, with *0,0* in the upperleft) and an ending position (like *30,100*), and a line is drawn.

.. figure:: Figures/drawLine.png
    :width: 400px
    :align: center
    :alt: Draw a line
    :figclass: align-center


But that's not how Seymour Papert's turtles worked.  They didn't know where they were in the world.  *Real* turtles don't know their *x,y* position on the beach!  They can simply move and turn.  They only know where *they* are in the world.  

Today, we can play with Seymour's turtles in a fully-graphical and non-robotic way.  Try clicking the |runbutton| button below to see the program work: 

.. |runbutton| image:: Figures/run-button.png

.. |audiobutton| image:: Figures/start-audio-tour.png

.. |teachernote| image:: Figures/teachernote.png
    :width: 25px
    :align: top
    :alt: teachernote


.. activecode:: csp_turtle_1
    :tour_1: "Line-by-line Tour"; 1: first-turtle-line-1; 2: first-turtle-line-2; 3: first-turtle-line-3; 4: first-turtle-line-4; 5: first-turtle-line-5; 6: first-turtle-line-6;
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alex = Turtle()   			# create a turtle named alex
    alex.forward(150)        	# tell alex to move forward by 150 units
    alex.left(90)           	# turn by 90 degrees
    alex.forward(75)         	# complete the second leg of a triangle

Underneath the program, next to the **Run** button |runbutton|, you'll see the button to open the audio tour for this program: |audiobutton|.  Try it, and listen to the "Line-by-Line Tour."  You can use the provided buttons to pause, play, jump ahead, or go back.  You can also click on any line to hear the audio explanation for that line.

Teacher Note: Audio explanations
----------------------------------
|teachernote| The icon to the left indicates a teacher note, for more explanation behind the pedagogy, suggestions how to teach something, or insight into student difficulties with a concept.  Why are we using audio here?  Research in educational psychology suggests that text explanation for a text program may lead to cognitive overload.  Learners might understand a program better with an audio explanation, rather than a text explanation, so that you can be looking at the program while you hear the explanation.  In the classroom, your voice explaining a program may be more easier for a student to understand than reading a textbook.

.. mchoicemf:: csp_turtle_equallines
   :answer_a: Change the 150 to 90
   :answer_b: Change the 75 to 90
   :answer_c: Change the 75 to 150
   :correct: c
   :feedback_a: No, 150 is a length and 90 is the degree angle.
   :feedback_b: No, 75 is a length and 90 is the degree angle.
   :feedback_c: Yes, both triangle legs would be 150 units long.

   If you wanted to make both legs of the triangle the same, what change would you make to the program?  (Feel free to actually make the change in the program and press ``Run`` to try it!)

.. parsonsprob:: csp_turtle_L

   The following program uses a turtle to draw a capital L as shown in the picture to the left of this text, <img src="../_static/TurtleL4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order.</p>
   -----
   from turtle import *
   window = Screen()
   ella = Turtle()
   =====
   ella.right(90)
   ella.forward(150)
   =====
   ella.left(90)
   ella.forward(75)


**Slightly Harder Problem:** Now, let's connect the point where the turtle started to the point where the last program ended.  The shape we'll create is an equilateral triangle.  The number 57 isn't guesswork -- it is roughly the square root of 40^2 + 40^2.

.. activecode:: csp_turtle_2
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alex = Turtle()   			# create a turtle named alex
    alex.forward(40)        	# tell alex to move forward by 150 units
    alex.left(90)           	# turn by 90 degrees
    alex.forward(40)         	# complete the second leg of a triangle
    alex.left(0)				# ZERO won't actually work
    alex.forward(57)			# Close the triangle


.. mchoicemf:: csp_turtle_hypot
   :answer_a: alex.left(135)
   :answer_b: alex.left(90)
   :answer_c: alex.left(45)
   :correct: a
   :feedback_a: Exactly!  Feel free to try it.
   :feedback_b: No, that would make another right angle. Getting closer to a square that way.
   :feedback_c: No, because the turtle turns the exterior angle, not the interior angle.

   ``alex.left(0)`` will not turn the turtle toward the starting point.  Which of these does it?
   

Making shapes
-----------------

Just by going forward, backward, left, and right, we can do a lot of interesting computer graphics using turtles.  Let's write a simple program for drawing a square.  Try running this program by clicking |runbutton|.

Here's the simplest version:

.. activecode:: csp_turtle_3
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alice = Turtle()   			# create a turtle named alice
    alice.setheading(90)        # Point due north
    alice.forward(100)        	# tell alice to move forward by 100 units
    alice.right(90)           	# turn by 90 degrees
    alice.forward(100)        	# tell alice to move forward by 100 units
    alice.right(90)           	# turn by 90 degrees
    alice.forward(100)        	# tell alice to move forward by 100 units
    alice.right(90)           	# turn by 90 degrees
    alice.forward(100)        	# tell alice to move forward by 100 units
    alice.right(90)           	# turn by 90 degrees

This program has the turtle *alice* make a square.  She goes forward 100 steps, then turns right, 9 times.


Teacher Note: Body Syntonic
-----------------------------
|teachernote| One of the things that Seymour Papert most liked about the turtle is that students could test their programs using `body syntonic <http://en.wikipedia.org/wiki/Turtle_graphics>`_ reasoning.  This means the turtle moves in the way that the student moves.  Students can go forward and turn right.  Students could *play* turtle, doing exactly what the program was doing.  In this video, our "turtle" person doesn't take 100 steps.  Instead, we go forward 4 steps, figuring that one human step is about 25 turtle steps.

.. video:: body_syntonic_turtle
   :controls:
   :thumb: ../_static/body-syntonic-turtle.png

   http://www.cc.gatech.edu/~mark.guzdial/videos/Body-syntonic-turtle.mov
   http://www.cc.gatech.edu/~mark.guzdial/videos/Body-syntonic-turtle.webm

Making loops
-------------

The program above *works*, but it's hiding the looping.  We tell ``alice`` to go forward and turn right four times, but we don't *explicitly* say "four times."  We can tell the computer to do something explicitly for a certain number of times.  We can use a *loop*.


.. activecode:: csp_turtle_loop3
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alice = Turtle()   			# create a turtle named alice
    alice.setheading(90)        # Point due north
    for sides in [1,2,3,4]:
      alice.forward(100)        	# tell alice to move forward by 100 units
      alice.right(90)           	# turn by 90 degrees

.. mchoicemf:: csp_turtle_sides
   :answer_a: [0,1,2,3]
   :answer_b: [0,1,2]
   :answer_c: [2,3,4,5]
   :answer_d: [1,2,3,4,5]
   :correct: b
   :feedback_a: This still has four sides -- they are just numbered differently.
   :feedback_b: Right -- this has only three sides.
   :feedback_c: This still has four sides -- they are just numbered differently.
   :feedback_d: This *will* generate a square. The turtle will just go on to trace the first side twice.

   The numbers in the list ``[1,2,3,4]`` are unimportant.  It's the fact that there are *four* items in the list that is important.  Only one of these choices does *not* make a square.  Which one?  (It's not cheating to actually try each of them and run the program each time!)
   
Since it doesn't matter what's in the list, just as long as there are *four* items, there is a special way of writing that loop.  We use a ``range`` function. 

.. activecode:: csp_turtle1_for
  :tour_1: "Line-by-line tour"; 1: sqline1; 2: sqline2; 3: sqline3; 4: sqline4; 5: sqline5; 6: sqline6; 7: sqline7; 8: sqline8;
 
  from turtle import *       	# access the turtles library
  screen = Screen()    		# create a turtle screen
  alice = Turtle()   			# create a turtle named alice
  alice.setheading(90)        # Point due north
  # Now make a square
  for sides in range(4):
    alice.forward(100)        	# tell alice to move forward by 100 units
    alice.right(90)           	# turn by 90 degrees


The ``range`` function returns a value so that the *for* loop executes that many times.  This makes the turtle go forward and turn right 90 degrees *four* times.

.. |turtlegeometry| image:: Figures/turtle-geometry.jpg
    :width: 200px
    :align: top
    :alt: teachernote


Teacher Note: Turtle Geometry
-----------------------------
|teachernote| The turtle is actually useful for exploring a wide variety of geometry ideas -- including external and internal angles and computing a hypotenuse, as seen in these examples.  The book `Turtle Geometry <http://www.amazon.com/Turtle-Geometry-Mathematics-Artificial-Intelligence/dp/0262510375>`_ does a wonderful job of showing how turtles can be used to explore a wide variety of geometric, mathematical, and scientific ideas (e.g., using turtles to model insect behavior).  The example *PATTERN* below is drawn from that book. 

A scan of my copy of the book: |turtlegeometry|

Total Turtle Trip Theorem
----------------------------

That last piece of code is actually a **pattern** for a wide variety of geometric shapes.  Here's a triangle.

.. activecode:: csp_turtle_triangle
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alice = Turtle()   			# create a turtle named alice
    alice.setheading(90)        # Point due north
    for sides in range(3):
      alice.forward(100)        	# tell alice to move forward by 100 units
      alice.right(120)           	# turn by 120 degrees

And here's a pentagon.

.. activecode:: csp_turtle_pentagon
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alice = Turtle()   			# create a turtle named alice
    alice.setheading(90)        # Point due north
    for sides in range(5):
      alice.forward(100)        	# tell alice to move forward by 100 units
      alice.right(72)           	# turn by 72 degrees

The **Total Turtle Trip Theorem** states that the turtle will draw a closed figure with *n* sides when the sum of the angles turned is a multiple of 360.  3 * 120 = 360.  5 * 72 = 360.

.. activecode:: csp_turtle_dodecagon
	
    from turtle import *       	# allows us to use the turtles library
    screen = Screen()    		# create a turtle screen
    alice = Turtle()   			# create a turtle named alice
    alice.setheading(90)        # Point due north
    for sides in range(12):
      alice.forward(50)        	# tell alice to move forward by 100 units
      alice.right(??)           	# turn by ?? degrees

.. mchoicemf:: csp_turtle_dodquestion
   :answer_a: 15
   :answer_b: 30
   :answer_c: 12
   :answer_d: 90
   :correct: b
   :feedback_a: This one will not close
   :feedback_b: Exactly! 12 * 30 = 360
   :feedback_c: No, 12 * 12 is 144, which is not a multiple of 360
   :feedback_d: This one will generate a square, three times. 12 * 90 = 1080 = 360 * 3

   How much should ``alice`` turn to create a closed dodecagon (12-sided figure)?  Only one of these works.


Making Patterns of Patterns
-----------------------------

We now know the pattern for creating any polygon now.  We can wrap that pattern in another loop to create `spirograph <http://en.wikipedia.org/wiki/Spirograph>`_ like patterns.  The example below makes pentagons, but we could make others.

.. activecode:: csp_turtle_spiro1
	
    from turtle import *        # allows us to use the turtles library
    screen = Screen()           # create a turtle screen
    alice = Turtle()            # create a turtle named alice
    alice.setheading(90)        # Point due north
    for repeats in range(20):   # How many times to draw the pattern
      alice.forward(10)         # Offset the shapes a bit
      alice.right(18)           # And turn each one a bit
      # This part makes a pentagon
      for sides in range(5):
        alice.forward(50)       # tell alice to move forward by 100 units
        alice.right(72)         # turn by 72 degrees

By setting the pen color differently, we can distinguish the part that draws the shape, from the part that draws *between* the shapes.

.. activecode:: csp_turtle_spiro2
	
    from turtle import *        # allows us to use the turtles library
    screen = Screen()           # create a turtle screen
    alice = Turtle()            # create a turtle named alice
    alice.setheading(90)        # Point due north
    for repeats in range(20):   # 20 times to draw the pattern
      alice.pencolor("green")   # Draw between
      alice.forward(10)         # Offset the shapes a bit
      alice.right(18)           # And turn each one a bit
      alice.pencolor("red")     # Draw the shape
      # This part makes a pentagon
      for sides in range(5):
        alice.forward(50)       # tell alice to move forward by 100 units
        alice.right(72)         # turn by 72 degrees

You can use the coloring to help figure out the correct order of the lines below.

.. parsonsprob:: csp_turtle_parfigure

   There is a way of arranging the statements below such that this image is created. <img src="../_static/TurtleColoredImage.png" width="200" align="left" hspace="10" vspace="5" /> Move the pieces of the program from the left into the space on the right.
   -----
   from turtle import *
   screen = Screen()
   alice = Turtle()
   alice.setheading(90)
   =====
   for repeats in range(20):
   =====
      alice.forward(10)
      alice.left(18)
   =====
      alice.pencolor("red")
   =====
      for sides in range(3):
   =====
         alice.forward(50) 
         alice.right(120)
   =====
         alice.pencolor("blue")


In the next chapter, we'll use programming in the way that Seymour Papert used Logo *before* the turtle: to do language and math play.