..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-13-2-

Interactive Stories with Input
===============================
..	index::
   	single: input
   	
You can use ``if`` statements to make a story interactive where the reader picks from several possible next actions.  The ``input`` method will display the string and return what the user types.  You can check if two strings have the same characters using ``==`` in Python.

.. activecode:: csp_sd_story
    :tour_1: "Structural Tour"; 1: sd3-line1; 2: sd3line2; 3: sd3line3; 4: sd3line4; 5-6: sd3line5-6; 7: sd3line7; 8-9: sd3line8-9; 10: sd3line10; 11-12: sd3line11-12; 
    :nocodelens:
    
    print("You are in front of a creepy door in a hallway.")
    print("What do you want to do?")
    action = input ("Type: in, left, or right. Then click OK or press enter")
    if action == "in":
        print("You choose to go in.")
        print("The room is pitch black.")
    if action == "left":
        print("You choose to turn left.")
        print("A ghost appears at the end of the hall.")
    if action == "right":
        print("You choose to turn right.")
        print("A greenish light is visible in the distance.")
       
.. mchoice:: 13_2_1_story1
   :answer_a: The room is pitch black.
   :answer_b: A ghost appears at the end of the hall.
   :answer_c: A greenish light is visible in the distance.  
   :answer_d: None of the above is printed.
   :correct: b
   :feedback_a: This line will be printed when the user enters in.
   :feedback_b: This line will printed when the user enters left.
   :feedback_c: This line will printed when the user enters right.
   :feedback_d: If the user enters something besides in, left, or right none of the logical expressions will be true and none of these will be printed.  

   What is the second thing printed if the user answers left?
   
.. mchoice:: 13_2_2_story2
   :answer_a: The room is pitch black.
   :answer_b: A ghost appears at the end of the hall.
   :answer_c: A greenish light is visible in the distance.  
   :answer_d: None of the above is printed.
   :correct: d
   :feedback_a: This line will be printed when the user enters in.
   :feedback_b: This line will printed when the user enters left.
   :feedback_c: This line will printed when the user enters right.
   :feedback_d: None of the conditions will be true if the user enters something other than in, left, or right so none of these will be printed.

   What is the printed if the user answer something other than in, left, or right?
   
What should the program do if the user enters something besides in, left, or right?  Fix the code above to let the user know what went wrong.  Also add another possibility like "out".







