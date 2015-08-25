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
	:prefix: csp-3-4-

.. highlight:: java
   :linenothreshold: 4


How Expressions are Evaluated
===============================

The order that expressions are executed is the same as it is in math and is shown in the table below from highest precedence to lowest. If two symbols have the same precedence they are evaluated from left to right.   

+------------------------+----------------------------------------------------+
|Operator                | Name                                               |
+------------------------+----------------------------------------------------+
| -x                     | Negation                                           |
+------------------------+----------------------------------------------------+
| x * y, x / y, x % y    | Multiplication, Division, and Modulo               |
+------------------------+----------------------------------------------------+
| x + y, x - y           | Addition and subtraction                           |
+------------------------+----------------------------------------------------+

.. fillintheblank:: 3_4_1_Order1_fill

    .. blank:: 3_4_1_Order1
        :correct: ^-2$
        :feedback1: ('.*','Did you actually run the program?')
        
        What is printed when you click on the Run button in the code below? 

.. activecode:: Expression_Order1
    :nocodelens:
    
    result = 4 + -2 * 3
    print(result)
   
You can change the default order by adding parentheses around part of an expression.

.. fillintheblank:: 3_4_2_Order2_fill

    .. blank:: 3_4_1_Order2
        :correct: ^6$
        :feedback1: ('.*','Did you actually run the program?')

        What is printed when you click on the Run button in the code below? 

.. activecode:: Expression_Order2
    :nocodelens:
    
    result = (4 + -2) * 3
    print(result)

