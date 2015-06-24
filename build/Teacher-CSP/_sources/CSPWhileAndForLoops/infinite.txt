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
	:prefix: csp-8-1-
	
.. highlight:: java
   :linenothreshold: 4
   
	
Loops - While and For
=======================

*Learning Objectives:*

- Introduce the concept of an *infinite loop*
- Use a ``while`` loop to repeat code.
- Compare and contrast ``while`` and ``for`` loops

..	index:
	single: while
	single: variable
	single: index variable
	single: infinite loop
	pair: statements; while
	pair: statements; for

Infinite Loops
================

Getting a computer to repeat is simple.  Getting it to *stop* can be tricky.  A simple way of getting a computer to repeat is to use a ``while`` loop.  A ``while`` loop includes a logical expression, and is followed by a block.  **AS LONG AS THE EXPRESSION IS TRUE**, the block of statements gets executed.

..	index::
	single: infinite loop
	pair: loop; infinite
	
So, here's a program that loops forever. 

.. sourcecode:: python

  	while 1 == 1:
  	    print("Looping")
  	    print("Forever")

Since ``1`` will always be equal to ``1``, the two ``print`` statements will just be repeated over and over and over again.  We call that an **infinite loop**, which means a loop that continues forever or until it is forced to stop. We ran this in a form of Python where he could stop the computer easily:

.. sourcecode:: python

 	>>> while 1==1:
 	        print ("Looping")
 	        print ("Forever")
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever

(We stopped the computer around this point.)

