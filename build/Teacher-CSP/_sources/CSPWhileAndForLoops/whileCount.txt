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
	:prefix: csp-8-2-
	
.. highlight:: java
   :linenothreshold: 4

Loops that Count
================

It's much easier to have the computer repeat something for a specific number of times.  For example, we could have a computer count from 1 to 10 pretty easily.  We will use a ``counter`` variable that we will **increment** inside the loop.  **Increment** means increase the value by one.

.. codelens:: While_Counter
   :showoutput: 

   counter = 1
   while counter <= 10:
       print(counter)
       counter = counter + 1

.. mchoicemf:: 8_2_1_While_Counter_Q1
		  :answer_a: It increments the variable counter. 
		  :answer_b: Since counter is in the test for the while loop, it has to change or it would be an infinite loop. 
		  :correct: b
		  :feedback_a: Why is it in the loop?
		  :feedback_b: It must change inside the loop for the loop to stop

	   	  Why is it important to have ``counter = counter + 1`` inside the loop?


.. mchoicemf:: 8_2_2_While_Counter_Q2
	  :answer_a: 1
	  :answer_b: 10
	  :answer_c: 11
	  :correct: c
	  :feedback_a: Counter gets incremented from 1.
	  :feedback_b: The last value to be printed is 10.
	  :feedback_c: Counter gets incremented to 11 after printing, and then the while loop tests counter, finds counter > 10 and stops.

   	  When this program is done, what is the value of counter?
   	
.. parsonsprob:: 8_2_3_While_Countdown

   The following is the correct code for printing a countdown from 10 to 0, but it is mixed up. Drag the blocks from the left and put them in the correct order on the right.  Don't forget to indent blocks in the body of the loop.  Just drag the block to the further right to indent.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   counter = 10
   while counter >= 0:
       print(counter)
       counter = counter - 1 

.. index::
	pair: statements; for
	single: definite loop
	
.. parsonsprob:: 8_2_4_While_Count_Even

   The following is the correct code for printing the even numbers from 0 to 10, but also some extra code that you won't need. Drag the needed blocks from the left and put them in the correct order on the right.  Don't forget to indent blocks in the body of the loop.  Just drag the block to the further right to indent.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   counter = 0
   =====
   while counter <= 10:
   =====
       print(counter)
   =====
       counter = counter + 2
   =====
       counter = counter + 1 #distractor
    

.. index::
	pair: statements; for
	single: definite loop

Because we count in a loop so often, there is a special loop just for *definite loops* (loops that repeat a known number of times).  That's a ``for`` loop which we saw last chapter.  The ``for`` loop has a counter variable that takes on values within a ``range``.  A ``for`` loop is much simpler and much easier to use than a ``while`` loop for looping a known number of times.  Here is the counter program rewritten using a ``for`` loop.

.. codelens:: For_Counter
	:showoutput: 

	for counter in range(1,10):
	    print(counter)

Before tracing the above to the end, see if you figure out this question:

.. mchoicemf:: 8_2_5_For_Counter_Q1
		  :answer_a: 9
		  :answer_b: 10
		  :answer_c: 11
		  :correct: a
		  :feedback_a: A range goes from a starting point to one *less* than the ending point. If we want to count to 10, range(1,11).
		  :feedback_b: Try it -- nope, never gets to 10.
		  :feedback_c: In fact, it doesn't even get to 10! Try it.

	   	  What is the last value to be printed here?

The body of any loop, can even include...another loop!  Here is a super-simple program that generates all the times tables from 0 to 10.  The ``str()`` function changes a numeric value into a string.

.. codelens:: Times_Table
	:showoutput: 

	for x in range(0,11):
	    for y in range(0,11):
	        print(str(x) + " * " + str(y) + " = " + str(x*y))
		

Here are two different ways to look at this program.  In the first one, we look at the *structure* of the program -- what you can understand by just *looking* at the program.

.. video:: timesTableStructure
		   :controls:
		   :thumb: ../_static/timesTableStructure.png

		   http://ice-web.cc.gatech.edu/ce21/1/static/video/nestedLoopStructure.mov
		   http://ice-web.cc.gatech.edu/ce21/1/static/video/nestedLoopStructure.webm


In this video, we look at the *execution* of the program -- how it actually works when it's being *run* by the computer.

.. video:: timesTableTrace
		   :controls:
		   :thumb: ../_static/timesTableTrace.png

		   http://ice-web.cc.gatech.edu/ce21/1/static/video/nestedLoopTrace.mov
		   http://ice-web.cc.gatech.edu/ce21/1/static/video/nestedLoopTrace.webm
