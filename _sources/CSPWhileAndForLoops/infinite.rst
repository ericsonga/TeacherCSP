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

Infinite Loops
================

Getting a computer to repeat a set of statements is simple.  Sometimes it can be tricky to get it to *stop*.  Remember that a while loop will execute as long as the logical expression is true.  What happens if the logical expression is *always* true?

..	index::
	single: infinite loop
	pair: loop; infinite
	
So, here's a program that loops forever. 

.. sourcecode:: python

  	while 1 == 1:
  	    print("Looping")
  	    print("Forever")

Since ``1`` will always be equal to ``1``, the two ``print`` statements will just be repeated over and over and over again and the logical expression will never be false.  We call that an **infinite loop**, which means a loop that continues forever or until it is forced to stop. 

.. note::
   The expression ``1 == 1`` tests if 1 is equal to 1.  Remember that ``x = 3`` sets the value of x to 3, it doesn't test if x is equal to 3.  To do that use ``x == 3``.  

We ran the following code in a form of Python where we could stop the computer easily:

.. sourcecode:: python

 	>>> while 1==1:
 	        print ("Looping")
 	        print ("Forever")
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever
	
(We stopped the computer around this point.)

.. mchoice:: 8_2_1_While_Inf_NumLines
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :correct: b
   :feedback_a: All the statements that are indented 4 spaces to the right of the <code>while</code> are part of the body of the loop.
   :feedback_b: There are two statements that are indented 4 spaces to the right of the <code>while</code> statement, so there are two statements in the body of this loop.
   :feedback_c: There are three lines here total, but not all of them are in the body of the loop.

   How many lines are in the body of the ``while`` loop in shown above?

