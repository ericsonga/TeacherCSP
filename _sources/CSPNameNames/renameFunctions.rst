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
	:prefix: csp-6-8-
	
.. highlight:: java
   :linenothreshold: 4

Renaming Python's Functions
=============================

The functions ``abs`` and ``int`` are *names*.  They are *variables* whose values are a set of statements that achieve a goal.  Later on, we'll know enough code to write ``abs`` and ``int`` ourselves.  The important point right now is that ``abs`` and ``int`` are *names* for functions.  You can create several names that have the same value.  You can think of this like how a person can have both a name and a nickname.  In the program below we demonstrate that you can even create new names for Python functions.

.. activecode:: Rename_Internal
  :tour_1: "Line-by-line tour"; 1: funName-line1; 2: funName-line2; 3: funName-line3; 4: funName-line4; 5: funName-line5; 6: funName-line6;

  absolute = abs
  print("Absolute value of -5:")
  print(absolute(-5))
  noDecimal = int
  print("Integer part of of 34.2")
  print(noDecimal(34.2))

.. mchoicemf:: 6_8_1_Rename_Internal_Q1
   :answer_a: -16
   :answer_b: -16.789
   :answer_c: 16.789
   :answer_d: 16
   :correct: d
   :feedback_a: No, absolute will change the negative
   :feedback_b: No, the original number will change
   :feedback_c: No, noDecimal will remove the decimal part
   :feedback_d: Yes! Absolute will make it positive, and noDecimal will throw away the values after the decimal point leaving just the 16.
   
   If you add one more line to the above program, `print(noDecimal(absolute(-16.789)))`, what prints?
   
.. note::  

   This is the end of chapter 6.  Readers who are part of the teacher study should go to `https://www.surveymonkey.com/s/TeacherQ56 <https://www.surveymonkey.com/s/TeacherQ56>`_ and take the post test for chapters 5 and 6 before continuing on to chapter 7.


