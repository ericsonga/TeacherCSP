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
	:prefix: csp-6-2-
	
.. highlight:: java
   :linenothreshold: 4

Naming Procedures and Functions
========================================

..	index::
	single: procedure
	pair: programming; procedure
	
..	index::
	single: function
	pair: programming; function	
	
We've already seen how we can use names to represent numbers (both integers like ``3`` and ``-325`` and decimal numbers like ``2.4`` and ``-322.9392``), strings (like ``"Hi There"``), turtles, and images.  When we do calculations using the names, the computer will look up the value for each name, and then use the value in the calculation.  We can also name a sequence of statements and then ask the computer to run that sequence whenever we use that name.  This is similar to asking someone to do a dance that they know, like the `Macarena <http://en.wikipedia.org/wiki/Macarena_(song)>`_ or `Salsa <http://en.wikipedia.org/wiki/Salsa_(dance)>`_. Once you know the dance you can do the steps.    

.. figure:: Figures/salsaDancer.jpg
    :height: 100px
    :align: center
    :alt: a women dancing Salsa
    :figclass: align-center

    Figure 1: A Salsa dancer
    
In programming there are two different terms used for a named sequence of statements: **procedure** and **function**.  A **procedure** accomplishes some task or makes something happen, but doesn't return anything. A **function** returns a result. Many procedures and functions are built into Python.  The function ``abs`` returns the absolute value of its input.  The function ``int`` takes a decimal number as input and returns just the integer part.

.. activecode:: Functions
  :tour_1: "Line by line tour"; 1: fun-line1; 2: fun-line2; 3: fun-line3; 4: fun-line4;

  print("Absolute value of -5:")
  print(abs(-5))
  print("Integer part of 34.2")
  print(int(34.2))
  
.. mchoicemf:: 6_2_1_Functions_Q1
   :answer_a: -16
   :answer_b: -16.789
   :answer_c: 16.789
   :answer_d: 16
   :correct: d
   :feedback_a: The function abs will change the negative.
   :feedback_b: The original number will change.
   :feedback_c: The function int will remove the decimal part.
   :feedback_d: The function abs will make it positive, and the function int will cut it down to 16.
   
   What do you think `print(int(abs(-16.789)))`, prints?

