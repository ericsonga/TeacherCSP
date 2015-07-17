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
	:prefix: csp-8-3-
	
.. highlight:: java
   :linenothreshold: 4

Counting with a While Loop
===========================

It's easy to have the computer repeat something a specific number of times.  We have done this with a ``for`` loop and a list of numbers or the ``range`` function.  We can also do it with a ``while`` loop.  

For example, we could have a computer count from 1 to 10.  We will use a ``counter`` variable that we will **increment** inside the loop.  **Increment** means increase the value by one.

.. activecode:: while_count

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
    
