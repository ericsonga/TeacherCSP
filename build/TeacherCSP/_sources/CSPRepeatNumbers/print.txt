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
	:prefix: csp-7-6-
	
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teacher Note: Print() is Your Friend
======================================================
The goal of this stage of learning about programming is to develop a mental model of how the program works.  Can students look at a program and *predict* what's going to happen?  Can they figure out the values of the variables?  Feel free to insert lots of ``print()`` function calls.  Have students make a prediction about variable values, then insert ``print()`` calls to display the variable values, and run the program to find out whether the prediction is right.  Run this version to see what gets printed.

.. activecode:: Numbers_Sum_Print
    :tour_1: "Code tour"; 2: accL_line2; 4: accL_line4; 5: accL_line5; 7: accL_line7; 8: accL_line8; 10: accL_line10; 12: accL_line12;
	
    # STEP 1: INITIALIZE ACCUMULATOR 
    sum = 0  # Start out with nothing
    # STEP 2: GET DATA
    numbers = range(0,101,2)
    print("All the numbers:",numbers)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
    	print("Number:",number)
    	# STEP 4: ACCUMULATE
    	sum = sum + number
    # STEP 5: PROCESS RESULT
    print(sum)
    
.. parsonsprob:: 7_6_1_Print-Sum-Evens

   The following is the correct code for printing the value of number and the sum each time through the loop, but it is mixed up. The code should initialize the accumulator, create the list of numbers, and then loop through the list of numbers.  Each time through the loop it should print the value of number, add the value of number to the accumulator, and then print the current sum.  Drag the blocks from the left and put them in the correct order on the right.  Don't forget to indent blocks in the body of the loop.  Just drag the block further right to indent.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0  
   =====
   numbers = range(0,101,2)
   =====
   for number in numbers:
   =====
       print("Number:",number)
   =====
       sum = sum + number
   =====
       print(sum)


