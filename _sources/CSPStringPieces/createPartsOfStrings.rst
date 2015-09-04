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
	:prefix: csp-17-6-

   
Creating parts of strings
=================================

As we have seen before the ``find(string)`` function takes a target string as input and returns the index where that target string is found in the current string. If the string isn't found it returns -1.

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
     
.. mchoice:: 17_6_1_Find_red
   :answer_a: 1
   :answer_b: 9
   :answer_c: 10
   :answer_d: -1
   :correct: a
   :feedback_a: The find function returns the index of the first position that contains the given string.
   :feedback_b: This would be true if it was pos = str.find(" is").
   :feedback_c: This would be true if it was pos = str.find(" is") and the first position was 1, but it is 0.
   :feedback_d: A -1 is returned if the string you are looking for isn't found.  

   What will be printed when the following executes?
   
   :: 

     str = "His shirt is red"
     pos = str.find("is")
     print(pos)
     
.. mchoice:: 17_6_2_Find_Red
   :answer_a: 1
   :answer_b: 13
   :answer_c: 14
   :answer_d: -1
   :correct: d
   :feedback_a: Why would this return 1?  What string was it looking for and where is that string in <code>str</code>
   :feedback_b: This would be true if it was <code>str.find("red")</code>.
   :feedback_c: This would be true if it was <code>str.find("red")</code> and the first position was 1, but it is 0.
   :feedback_d: A -1 is returned when the string you are looking for isn't found.  Remember that case matters in Python!

   What will be printed when the following executes?
   
   :: 

     str = "His shirt is red"
     pos = str.find("Red")
     print(pos)
   
..	index::
	single: dot-notation
	pair: programming; dot-notation

..	index::
	single: index
	single: slice
	pair: string; slice

You can use the ``find`` function along with the slice feature to get part of a string.  To get a **slice** (part) of a string use ``stringName[start:end]``, which returns a new string with all the characters from the start position to one before the end position.  

Say that you are looking for a name in a string but don't know the exact position of the name in the string.  However you do know that it will be after ``name:``.  

.. activecode:: String_Slice1
   :nocodelens:
   
   namePart = "name: Anu Gao"
   posName = namePart.find("name:")
   if (posName > -1):
       name = namePart[posName+6:len(namePart)]
   else:
       name = "Unknown"
   print(name)
   
  
    
   
