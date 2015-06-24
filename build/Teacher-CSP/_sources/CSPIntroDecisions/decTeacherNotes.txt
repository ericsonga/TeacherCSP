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
	:prefix: csp-12-8-
	
.. highlight:: python
   :linenothreshold: 3
     
|bigteachernote| Delaying the else
==========================================

We don't recommend that you require students to use ``else`` right away.  It actually makes code **much** harder for students to *read*.  Using an ``else`` hides away the condition when the ``else`` block would execute.  Beginning students are having enough trouble just reading the code and making sense of it.  Using an ``else`` hides away clues to how the program is working.  Studies show that making the test *explicit* makes it **ten times** easier for beginning students to read programs with ``if`` statements.  

To do a something like an ``else`` using two ``if`` statements, use a `not`.

.. activeCode:: if_and_not_if
     :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c3-line2-3; 4-5: c6-line4-5; 6: c1-line6; 7-9: c3f-line7-9;

     weight = 0.5
     if weight < 1:
         price = 1.45
     if not weight < 1: 
         price = 1.15
     total = weight * price
     print(weight)
     print(price)
     print(total)
 

|bigteachernote| Sneak up on and and or
======================================================

Students have a difficult time with logical expressions.  It's probably just a matter of less experience with them.  They do a lot with arithmetic expressions, but *expressions whose value is true or false* are much less common in mathematics.

In particular, expressions with *multiple* logical expressions, combined with ``and`` and ``or``, are challenging for students.  There is some research that shows that the more logical expressions in the program, the more difficult (in terms of time to understand it, ability to read or modify the program) it is for students.

Don't ask students to do much with ``and`` and ``or`` to start.  Give them a lot of experience with simple logical expressions, before requiring them to use ``and`` and ``or``.


|bigteachernote| Teacher Note: Confusing while and if
==========================================================

A ``while`` loop and an ``if`` loop **look** almost the same.  They each have a logical expression, and a block of instructions underneath them.  

Students often get them confused.  Some key distinctions to make to students:

- An ``if`` block executes only once.  It does the test, then executes the instructions indented underneath *once*.

- A ``while`` block executes **repeatedly** *as long as the expression is true*.  The body of the loop can be executed *many* times.

When you show students examples of ``while`` loops, make sure that you choose examples where the body of the loop gets executed several times, to show a difference from ``if``.  When you trace the program, trace more than one iteration through the body of the loop, to emphasize the multiple times.
