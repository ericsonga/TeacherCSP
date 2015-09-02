..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-13-3-

Fortune Teller
===============

You can tell someone's fortune by having them pick a number and then using ``if`` statements to print the fortune for the number.   

.. activecode:: sd_fortune
    :tour_1: "Structural Tour"; 1: sd4-line1; 2-3: sd4-line2-3; 4-5: sd4-line4-5; 6-7: sd4-line6-7; 8-9: sd4-line8-9; 10-11: sd4-line10-11;
    :nocodelens:
    
    num = input ("Type a number from 1 to 5. Then click OK or press enter")
    if num == "1": 
        print("You will get a treat.")
    if num == "2":
        print("You will lose something.")
    if num == "3":
        print("You will meet a new friend.")
    if num == "4":
        print("You will catch a cold.")
    if num == "5":
        print("You will ace a test.")
       
.. mchoice:: 13_3_1_fortune1
   :answer_a: 1
   :answer_b: 2
   :answer_c: 5
   :answer_d: 6
   :correct: c
   :feedback_a: It would have to at least check if it was 1 or 2.  
   :feedback_b: It executes every if, even if it already found the answer.  
   :feedback_c: It executes every if.  
   :feedback_d: There are only 5 logical expression here so it can't be more than 5.  

   How many conditions (logical expressions) are checked if the user answered 2?
   
.. mchoice:: 13_3_2_fortune2
   :answer_a: 1
   :answer_b: 2
   :answer_c: 5
   :answer_d: 6
   :correct: c
   :feedback_a: It has to execute each if in order from top to bottom. 
   :feedback_b: How would this work? 
   :feedback_c: It executes every if.  
   :feedback_d: There are only 5 logical expression here so it can't be more than 5.  

   How many conditions (logical expressions) are checked if the user answered 6?
   
Modify the program to handle when the user enters something other than a number from 1 to 5.  Also add some additional fortunes and allow the user to pick a number from 1 to 10.






