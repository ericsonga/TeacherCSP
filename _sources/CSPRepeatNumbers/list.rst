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
	:prefix: csp-7-3-
	
.. highlight:: java
   :linenothreshold: 4

What is a List?
=================

A **list** holds items in order. A **list** in Python is enclosed in ``[`` and ``]`` and can have values separated by commas, like ``[1,2,3,4,5,6,7,8,9,10]``.  You probably use **lists** all the time.  People often 
make a list before they go shopping or a list of things to do.  A **list** has an order and each list item has a position in the list, like the first item in a list or the last item in a list.

.. figure:: Figures/lists.jpg
    :height: 250px
    :align: center
    :alt: a shopping list
    :figclass: align-center

    Figure 2: A shopping list

When you ran the code in the last section, did you get 55?  That's the sum of all the numbers from 1 to 10.  Here is the program again.  Run it if you don't remember what it printed before.

.. activecode:: Numbers_Repeat2
    :tour_1: "Line by line tour"; 1: for1_line1; 2: for1_line2; 3: for1_line3; 4: for1_line4; 5: for1_line5;
    :tour_2: "High level tour"; 1-2: for1_line1-2; 3-4: for1_line3-4; 5: for1_s_line5;
	
    sum = 0  # Start out with nothing
    thingsToAdd = [1,2,3,4,5,6,7,8,9,10]
    for number in thingsToAdd:
    	sum = sum + number
    print(sum)

.. mchoicemf:: 7_3_1_Numbers_Repeat2_Q1
   :answer_a: 55
   :answer_b: 0
   :answer_c: 3628800
   :answer_d: Error - number is too big
   :correct: c
   :feedback_a: That's the sum
   :feedback_b: That's what you get if you leave the sum as 0.  Multipying everything by 0 gets you 0
   :feedback_c: That's 1*2*3*4*5*6*7*8*9*10
   :feedback_d: It should actually work

   Now, change the program above to get the product instead of the sum (e.g., replace `+` with `*`, and replace the `0` as the initial value of `sum` to `1`).  What do you get now when you run the program?

|bigteachernote| Teacher Note: Names are Just Words
======================================================
Once you change the program above in order to use ``*`` instead of ``+``, you will see that it is still using the name (*variable*) ``sum`` to represent the `product` of all the numbers in ``thingsToAdd``.  The program would be *better* if we used the right name for the variable: ``product`` instead of ``sum`` once we switched to multiplication (``*``) from addition (``+``).  However, the program still *works*.  In the end, the names for the variables are there for the benefit of the *humans*, not the computer.  The computer doesn't care if we name the program `xyzzy1776`.  It will *work* with a bad variable name.  It's just not as readable.  **You should write your programs so that people can understand them, not just computers.** 

Using Better Variable Names
-----------------------------

Let's write that program again with a better variable name.  We will use ``product`` instead of ``sum`` for the variable name that holds the result of the calculation.  Step through the code below by clicking on the *Forward* button and note what value the variable ``number`` is set to each time through the loop.  Also note how the variable ``product`` changes during the loop.

.. codelens:: Numbers_Product
	
    product = 1  # Start out with nothing
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for number in numbers:
    	product = product * number
    print(product)
    
.. mchoicemf:: 7_3_2_Numbers_Product_Q1
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :answer_e: 10
   :correct: c
   :feedback_a: That's the value the first time through the loop
   :feedback_b: That's the value the second time through the loop
   :feedback_c: That's the value the third time through the loop
   :feedback_d: That's the value the fourth time through the loop
   :feedback_e: That's the value the last time through the loop

   What is the value of number the 3rd time through the loop?
   
.. mchoicemf:: 7_3_3_Numbers_Product_Q2
   :answer_a: 6
   :answer_b: 10
   :answer_c: 24
   :answer_d: 120
   :correct: c
   :feedback_a: That's the value after the 3rd time through the loop.
   :feedback_b: That's the value if we were adding up the values rather than multiplying them.
   :feedback_c: That's the value after the 4th time through the loop.
   :feedback_d: That's the value after the 5th time through the loop.

   What is the value of product after the 4th time through the loop?



