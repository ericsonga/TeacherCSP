..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-14-3-
  
Detecting Odd and Even
=======================
   
..	index::
   	single: remainder
   	single: modulo
   	single: odd
   	single: even

   	
One common thing to do with conditionals is to check if a number is odd or even.  If a number is evenly divisible by 2 with no remainder, then it is even.  You can calculate the remainder with the **modulo** operator ``%`` like this ``num % 2 == 0``.  If a number divided by 2 leaves a remainder of 1, then the number is odd.  You can check for this using ``num % 2 == 1``.  The code below uses two ``if`` statements to check if the current value of ``y`` is even or odd.  It uses this to draw two alternating color stripes.

The code below uses the ``window_width()`` function of the ``Screen`` object that returns the width of the Screen (drawing area). There is also a ``window_height()`` function that returns the height of the Screen (drawing area).
   
.. activecode:: td_stripes
    :tour_1: "Structural Tour"; 1-4: td2a-line1-4; 6-7: td2a-line6-7; 9-10: td2a-line9-10; 12: td2a-line12; 13: td2a-line13; 14-15: td2a-line14-15; 16-17: td2a-line16-17; 18: td2a-line18; 19: td2a-line19; 20: td2a-line20;
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
       	
This code calculates ``maxX`` as half the width of the drawing space.  This is used to determine the x value for the left side of the window.  The left side is at ``-1 * maxX`` since the window uses the cartesian coordinate system with (0,0) as the center of the window.  

For more information on what this code is doing listen to the audio tour.
       
.. mchoice:: 14_3_1_finish_stripes
   :answer_a: 10
   :answer_b: 16
   :answer_c: 17
   :answer_d: 32
   :correct: c
   :feedback_a: This will stop before filling the top half of the space. Try it.
   :feedback_b: The turtle starts at the middle of height and draws 5 pixels below it and 5 pixels above it, so this leaves 5 pixels at the top that need to be filled.
   :feedback_c: The height of the top half is 160 and each stripe is a height of 10 so 16 nearly does it, but 17 fills the entire area.  The turtle starts in the middle of the space so the first row has 5 pixels above the middle and 5 below.
   :feedback_d: This would fill more than the top half.

   What value should you use as the parameter for the range function in line 12 to fill the top half of the drawing space with stripes?  The height of the space is 320.  
       
Try to change the code above to use an ``else`` instead of the second ``if`` and yet still have the same result.  
Try to change the code above to use both an ``elif`` and ``else`` to draw three different colored stripes in a repeated pattern.  You can use ``y % 3`` for three different conditions.  

**Mixed up programs**

.. parsonsprob:: 14_3_2_vert_stripes

   The following program should draw vertical color stipes alternating between red and black, but the code is mixed up.  Drag the block from left to right and place them in the correct order with the correct indention.
   -----
   from turtle import *     
   space = Screen()        
   height = space.window_height()
   =====
   maxY = height / 2         
   sue = Turtle()              
   sue.pensize(10) 
   sue.left(90)       
   =====
   for index in range(5):      
   =====
       sue.penup() 
   =====           
       if index % 2 == 0:     
   ===== 
           sue.color('red')        
   =====
       else:                     
   ===== 
           sue.color('black')      
   =====
       sue.goto(index * 10, -1 * maxY)
       sue.pendown()             
       sue.forward(height)  
      
    
