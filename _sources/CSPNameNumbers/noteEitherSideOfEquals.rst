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
	:prefix: csp-3-7-

.. highlight:: java
   :linenothreshold: 4

|bigteachernote| Teacher Note: Names on either side of =
===========================================================================

..	index::
	pair: misconceptions; assignment
	single: assignment box vs value misconception

Notice that we can use a variable name on either side of the equal sign, ``=`` (the assignment operator). However, also notice that a variable name is treated differently when found on the left or the right of the equal sign .

For instance, consider this series of assignment statements:

.. activecode:: Assign1
   
    a = 5
    b = a + 1
    print(a)
    print(b)

If we think of a variable as a **box** that holds a *value*, the meaning of line 1 is fairly obvious: place the *value* 5 in the **box** labelled ``a``. In line 1, ``a`` stands for the **box** associated with the name ``a``.

In line 2, however, ``a`` is found on the right side of ``=`` . In this case, ``a`` no longer stands for the **box** labelled ``a`` , but rather, the *value* stored in the box labelled ``a`` . Therefore, ``a + 1`` in this case actually means ``5 + 1`` . In fact, line 2 is executed in 3 steps:

1. Replace ``a`` on the right of the ``=`` with the value stored in the    box labelled ``a`` (5, in this case)
2. Add 1 to that value (5 + 1)
3. Store the result (6) in the box labelled ``b``

Of course, the computer performs all these steps for you!

After the first two lines are executed, the print statements will show that ``a`` will contain 5, while ``b`` will contain 6.

Incrementing a variable
-----------------------

It’s important to understand the above steps to make sense of the following example. This is a common operation in which the value of a variable is *incremented* (it’s value is increased by 1):

.. activecode:: Assign2

    a = 5
    a = a + 1
    print(a)

Line 1 may be straightforward to interpret (assign 5 to the box labelled ``a`` ), but in line 2, ``a`` appears twice! This may prove to be confusing to some students. But armed with the above understanding, we can interpret line 2 as follows:

1. Replace ``a`` on the right of the ``=`` with the value stored in the    box labelled ``a`` (5, in this case)
2. Add 1 to that value (5 + 1)
3. Store the result (6) in the box labelled a

Run the above code to see what the value of the box labelled ``a`` is when it is printed.

Self check
~~~~~~~~~~

Consider this example:

.. sourcecode:: python

    distance = 924.7
    mpg = 35.5
    gallons = distance / mpg

.. parsonsprob:: Either_Side

    The following mixed-up boxes represent the steps that the computer performs to execute these lines. Drag the blocks from the left and put them in the correct order on the right.

    -----
    Assign 924.7 to the variable distance
    =====
    Assign 35.5 to the variable mpg
    =====
    Replace distance on the right of 
    the '=' with the value 924.7, and 
    replace mpg on the right of 
    the '=' with 35.5
    =====
    Perform this division: 924.7 / 35.5
    =====
    Assign the result of the division 
    (26.047887324) to the variable gallons

