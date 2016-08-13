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
	:prefix: csp-3-2-

.. highlight:: java
   :linenothreshold: 4



Expressions
=============

..	index::
	single: expressions
	single: arithmetic expressions

The *right hand* side of the assignment statement doesn't have to be a value.  It can be *an arithmetic expression*, like ``2*2``.  The expression will be evaluated and the result from the expression will be stored in the variable.  

.. fillintheblank:: 3_2_1_Mult_fill

    .. blank:: 3_2_1_Mult
        :correct: ^4$
        :feedback1: ('.*','Did you actually run the program?')
 
        What will be printed when you click on the Run button in the code below? 

.. activecode:: Expression_Mult
    :tour_1: "Line-by-line Tour"; 1: ex1-line1; 2: ex1-line2; 
    :nocodelens:
    
    result = 2 * 2
    print(result)
    
|bigteachernote| Teacher Note: Assignment Dyslexia
----------------------------------------------------

..	index::
	single: assignment dyslexia

Some students will write the expression on the left side of the ``=`` and the variable name on the right side (``2 * 2 = a``).  This is called assignment dyslexia and will result in an error.  The variable name *always* has to be on the left side of the ``=`` in an assignment.  

Integer Division
-------------------

..	index::
	single: integer division
   
You can use all the standard mathematical symbols.

.. fillintheblank:: 3_2_2_Div_fill

    .. blank:: 3_2_2_Div
        :correct: ^0.333333333333$
        :feedback1: ('.*','Did you actually run the program?')

        What will be printed when you click on the Run button in the code below? 
   
.. activecode:: Expression_Div
    :tour_1: "Line-by-line Tour"; 1: ex2-line1; 2: ex1-line2; 
    :nocodelens:
    
    result = 1 / 3
    print(result)

.. note::
   This book is using Python 3.0 which returns a decimal value from an integer calculation like ``1 / 3``.  If we had executed ``1 / 3`` in an older Python development environment it would have printed ``0`` instead.  In many languages if you are only using integers in calculations (whole numbers - like -3,65, -39028, 602939) the result will also be an integer and the factional part (part after the decimal point) is thrown away. In those environments it is important to use decimal values (like ``1.0 / 2``, ``1 / 2.0``, or ``1.0 / 2.0``) if you want a decimal result.
   
Modulo 
---------

..	index::
	single: modulo
	single: remainder
   
There are also some symbols that may be used in ways that you don't expect.  

.. fillintheblank:: 3_2_3_Mod_fill

    .. blank:: 3_2_3_Mod
        :correct: ^0$
        :feedback1: ('.*','Did you actually run the program?')

        What will be printed when you click on the Run button in the code below? 
   
.. activecode:: Expression_Mod
    :tour_1: "Line-by-line Tour"; 1: ex3-line1; 2: ex1-line2; 
    :nocodelens:
    
    result = 4 % 2
    print(result)

You may not be familiar with the **modulo** (remainder) operator ``%``.  It returns the remainder when you divide the first number by the second.  You probably did this long ago when you were learning long division.  In the case of ``4 % 2``, ``2`` goes into ``4`` two times with a remainder of ``0``.  The result of ``5 % 2`` would be ``1`` since ``2`` goes into ``5``, two times with a remainder of ``1``. In fact you can check if the result of ``X % 2`` is equal to ``1`` to see if ``X`` is odd and if the result of ``X % 2`` is equal to ``0`` then ``X`` is even.

.. figure:: Figures/mod-py.png
    :width: 150px
    :align: center
    :figclass: align-center
    
    Figure 3: Long division showing the whole number result and the remainder
    
.. note::
   The result of ``x % y`` when ``x`` is smaller than ``y`` is always ``x``.  The value ``y`` can't go into ``x`` at all, since ``x`` is smaller than ``y``, so the result is just ``x``.  So if you see ``2 % 3`` the result is ``2``.  Edit the code above to try this for yourself.  Change the code to ``result = 2 % 3`` and see what that prints when it is run.

