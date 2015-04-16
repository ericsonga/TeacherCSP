..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-13-4-

Using elif for more options
================================
We have used ``if`` and ``else`` to handle two possible options, but what could you do for if you want more than two options?  What if you want to test if a value is negative, 0, or positive?  One way to do this using multiple ``if`` statements is shown below.  

.. activecode:: sd_three_options
    :tour_1: "Structural Tour"; 1: sd5-line1; 2-3: sd5-line2-3; 4-5: sd5-line4-5; 6-7: sd5-line6-7;

    x = 8
    if x < 0:
        print("x is negative")
    if x == 0: 
        print("x is 0")
    if x > 0: 
        print("x is positive") 
       
Run this several times and change the value of x each time.  Try it with a positive number, a negative number, and 0 to check that it works correctly.  Modify the code to 
take a number as input from the user instead.  

..	index::
   	single: elif

Another way to choose between three options is to use ``if`` followed by ``elif`` and finally ``else`` as shown below.  

.. activecode:: sd_three_options_elif
    :tour_1: "Structural Tour"; 1: sd6-line1; 2-3: sd6-line2-3; 4-5: sd6-line4-5; 6-7: sd6-line6-7;

    x = 8
    if x < 0:
        print("x is negative")
    elif x == 0: 
        print("x is 0")
    else:
        print("x is positive")
       
**Mixed up programs**

.. parsonsprob:: 13_4_1_string_elif

   The following program should report which team won or if there was a tie.  But the code has been mixed up.  Drag it into the right order with the right indention.   
   -----
   team1 = 20
   team2 = 20
   =====
   if (team1 < team2):
       print("team1 won")
   =====
   elif (team2 > team1)
   =====
       print("team2 won")
   =====
   else
   =====
       print("team1 and team2 tied")
      
You can use as many ``elif`` statements as you need.  You can only have one ``else`` statement.  What if you have scaled some data from 0 to 1 and want to know what quartile a value is in?  

.. activecode:: sd_four_options
    :tour_1: "Structural Tour"; 1: sd7-line1; 2-3: sd7-line2-3; 4-5: sd7-line4-5; 6-7: sd7-line6-7; 8-9: sd7-line8-9;

    x = .25
    if x <= .25:
        print("x is in the first quartile - x <= .25")
    elif x <= .5: 
        print("x is in the second quartile - .25 < x <= .5")
    elif x <= .75:
        print("x is in the third quartile - .5 < x <= .75")
    else:
        print("x is in the fourth quartile - .75 < x <= 1")
       
.. mchoicemf:: 13_4_2_elif1
   :answer_a: x is in the first quartile - x <= .25
   :answer_b: x is in the second quartile - .25 < x <= .5
   :answer_c: x is in the third quartile - .5 < x <= .75
   :answer_d: x is in the fourth quartile - .75 < x <= 1
   :correct: c
   :feedback_a: This will only print if x is less then or equal to .25.  
   :feedback_b: This will print if the other if's were not true, and if x is less than or equal to .5.  By moving lines 6-7 before lines 4-5 this will never print.
   :feedback_c: This will print if the other if's are not true and if x is less than or equal to .75.  So, moving lines 6-7 before lines 4-5 messes up what this code is intended to do and incorrectly prints that .5 is in the third quartile.  
   :feedback_d: This will only print if all of the other if's were false.  

   What would be printed if you moved lines 6-7 before lines 4-5 and set x equal to .5?
   
Here's the fortune teller code from before but now it is written using ``elif`` and ``else`` instead of just ``if``.
   
.. activecode:: fortune_elif
    :tour_1: "Structural Tour"; 1: elif1-line1; 2-3: elif1-line2-3; 4-5: elif1-line4-5; 6-7: elif1-line6-7; 8-9: elif1-line8-9; 10-11: elif1-line10-11;
    :nocodelens:
    
    num = input ("Type a number from 1 to 5. Then click OK or press enter")
    if num == "1": 
        print("You will get a treat.")
    elif num == "2":
        print("You will lose something.")
    elif num == "3":
        print("You will meet a new friend.")
    elif num == "4":
        print("You will catch a cold.")
    else:
        print("You will ace a test.")
       
.. mchoicemf:: 13_4_3_fortune-elif-1
   :answer_a: 1
   :answer_b: 2
   :answer_c: 5
   :answer_d: 6
   :correct: b
   :feedback_a: It will have to test if <code>num</code> is equal to 1 and because that is false it will test if <code>num</code> is equal to 2.   
   :feedback_b: With the <code>elif</code> it won't execute the other <code>elif</code>'s if one of them is true.
   :feedback_c: With <code>elif</code> it will test each until one of the conditions is true and then skip the rest. 
   :feedback_d: There are only 5 logical expression here so it can't be more than 5.  

   How many conditions (logical expressions) are checked in the code above if the user answered 2?
   
.. note::  

   This is the end of chapter 13.  Readers who are part of the teacher study should go to `https://www.surveymonkey.com/s/TeacherQ1213 <https://www.surveymonkey.com/s/TeacherQ1213>`_ and take the post test for chapters 12 and 13 before continuing on to chapter 14.


       




