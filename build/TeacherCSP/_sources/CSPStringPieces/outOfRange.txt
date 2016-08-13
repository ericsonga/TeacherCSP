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
	:prefix: csp-17-4-
	
Out of Range Error 
===================

.. index:: 
	single: out of range error
		  
If you try to access a value at an index that is either less than 0 or larger than the last index in the list, you will get an error **index out of range**.  Try running the example below to see what that error looks like. Then fix the code to work and run it again.

.. activeCode:: Index_Error
   :tour_1: "Structural tour"; 2: StP3-line1; 5: StP1-line2; 8-12: StP2-line3-7; 15-19: StP2-line8-12; 22-26: StP2-line13-17;

   # create the input
   input = "Abe,Brown,boy,1313 Maple Lane,trick"
   
   # split at the comma
   pieces = input.split(",")
   
   # initialize the variables
   firstName = pieces[1]
   lastName = pieces[2]
   gender = pieces[3]
   address = pieces[4]
   verb = pieces[5]
   
   # create the story
   start = "Once there was a " + gender + " named " + firstName + "."
   next1 = "A good " + gender + " living at " + address + "."
   next2 = "One day, a wicked witch came to the " + lastName + " house."
   next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
   ending = "But " + firstName + " was smart and avoided the wicked witch."
   
   # print the story
   print(start)
   print(next1)
   print(next2)
   print(next3)
   print(ending)

.. note:: 

   Whatever the length of the collection (the number of items in the collection), the highest valid *index* is one *less* than the length.  (Since the first item in the collection is index `0`.)  
   
You have probably figured out why the `range` in the `for` loop stops at one less than the last value.  If you access the ``range`` based on the ``len`` of the collection, you get exactly the right thing.  We want to be able to do something like this:

.. activecode:: Range_Len
  :tour_1: "Line by Line Tour"; 1: lst2-line1; 2: lst2-line2; 3: lst2-line3;

  myString = "Hello"
  for index in range(0,len(myString)):
      print(myString[index])

**Programming Challenge**: Complete the program below to print out each item in the list ``myList``, one per line.  The code is very similar to the code above for printing each character in a string.  

.. activecode:: All_Items
  
  myList = ["this",1,"can","do", 2]
  # You fill in here
  
			   		   


