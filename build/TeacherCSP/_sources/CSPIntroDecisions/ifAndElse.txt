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
	:prefix: csp-12-7-
	
.. highlight:: python
   :linenothreshold: 3

Using if and else
==========================

..	index::
   	pair: if; else

Most professional programmers would write the following code:

.. activeCode:: Multiple_Ifs_2
     :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c1-line2-3; 4-5: c1-line4-5; 6: c1-line6; 7-9: c3f-line7-9;

     weight = 0.5
     if weight < 1:
         price = 1.45
     if weight >= 1: 
         price = 1.15
     total = weight * price
     print(weight)
     print(price)
     print(total)
     
Like this:

.. activeCode:: if_and_else
     :tour_1: "Structural Tour"; 1: c5-line1; 2-3: c5-line2-3; 4-5: c5-line4-5; 6: c5-line6; 7-9: c3f-line7-9;

     weight = 0.5
     if weight < 1:
         price = 1.45
     else:
         price = 1.15
     total = weight * price
     print(weight)
     print(price)
     print(total)

An ``else`` is an additional optional phrase on an ``if`` statement.  IF AND ONLY IF the *test* in the ``if`` is **false** does the block of statements after the ``else`` get executed.  Using an ``if`` with an ``else`` makes sure that *either* the ``if`` block is executed *or* the ``else`` block is executed, but **never** both.  

.. figure:: Figures/ifAndElseFlow.png
    :height: 350px
    :align: center
    :alt: Flowchart for both an if and else
    :figclass: align-center

    Figure 4: Flow of execution for both an if and else
    
**Mixed up programs**

.. parsonsprob:: 12_7_1_Even_Odd

   The following program should print out "x is even" if the remainder of x divided by 2 is 0 and "x is odd" otherwise, but the code is mixed up. The ``%`` symbol gives the remainder after the first number is divided by the second number.  Drag the blocks from the left and place them in the correct order on the right.  Be sure to also indent correctly! Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or have the wrong indention.</p>
   -----
   x = 92
   if x % 2 == 0:
       print("x is even")
   else: 
       print("x is odd")

It is easy to write an ``if`` when you want *exactly* one block to execute, but you can accidentally create a "hole" -- a condition where neither block executes.  That's what happened in the example below when the weight is equal to 1 pound.

.. activeCode:: Price_If_Broken2
     :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c1-line2-3; 4-5: c3-line4-5; 6: c1-line6; 7-9: c3f-line7-9;

     weight = 0.5
     if weight < 1:
         price = 1.45
     if weight > 1: 
         price = 1.15
     total = weight * price
     print(weight)
     print(price)
     print(total)
