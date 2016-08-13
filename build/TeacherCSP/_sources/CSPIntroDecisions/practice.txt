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
	:prefix: csp-12-6-
	
.. highlight:: python
   :linenothreshold: 3

Practice with if
======================

The program below is broken in a subtle way.  For one value of ``weight``, the ``price`` will not be set to any value, so the calculation of ``total`` will fail with an error that something ``is not defined``.  This is why professional programmers will assign *some* value to a variable like ``price`` at the beginning of the program, so that errors like this won't happen.  Can you figure out the value of ``weight`` that will result in an error?  Modify the code below to try different values for weight.  

.. activeCode:: Price_If_Broken
  :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c1-line2-3; 4-5: c3-line4-5; 6: c1-line6; 7-9: c3f-line7-9;

  weight = 0.5
  if weight < 1:
      price = 1.45
  if weight > 1: 
      price = 1.15
  total = weight * price
  print(weight)
  print(price)
  print(total)

Try different values for ``weight`` in the above code and then answer the question below:
        
.. fillintheblank:: 12_6_1_brokenrange_fill

    .. blank:: 12_6_1_brokenrange
        :correct: ^1$|1\.[0]*$
        :feedback1: (".*", "Which value is not tested currently?")

        What value for weight will result in an error complaining that price is not defined?

It is certainly possible to have multiple ``if`` statements, and each one can match (or not match) the data.  Imagine a more complicated price scheme, where the price is based on the weight, but there is also a 10% discount for buying more then 10 items.

.. activeCode:: Multiple_Ifs
  :tour_1: "Structural Tour"; 1: c1-line1; 2: c4-line2; 3-4: c1-line2-3; 5-6: c1-line4-5; 7: c1-line6; 8-9: c4-line8-9; 10-12: c3f-line7-9; 

  weight = 0.5
  numItems = 5
  if weight < 1:
      price = 1.45
  if weight >= 1: 
      price = 1.15
  total = weight * price
  if numItems >= 10:
      total = total * 0.9
  print(weight)
  print(price)
  print(total)

.. mchoice:: 12_6_2_Multiple_Ifs
  :answer_a: $3.45
  :answer_b: $3.11
  :answer_c: $3.105
  :answer_d: $3.10
  :correct: c
  :feedback_a: This would be the answer without the 10% discount for buying 10 or more items
  :feedback_b: Python doesn't automatically round up
  :feedback_c: This is the actual result.  But, can you pay $3.105?
  :feedback_d: Python doesn't automatically change $3.105 to $3.10.  

   What is the total for 12 items that weigh 3 pounds?
   
.. mchoice:: 12_6_3_Grade_Ifs
   :answer_a: A
   :answer_b: B
   :answer_c: C
   :answer_d: D
   :answer_e: E
   :correct: d
   :feedback_a: Notice that each of the first 4 statements start with an if.  What is the value of grade when it is printed?
   :feedback_b: Each of the first 4 if statements will execute.
   :feedback_c: Copy this code to an activecode window and run it.
   :feedback_d: Each of the first 4 if statements will be executed. So grade will be set to A, then B then C and finally D.  
   :feedback_e: This will only be true when score is less than 60.   

   What is printed when the following code executes?
   
   :: 
   
     score = 93
     if score >= 90: 
         grade = "A"
     if score >= 80: 
         grade = "B"
     if score >= 70: 
         grade = "C"
     if score >= 60: 
         grade = "D"
     if score < 60: 
         grade = "E"
     print(grade)
     
.. mchoice:: 12_6_4_Logic_Ifs
   :answer_a: x will always equal 0 after this code executes for any value of x
   :answer_b: if x is greater than 2, the value in x will be doubled after this code executes
   :answer_c: if x is greater than 2, x will equal 0 after this code executes
   :correct: c
   :feedback_a: If x was set to 1 originally, then it would still equal 1.
   :feedback_b: What happens in the original when x is greater than 2?  
   :feedback_c: If x is greater than 2, it will be set to 0.  

   Which of the following is true about the code below?  
   
   :: 

     x = 3
     if (x > 2): 
         x = x * 2;
     if (x > 4): 
         x = 0;
     print(x)
     
