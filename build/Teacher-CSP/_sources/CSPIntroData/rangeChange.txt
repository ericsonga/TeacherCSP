..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note
    
.. 	qnum::
	:start: 1
	:prefix: csp-16-7-
		   
Vary the Change Amount in Range
================================

.. index:: 
	pair: range; change amount

There is a version of ``range`` that takes an **change amount**, so that you can go up by more than one each time, or even down by a negative number.  Try it out!

.. activecode:: addEvensQ1
  :tour_1: "Line by Line Tour"; 1: lst7-line1; 2: lst7-line2; 3: lst7-line3; 4: lst7-line4; 5: lst7-line5; 

  numbers = [0,1,2,3,4,5,6,7,8,9,10]
  evens = []
  for index in range(0,len(numbers),2):
      evens = evens + [numbers[index]]
  print evens

.. mchoicema:: 16_7_1_addEvensQ2
		  :answer_a: Start with numbers=[1,2,3,4,5,6,7,8,9,10]
		  :answer_b: Change the range to range(1,len(numbers),2)
		  :answer_c: Change the range to range(0,len(numbers),1)
		  :answer_d: Change the range to range(0,len(numbers),3)
		  :correct: a,b
		  :feedback_a: Yes, that would work, but there's an easier way
		  :feedback_b: Yes, just by starting at 1, then skipping 2 each time, we'd collect the odds
		  :feedback_c: No, that would collect all the numbers in evens
		  :feedback_d: No, that would result in 0,3,6,9 in evens

		   Which of these changes to the program would you give you just the odds? (Again: Try it!)  Select all that work.
		   


