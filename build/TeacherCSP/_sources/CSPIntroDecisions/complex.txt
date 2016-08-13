..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. 	qnum::
	:start: 1
	:prefix: csp-12-5-
	
.. highlight:: python
   :linenothreshold: 3

Complex Conditionals (and, or, and not)
=========================================

.. 	index::
	single: and
	single: or
	pair: logical operators; and
	pair: logical operators; or
	pair: logical operators; not
	
We can also use ``and`` and ``or`` to join several logical expressions together as shown in the table below.  An ``or`` joining two expressions means that if *either* of the expressions is true, the whole expression is true.  An ``and`` used to join two expressions is only true if *both* expressions are true.  A ``not`` negates the logical value that follows it.  If it was true, then a ``not`` changes the result to false.  If it was false, the ``not`` changes the result to true.

====================        ================
Expression                  Meaning
====================        ================
(a < b) or (c < d)          The whole expression is true if a is less than b or c is less than d. 
--------------------        ----------------
(a < b) and (c < d)         The whole expression is true if a is less than b **AND** *ALSO* c is less than d.  
--------------------        ----------------
not a < b                   Only true if a is actually greater than or equal to b.  The logical expression ``not a < b`` is the same as ``a >= b``.
====================        ================

A common use of ``and`` is to check that a value is in a range between a minimum value and a maximum value.  For example, if you have asked a person to pick a number between 1 and 10 you can check for this using the following.

.. activecode:: Example_With_And
  :tour_1: "Structural Tour"; 1: and1-line1; 2-3: and1-line2-3; 4: and1-line4;

  x = 3
  if x >= 1 and x <= 10:
      print ("x is a number from 1 to 10")
  print ("All done")
  
.. mchoice:: 12_5_1_and1
  :answer_a: 1 to 10
  :answer_b: 0 to 9
  :answer_c: 1 to 9
  :correct: c
  :feedback_a: This would be true if the second expression was x <= 10. 
  :feedback_b: This would be true if the first logical expression was x >= 0.
  :feedback_c: The "condition true" will only be printed when x is greater than 0 and less than 10 so this is the range from 1 to 9.

   Given the code below, what describes the values of x that will cause the code to print "condition true"?
   
   :: 
   
     if x > 0 and x < 10:
         print ("condition true")
     print ("All done")
    
A common use of ``or`` is to check if either one of two conditions are true.  For example, a parent has told a teen that she can go out if she has cleaned her room or finished her homework.  If either of these is true she can go out.  In Python a value of ``0`` means false and any non-zero value is true, but ``1`` is often used for true.  

.. activecode:: Example_With_Or
  :tour_1: "Structural Tour"; 1: and2-line1; 2: and2-line2; 3-4: and2-line3-4; 5: and2-line5;

  cleanedRoom = 1
  finishedHomework = 0
  if cleanedRoom or finishedHomework:
      print ("You can go out!")
  print ("All done")
  
.. mchoice:: 12_5_2_or1
  :answer_a: all values of x
  :answer_b: 1 to 9
  :answer_c: 0 to 9
  :correct: a
  :feedback_a: This will be true if x is greater than 0 or less than 10.  This covers all possible values of x.  
  :feedback_b: This would be true if the logical expressions were joined with and instead of or.
  :feedback_c: This would be true if the logical expressions were jointed with and instead of or and if the first logical expression was x >= 0.

   Given the code below, what describes the values of x that will cause the code to print "condition true"?
   
   :: 
   
     if x > 0 or x < 10:
         print ("condition true")
     print ("All done")

