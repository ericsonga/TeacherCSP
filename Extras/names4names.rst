..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/teachernote.png
    :width: 25px
    :align: bottom
    :alt: teachernote


Ability #2: A computer can name anything
===========================================

A "value" for a computer can be anything.  It doesn't have to just be a number
or a word.  It can be steps, instructions, and even other names.  This ability to 
name other things is key to Alan Turing's vision of a computer.  A computer is 
a device than be any other computer.  We can use names to make one computer
look like, act like, and be programmed like any other kind of computer.

Naming procedures
-------------------

We've already seen how we can use names to represent numbers (both integers and with decimal points), strings (characters), turtles, and images.  What's particularly amazing is that names can also represent sequences of statements, steps of a procedure.

First, there are already named procedures built in to Python.  The function `abs` returns the absolute value of its input.  The function `int` takes a number with a decimal part as input and returns just the integer part.

.. activecode:: csp_internal_functions

  print("Absolute value of -5:")
  print(abs(-5))
  print("Integer part of 34.2")
  print(int(34.2))

The functions `abs` and `int` are *names*.  They are *variables* whose values are a set of statements that achieve a goal.  Later on, we'll know enough code to write `abs` and `int` ourselves.  The important point right now is that `abs` and `int` are *names* that have procedures for *values*.  That means we can create new names for those names.

.. activecode:: csp_renamed_internal

  absolute = abs
  print("Absolute value of -5:")
  print(absolute(-5))
  nodecimal = int
  print("Integer part of of 34.2")
  print(nodecimal(34.2))

.. mchoicemf:: csp_renamed_internal
   :answer_a: -16
   :answer_b: -16.789
   :answer_c: 16.789
   :answer_d: 16
   :correct: d
   :feedback_a: No, absolute will change the negative
   :feedback_b: No, the original number will change
   :feedback_c: No, nodecimal will remove the decimal part
   :feedback_d: Yes! Absolute will make it positive, and nodecimal will cut it down to 16.
   
   If you add one more line to the above program, `print(nodecimal(absolute(-16.789)))`, what prints?

Naming sets of steps
---------------------

How did `abs` and `int` get defined?  By *defining* new functions, we can associate a name with a set of steps.

.. activecode:: firstfunc

  def square(turtle):
    for steps in range(4):
       turtle.forward(100)
       turtle.right(90)

Run that program.  Congratulations!  You have successfully defined the function `square` which takes a turtle as input and draws a square with that turtle.  Oh?  Did you want to *make* a square?  Then you need to *call* the function.

..	index::
	single: def
	single: functions
	single: calling functions

.. activecode:: csp_firstfunc_call


  def square(turtle):
    for steps in range(4):
       turtle.forward(100)
       turtle.right(90)

  from turtle import *       	# allows us to use the turtles library
  screen = Screen()    		# create a turtle screen
  bernie = Turtle()   		# create a turtle named bernie
  square(bernie)

In this program, we *DEFine* the word `square` to represent the steps of Python statements that create a square with a turtle.  The `square` function takes as input a `turtle` that will be used to make the square.  Notice how we call `square(bernie)`.  We say that `bernie` is an *input*. Sometimes we say it's an *argument*.  You can imagine when you call `square(bernie)` that there's a hidden assignment statement: `turtle = bernie`.  The variable `turtle` now represents the input turtle `bernie`.  We say that the word `turtle` is an *alias* for the input `bernie`. Sometimes we say it's a *parameter*.

..	index::
	pair: function; inputs
	pair: function; arguments
	pair: function; parameters

We can pass other parameters to the function, too.  Like, let's make the `square` function take the size of the square as an input.

.. activecode:: csp_firstfunc_call


  def square(turtle,size):
    for steps in range(4):
       turtle.forward(size)
       turtle.right(90)

  from turtle import *       	# allows us to use the turtles library
  screen = Screen()    		# create a turtle screen
  bernie = Turtle()   		# create a turtle named bernie
  square(bernie, 100)
  square(bernie, 75)
  square(bernie, 50)
  square(bernie, 25)

Teachers Note: Naming functions, arguments, and parameters
------------------------------------------------------------

|teachernote| You probably don't quite feel comfortable with naming functions, arguments, and parameters right now.  That's okay.  Our research on how students learn programming says that having *names* represent *something else* takes alot of practice.  Right now, your students will probably prefer:

|  from turtle import *       	# allows us to use the turtles library
|  screen = Screen()    		# create a turtle screen
|  bernie = Turtle()   		# create a turtle named bernie
|  for steps in range(4):
|       bernie.forward(100)
|       bernie.right(90)

To the function definition:

|  def square(turtle,size):
|    for steps in range(4):
|       turtle.forward(size)
|       turtle.right(90)

and then calling it like this:

|  from turtle import *       	# allows us to use the turtles library
|  screen = Screen()    		# create a turtle screen
|  bernie = Turtle()   		# create a turtle named bernie
|  square(bernie, 100)

When students are first coming to understand programming, they want to see constants like 100.  They don't want to use names like `size`.  They can probably recognize that that one `square` function can make squares of all kinds of sizes, so it is flexible and thus powerful.  But they are probably still trying to understand the baisc turtle commands yet.  

Don't test them on naming functions, arguments, and parameters yet.  That will come later in the **Abstraction** chapter.  Right now, it's okay to just have your students read and use the names as they are.  As they become more familiar with the statements, they will be ready to abstract out to using names to represent things.

Naming sets of procedures
---------------------------

Let's step out one more level of naming.  We've seen names for values, like strings and numbers.  We've seen names for functions.  We've now seen how to *define* functions, using other names to store the inputs to those functions.

Sometimes, you will want to have have a whole group of functions, and you will want to store them somewhere and *name* that *whole set of functions*.  In fact, you can.  And in fact, you have already used those.

.. index::
	single: import, from import

That is what you are doing when you execute a statement like `from turtle import *`.  That is where the functions like `forward` and `right` and `Screen` are defined.  We can mix functions that *we* define with functions that we *import*.

.. activecode:: csp_squares_patterns

  def square(turtle,size):
    for steps in range(4):
       turtle.forward(size)
       turtle.right(90)

  from turtle import *        # allows us to use the turtles library
  screen = Screen()           # create a turtle screen
  alice = Turtle()            # create a turtle named alice
  alice.setheading(90)        # Point due north
  for repeats in range(20):   # How many times to draw the pattern
    alice.forward(10)         # Offset the shapes a bit
    alice.right(18)           # And turn each one a bit
    square(alice,repeats+5)

.. mchoicemf:: csp_function_names
   :answer_a: square
   :answer_b: range
   :answer_c: forward
   :answer_d: right
   :answer_e: All of the above
   :correct: 3
   :feedback_a: Yes, but more
   :feedback_b: Yes, but more
   :feedback_c: Yes, but more
   :feedback_d: Yes, but more
   :feedback_e: Yes, all of the turtle stuff from the import, plus the square we defined
   
   Imagine that you add one more line to the above program.  Which function can you use safely, because it will be defined?

Similarly, when we did the image processing, we did `from processing import *`.  That made the functions like `loadImage` and `red` be accessible.  We could define functions that might make a new color, or do a more complex transformation of images.  If you recall our image processing code (like below), we called the function `run()` at the bottom.  That function calls `setup()` and `draw()` which *we* defined.  Thus, we can write functions that pre-defined functions can call.

.. activecode:: csp_images_decreasered2

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():  # run calls this
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():  # run calls this
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r*0.5,b,g)
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)

 run()  # Pre-defined in processing


This ability to name functions, and sets of functions, and absolutely anything and any set of things in a computer is insanely powerful.  It allows us to create **Abstraction** that makes the computer easier to program and use.  More on that in a future chapter.
