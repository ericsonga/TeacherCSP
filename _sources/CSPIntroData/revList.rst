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
		   
Reversing a List
=================

.. index:: accumulator

We can use the looping ability of computers, plus the indexing ability, to manipulate lists in interesting and even surprising ways. In the below program, we use an **accumulator**, which is something that accumulates values.  We start with the accumulator ``soFar`` set to an empty list -- a list with nothing in it.  As the program executes, it appends items from the ``source`` list into the ``soFar`` list.  

.. activecode:: Reverse_List
  :tour_1: "Line by Line Tour"; 2: lst6-line1; 5: lst6-line2; 8: lst6-line3; 11: lst6-line4; 12: lst6-line5; 
  
  # setup the source list
  source = ["This","is","a","list"]
  
  # Set the accumulator to the empty list
  soFar = []
  
  # Loop through all the items in the source list
  for index in range(0,len(source)):
  
      # Add a list with the current item from source to soFar
      soFar = [source[index]] + soFar
      print(soFar)
      
.. note:: 

    Notice the ``[`` and ``]`` around the value in the ``source`` at the current value of ``index``.  This is needed because you can only concatenate two lists together.  Try removing the ``[`` and ``]``.  What error do you get?

.. mchoice:: 16_5_1_reversinglist
		  :answer_a: Because we started at 0 and went to len(source).
		  :answer_b: Because we put the new element ahead of the others in soFar.
		  :answer_c: Because of the square brackets around source[index].
		  :correct: b
		  :feedback_a: That is the normal way of accessing each element, one at a time.
		  :feedback_b: If we had done soFar = soFar + [source[index]], soFar would have just duplicated the list, in order.
		  :feedback_c: We need those in order to add elements into the list.  You can only add a list to a list.

		   Why did the code above end up reversing the list?
		   


