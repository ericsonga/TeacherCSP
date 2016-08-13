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
	:prefix: csp-12-1-
	
.. highlight:: python
   :linenothreshold: 3


Making Decisions
==================

*Learning Objectives:*

- Write programs that make decisions.
- Introduce conditional execution with ``if`` statements.
- Give examples of logical expressions and relational operators.
- Introduce complex conditionals (with ``and``, ``or``, and ``not``).
- Understand programs with multiple ``if`` statements.
- Introduce ``if`` and ``else``.
- Understand common difficulties students have with conditionals.

We have discussed two major abilities that computers have.  Computers can name values.  Computers can repeat steps.  The third major ability that a computer has is the ability to make decisions.  We make decisions all the time.  Before we leave the house we may check to see if it will rain that day, and if it will, we bring an umbrella.

.. figure:: Figures/umbrella.jpg
    :height: 200px
    :align: center
    :alt: Picture of an umbrella
    :figclass: align-center

    Figure 1: An umbrella in the rain


Computers can also make decisions or take action when something is true.  More specifically, (1) a computer can *test data* and (2) a computer can *execute instructions* if that test is true.  The ability to test data and take actions on the result is what allows the computer to deal with input and take action on it (e.g., if the credit card is valid then charge the card), or deal with data from the world around (e.g., if I see a stop sign then stop.).

.. figure:: Figures/stop.jpg
    :height: 200px
    :align: center
    :alt: Picture of a stop sign
    :figclass: align-center

    Figure 2: Picture of a stop sign
    
..	index::
	single: conditional execution
	
The computer's ability to take action (execute some code) when something is true is also called **conditional execution**.  


