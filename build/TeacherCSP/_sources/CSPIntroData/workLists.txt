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
	:prefix: csp-16-3-
   	  
Working with Lists
=====================

In earlier chapters we worked with lists of numbers as shown below.  

.. activecode:: Sum_Numbers
    :tour_1: "Line by line tour"; 2: for1_line1; 3: for1_line2; 6: for1_line3; 7: for1_line4; 10: for1_line5;
    :tour_2: "High level tour"; 2-3: for1_line1-2; 6-7: for1_line3-4; 10: for1_s_line5;
	
    # initialize the variables
    sum = 0  
    thingsToAdd = [1,2,3,4,5,6,7,8,9,10]
    
    # loop through the list and add each value to the sum
    for number in thingsToAdd:
    	sum = sum + number
    	
    # print the sum
    print(sum)

But a list in Python can also hold different types of things in the same list, like numbers and strings. You start and end a list with square brackets (``[]``) and separate elements with commas as shown in line 1 below.
The function ``len`` will return the number of items in the list.  You can do "arithmetic" with lists using ``*`` and ``+``, just like you can with strings.  Multiplication repeats items in the list.  We can add two lists together, even if one of the lists only has a single item in it.

.. codelens:: Simple_Lists
  :showoutput:

  myFirstList = [12,"ape",13]
  print(len(myFirstList))
  print(myFirstList * 3)
  mySecondList = myFirstList + [321.4]
  print(mySecondList)
	
.. mchoice:: 16_3_1_lenList
   :answer_a: 1
   :answer_b: 3
   :answer_c: 4
   :answer_d: 14
   :correct: c
   :feedback_a: This is just how many numbers are in the list.  There are also strings in this list.  
   :feedback_b: This is just the number of strings in this list.  There is also a number in this list. 
   :feedback_c: This is the number of items in this list.  There are 3 strings and 1 number.
   :feedback_d: Count each string as one item.
	
   What is the length of the list ["Sue","Maria",5,"Erica"]?
	   
.. mchoice:: 16_3_2_addLists
   :answer_a: 1
   :answer_b: 2 
   :answer_c: 3
   :correct: c
   :feedback_a: That is the number of items in the list start on line 1, but line 2 adds more.
   :feedback_b: That is how many items were in the list that was added to start.  But, start already had one element.
   :feedback_c: The list start has one item and then two more were added.
  
	
   What would the following code print?
	   
   :: 
   
      start = [3]
      start = start + [6,7]
      print (len(start))
      
      
.. note:: 

    Remember that a list starts with a ``[`` and ends with a ``]``.  Items in the list are separated by commas.  
    
Run the code below to see what type of error you get if you forget the ending ``]`` as shown below on line 1.  Also see what happens if you don't separate the list items with commas as shown on line 2. Fix the code to run and print.

.. activecode:: intro_data_string_error

    start = [3
    start = start + ["What"3]
    print(start)