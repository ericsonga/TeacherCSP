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
	:prefix: csp-12-2-
	
.. highlight:: python
   :linenothreshold: 3

The if Statement
=====================
..	index::
	pair: if; statements
	single: logical expression
	single: Boolean expression
	single: Conditional expression
	
In Python, we test data and execute instructions if the test is true using an ``if`` statement.  An ``if`` statement includes a **logical expression** which is the 'test.'   A **logical expression** is one that is either true or false.  This is also called a **Boolean expression**.  An example of a **logical expression** is ``x < 3``. The ``if`` statement is followed by a colon ``if x < 3:`` and a **block of code**.  The colon (``:``) at the end of the ``if`` statement is required.  The **block of code**  includes the instructions to execute if the test is true.  The **block of code** includes all the statements that are indented following the ``if`` statement.  If the test is true, execute the statement or statements in the block following the ``if`` will be executed.  If the test isn't true (is false) then execution will skip the block following the if and continue with the next statement following the block after the ``if`` statement.  
    
Run the code below with x set to 0 and then change x to 4 and see how the output differs depending on the value of x.   
    
.. activecode:: If_Structure
    :tour_1: "Structural Tour"; 1: c0-line1; 2-3: c0-line2-3; 4: c0-line4;

    x = 0
    if x < 3:
    	print ("x is less than 3")
    print ("All done")
    
..	index::
	single: flowchart
	single: condition
    
The figure below is called a **flowchart**.  It shows the execution paths for a program.  The diamond shape contains the **logical expression** and shows the path 
that the execution takes if the logical expression (also called the **condition**) is true as well as the path if the logical expression is false.  Notice that it will only execute the statements in the 
indented block if the logical expression was true.  If the logical expression was false, execution will skip the code in the indented block and resume with the next statement.

.. figure:: Figures/decision.png
    :height: 350px
    :align: center
    :alt: Flowchart for an if statement
    :figclass: align-center

    Figure 3: Flow of execution for an if statement
    
.. mchoice:: 12_2_1_If_Structure
  :answer_a: line 3
  :answer_b: line 4
  :correct: b
  :feedback_a: Line 3 will only execute when x is less than 3.
  :feedback_b: Execution continues at the next statement beyond the block following the <code>if</code> when the logical expression is false.

   Given the code below, what line executes after line 2 executes? 
   
   :: 
   
     x = 4
     if x < 3:
         print ("x is less than 3")
     print ("All done")

 

