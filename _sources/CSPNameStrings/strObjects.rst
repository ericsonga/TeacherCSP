..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/apple.jpg
    :width: 30px
    :align: top
    :alt: teacher note
    
.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note
    
.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. 	qnum::
	:start: 1
	:prefix: csp-4-2-

   
Strings are Objects
=====================
   
..	index::
	single: dot-notation
	pair: programming; dot-notation

Strings are objects in Python which means that there is a set of built-in functions that you can use to manipulate strings.  You use **dot-notation** to invoke the functions on a string object such as ``sentence.lower()``.  The function ``lower()`` returns a new string with all of the characters in the original string set to lowercase.  The function ``capitalize()`` will return a new string with the first letter of the string capitalized.

.. activecode:: String_Methods2
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5;
   :nocodelens:
   
   sentence = "THIS IS A TEST"
   better = sentence.lower()
   print(better)
   betterStill = better.capitalize() + "."
   print(betterStill)
   
   
Getting Part of a String
-------------------------

..	index::
	single: index
	single: slice
	pair: string; slice

A string has characters in a sequence.  Each character is at a position or **index** which starts with 0 as shown below.  An **index** is a number associated with a position in a collection of values like a string.

.. figure:: Figures/stringIndicies.png
    :width: 400px
    :align: center
    :alt: a string with the position (index) shown above each character
    :figclass: align-center

    Figure 1: A string with the position (index) shown above each character
   
A **slice** is a way to get part of a string.  One way to use a **slice** is to do `stringName[num]``.  This will return a new string with just the character at that position in the string.

.. activecode:: String_Slice1
   :nocodelens:
   
   sentence = "This is a test"
   s1 = sentence[1]
   print(s1)
   s2 = sentence[5]
   print(s2)
   s3 = sentence[8]
   print(s3)
   s4 = sentence[10]
   print(s4)
   
.. figure:: Figures/stringIndicies.png
    :width: 400px
    :align: center
    :alt: a string with the position (index) shown above each character
    :figclass: align-center

    Figure 2: A string with the position (index) shown above each character
   
A **slice** with two values separated with a ``:`` between them returns a new string with the characters from the given start position to the one before the given end position.

.. activecode:: String_Slice2
   :nocodelens:
   
   sentence = "This is a test"
   s1 = sentence[1:3]
   print(s1)
   s2 = sentence[5:7]
   print(s2)
   s3 = sentence[8:11]
   print(s3)
   s4 = sentence[10:14]
   print(s4)
   
**Check Your Understanding**

.. mchoice:: 4_2_1_Slice
   :answer_a: This is the end
   :answer_b: This
   :answer_c: his
   :correct: c
   :feedback_a: This would be true if we were printing the value of str and we hand't changed it on line 2.
   :feedback_b: This would be true if the first position was 1 and the substring included the character at the end position, but the first character in a string is at position 0 and the substring won't include the character at the last position.  
   :feedback_c: This will return a string that starts at position 1 and ends at position 3.  

   What will be printed when the following executes?
   
   :: 

     str = "This is the end"
     str = str[1:4]
     print(str)
     
.. mchoice:: 4_2_2_Slice2
   :answer_a: i
   :answer_b: s
   :answer_c: is the end
   :correct: a
   :feedback_a: This will print the character at position 5 in the string which is i.  Remember that the first character is at position 0.  
   :feedback_b: This would be true if the first character was at position 1 instead of 0.
   :feedback_c: This would be true if it returned from the given position to the end of the string, but that isn't what it does.

   What will be printed when the following executes?
   
   :: 

     str = "This is the end"
     str = str[5]
     print(str)
   
Some Other String Functions
----------------------------

..	index::
	single: len
	pair: string; len

The ``len(string)`` function takes a string as input and returns the number of characters in the string including spaces. 

.. activecode:: String_Length
   :nocodelens:
   
   sentence = "This is a test"
   length = len(sentence)
   print(length)
   sentence = "Hi"
   length = len(sentence)
   print(length)
   
..	index::
	single: find
	pair: string; find

The ``find(string)`` function takes a string as input and returns the index where that string is found in the current string. If the string isn't found it returns -1.

.. activecode:: String_Find
   :nocodelens:
   
   sentence = "This is a test"
   pos = sentence.find("is")
   print(pos)
   pos = sentence.find("love")
   print(pos)
   
.. note::
   The ``find`` function will return the first position it finds the given string in.  Notice that above it printed 2 which means it found the "is" in "This" first.  
   
   **Check your understanding**
   
.. mchoice:: 4_2_3_stringLen
   :answer_a: 13
   :answer_b: 15
   :answer_c: 10
   :correct: b
   :feedback_a: Don't forget to include the spaces in the count.
   :feedback_b: The len function returns the number of elements in the string including spaces.
   :feedback_c: This would be true if the len function only returned the number of alphabetic characters, but it includes all including spaces.


   Given the following code segment, what will be printed?
   
   ::

     street = "125 Main Street"
     print(len(street))
     
.. mchoice:: 4_2_4_Find
   :answer_a: 1
   :answer_b: 9
   :answer_c: 10
   :correct: a
   :feedback_a: The find function returns the index of the first position that contains the given string.
   :feedback_b: This would be true if it was pos = str.find(" is").
   :feedback_c: This would be true if it was pos = str.find(" is") and the first position was 1, but it is 0.

   What will be printed when the following executes?
   
   :: 

     str = "His shirt is red"
     pos = str.find("is")
     print(pos)
     



   
   

