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
    
Counting with a For Loop
==========================

.. index::
	pair: statements; for
	single: definite loop

We often want to repeat code a known number of times.  This is also know as a **definite loop** (a loop that repeats a known number of times).  We typically use a ``for`` loop for this as we have seen in previous chapters.  The ``for`` loop has a counter variable that takes on the values in a ``range`` one at a time from left to right each time the loop repeats.  

A ``for`` loop is much simpler and much easier to use than a ``while`` loop for looping a known number of times.  Here is the counter program rewritten using a ``for`` loop.

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
	   	  
Nested For Loops
------------------

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
