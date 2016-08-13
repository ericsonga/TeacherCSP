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
	:prefix: csp-3-9-

.. highlight:: java
   :linenothreshold: 4

Figuring out an Invoice
====================================

We can use variables to solve problems like those we might solve in a spreadsheet.  Imagine that you had a spreadsheet with an invoice for an office supply company.

.. figure:: Figures/invoice.png
    :width: 600px
    :align: center
    :alt: a spreadsheet
    :figclass: align-center
    
    Figure 3: A spreadsheet with order information  

Here's a program to compute the total price for the invoice.  Be sure to click |audiobutton| to understand what's happening here.

.. activecode:: Invoice1
    :tour_1: "Line by line tour"; 1: inv-line1; 2: inv-line2; 3: inv-line3; 4: inv-line4; 5: inv-line5; 6: inv-line6; 7: inv-line7; 8: inv-line8; 

    quantity1 = 2
    unitPrice1 = 7.56
    total1 = quantity1 * unitPrice1
    quantity2 = 4
    unitPrice2 = 4.71
    total2 = quantity2 * unitPrice2
    invoiceTotal = total1 + total2
    print(invoiceTotal)

.. mchoice:: 3_9_1_Invoice1_Q1
		   :answer_a: 7
		   :answer_b: 6
		   :answer_c: 5
		   :answer_d: 2
		   :correct: a
		   :feedback_a: Yes, quantity1, unitPrice1, total1, quantity2, unitPrice2, total2, invoiceTotal.
		   :feedback_b: There are three variables per line, two lines, and one total.
		   :feedback_c: There are three variables per line, two lines, and one total.
		   :feedback_d: There are three variables per line, two lines, and one total.

		   How many variables are in this program?

We don't really have to create new variables ``quantity2`` and ``unitPrice2``.  We only use those to compute the total for the line, and then we could reuse those variable names.

.. codelens:: Invoice2

  quantity = 2
  unitPrice = 7.56
  total1 = quantity * unitPrice
  quantity = 4
  unitPrice = 4.71
  total2 = quantity * unitPrice
  invoiceTotal = total1 + total2
  print(invoiceTotal)

.. mchoice:: 3_9_2_Invoice2_Q1
		   :answer_a: 7
		   :answer_b: 6
		   :answer_c: 5
		   :answer_d: 2
		   :correct: c
		   :feedback_a: We have two fewer variables now.
		   :feedback_b: We have a total for each line (two), a quantity, a unitPrice, and an invoiceTotal.
		   :feedback_c: The variables are quantity, unitPrice, total1, total2, and invoiceTotal. 
		   :feedback_d: We have a total for each line (two), a quantity, a unitPrice, and an invoiceTotal.

		   How many variables are in this program?
		   
.. Note::
   It is best to use variable names that make sense like ``invoiceTotal`` and ``quantity`` instead of names that don't make any sense like ``thisVariableIsMyFriend`` and ``Fred``.  The name should help you remember what the variable is representing.  

Let's say that apples are $0.40 apiece, and pears are $0.65 apiece.  Modify the program below to calculate the total cost.

.. activecode:: Complete_Assignment

   apples = 4
   pears = 3
   totalCost =
   print(totalCost)

You are welcome to try out the following answers by copying and pasting them into the program above before answering this question:

.. mchoice:: 3_9_3_Make_An_Assignment_Q1
  :answer_a: totalCost = apples + pears
  :answer_b: totalCost = (0.4 * apples) + (0.65 * pears)
  :answer_c: totalCost = (0.4 * pears) + (0.65 * apples)
  :answer_d: totalCost = (0.4 + apples) * (0.65 + pears)
  :correct: b
  :feedback_a: That does not consider the cost of the apples or pears.
  :feedback_b: We need to multiply the cost per apple times the number of apples and add it to the cost per pear times the number of pears.
  :feedback_c: That gets the costs backwards
  :feedback_d: That is the wrong formula for computing total cost.

   Which line of code will compute the correct ``totalCost`` if put into line 3 above?


