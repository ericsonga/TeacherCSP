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
	:prefix: csp-7-2-
	
.. highlight:: java
   :linenothreshold: 4

Repeating with Numbers
=======================

..	index::
	single: list

..	index::
	single: for loop
	pair: loop; for
	pair: loop; body
	pair: loop; indention
	
We are going to use a ``for`` loop.  A ``for`` loop is one type of loop or way to repeat a statement or set of statements in a program.  A ``for`` loop will use a variable and make the variable take on each of the values in a **list** of numbers one at a time.  A **list** holds values in an order.  

Notice that line 3 in the program below ends with a ``:`` and that line 4 is **indented** four spaces so that it starts under the ``n`` in ``number``.  **Indented** means that text on the line has spaces at the beginning of the line so that the text doesn't start right at the left boundary. Both the ``:`` and the indention are required in a loop.  Line 3 is the start of the ``for`` loop and line 4 is the **body** of the loop.  The **body** of the loop is repeated for each value in the list ``thingsToAdd``.   

What is the sum of all the numbers between 1 and 10?  Run the program below to calculate the answer.

.. activecode:: Numbers_Repeat1
    :tour_1: "Line by line tour"; 1: for1_line1; 2: for1_line2; 3: for1_line3; 4: for1_line4; 5: for1_line5;
    :tour_2: "High level tour"; 1-2: for1_line1-2; 3-4: for1_line3-4; 5: for1_s_line5;
	
    sum = 0  # Start out with nothing
    thingsToAdd = [1,2,3,4,5,6,7,8,9,10]
    for number in thingsToAdd:
    	sum = sum + number
    print(sum)
    
.. mchoice:: 7_2_1_Numbers_Repeat1_Q1
   :answer_a: It prints the same thing it did before.
   :answer_b: It prints the value of sum 10 times and sum is different each time it is printed.
   :answer_c: It prints the same sum 10 times.
   :answer_d: You get an error.
   :correct: b
   :feedback_a: Did you actually try it?
   :feedback_b: Both lines 4 and 5 are now in the body of the loop and are executed each time through the loop. 
   :feedback_c: Sum should be changing.  
   :feedback_d: You can have more than one line in the body of a loop.

   What is printed if you change the program above so that line 5 is also indented the same amount as line 4?
   
.. mchoice:: 7_2_2_Numbers_Repeat1_Q2
   :answer_a: It prints the same thing it did before.
   :answer_b: It prints the value of sum 10 times and sum is different each time it is printed.
   :answer_c: It prints the same sum 10 times.
   :answer_d: You get an error.
   :correct: d
   :feedback_a: Did you actually try it?
   :feedback_b: Both lines 4 and 5 are not in the loop anymore.
   :feedback_c: Is the print repeated now? 
   :feedback_d: You have to have at least one statement in the body of a loop.

   What is printed if you change the program above so that lines 4 and 5 are not indented?
   


