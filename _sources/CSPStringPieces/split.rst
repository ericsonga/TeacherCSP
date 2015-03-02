..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".
    
.. 	qnum::
	:start: 1
	:prefix: csp-17-3-

Using the Split Function
===================================

The ``split`` function does exactly that.  It takes as input the character to split on, then returns a *list* with pieces.  The pieces can then be *indexed*.

Try running this program.

.. activecode:: firstsplit
   :tour_1: "Line by line tour"; 1: StP1-line1; 2: StP1-line2; 3: StP1-line3; 4: StP1-line4; 5: StP1-line5;

   input = "Pat,Smith,girl,65 Elm Street,eat"
   pieces = input.split(",")
   print(pieces)
   print("First name is:")
   print(pieces[0])

.. mchoicemf:: 17_3_1_question_firstsplit
   :answer_a: Smith
   :answer_b: girl
   :answer_c: 65 Elm Street
   :answer_d: eat
   :answer_e: We would get an error
   :correct: c
   :feedback_a: That's pieces[1].
   :feedback_b: That's pieces[2]
   :feedback_c: The address is at position 3 in the resulting list.
   :feedback_d: That's pieces[4]
   :feedback_e: Why would this cause an error?  We can use indices to get the element at an index in a list.

   What do you think we would get if we executed ``print(pieces[3])``

.. mchoicemf:: 17_3_2_question_firstsplit2
   :answer_a: Smith
   :answer_b: girl
   :answer_c: 65 Elm Street
   :answer_d: eat
   :answer_e: We would get an error
   :correct: e
   :feedback_a: That's pieces[1].
   :feedback_b: That's pieces[2].
   :feedback_c: That's pieces[3].
   :feedback_d: That's pieces[4].
   :feedback_e: The error happens because that index is past the end of the list.  The last item is at index 4.

   What do you think we would get if we executed ``print(pieces[5])``
   
The code below is the first activecode modified to use the ``split`` function to assign the values to the variables.

.. activecode:: madlib1_split
   :tour_1: "Structural tour"; 1: StP1-line1; 2: StP1-line2; 3-7: StP2-line3-7; 8-12: StP2-line8-12; 13-17: StP2-line13-17;

   input = "Pat,Smith,girl,65 Elm Street,eat"
   pieces = input.split(",")
   firstName = pieces[0]
   lastName = pieces[1]
   gender = pieces[2]
   address = pieces[3]
   verb = pieces[4]
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

This makes it easy to change all of the data, by changing only one line as shown below.

.. activecode:: madlib1_split2
   :tour_1: "Structural tour"; 1: StP3-line1; 2: StP1-line2; 3-7: StP2-line3-7; 8-12: StP2-line8-12; 13-17: StP2-line13-17;

   input = "Abe,Brown,boy,1313 Maple Lane,trick"
   pieces = input.split(",")
   firstName = pieces[0]
   lastName = pieces[1]
   gender = pieces[2]
   address = pieces[3]
   verb = pieces[4]
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
   

