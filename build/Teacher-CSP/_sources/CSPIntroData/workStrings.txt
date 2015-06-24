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
Strings start with single quotes or double quotes.  You can actually do some simple "arithmetic" with strings using ``+`` and ``*`` as shown below. You can also get the length of any collection (including strings) with the ``len`` function.

.. codelens:: String_Manip
  :showoutput:

  name = "Mark"
  start = 'My name is '
  combined = start + name
  print(len(combined))
  print(combined)
  print(name * 3)

.. mchoicema:: 16_2_1_Str_Combine
		  :answer_a: start+name
		  :answer_b: start+name+name+name
		  :answer_c: start + (3 * name)
		  :answer_d: start + 3 * name
		  :correct: b,c,d
		  :feedback_a: No, this just generates: My name is Mark
		  :feedback_b: Yes, this will work. Could you also use multiplication?
		  :feedback_c: Yes, this will work, but multiplication is processed before addition, so you do not have to have parentheses.
		  :feedback_d: Yes, this will work just fine.

	   	  If we wanted to add one line to the above to print "My name is MarkMarkMark", which one of these would do it? Choose all that are correct.
	   	  


