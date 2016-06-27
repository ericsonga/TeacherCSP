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
    :prefix: csp-12-3-
    
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teacher note: "Waiting" if
===========================================

Researchers have found that some students hold the following misconception: ``if`` statements "wait" for their conditional statement to become true. When that happens (at whichever point in the program), the corresponding block of code is executed.

For instance, consider this program:

.. codelens:: WaitingIf1

    size = 0
    if size == 5:
        print("Hello")

    for i in [1, 2, 3, 4, 5]:
        size = size + 1
        print(size)

If a student understands this correctly, she would say that since ``size`` is not equal to 5 when the ``if`` statement is evaluated, "Hello" is never printed. The program proceeds to execute the ``for`` loop and never returns to the ``if`` statement to evaluate that again. Step through the above code using CodeLens to see that the ``if`` statement is never executed.

A student who holds the above misconception, however, would say that after ``size`` becomes 5 at the end of the loop, the ``if`` statement (which had been "waiting" all this time) would see that its condition would now evaluate to true. "Hello" would then be printed.

In this case, the student fails to see that each line of the program is executed in sequence, one line at a time. Instead, she views all lines of the program as being active all at once, monitoring the status of the variables constantly.

Compare the previous program to the following example, in which the *intended* behavior is to display “Hello” when ``size`` becomes 5:

.. codelens:: WaitingIf2

    size = 0
    for i in [1, 2, 3, 4, 5]:
        size = size + 1
        print(size)
        if size == 5:
            print("Hello")


To find out if students hold this misconception, show these program examples and ask them to predict the output. Alternatively, observe them as they trace through these examples by hand line-by-line. Then, have them compare their predictions to results from tracing the code using CodeLens, and, if different, ask them to try and explain why. Emphasize the sequential flow of execution through the program.