..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-13-1-

Using Decisions with Strings
==============================

*Learning Objectives:*

- Give examples of programs that use conditions with strings.
- Use the ``input`` function to get input from a user
- Introduce using ``elif`` to handle 3 or more options.
- Introduce using ``str`` to convert a number to a string.

Here's an example of conditional execution using ``if`` statements with strings.  We can print different strings based on the value of a number. For example, if the user only orders 1 item we can print that out differently than if the user orders more than one item. Notice the use of ``str(numItems)`` in the code below.  The function ``str`` turns a number into a string so that it can be appended to a string.
       
.. activecode:: csp_sd_invoice
    :tour_1: "Structural Tour"; 1: sd1line1; 2-3: sd1line2-3; 4-5: sd1line4-5; 6: sd1line6;

    numItems = 1
    if numItems == 1:
        message = "You ordered 1 item"
    if numItems > 1:
        message = "You ordered " + str(numItems) + " items"
    print(message)
    
Change the value of ``numItems`` to see how that changes the output.
       
.. mchoice:: 13_1_1_invoice_neg
   :answer_a: You ordered 1 item
   :answer_b: Your ordered -1 items
   :answer_c: Nothing will be printed.
   :answer_d: You will get an error message that message is not defined.
   :correct: d
   :feedback_a: This line will only print when the numer of items is 1.
   :feedback_b: This line will print whenever the number of items is greater than 1.
   :feedback_c: If numItems is negative neither of the if's will be true so the variable message will not be created.
   :feedback_d: The variable message won't be created if the number of items is less than 1, so trying to print the value of message will cause an error.

   What will be printed if numItems = -1? 

.. mchoice:: 13_1_2_invoice_else
   :answer_a: You ordered 1 item
   :answer_b: Your ordered -1 items
   :answer_c: Nothing will be printed.
   :answer_d: You will get an error message that message is not defined.
   :correct: b
   :feedback_a: This line will still only print when the numer of items is 1.
   :feedback_b: This line will print whenever the number of items was not equal to 1 when you change the second if to an else. 
   :feedback_c: If numItems is negative neither of the if's will be true so the variable message will not be created.
   :feedback_d: The variable message won't be created if the number of items is less than 1, so trying to print the value of message will cause an error.

   What will be printed if you change the second if to an else and set numItems = -1?
   
What if you want different messages to be printed based on the user's score in a game?  The code below should print 
"You can do better!" if the score is less than 10, "Good job" if the score is between 10 and 19 inclusive, and "Amazing" if the score is 20 or more, but it needs to be fixed.  First run it with different values to see what happens and 
then answer the multiple choice questions below.  

.. activecode:: csp_sd_score
    :tour_1: "Structural Tour"; 1: sd2line1; 2-3: sd2line2-3; 4-5: sd2line4-5; 6-7: sd2line6-7;

    score = 8
    if score < 10:
        print("You can do better.")
    if score > 10:
        print("Good job!")
    if score > 20:
        print("Amazing")
         
.. mchoice:: 13_1_3_score1
   :answer_a: You can do better.
   :answer_b: Good job!
   :answer_c: Amazing!
   :answer_d: Nothing is printed
   :correct: d
   :feedback_a: This line will only print when score is less than 10.
   :feedback_b: This line will only print whenever the score is more than 10.
   :feedback_c: This line will only print whenever the score is more then 20.
   :feedback_d: When score equals 10 none of the current if statements will be true, so nothing is printed.

   What is printed when the score is 10?
   
.. mchoice:: 13_1_4_score2
   :answer_a: You can do better.
   :answer_b: Good job!
   :answer_c: Amazing!
   :answer_d: Nothing is printed
   :correct: b
   :feedback_a: This line will only print when score is less than 10.
   :feedback_b: This line will print whenever the score is more than 10, so if the value is 25 it will print first.  And then it will also print "Amazing!".
   :feedback_c: This line will print whenever the score is more than 20, but another line will print first.
   :feedback_d: The value 25 is more than 10.

   What is the first thing printed when the score is 25?
   
Now go back and change the last active code (csp_sd_score) to work correctly.  Remember that you can use ``and`` to join two logical expressions.  This is especially useful if you want to test if a number is in a range of numbers like 10 to 19 inclusive.  So change the example to print the first thing if less than 10, the second thing if it is between 10 and 19 and the third thing if it is 20 or more.  







