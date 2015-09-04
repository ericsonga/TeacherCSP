..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/apple.jpg
    :width: 30px
    :align: top
    :alt: teacher note
    
.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |codelensfirst| image:: Figures/codelens-first.png
    :height: 20px
    :align: top
    :alt: move to first button

.. |codelensback| image:: Figures/codelens-back.png
    :height: 20px
    :align: top
    :alt: back button

.. |codelensfwd| image:: Figures/codelens-forward.png
    :height: 20px
    :align: top
    :alt: forward (next) button

.. |codelenslast| image:: Figures/codelens-last.png
    :height: 20px
    :align: top
    :alt: move to last button
    
.. 	qnum::
	:start: 1
	:prefix: csp-3-8-

.. highlight:: java
   :linenothreshold: 4

|bigteachernote| Teacher Note: Misconceptions
======================================================

..	index::
	pair: misconceptions; assignment
	single: assignment move misconception
	single: assignment relationship misconception

There is a lot of research evidence that assignment is a difficult topic for students who are first learning to program.  `In a study of professional graphic designers who had taught themselves to program <http://doi.acm.org/10.1145/1753326.1753430>`_, the assignment statement was rated the top most difficult programming statement to learn.  Why is that?  

One reason may be because assignment requires the programmer to be *consistent* in understanding and predicting what happens in a program.  Assignment is always the *value on the right* gets copied to the space (in the computer's memory) named by *the variable on the left*.  `Researchers at Middlesex University in England <http://www.eis.mdx.ac.uk/research/PhDArea/saeed/>`_ found that a critical predictor of success in programming is to see that assignment **always** does the same thing 

**How do students get assignment wrong?**   Here are three ways.  One is that they see assignment as being a *move* of the value (rather than a *copy*).  So, they think that after ``var1 = var2`` the variable ``var1`` has the value from ``var2`` and the variable ``var2`` has a value of nothing or zero.

**Click on the right arrow below to play the following video.**
   
.. video:: assignment_zero
   :controls:
   :thumb: ../_static/video-misconception-zeroing.png

   http://ice-web.cc.gatech.edu/ce21/1/static/video/assignment-zeroed-small.mov
   http://ice-web.cc.gatech.edu/ce21/1/static/video/assignment-zeroed-small.webm  

A second model, which may be more common, is that they see assignment as a *relationship*.   Once ``var1 = var2`` then any change to ``var2`` will automatically change ``var1``.  The problem here is that the student doesn't see the assignment as an *action*.  If a student doesn't see the assignment as an action, it's hard to understand why the *ordering* of statements is important.

.. video:: assignment_relationship
   :controls:
   :thumb: ../_static/video-misconception-relationship.png

   http://ice-web.cc.gatech.edu/ce21/1/static/video/assignment-relationship-small.mov
   http://ice-web.cc.gatech.edu/ce21/1/static/video/assignment-relationship-small.webm 
   
A third problem is that some students have *assignment dyslexia*, which means that instead of writing the assignment with the variable name on the left side of the ``=`` and the value on the right, they reverse it as shown below.    


:: 

   7 = daysInWeek
   
The computer sees the above assignment statement as an attempt to change what 7 means, and won't allow it.  It will cause an error when you try to run it.  

**How do we help students get assignments right?**  Have students trace programs with assignments, where they draw values in boxes.  Watch what they do, and try to be aware of their model for how assignment works.  If they have one of these other models, try some of the examples in this section -- by tracing, and then on the computer.  Get students to see where their model doesn't accurately capture what the computer is doing.

Let's say that you showed Sam this program:

.. sourcecode:: python

	number2 = 32
	number1 = number2
	number2 = 17

Then asked Sam, "What's the value for the variable `number1`?"

.. mchoice:: 3_8_1_Diagnosing_Assignment_Q1
  :answer_a: Sam may see assignment as a move.
  :answer_b: Sam may see assignment as a copy.
  :answer_c: Sam may see assignment as a relationship.
  :correct: c
  :feedback_a: Assignment-as-move says that number1 is 32 and number2 has 17, but number2 was empty or zero after number1 = number2
  :feedback_b: Assignment really is a copy, so that's not a misconception.  Assignment-as-copy wouldn't lead to number1 being 17.
  :feedback_c: If Sam thinks changing number2 changes number1, Sam may misunderstand assignment as creating a relationship.

   If the answer was `17`, Sam might have what kind of misconception?


