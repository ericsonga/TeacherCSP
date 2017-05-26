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
	:prefix: csp-16-2-

Working with Strings
=====================
.. index:: 
	single: len;
	
A **string** is a collection of characters, in a sequence.  ``"My name is Mark."`` is a string with 16 characters in it. Spaces and periods are separate characters.
Strings start with single quotes or double quotes.  As you have seen before you can actually do some simple "arithmetic" with strings using ``+`` and ``*`` as shown below. You can also get the length of any collection (including strings) with the ``len`` function.

.. codelens:: String_Manip
  :showoutput:

  name = "Mark"
  start = 'My name is '
  combined = start + name
  print(len(combined))
  print(combined)
  print(name * 3)

.. mchoice:: 16_2_1_Str_Combine
   :multiple_answers:
   :correct: b,c,d
   :answer_a: print(start+name)
   :answer_b: print(start+name+name+name)
   :answer_c: print(start + (3 * name))
   :answer_d: print(start + 3 * name)
   :feedback_a: This just generates: My name is Mark
   :feedback_b: Could you also use multiplication?
   :feedback_c: This will work, but multiplication is processed before addition, so you do not have to have parentheses.
   :feedback_d: This will work just fine.

   If we wanted to add one line to the above to print "My name is MarkMarkMark", which one of these would do it? Choose all that are correct.
	
.. mchoice:: 16_2_2_lenString
   :answer_a: 5
   :answer_b: 6
   :answer_c: 7
   :answer_d: 9
   :correct: c
   :feedback_a: This is just the numer of alphabetic characters.  The length of a string includes the spaces and punctuation characters too.
   :feedback_b: Don't forget to count the space too.  
   :feedback_c: The length of a string includes all the characters which includes spaces and punctuation.  
   :feedback_d: We don't include the single or double quotes in the length of the string.
	
   What is the length of the string ``"Hi sis!"``?
	   
.. mchoice:: 16_2_3_addStrings
   :answer_a: Watch Out
   :answer_b: WatchOut 
   :answer_c: Watch Out Watch Out
   :answer_d: WatchOutWatchOut
   :answer_e: WatchOut2
   :correct: d
   :feedback_a: When you append strings together no extra spaces are added.
   :feedback_b: Don't forget the <code>* 2</code> part.  What does that do?
   :feedback_c: When you append strings together no extra spaces are added.
   :feedback_d: The <code>+</code> appends strings together and the <code>*</code> makes that many copies of the string appended together.
   :feedback_e: The <code>*</code> makes that many copies of the string appended together.
	
   What would the following code print?
	   
   :: 
   
      first = "Watch"
      next = 'Out'
      print ((first + next) * 2)
	   	  
.. note:: 

    Remember that strings must start and end with the same character. That character can be ``"`` or ``'``, but whatever you use as the starting character must match the ending character.  
    
Run the code below to see what type of error you get if you use a different starting character than ending character in a string.  Then try to fix the 2 errors in the code and run the code again.  You should get the same results as in CodeLens 1 (String_Manip) above.

.. activecode:: intro_data_string_error
    
    name = "Mark'
    start = 'My name is "
    combined = start + name
    print(len(combined))
    print(combined)
    print(name * 3)
    


