..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".
    
.. 	qnum::
	:start: 1
	:prefix: csp-17-5-
   
Creating a Procedure with Parameters
=====================================
   
Is there another way to make it easy to change the story, rather than creating a string and then splitting it into pieces?  We can create a procedure with parameters and then pass in the input values when we call the procedure as shown below.  


.. activecode:: madlib_function
   :tour_1: "Structural tour"; 1: Stf1-line1; 4: Stf1-line2; 5: Stf1-line3; 6: Stf1-line4; 7: Stf1-line5; 8: Stf1-line6; 11-15: Stf1-line7-11; 18: Stf1-line13;

   def witchStory (firstName, lastName, gender, address, verb):
   
       # create the story
       start = "Once there was a " + gender + " named " + firstName + "."
       next1 = "A good " + gender + " living at " + address + "."
       next2 = "One day, a wicked witch came to the " + lastName + " house."
       next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
       ending = "But " + firstName + " was smart and avoided the wicked witch."
       
       # print the story
       print(start)
       print(next1)
       print(next2)
       print(next3)
       print(ending)

   # call the procedure
   witchStory("Abe", "Brown", "boy", "1313 Maple Lane", "trick")
   
Creating a procedure with parameters makes it easy to customize the madlib stories without having to split a string.  The ``split`` function is very useful when you read data from a file or from a website.   

.. mchoice:: 17_5_1_madlib_proc1
   :answer_a: Emily
   :answer_b: Smith
   :answer_c: girl
   :answer_d: 2783 Main Street
   :answer_e: smell
   :correct: b
   :feedback_a: That is the value of firstName.
   :feedback_b: That is the value of lastName.
   :feedback_c: That is the value of gender.
   :feedback_d: That is the value of address.
   :feedback_e: That is the value of verb.

   What would be the value of ``lastName`` in ``witchStory`` given the following call to the procedure?
   
   ::
   
       witchStory("Emily", "Smith", "girl", "2783 Main Street", "smell")

       

