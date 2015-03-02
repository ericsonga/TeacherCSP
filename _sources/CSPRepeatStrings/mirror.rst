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
	:prefix: csp-9-3-
	
.. highlight:: java
   :linenothreshold: 4

Mirroring Text
===============

What happens if we add the letter to *both* sides of the new string that we're making?

.. activecode:: Copy_Mirror
    :tour_1: "Lines of code"; 2: strR3-line1; 4: strR3-line2; 6: strR3-line3; 8: strR3-line4; 10: strR3-line5;
	
    # STEP 1: INITIALIZE ACCUMULATOR 
    newString = ""
    # STEP 2: GET DATA
    phrase = "This is a test"
    # STEP 3: LOOP THROUGH THE DATA
    for letter in phrase:
      	# STEP 4: ACCUMULATE
      	newString = letter + newString + letter
    # STEP 5: PROCESS RESULT
    print(newString)

Try changing the phrase and see what effects you can generate.

.. mchoicemf:: 9_3_1_Copy_Mirror_Q1
   :answer_a: Make the phrase <code>"Time to panic!"</code>
   :answer_b: Change the <code>newString</code> in line 1 to <code>"!"</code> instead of <cod>""</code>
   :answer_c: Change the right hand side of line 4 to <code>letter + "!" + newstring + letter</code>
   :answer_d: Change the right hand side of line 4 to <code>letter + newstring + "!" + letter</code>
   :correct: b
   :feedback_a: That would give us <code>!cinaP ot emiTTime to Panic!</code>.
   :feedback_b: We can start our accumulator with something in it.
   :feedback_c: That would give us <code>!!c!i!n!a!P! !o!t! !e!m!i!T!Time to Panic!</code> -- exclamation points between the letters in the first half of the mirror.
   :feedback_d: That would give us <code>!cinaP ot emiT!T!i!m!e! !t!o! !P!a!n!i!c!!</code> -- exclamation points between the letters in the second half of the mirror.

   Change the mirroring program to mirror the phrase ``"Time to Panic"`` with a single exclamation point in the middle, to make the printed words look like this: ``cinaP ot emiT!Time to Panic``.  How do you do it?

The accumulator doesn't have to be set to be an empty string.  You can put something in the accumulator, and then it will show up in the middle of the mirrored phrase.

.. codelens:: Char_In_Middle

    newString = "!"
    phrase = "We're off to see the Wizard!"
    for letter in phrase:
        newString = letter + newString + letter
    print(newString)

.. mchoicemf:: 9_3_2_Count_Exclamations_Q1
   :answer_a: One
   :answer_b: Two
   :answer_c: Three
   :answer_d: Four
   :correct: a
   :feedback_a: There is just the one in the accumulator to start.
   :feedback_b: If we just mirrored the string, there would be only two.  But we are mirroring with something in the accumulator.
   :feedback_c: That is true at the end, but not when letter contains the first letter of <code>"Wizard"</code>
   :feedback_d: At most, there will be three in <code>newString</code>.

   When the variable ``letter`` contains the ``"W"`` from ``Wizard``, how many exclamation points are in ``newString``?

.. parsonsprob:: 9_3_3_Palindrome

   <p>The phrase <code>"A but tuba"</code> is a <b>palindrome</b>.  The letters are the same forward and backward.  The below program generates the output: <code>"abut tub a<=>a but tuba"</code>  Put the lines in the right order with the right indentation.</p>
   -----
   newStr = "<=>"
   phrase = "a but tuba"
   =====
   for char in phrase:
   =====
       newStr = char + newStr + char
   =====
   print(newStr)