..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note
    
.. 	qnum::
	:start: 1
	:prefix: csp-16-10-
  
|bigteachernote| Teacher Note: The Rainfall Problem
=====================================================

..	index::
	pair: rainfall; research
	
The Rainfall Problem is perhaps the most famous problem in computer science education research.  Elliot Soloway invented it and had students at Yale University try it in 1983.  Only 14% of students in week 10 of their first semester could solve the problem correctly.  Only 36% of the students in the second course could do it.  Only 69% of Juniors and Seniors could do it.  Every study of this problem in the last 30 years has come up with the same result -- students find this to be a very hard problem.

Why?  Thinking about that gives us insights into what students find hard about programming:

- There are several different kinds of tests going on here.  Did we see a negative number?  Did we read any positive integers at all?  In the full version of the problem, students also have to check if they have reached the end of the data.

- There are two accumulators (a sum and a count), and they have to be used together -- and **only** if the integer is positive.

So that gives you a sense for what pace to expect from your students.  Two accumulators and three conditionals is enough that only 14% of Ivy League students can write the program after 10 weeks of undergraduate computer science class.  Notice how we dealt with the problem here -- we asked you to *assemble* the program out of *pieces* we already gave you.  That's already an easier task.  

Have your students write lots of small simple programs before you expect them to write more complicated programs.



