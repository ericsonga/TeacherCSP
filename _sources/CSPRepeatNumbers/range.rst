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
	:prefix: csp-7-4-
	
.. highlight:: java
   :linenothreshold: 4

The Range Function
====================

You can use the ``range`` function to create a list of numbers.    If the ``range`` function is passed just one value it will return a list of all the numbers from 0 to one less than that number.

.. activecode:: Numbers_Range1
	
    print(range(3))
    print(range(5))
    print(range(11)) 
    
.. mchoice:: 7_4_1_Numbers_Range1
   :answer_a: range(5)
   :answer_b: range(6)
   :answer_c: range(7)
   :correct: b
   :feedback_a: This will return a list of all the numbers from 0 to 4.
   :feedback_b: This will return a list of all the numbers from 0 to 5.
   :feedback_c: This will return a list of all the numbers from 0 to 6.

   Which of the following lines actually gives us a list of all the numbers from 0 to 5?
    
If two values are passed as input to the ``range`` function then it will return a list of values that includes the first value, but ends at one less than the second value.  It is *inclusive* of the first value and *exclusive* of the second value.

.. activecode:: Numbers_Range2
	
    print(range(1,10))
    print(range(0,11))
    print(range(20,31))

.. mchoice:: 7_4_2_Numbers_Range2
   :answer_a: range(10)
   :answer_b: range(1,10)
   :answer_c: range(11)
   :answer_d: range(1,11)
   :correct: d
   :feedback_a: That includes zero and doesn't include 10: [0,1,2,3,4,5,6,7,8,9]
   :feedback_b: That doesn't include 10: [1,2,3,4,5,6,7,8,9]
   :feedback_c: That includes zero: [0,1,2,3,4,5,6,7,8,9,10]
   :feedback_d: That returns [1,2,3,4,5,6,7,8,9,10]

   Which of the following lines actually gives us a list of all numbers from 1 to 10?
   
Let's rewrite the program that calculates the product using the ``range`` function to generate the list of numbers as shown below.

.. activecode:: Numbers_Product2
    :tour_1: "Line by line tour"; 1: for2_line1; 2: for2_line2; 3: for2_line3; 4: for2_line4; 5: for2_line5;
	
    product = 1  # Start out with nothing
    numbers = range(1,11)
    for number in numbers:
    	product = product * number
    print(product)

.. mchoice:: 7_4_3_Numbers_Product_Q3
   :answer_a: 121645100408832000
   :answer_b: 3628800
   :answer_c: 362880
   :answer_d: 2432902008176640000
   :correct: d
   :feedback_a: That is the product of all numbers from 1 to 19 (e.g., you changed the 11 to 20)
   :feedback_b: That is the product of all numbers from 1 to 10 (e.g., no change at all)
   :feedback_c: That is the product of all numbers from 1 to 9 (e.g., you changed the 11 to 10)
   :feedback_d: That is the product of all numbers from 1 to 20 (e.g., you changed the 11 to 21)

   Change ONE number in the above program to tell us the product of all numbers from 1 to 20



