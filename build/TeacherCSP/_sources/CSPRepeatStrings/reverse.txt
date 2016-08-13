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
    
.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. 	qnum::
	:start: 1
	:prefix: csp-9-2-
	
.. highlight:: java
   :linenothreshold: 4

Reversing Text
================

Run this next one, and look at how a simple change to the pattern gives a very different result.    Here we'll combine *before* rather than *afterward*, changing only Step 4 (how values are accumulated).

.. activecode:: Copy_Reverse
    :tour_1: "Lines of code"; 2-3: strR2-line2-3; 5: strR2-line5; 7: strR2-line7; 9: strR2-line9; 10: strR2-line10; 12: strR2-line12; 13: strR2-line13; 14: strR2-line14; 15: strR2-line15;
	
    # STEP 1: INITIALIZE ACCUMULATORS
    newStringA = ""
    newStringB = ""
    # STEP 2: GET DATA
    phrase = "Happy Birthday!"
    # STEP 3: LOOP THROUGH THE DATA
    for letter in phrase:
    	# STEP 4: ACCUMULATE
      	newStringA = letter + newStringA
      	newStringB = newStringB + letter
    # STEP 5: PROCESS RESULT
    print("Here's the result of using letter + newStringA:")
    print(newStringA)
    print("Here's the result of using newStringB + letter:")
    print(newStringB)

.. mchoice:: 9_2_1_Copy_Reverse_Q1
   :answer_a: Because we add each new letter at the <i>end</i> of <code>newStringB</code>.
   :answer_b: Because <code>newStringA</code> is adding the characters from left to right.
   :answer_c: Because we called a reverse function.
   :answer_d: Because the <code>for</code> loop is doing a reversal
   :correct: a
   :feedback_a: Each new letter gets added at the end, which creates a reversal.
   :feedback_b: How would that reverse the other string?
   :feedback_c: There is no reverse function in this program.
   :feedback_d: The same <code>for</code> loop is creating both an in-order copy of the string and a reversed order of the string.  The <code>for</code> loop is the same in both cases.

   Why do you think ``newStringB`` has all the letters, but in the reverse order?
