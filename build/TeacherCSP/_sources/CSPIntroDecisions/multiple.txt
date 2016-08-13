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
	:prefix: csp-12-3-
	
.. highlight:: python
   :linenothreshold: 3

Using Multiple if statements
====================================

You can use more than one ``if`` statement in your code.  Here's an example of a calculation that uses two ``if`` statements.  Let's compute the total cost of an item where the price is based on the weight of the item.  If the item weighs less than 1 pound then the price is 1.45 a pound.  If the item weighs 1 pound or more the price is 1.15 a pound.

.. activecode:: Price_If
    :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c1-line2-3; 4-5: c1-line4-5; 6: c1-line6; 7-9: c3f-line7-9;
    
    weight = 0.5
    if weight < 1:
    	price = 1.45
    if weight >= 1: 
    	price = 1.15
    total = weight * price
    print(weight)
    print(price)
    print(total)

Edit the code above and change the first line so that ``weight`` has a different value. Run it again and see what changes.  Try it in the codelens as well to see how the different values for weight changes the lines of code that are executed.   

In this second version, we set a ``price`` as a *default*, then change it only on the special condition. Does it work the same as the above example?

.. activecode:: Price_If_Default
  :tour_1: "Structural Tour"; 1: c2-line1; 2: c2-line2; 3-4: c2-line3-4; 5: c2-line5; 6-8: c3f-line7-9;

  weight = 0.5
  price = 1.45
  if weight >= 1: 
      price = 1.15
  total = weight * price
  print(weight)
  print(price)
  print(total)

.. mchoice:: 12_3_1_Price_If_Equivalent
  :answer_a: No, they're always the same.
  :answer_b: Yes, they're different if the weight is exactly 1 pound.
  :answer_c: Yes, they're different if the weight is under 1 pound.
  :answer_d: Yes, they're different if the weight is over 1 pound.
  :correct: a
  :feedback_a: The end result is the same.
  :feedback_b: If the weight is exactly 1 pound the price will be 1.15 in both programs.
  :feedback_c: If the weight is under 1 pound the price will be 1.45 in both programs.
  :feedback_d: If the weight is over 1 pound the price will be 1.15 in both programs.

   Are there values for weight that make the two programs above print different results when the same weight is used in both programs?
   
**Mixed up programs**

.. parsonsprob:: 12_3_2_Price_By_Weight

   The following program should calculate the total price, but the lines are mixed up.   The price is based on the weight.  Items that weigh less than 2 pounds should cost 1.5.  Items that weigh more than 2 pounds should cost 1.3.   Drag the blocks from the left and place them in the correct order on the right.  Be sure to also indent correctly! Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or have the wrong indention.</p>
   -----
   weight = 0.5
   numItems = 5
   if weight < 2:
   =====
       price = 1.50
   =====
   if weight >= 2: 
   =====
       price = 1.30
   =====
   total = weight * price
   =====
   print(weight)
   print(price)
   print(total)
   

