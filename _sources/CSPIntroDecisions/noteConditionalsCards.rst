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

..  qnum::
  :start: 1
  :prefix: csp-12-8-
  
.. highlight:: python
   :linenothreshold: 3

|bigteachernote| Teacher note: Conditionals with cards 
==================================

A misconception that students have about conditionals is that both the statements or blocks under the if
and ``else`` are executed each time. For instance:

.. sourcecode:: python

    if x < 2:
        print("Programming rules!")
    else:
        print("This is great!")

Some students think that if ``x`` is 1 when the above code is run, the computer will print Programming rules!” and then continue to the ``else`` and print “This is great!”. In fact, only one of the statements is ever printed, never both.

Code.org has a great “unplugged” activity called `Conditional with Cards <https://code.org/curriculum/course2/12/Teacher>`__ which can help students learn the “conditional” execution of code.

**Summary**

Two teams take turns drawing from a deck of cards. Based on conditions like the card’s suit, color, or value, the teams can gain or lose points, depending on the “program” being run at the time. The game ends when either team reaches a set number of points, or when you run out of cards.

**To prepare**

-  A deck of cards
-  A set of “programs” that are made up of ``if-else`` statements based on characteristics of a card. Here are a couple of examples *(warning: not real Python programs!)*:


.. sourcecode:: python

    if Card is Red: 
        Award YOUR team 1 point 
    else: 
        Award the OTHER team 1 point

.. sourcecode:: python

    if the Card's value < 5: 
       Deduct 2 points from YOUR team 
    else: 
        Deduct 2 points from the OTHER team

**Directions**

1. Split the class into two teams, say, Team A and Team B. (More fun: have them choose their own team names!)
2. Shuffle the cards and place the deck in the middle of the room.
3. Put a “program” up on the board for all to see.
4. Have the teams take turns drawing cards and “running” the program to see how many points they score each time (keep the score on the   board).
5. At different points in the game, change the program on the board. Do this several times, so students get practice with different types of conditionals.

**Wrap up questions**

-  What type of expressions can follow the ``if`` ? (Boolean expressions/logical expressions/true or false)
-  When is the code after the ``else`` executed? (If AND ONLY IF the condition is false)
