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
	:prefix: csp-6-4-
	
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teacher Note: A procedure is not executed when it is defined
=============================================================================

*Note: this misconception applies both to procedures and functions*


**Misconception**
Some students may think that the indented lines of code below a procedure or function definition (called the *body*), are executed when the procedure or function is defined, rather than when the procedure or function is called.

**Correct understanding** A procedure is not executed when it is defined. The ``def`` keyword merely instructs the computer to remember that the function name corresponds to the indented lines of code below it. Stated another way, ``def`` instructs the computer to match the procedure or function name with the procedure or function body.

It is only when the procedure is called (the name is used without the def keyword) that the procedure body is executed. Here’s an example of a procedure definition followed by a procedure call:

.. activecode:: FunDef1

        def greetJohn():  # procedure definition: body not executed yet!
            name = "John"
            print("Good day, " + name + "!")
            
        greetJohn()       # procedure call: body is executed at this point

**How to tell if a student has this misconception** Show the student a procedure definition with some print statements in the procedure body, but omit the code that calls the procedure. Ask the student to describe the output of the code. A student that has this misconception s/he will predict that the print statements will be executed, even if there is no call to the procedure yet.

