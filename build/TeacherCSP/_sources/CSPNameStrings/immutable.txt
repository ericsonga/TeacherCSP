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
	:prefix: csp-4-3-

Strings are Immutable
======================

..	index::
	pair: string; immutable

Even though you can manipulate a string to create a new string the original string is **immutable** which means that it doesn't change.  Notice that after you execute the code below the string stored in the variable ``sentence`` hasn't changed.  
  
.. activecode:: String_Immutable
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5; 6: str2-line6;
   
   sentence = "THIS IS A TEST"
   better = sentence.lower()
   print(better)
   betterStill = better.capitalize() + "."
   print(betterStill)
   print(sentence)
   
While the strings themselves can't be changed you can change the value of a variable. This throws away the original string and sets the variable's value to the new string.   

.. activecode:: String_Reassign
   :tour_1: "Line-by-line Tour"; 1: sa2-line1; 2: sa2-line3; 3: sa2-line2; 4: str2-line6;
   
   sentence = "THIS IS A TEST"
   print(sentence)
   sentence = "Hi there"
   print(sentence)
   
.. mchoice:: 4_3_1_s1
   :answer_a: xyz
   :answer_b: xyxyz
   :answer_c: xy xy z
   :answer_d: xy z
   :answer_e: z
   :correct: b
   :feedback_a: s1 will equal "xy" plus another "xy" then z at the end.
   :feedback_b: s1 contains the original value, plus itself, plus "z"  
   :feedback_c: No spaces are added during concatenation.
   :feedback_d: No spaces are added during concatenation, and an additional "xy" should be included at the beginning.
   :feedback_e: s1 was set to "xy" initially, so the final answer will be "xyxyz"

   Given the following code segment, what is the value of the string s1 after these are executed?
   
   ::

     s1 = "xy"
     s2 = s1
     s1 = s1 + s2 + "z"
     
.. mchoice:: 4_3_2_s2
   :answer_a: Hey
   :answer_b: hey
   :answer_c: HEY
   :correct: c
   :feedback_a: This would be correct if we had asked what the value of s3 was. What is the value of s1?
   :feedback_b: This would be true if we asked what the value of s2 was after the code executes.  What is the value of s1?
   :feedback_c: Strings are immutable, meaning they don't change.  Any function that changes a string returns a new string.  So s1 never changes unless you set it to a different string. 

   What is the value of s1 after the following code executes?
   
   :: 

     s1 = "HEY"
     s2 = s1.lower()
     s3 = s2.capitalize()


