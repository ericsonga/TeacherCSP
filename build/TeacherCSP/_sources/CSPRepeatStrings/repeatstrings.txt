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
	:prefix: csp-9-1-
	
.. highlight:: java
   :linenothreshold: 4

Using Repetition with Strings
==============================

*Learning Objectives:*

- Show how the accumulator pattern works for strings.
- Show how to reverse a string.
- Show how to mirror a string.
- Show how to use a while loop to modify a string.

..	index::
	single: assignment
	pair: strings; assignment

.. index::
    single: words
    single: strings
	single: for loop

Python already has built in the ability to play with words or **strings**, just like how we played with numbers in the last chapter.  A **string** is a collection of letters, numbers, and other characters. A Python ``for`` loop knows how to step through letters, and addition (``+``) appends strings together. What's cool is that the same accumulator pattern works.

As a reminder, here are the five steps in the accumulator pattern.

1. Set the accumulator variable to its initial value.  This is the value we want if there is no data to be processed.
2. Get all the data to be processed.
3. Step through all the data using a ``for`` loop so that the variable takes on each value in the data.
4. Combine each *piece* of the data into the accumulator.
5. Do something with the result.

Be sure to press the |audiobutton| to get an explanation for how this program works.

.. activecode:: Copy_Words
    :tour_1: "Lines of code"; 2: strR1-line2; 4: strR1-line4; 6: strR1-line6; 8: strR1-line8; 10: strR1-line10;

    # STEP 1: INITIALIZE ACCUMULATOR 
    newString = ""
    # STEP 2: GET DATA
    phrase = "Rubber baby buggy bumpers."
    # STEP 3: LOOP THROUGH THE DATA
    for letter in phrase:
    	# STEP 4: ACCUMULATE
    	newString = newString + letter
    # STEP 5: PROCESS RESULT
    print(newString)

Run this program.  Enh, not that interesting, eh?  It just copies all the letters from ``phrase`` to ``newString``.

