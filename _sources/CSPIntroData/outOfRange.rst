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
	:prefix: csp-16-4-
	
Out of Range Error 
===================

.. index:: 
	single: out of range error
		  
If you try to access an index that isn't in the collection, you get an error **index out of range**.  That means that you have tried to access an item past the end of the list. Try running the example below to see what that error looks like.

.. activeCode:: Index_Error
  :tour_1: "Line by Line Tour"; 1: lst1-line1; 2: lst1-line2; 3: lst1-line3; 4: lst1-line4; 5: lst1-line5; 6: lst1-line6; 7: lst1-line7;

  items = [2,4,6,8]
  print("The number of items is", len(items))
  items[0]="First item"
  items[1] = items[0]
  items[2] = items[2] + 1
  items[4] = "Last item"
  print(items)

What would the programmer who wrote ``items[4] = "Last item"`` be trying to do?  Maybe he or she was trying to *add* an additional item to the list. 

.. mchoicema:: 16_4_1_AddItem
	:answer_a: items.append("Last item")
	:answer_b: items = items + ["Last item"]
	:answer_c: items.addIndex(4)
	:answer_d: items = items + "Last item"
	:correct: a,b
	:feedback_a: Yes -- append is a *method* that lists understand.
	:feedback_b: Yup, we know that we can add two lists together, and that's what we're doing here.
	:feedback_c: That does not actually work.  A programmer could add the ability for lists to understand addIndex, though.
	:feedback_d: No, you would get an error because you cannot add a list (items) to a string (Last item)
	
	Which of these line or lines *would* actually add "Last item" to the end of the ``items`` list? (Hint: Go ahead and try them above!)  Select all that work.

Whatever the length of the collection (the number of items in the collection), the highest valid *index* is one *less* than the length.  (Since the first item in the collection is index `0`.)  You have probably figured out why the `range` in the `for` loop stops at one less than the last value.  If you access the ``range`` based on the ``len`` of the collection, you get exactly the right thing. We want to be able to do something like this:

.. activecode:: Range_Len
  :tour_1: "Line by Line Tour"; 1: lst2-line1; 2: lst2-line2; 3: lst2-line3;

  myString = "Hello"
  for index in range(0,len(myString)):
      print(myString[index])

**Programming Challenge**: Complete the program below to print out each item in the list ``myList``, one per line.  The code is very similar to the code above for printing each character in a string.

.. activecode:: All_Items
  
  myList = ["this",1,"can","do", 2]
  # You fill in here
  
			   		   


