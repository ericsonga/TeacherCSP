..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-10-5-


Chapter 10 - Summary
============================

Chapter 10 included the following concepts from computing.

..	index::
    single: for loop
    single: loop body
	single: range
	single: stamp
	single: total turtle trip theorem
	single: turtle geometry

- **Loop Body** - The statement or statements that are repeated in a loop.  In Python indention is used to show the statements that are part of the body of a loop.
- **Total Turtle Trip Theorem** - The total turtle trip theorem states that the turtle will draw a closed figure with n sides when the sum of the angles turned is a multiple of 360. 
- **Turtle Geometry** - Turtle Geometry is a book by Hal Abelson and Andrea diSessa that explores math using turtles.   

Summary of Python Keywords and Functions
-------------------------------------------- 

- **def** - The ``def`` keyword is used to define a procedure or function in Python.  The line must also end with a ``:`` and the body of the procedure or function must be indented 4 spaces.
- **for** - A ``for`` loop is a programming statement that tells the computer to repeat a statement or a set of statements. It is one type of loop. 
- **print** - The ``print`` statement in Python will print the value of the items passed to it.  
- **range** - The ``range`` function in Python returns a list of consecutive values.  If the range function is passed one value it returns a list with the numbers from 0 up to and not including the passed number.  For example, ``range(5)`` returns a list of ``[0,1,2,3,4]``.  If the range function is passed two numbers separated by a comma it returns a list including the first number and then up to but not including the second number.  For example, ``range(1,4)`` returns the list ``[1, 2, 3]``.  If it is passed three values ``range(start,end,step)`` it returns all the numbers from start to one less than end changing by step.  For example, ``range(0,10,2)`` returns ``[0,2,4,6,8]``.
- **while** - A ``while`` loop is a programming statement that tells the computer to repeat a statement or a set of statements. It repeats the **body of the loop** while a **logical expression** is true.


Summary of Turtle Functions and Procedures
--------------------------------------------

The table below shows the turtle functions and procedures that we have covered so far.

==========  ==========  =========================
Name        Input       Description
==========  ==========  =========================
backward    amount        Moves the turle backward by the specified amount
color       colorname     Sets the color for drawing.  Use 'red', 'black', etc
forward     amount        Moves the turtle forward by the specified amount	  
goto        x,y           Moves the turtle to position x,y
left        angle         Turns the turtle counter clockwise by the specified angle
pendown     None          Puts down the turtles tail so that it draws when it moves
penup       None          Picks up the turtles tail so that it doesn't draw when it moves
pensize     width         Sets the width of the pen for drawing
right       angle         Turns the turtle clockwise by the specified angle
setheading  angle         Turns the turtle to face the given heading.  East is 0, north is 90, west is 180, and south is 270. 
shape       shape name 	  Takes a shape name as a string to use for the turtle.  The allowed values are "arrow", "turtle", "circle", "square", "triangle", and "classic".  
stamp       None		  Leaves a copy of the turtle shape at the current location
Turtle      None          Creates and returns a new turtle object
==========  ==========  =========================

.. note::  

   This is the end of chapter 10.   We would love it if you could give us some feedback on this chapter at https://www.surveymonkey.com/r/ch10-teacher-fb.  You might want to open this link in a new tab to make it easier for you to return to your place in this ebook.