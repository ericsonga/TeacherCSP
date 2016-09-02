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
    :prefix: csp-8-5-
    
.. highlight:: java
   :linenothreshold: 4


|bigteachernote| Teacher note: "Waiting" while
==================================================

Researchers have found that some students hold the following misconception: ``if`` statements "wait" for their conditional statement to become true. When that happens (at whichever point in the program), the corresponding block of code is executed.

This misconception might also appear in students' understanding of the ``while`` loop: the loop body is executed whenever its condition becomes true.

.. codelens:: WaitingWhile1

    size = 10
    while size < 5:
        size = size + 1
        print(size)

    size = 0

In the above example, the student might predict that the ``while`` loop will execute as soon as ``size`` is set to 0 at the end of the program, displaying the following output:

::

    1
    2
    3
    4

On the contrary, the ``while`` loop is never executed in the example, since ``size`` is not less than 5 at the point of evaluation of its conditional statement. The loop is never returned to even after ``size`` is set to 0.

To find out if students hold these misconceptions, show these program examples and ask them to predict the output. Alternatively, observe them as they trace through these examples by hand line-by-line. Then, have them compare their predictions to results from tracing the code using CodeLens, and, if different, ask them to try and explain why. Emphasize the sequential flow of execution through the program.

Let’s say that you showed Sam this program that simulated a thermostat of an air conditioner:

.. sourcecode:: python

    targetTemperature = 75
    roomTemperature = 90
    while roomTemperature > targetTemperature:
        roomTemperature = roomTemperature - 2

    targetTemperature = 64
    print(roomTemperature)    



.. mchoice:: 8_5_1_Diagnosing_While_Q1
  :answer_a: 74
  :answer_b: 64
  :answer_c: 75
  :correct: b
  :feedback_a: This is the actual value to be printed. If Sam predicted 74, then he has a correct understanding of the while loop.
  :feedback_b: If Sam held this misconception, he would predict that the while loop would run twice: the second time when targetTemperature is set to 64.
  :feedback_c: If Sam chose this option, he might have a correct understanding of the while loop, but his arithmetic will be slightly off: since the program reduces roomTemperature by 2 each time, and since roomTemperature starts at 90, an even number, we expect the final roomTemperature value to be an even number as well, not 75.

   If Sam had the “waiting” ``while`` misconception, what would he predict the output would be?