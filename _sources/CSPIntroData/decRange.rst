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
	:prefix: csp-16-8-
		   
Using a Negative Change Value with Range
==========================================

.. index:: 
	pair: range; negative change amount
	pair: range; inclusive
	pair: range; exclusive
	
The ``range(start, end, change)`` function can have 3 parameters: the ``start``, the ``end``, and the amount to ``change`` by.  It returns a list that begins with the ``start`` value and generates the rest of the list items by adding the ``change`` value to the ``start`` value.  It stops generating the list when the current value is equal or greater than the ``end`` value.  So the generated list *includes* the ``start`` value and *excludes* the ``end`` value.  We have mostly used the ``range`` function to create an increasing sequence of numbers like [0, 1, 2, 3, 4, 5].  But, it can also be used to create a decreasing sequence like [5, 4, 3, 2, 1, 0] as shown below.  Remember that the second number to the range function says when to stop and that number is not included in the returned list of numbers.

.. activecode:: Dec_Range
  :tour_1: "Line by Line Tour"; 1: range1-line1; 2: range1-line2;

  for index in range(5, -1, -1):
      print index

Here's a program we saw earlier, but with the ``range`` function parameters changed to create a decreasing list from the last valid index (the length of the list minus 1) to 0.  

.. activecode:: Build_Up_String
  :tour_1: "Line by Line Tour"; 1: lst8-line1; 2: lst8-line2; 3: lst8-line3; 4: lst8-line4; 5: lst8-line5; 

  source = ["This","is","a","list"]
  slowly = []
  for index in range(len(source)-1,-1,-1):
      slowly = [source[index]] + slowly
      print slowly

.. mchoicemf:: 16_8_1_lenMinusOne
	  :answer_a: If we started with len(source), we would get an error for indexing past the end of the list
	  :answer_b: It is a mistake and should be len(source)
	  :answer_c: Because we have -1 in the other two spots
	  :correct: a
	  :feedback_a: Right -- the end element is at index len(source)-1
	  :feedback_b: No -- if accessed len(source) as an index, we would be going past the end of the list
	  :feedback_c: We have -1 in the end position because we want to stop at zero, and we have an increment of -1 (last position)
	
	   Why do we start at ``len(source)-1`` in this program?

Can you figure out what the following program does?

.. sourcecode:: python

  source = "United States of America"
  slowly = ""
  for index in range(len(source)-1,-1,-1):
      slowly = slowly + source[index]
      print slowly

Try to figure out what the program above does, then try to answer this question.

.. mchoicemf:: 16_8_2_ReversedQ
			  :answer_a: <image src="../_static/reversal.png"/>
			  :answer_b: <image src="../_static/build-up-rightway.png"/>
			  :answer_c: <image src="../_static/build-up-missed-one.png"/>
			  :correct: a
			  :feedback_a: This takes letters from the end of the string forward, and adds them to the end
			  :feedback_b: This one is adding up letters in the forward direction
			  :feedback_c: This one ends at 0 (or rather, 1)

		   	  Which one of these is the output of that program?



