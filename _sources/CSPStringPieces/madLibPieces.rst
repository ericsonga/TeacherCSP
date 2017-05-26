..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".
    
.. 	qnum::
	:start: 1
	:prefix: csp-17-2-

Making MadLib Stories, Easier
===================================

You might recall this example from earlier in this section of the book.

.. activecode:: madlib1
   :tour_1: "Line by line tour"; 2: StEx-line1; 3: StEx-line2; 4: StEx-line3; 5: StEx-line4; 6: StEx-line5; 9: StEx-line6; 10: StEx-line7; 11: StEx-line8; 12: StEx-line9; 13: StEx-line10; 16: StEx-line11; 17: StEx-line12; 18: StEx-line13; 19: StEx-line14; 20: StEx-line15; 
   :tour_2: "Structural tour"; 2-6: StEx-line1-5; 9-13: StEx-line6-10; 16-20: StEx-line11-15;

   # initialize the variables
   firstName = "Pat"
   lastName = "Smith"
   gender = "girl"
   address = "65 Elm Street"
   verb = "eat"
   
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
   print (next3)
   print(ending)

What if we want to change this story? We can change the values for ``firstName``, ``lastName``, ``gender``, ``address``, and ``verb``.  But, if we change each of these we are changing 5 lines.  Is there another way to do this?  What if we want to specify the values like this ``inputs="Pat,Smith,boy,65 Elm Street,eat"``?  Can we do that?

Sure, we can -- if we can take that string apart.  The computer knows how to break larger pieces of data into smaller ones.


