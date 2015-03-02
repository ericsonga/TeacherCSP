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
	:prefix: csp-3-3-

.. highlight:: java
   :linenothreshold: 4



Summary of Expression Types
============================

+------------+--------------------------------------------------------------------------------------------+
| Expression | Arithmetic meaning                                                                         |
+------------+--------------------------------------------------------------------------------------------+
| 1 + 2      | Addition, the result is 3                                                                  |
+------------+--------------------------------------------------------------------------------------------+
| 3 * 4      | Multiplication, the result is 12                                                           |
+------------+--------------------------------------------------------------------------------------------+
| 1 / 3      | Integer division, the result is 0 in typical Python environments, but 0.333333333333 here  |
+------------+--------------------------------------------------------------------------------------------+
| 2.0 / 4.0  | Division, the result is 0.5, since you are using decimal numbers in the calculation        |
+------------+--------------------------------------------------------------------------------------------+
| 2 % 3      | Modulo (remainder), the result is 2                                                        |
+------------+--------------------------------------------------------------------------------------------+
| -1         | Negation, the result is -1                                                                 |
+------------+--------------------------------------------------------------------------------------------+

.. mchoicemf:: 3_3_1_intDiv_Q1
   :answer_a: 0
   :answer_b: 1
   :answer_c: 0.75
   :answer_d: 0.25
   :correct: c
   :feedback_a: If the two values are both integers (whole numbers) you will normally get an integer (whole number) result in most Python environments.  But, since in the eBook we translate the Python to JavaScript it gives a decimal result.
   :feedback_b: This would be correct if the result was rounded up before the values after the decimal point were thrown away, but it does not do this.   
   :feedback_c: While this isn't the what most Pyton development environments would return, in this book we are translating the Python to JavaScript so it will give a decimal result.
   :feedback_d: This would be correct if it was <code>1 / 4</code>, <code>1.0 / 4</code>, or <code>1 / 4.0</code>

   What is the result of ``3 / 4``?
    
.. mchoicemf:: 3_3_2_mod_Q1
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: d
   :feedback_a: This would be correct if it was <code>18 % 2</code>, but what is the remainder of 18 divided by 5? 
   :feedback_b: This would be correct if it was <code>18 % 17</code>, since 17 goes into 18 one time and the remainder is 18 - 17 = 1.  
   :feedback_c: What is the highest multiple of 5 that is less than or equal to 18? The remainder is 18 - that number.
   :feedback_d: The reminder is 3 since 5 goes into 18 three times (15) and 18 - 15 = 3.  

   What is the result of ``18 % 5``?
   
.. mchoicemf:: 3_3_3_mod_Q2
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 6
   :correct: c
   :feedback_a: This would be correct if it was <code>6 % 2</code>.  
   :feedback_b: This would be correct if it was some odd number divided by 2, but it is not.
   :feedback_c: 6 goes into 2 zero times with 2 left over.  
   :feedback_d: If you have a larger number divided by a smaller number the remainder is always the smaller number. 

   What is the result of ``2 % 6``?

