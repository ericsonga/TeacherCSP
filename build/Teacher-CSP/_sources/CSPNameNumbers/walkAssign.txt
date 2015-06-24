..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/apple.jpg
    :width: 30px
    :align: top
    :alt: teacher note
    
.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |codelensfirst| image:: Figures/codelens-first.png
    :height: 20px
    :align: top
    :alt: move to first button

.. |codelensback| image:: Figures/codelens-back.png
    :height: 20px
    :align: top
    :alt: back button

.. |codelensfwd| image:: Figures/codelens-forward.png
    :height: 20px
    :align: top
    :alt: forward (next) button

.. |codelenslast| image:: Figures/codelens-last.png
    :height: 20px
    :align: top
    :alt: move to last button
    
.. 	qnum::
	:start: 1
	:prefix: csp-3-7-

.. highlight:: java
   :linenothreshold: 4

Walking through Assignment more Generally
======================================================

Let's explore assignment in general.  Try tracing this example.

.. codelens:: Assign_Basic

   a = 1
   b = 12.3
   c = "Fred"
   d = b

.. mchoicemf:: 3_7_1_Assignment_Q1
   :answer_a: 1
   :answer_b: 12.3
   :answer_c: "b"
   :answer_d: "d"
   :correct: b
   :feedback_a: The variable a is not used in defining the variable b.
   :feedback_b: The variable d is set to a copy of the value in variable b.  The variable b still holds the value 12.3 as well.  
   :feedback_c: The variable d gets assigned the same value as the one stored in b.
   :feedback_d: The variable d gets its value from the variable b.  

   What is the value of variable ``d`` when this program is finished running?

The *sequence* of statements in a program is very important.  Assignment doesn't create some kind of relationship between the names, like in mathematics.  The variable ``a`` might equal ``12`` at one point, and ``15`` at another. An assignment statement is an action that occurs once, and then is over with.    

.. codelens:: Assign_Multiple

	    var1 = 45
	    var1 = 17.3
	    var2 = var1

.. mchoicemf:: 3_7_2_Assignment_Multiple_Q1
		   :answer_a: var1 is 45, var2 is 45
		   :answer_b: var1 is 45, var2 is var1
		   :answer_c: var1 is 17.3, var2 is 45
		   :answer_d: var1 is 17.3, var2 is 17.3
		   :correct: d
		   :feedback_a: The variable var1 was set to 45, but that gets changed in line 2, before var2 gets set to any value at all.
		   :feedback_b: Both variables contain numeric values, because those are the only values in this program.
		   :feedback_c: The variable var2 never gets set to 45 in this program.
		   :feedback_d: The variable var1 is first set to 45 and then changed to 17.3, and then, var2 gets the value from var1.

		   What are the values in ``var1`` and ``var2`` after this program runs?

We can see values (including the values for named variables) by printing them.  It's a useful way to see what's going on inside a program.  Try running this example where we're having the computer calculate the number of days in three weeks:

.. activecode:: Assign_Days
   :tour_1: "Line by line tour"; 1: calcDays-line1; 2: calcDays-line2; 3: calcDays-line3; 4: calcDays-line4; 5: calcDays-line5; 6: calcDays-line6;

   daysInWeek = 7
   print(daysInWeek)
   numDays = 7 * 3
   print(numDays)
   numDays2 = daysInWeek * 3
   print(numDays2)

.. mchoicemf:: 3_7_3_Assign_Days_Q1
		   :answer_a: 7, 7*3, daysInWeek*3
		   :answer_b: daysInWeek, numDays, numDays2
		   :answer_c: 7, 21, 21
		   :answer_d: 7, 21, 3
		   :correct: c
		   :feedback_a: The values will actually be computed and numbers will be printed.
		   :feedback_b: The variable names will not be printed.
		   :feedback_c: The first print will print the value of daysInWeek (7), the second the value of numDays (21), and the third the value of numDays2 (21).
		   :feedback_d: The value for daysInWeek will be computed and assigned.

		   What three values are printed when this program runs?
   
.. parsonsprob:: 3_7_4_Per_Person_Cost

   The following program should figure out the cost per person for a dinner including the tip. But the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   bill = 89.23
   =====
   tip = bill * 0.20
   =====
   total = bill + tip
   =====
   numPeople = 3
   perPersonCost = total / numPeople
   =====
   print(perPersonCost)



