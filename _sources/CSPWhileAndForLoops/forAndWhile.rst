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
	:prefix: csp-8-1-
	
.. highlight:: java
   :linenothreshold: 4
   
	
Loops - For and While
=======================

*Learning Objectives:*

- Introduce the concept of a *logical expression*, which is either true or false.
- Introduce the concept of a ``while`` loop, which will repeat the body of a loop while a logical expression is true.
- Introduce the concept of an *infinite loop*, which is a loop that never ends.
- Compare and contrast ``while`` and ``for`` loops

..	index:
	single: while
	single: body of a loop
	single: logical expression
	single: definite loop
	pair: statements; while
	pair: statements; for
	pair: loop: while
	pair: loop: for
	pair: loop: definite
	
Example For Loop
-----------------

We have been using a ``for`` loop to repeat the **body of a loop** a known number of times.  This is also know as a **definite loop**.  The **body of a loop** is all the statements that follow the ``for`` statement and are indented to the right of it.  Be sure to indent 4 spaces to indicate which statements are part of the body of the loop.

Before you run the code below try to predict the last value it will print and then answer the question below.

.. mchoicemf:: 8_1_1_For_Counter_Q1
		  :answer_a: 9
		  :answer_b: 10
		  :answer_c: 11
		  :correct: a
		  :feedback_a: A range goes from a starting point to one *less* than the ending point. If we want to count to 10, use range(1,11).
		  :feedback_b: Try it -- nope, never gets to 10.
		  :feedback_c: In fact, it doesn't even get to 10! Try it.

	   	  What is the last value that will be printed when the code below executes?
	   	  
If we want to print out a count that is increasing by 1, we can do easily do that with a ``for`` loop.  Run the code to see what prints.

.. activecode:: for_counter 

	for counter in range(1,10):
	    print(counter)

	   	  
Introducing the While Loop
----------------------------

Another way to repeat statements is the ``while`` loop.  It will repeat the **body of loop** as long as a **logical expression** is true.  The **body of the loop** is the statement or statements that are indented 4 or more spaces to the right of the ``while`` statement.   A **logical expression** is one that is either true or false like ``x > 3``.  

``While`` loops are typically used when you don't know how many times to execute the loop.  For example, when you play a game you will repeat the game while there isn't a winner.  If you ever played musical chairs you walked around the circle of chairs while the music was playing.

The code below will loop as long as the number that you enter isn't negative.  It will add each non negative number to the current sum.  It will print out the average of all of the numbers you have entered.

.. activecode:: while_input
	
    sum = 0
    count = 0
    value = input("Type in a value or a negative number to stop")
    while int(value) > 0:
        sum = sum + value
        count = count + 1

    print("The average is " + str(sum / count))
    
.. mchoicemf:: 8_1_2_While_Input1
		  :answer_a: 1
		  :answer_b: 2
		  :answer_c: 3
		  :correct: b
		  :feedback_a: A loop can have just one statement in the body of the loop, but this one has more than one.
		  :feedback_b: There are two statements indented 4 spaces to the right of the <code>while</code> statement, so there are two statements in the body of this loop.
		  :feedback_c: Is the <code>print(message)</code> line indented 4 spaces to the right of the <code>while</code>? If not it is not part of the body of the loop.

	   	  How many lines are in the body of this ``while`` loop?
    

