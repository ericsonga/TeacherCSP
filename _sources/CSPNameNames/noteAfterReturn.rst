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
	:prefix: csp-6-5-
	
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teacher Note: Statements after return are not executed
=======================================================================

Another common misconception students have about functions is that the entire body of the function is executed from top to bottom, regardless of where the ``return`` statement appears in the function body.

The following program illustrates this misconception. Before running the below example, answer this question: how many times is “4” printed?

.. activecode:: FunDef1

    def double(x):
        result = x * 2
        return result
        print(result)
        
    dbl = double(2)
    print(dbl)

A student that had this misconception would predict that “4” would be printed twice. In fact, in this program, “4” would only be printed once. Run the code to see for yourself.

**Correct understanding** We understand that the ``return`` statement identifies the value to be returned by the function. What students sometimes miss is that, additionally, the ``return`` statement specifies the point where the function “exits”, or where it ends execution. In the above program then, the function stops executing at line 3, skipping that ``print`` function call at line 4. That is, the function “exits” at line 3.

How would you change the above example to print “4” twice?

**How to tell if a student has this misconception** ``return`` statements are commonly at the end of functions, although they do appear in the middle of functions in some cases, discussed later in the book. At this point, however, watch out for code that includes a ``return`` statement in the middle of a function. Students who do this may have this misconception.

Similarly, some students might be puzzled that certain lines in their function do not seem to execute when they expect them to. There might be a misplaced ``return`` statement before these lines.

Remember: the function exits at the ``return`` statement. Any statements that come after a ``return`` are not executed.
