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
	:prefix: csp-16-5-
  
For Each Item Loop
===================

.. index:: 
	pair: loop; for each
	
Because it is very common to use a ``for`` loop to touch each of the elements of a collection, we can do it even without using a ``range`` and ``index``.  We can use a ``for`` loop that repeats the body of the loop one time for each value in the collection.  This is sometimes called a **for each loop** since it repeats the body of the loop one time for each element in the collection.

.. activecode:: For_Each
  :tour_1: "Line by Line Tour"; 1: lst3-line1; 2: lst3-line2; 3: lst3-line3; 4: lst3-line4; 5: lst3-line5; 6: lst3-line6;
  
  myList = [0,1,2,3,"end"]
  for item in myList:
      print(item)
  myString = "MLK"
  for character in myString:
      print(character)

This isn't actually a different ``for`` loop.  The function ``range`` actually creates a list of numbers, and the index just steps through each of those items one at a time.

.. activecode:: For_Each_Range
  :tour_1: "Line by Line Tour"; 1: lst4-line1; 2: lst4-line2; 3: lst4-line3; 4: lst4-line4;
  
  myString = "MLK"
  myList = range(0,len(myString))
  for index in myList:
      print(myString[index])

.. mchoicemf:: 16_5_1_foreachRangeQ
			  :answer_a: We would get an error for doing math in a range function.
			  :answer_b: We would get an error because len(myString)/2 is 7.5 which can't be used in a range.
			  :answer_c: We would get "M L K" printed with one character per line.
			  :answer_d: We would get "M L K " printed with one character per line plus an extra space at the end.
			  :correct: b
			  :feedback_a: You are allowed to do math in a range function.
			  :feedback_b: Dividing 15 by 2 results in 7.5, which can't be used in a range.  
			  :feedback_c: This would be true if dividing by 2 was truncated to 7.
			  :feedback_d: This would be true if 7.5 was rounded to 8, but that doesn't happen.

			   What would happen if we changed line 2 to `myList = range(0,len(myString)/2)`? (Hint: You could try it)
			   		   


