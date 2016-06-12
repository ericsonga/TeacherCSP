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
	:prefix: csp-8-6-
	
.. highlight:: java
   :linenothreshold: 4

	
|bigteachernote| Teacher Note: for loops are more natural
================================================================

Several researchers have studied how people "naturally" describe programs.  In one study, students as young as middle school are shown videos of someone playing a game like "Pokemon" then asked:

	"Imagine that you are going to program a computer to make this video game.  What do you think you would say to the computer?"

Participants rarely specify iteration like in a ``while`` loop.  They often say things like "For all the folders, I would..." or "For each of the characters, do this..."  Doing something "for all" is pretty common.  As we have seen, we can use ``for`` loops just like that, e.g., *for each item in a list*.  In general, ``for`` loops are closer to how people naturally talk about looping.

But computer science students often make an economic argument to themselves.

	"A ``while`` loop can do everything that a ``for`` loop can, and is more flexible.  I'll just learn that."

Mark Guzdial, one of the authors of this book, used to teach a 2nd year undergraduate course on *Object-oriented Design*.  He wanted to know how much programming they knew before we got started.  One year, he gave them the challenge of writing the program to print the times table, just as you just saw ealier.  With a ``for`` loop, it's three lines of code.  Out of 75 students, only 15 used a ``for`` loop.  *Every* other student used a ``while`` loop.  Using a ``while`` loop is more lines of code, and more opportunities for error. (And many of the students did make errors.)  But they were more *comfortable* with the ``while`` loop, because that's what they had used the most.

Start out using the ``for`` loop in your classes as we have done in the prior chapter.  It will be easier and more natural for students. 

