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

.. 	qnum::
	:start: 1
	:prefix: csp-4-2-

Making a MadLib story
===================================

You might have done MadLib stories when you were a kid.  You provide some pieces of information, like a name of a friend, a verb, and a favorite game (for example), and those pieces of information get plugged into a story.  Since you don't know the story beforehand, you're surprised at what happens to your friend in the story.

.. activecode:: Story1
   :tour_1: "Line by line tour"; 1: StEx-line1; 2: StEx-line2; 3: StEx-line3; 4: StEx-line4; 5: StEx-line5; 6: StEx-line6; 7: StEx-line7; 8: StEx-line8; 9: StEx-line9; 10: StEx-line10; 11: StEx-line11; 12: StEx-line12; 13: StEx-line13; 14: StEx-line14; 15: StEx-line15;
   :tour_2: "Structural tour"; 1-5: StEx-line1-5; 6-10: StEx-line6-10; 11-15: StEx-line11-15;

   firstName = "Pat"
   lastName = "Smith"
   gender = "girl"
   address = "65 Elm Street"
   verb = "eat"
   start = "Once there was a " + gender + " named " + firstName + "."
   next1 = "A good " + gender + " living at " + address + "."
   next2 = "One day, a wicked witch came to the " + lastName + " house."
   next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
   ending = "But " + firstName + " was smart and avoided the wicked witch."
   print(start)
   print(next1)
   print(next2)
   print (next3)
   print(ending)


.. mchoicemf:: 4_2_1_Story1_Q1
   :answer_a: realEnding = firstName + " called the police who took the witch away."
   :answer_b: print(firstName + " called the police who took the witch away.")
   :answer_c: print("Pat called the police who took the witch away.")
   :correct: b
   :feedback_a: This would only work if you also put <code>print(realEnding)</code> after this line.
   :feedback_b: This is a good way to do this since the line that is printed will have the correct first name.  You could also make a string named <code>realEnding</code> first, and then print it.
   :feedback_c: This <i>would</i> work.  But if you changed the <code>firstName</code> variable, this line would not change.  A different answer is better.

   Now you want to add more to the story. You want it to say: "Pat called the police who took the witch away."  Adding which of these lines to the end of the program will make that happen?  (Hint: It is okay to *try* each one!)


**You should really do this:** Run this program to see what gets generated, then change some of the variables to make different stories.  Try different names, different verbs.  


.. activecode:: Story2
   :tour_1: "Line by line tour"; 1: story-line1; 2: story-line2; 3: story-line3; 4: story-line4; 5: story-line5; 6: story-line6; 7: story-line7; 8: story-line8; 9: story-line9; 10: story-line10; 11: story-line11; 12: story-line12; 13: story-line13; 14: story-line14; 15: story-line15; 

   firstName = "Sofia"
   lastName = "Diaz"
   gender = "girl"
   address = "1600 Pennsylvania Avenue"
   verb = "burp at"
   start = "Once there was a " + gender + " named " + firstName + "."
   next1 = "A good " + gender + " living at " + address + "."
   next2 = "One day, a wicked witch came to the " + lastName + " house."
   next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
   ending = "But " + firstName + " was smart and avoided the wicked witch."
   print(start)
   print(next1)
   print(next2)
   print(next3)
   print(ending)
   
.. mchoicemf:: 4_2_2_Story2_Q1
   :answer_a: Yes
   :answer_b: No
   :correct: a
   :feedback_a: The only thing that is different is when the lines are printed, but the lines are the same.
   :feedback_b: Did you try it?  Copy the code into the program area above and run it.
 
   Would the following code print the same story as shown above? 
   
   :: 

     firstName = "Sofia"
     lastName = "Diaz"
     gender = "girl"
     address = "1600 Pennsylvania Avenue"
     verb = "burp at"
     start = "Once there was a " + gender + " named " + firstName + "."
     print(start)
     next1 = "A good " + gender + " living at " + address + "."
     print(next1)
     next2 = "One day, a wicked witch came to the " + lastName + " house."
     print(next2)
     next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
     print(next3)
     ending = "But " + firstName + " was smart and avoided the wicked witch."
     print(ending)
     
.. mchoicemf:: 4_2_3_StringVsVariableName
   :answer_a: Fred is Fred
   :answer_b: Fred is 5
   :answer_c: 5 is Fred
   :answer_d: 5 is 5
   :correct: b
   :feedback_a: There are no double quotes around the last Fred so it will use the value of the variable Fred.
   :feedback_b: The first Fred is in double quotes so it will print the string Fred and the second Fred is not in double quotes so it will print the value of the variable Fred.
   :feedback_c: The first Fred is in double quotes and the second is not.
   :feedback_d: The first Fred is in double quotes so it is a string and the characters in the string will be printed.
 
   What would the following code print?
   
   :: 

     Fred = 5
     print("Fred" + " is " + Fred)
     
.. Note::
   When you print a string (a sequence of characters in a pair of single or double quotes) in Python it will print the exact characters in the string.  When you print a variable it will print the value of that variable.
     
.. parsonsprob:: 4_2_4_Poem

   Put the blocks below into the correct order to print a twist on a famous poem.   
   -----
   print("Roses are red.")  	
   ===== 
   print("Violets are blue.)
   =====                
   print("Sugar is sweet.")
   =====
   print("And so is Sue.")
     
.. parsonsprob:: 4_2_5_Story

   Put the blocks below into the correct order to declare the variables and then print the following story. One day Jay went shopping.  He wanted to buy shoes.  But, he didn't like any.  So, Jay went home. 
   -----
   name = "Jay"
   item = "shoes"
   =====
   print("One day " + name + " went shopping.")  	
   ===== 
   print("He wanted to buy " + item + ".")
   =====                
   print("But, he didn't like any.")
   =====
   print("So, " + name + " went home.")
   

