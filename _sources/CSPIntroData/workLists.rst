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

When you go shopping, you might create a **list**. As you shop you might check things off your list (remove them from the list).  You might search your list to see if something is already on it. You might add to a list.  A **list** holds items in an order.   

.. figure:: Figures/lists.jpg
    :width: 400px
    :align: center
    :figclass: align-center

    Figure 1: A couple of lists

A **list** in Python can hold any number of items. It can also hold different types of things in the same list, like numbers and strings. You start and end a list with square brackets and separate elements with commas as shown in line 1 below.
The function ``len`` will return the number of items in the list.  You can do "arithmetic" with lists using ``*`` and ``+``, just like with strings.  Multiplication repeats items in the list.  We can add two lists together, even if one of the lists only has a single item in it.

.. codelens:: Simple_Lists
  :showoutput:

  myFirstList = [12,"ape",13]
  print len(myFirstList)
  print myFirstList * 3
  mySecondList = myFirstList + [321.4]
  print mySecondList

.. index:: 
	pair: list; index
	
To access individual items in a collection, we can use an **index**.  Each item in a collection has a number associated with it -- think of it as the item's address in the collection.  The first item in a collection has index ``0``, the next one ``1``, and so on.  See the image below for a view of the two lists created in the program above and the indicies for each list item.

.. figure:: Figures/listIndices.png
    :width: 300px
    :align: center
    :figclass: align-center

    Figure 2: Lists and their indicies

We use square brackets to access items of the list, e.g., ``myList[0]`` will always return the first item in the list.

.. mchoicemf:: 16_3_1_lastIndex
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :correct: b
   :feedback_a: This is the index of the second item in the list.  
   :feedback_b: This is the index of the last item in this list since it contains 3 items and the first index is 0.   
   :feedback_c: The length of the list is 3, but the first index is 0 so the 3rd item is at index 2.

   What is the value of the last index in the list ``myFirstList``?

You can access individual items of a list just like they were variables.  Using ``list[index]`` on the right side of an assignment returns the value at that index in the list. Using ``list[index]`` on the left side of an assignment statement changes the value at that index in the list.

.. codelens:: Items_As_Variables
  :showoutput:

  items = [2,4,6,8]
  items[0] = "First item"
  items[1] = items[0]
  items[2] = items[2] + 1
  print(items)

.. mchoicemf:: 16_3_2_ItemsAsVariablesQ
	:answer_a: items[0]
	:answer_b: items[1]
	:answer_c: items[2]
	:answer_d: items[3]
	:correct: d
	:feedback_a: Originally, items[0] was 2, but then we set it to the string: First item
	:feedback_b: We set items[1] to be the same as items[0]: First item
	:feedback_c: We increment items[2]
	:feedback_d: The value at items[3] doesn't change.  It still equals 8.

	Of the four items in the list named ``items``, which one is not changed in the program above?
	


