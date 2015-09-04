..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

..  shortname:: Chapter2: What can Computers Do?
..  description:: Describes what a computer can do.

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-2-2-


Turing Machines
==================================

..	index::
	single: Turing, Alan
	single: Turing Machine

The idea for a computer was first described in 1936, over a dozen years before the first electronic computer was ever built.  `Alan Turing <http://en.wikipedia.org/wiki/Alan_Turing>`_, a brilliant mathematician, was trying to answer a question that mathematicians were struggling with at the beginning of the 20th century, "What are the limits of mathematics?  What can be computed using mathematics, and what truths can't be computed?"  Turing defined a device (a `Turing Machine <http://en.wikipedia.org/wiki/Turing_machine>`_) that answered that question: *Anything that is possible to mathematically compute could be programmed on a Turing Machine.* 

.. figure:: Figures/Alan_Turing_photo.jpg
    :width: 200px
    :align: center
    :alt: A Photo of Alan Turing 
    :figclass: align-center
        
    Figure 2: Photo of Alan Turing
    
.. mchoice:: 2_2_1_Turing_Q1
		   :answer_a: He occasionally ran 40 miles to London for meetings.
		   :answer_b: He proposed the Turing Test to decide if a computer was intelligent.   
		   :answer_c: He worked on breaking Enigma ciphers in World War II.   
		   :answer_d: He went to school in Oxford, England. 
		   :correct: d
		   :feedback_a: This is true.  He was a talented runner and even tried out for the olympics.
		   :feedback_b: This is true.  He said that if a computer could fool a person into thinking it was a person, that that computer was intelligent.  
		   :feedback_c: This is true.  Winston Churchill said that Alan Turing made the single biggest contribution to winning World War II.   
		   :feedback_d: This is false.  He attended King's College at Cambridge and Princeton University.

		   Use the following link to learn more about `Alan Turing <http://en.wikipedia.org/wiki/Alan_Turing>`_.  Which of the following is **false** about him?

Today's computers work differently than Turing's machine, but are mathematically equivalent.  *Anything that is possible to compute can be programmed on any modern electronic computer.*  **ALL** computers, from the ones in your microwave to the super-duper computers that predict the weather all have the same basic abilities.  Click on the following link to learn more about `how Turing Machines work. <http://www.storyofmathematics.com/20th_turing.html>`_

.. figure:: Figures/turing_machine.gif
    :width: 300px
    :align: center
    :alt: A Turing Machine 
    :figclass: align-center
        
    Figure 3: Figure of a Turing Machine

The meaning of that statement is huge.  For example, it means that it's *possible* to run any program on any computer, but it might mean that you have to do a lot of programming to make it work.  But it doesn't mean that we can solve *all* problems on any computer.  One of the important things that Turing proved is that **some problems can't be solved by computers at all, ever**.

Turing's machine didn't actually know anything about numbers, which might be surprising for a device that could do any mathematical computation.  Instead, it could simply make marks on a piece of paper tape, and then *count* those marks to be able to do mathematics.  In reality, electronic computers are just as dumb.  They *count* using patterns of voltages on wires (e.g., "off,on,off,off" is a representation of the number *4* in binary).  But we don't really want to deal with patterns like this, so people have already programmed basic mathematical operations into the computer.  

..	index::
	single: abstraction
	
When you work with a computer, you have all kinds of abilities already built-in by others.  Your computer already knows how to deal with numbers and mathematical operations, and lots of other things as well.  At the basic level, though, even the biggest, most powerful, most expensive supercomputer cannot solve problems better than a Turing Machine. **All computers are exactly the same in terms of what they can do.** 

.. mchoice:: 2_2_2_Computers_Q1
		   :answer_a: There were female computers.
		   :answer_b: You can make a computer with Tinkertoys.     
		   :answer_c: Computers can solve any problem.   
		   :answer_d: Computers use sequences of voltages on wires to represent numbers.   
		   :correct: c
		   :feedback_a: This is true.  Look for information on the Harvard Computers and Secret Rosies.  
		   :feedback_b: This is true.  Some students at MIT did this in the 1980s.   
		   :feedback_c: This is false.  Turing provide that there are problems computers cannot solve.  
		   :feedback_d: This is true.  Computers use patterns of on and off voltages to represent numbers.  

		   Which of the following is **false** about computers?
	
..	index::
	single: programming language
	pair: programming; languages
	
A **programming language** (like *Java* or *Python*) which is a language that allows you to tell a computer what to do, can do anything that a Turing Machine can do (no more or less).  A programming tool like `Alice <http://www.alice.org>`_ or `Scratch <http://scratch.mit.edu>`_ can do *most* of what a Turing Machine can do, but typically, not everything.  **You can program anything that a Turing Machine can do in Python .**




