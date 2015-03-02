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
	:prefix: csp-4-1-

Assign a Name to a String
===================================

..	index::
	single: assignment
	pair: strings; assignment

*Learning Objectives:*

- Create a variable that can store text (a string)
- Add (append or concatenate) strings together to create new strings
- Convert a number into a string to concatenate it to another string
- Use dot-notation to invoke functions on objects
- Show that strings are immutable (don't change)

Computers can use names to represent *anything*.  In the last chapter we saw that we can name numbers (declare a variable and set its value to a number) and then do calculations using the names for the numbers.  We can also name strings and do calculations with their names, too.  What does it mean to do a calculation on a string?  Well, Python uses the ``+`` symbol to concatenate strings as shown below.

.. activecode:: String_Assign
   :tour_1: "Line-by-line Tour"; 1: sa1-line1; 2: sa1-line2; 3: sa1-line3; 4: sa1-line4; 
   
   first = "Jorge"
   last = "Garcia"
   fullName = first + " " + last
   print(fullName)
   
.. note::
   Blank spaces are not automatically added when you append two strings.  If you want a blank space in between two strings then put it there explicitly using a string with just a space in it ``" "`` as shown above.
   
Concatenating Strings and Numbers
-----------------------------------

You can print both strings and numbers, and you can concatenate strings using ``+``, but if you try to concatenate a string and a number you will get an error. The string ``"5"`` is stored very differently than the number ``5`` in computer memory, so to concatenate the number ``5`` and a string we need to convert the number into a string first.  The ``str(num)`` function will convert a number into a string.  

.. activecode:: String_Convert
   :tour_1: "Line-by-line Tour"; 1: sa3-line1; 2: sa3-line2; 3: sa3-line3; 4: sa3-line4; 
   
   Fred = 5
   print("Fred")
   print(Fred)
   print("Fred" + " is " + str(Fred))
   
.. note::
   Notice how printing the string ``"Fred"`` prints something different than printing the value of the variable ``Fred``. Printing the string ``"Fred"`` prints the exact characters in that string. Remember that strings are enclosed in pairs of double or single quotes and when they are printed it will print the exact characters in the string. When you print a variable it will print the *value* of that variable.  
   
We can update our driving example to print out the cost of the trip with just one ``print`` statement.

.. activecode:: Trip_Calculator2
   :tour_1: "Line by line tour"; 1: trp-line1; 2: trp-line2; 3: trp-line3; 4: trp-line4; 5: trp-line5; 6: trp2-line6;

   distance = 924.7
   mpg = 35.5
   gallons = distance / mpg
   costPerGallon = 3.65
   costTrip = gallons * costPerGallon
   print("Cost to get from Chicago to Dallas: $" + str(costTrip))
   
Strings are Objects
------------------------------------
   
..	index::
	single: dot-notation
	pair: programming; dot-notation

Strings are objects in Python which means that there is a set of built-in functions that you can use to manipulate strings.  You use **dot-notation** to invoke the functions on a string object such as ``sentence.lower()``.  The function ``lower()`` returns a new string with all of the characters in the original string set to lowercase.  The function ``capitalize()`` will capitalize the first letter of the string.  

.. activecode:: String_Methods2
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5;
   :nocodelens:
   
   sentence = "THIS IS A TEST"
   better = sentence.lower()
   print(better)
   betterStill = better.capitalize() + "."
   print(betterStill)
   

Strings are Immutable
-----------------------

..	index::
	pair: string; immutable

Even though you can manipulate a string to create a new string the original string is **immutable** which means that it doesn't change.  Notice that after you execute the code below the string stored in the variable ``sentence`` hasn't changed.  
  
.. activecode:: String_Immutable
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5; 6: str2-line6;
   
   sentence = "THIS IS A TEST"
   better = sentence.lower()
   print(better)
   betterStill = better.capitalize() + "."
   print(betterStill)
   print(sentence)
   
While the strings themselves can't be changed you can change the value of a variable. This throws away the original string and sets the variable's value to the new string.   

.. activecode:: String_Reassign
   :tour_1: "Line-by-line Tour"; 1: sa2-line1; 2: sa2-line3; 3: sa2-line2; 4: sa2-line3;
   
   sentence = "THIS IS A TEST"
   print(sentence)
   sentence = "Hi there"
   print(sentence)
   
.. mchoicemf:: 4_1_1_s1
   :answer_a: xyz
   :answer_b: xyxyz
   :answer_c: xy xy z
   :answer_d: xy z
   :answer_e: z
   :correct: b
   :feedback_a: s1 will equal "xy" plus another "xy" then z at the end.
   :feedback_b: s1 contains the original value, plus itself, plus "z"  
   :feedback_c: No spaces are added during concatenation.
   :feedback_d: No spaces are added during concatenation, and an additional "xy" should be included at the beginning.
   :feedback_e: s1 was set to "xy" initially, so the final answer will be "xyxyz"

   Given the following code segment, what is the value of the string s1 after these are executed?
   
   ::

     s1 = "xy"
     s2 = s1
     s1 = s1 + s2 + "z"
     
.. mchoicemf:: 4_1_2_s2
   :answer_a: Hey
   :answer_b: hey
   :answer_c: HEY
   :correct: c
   :feedback_a: This would be correct if we had asked what the value of s3 was. What is the value of s1?
   :feedback_b: This would be true if we asked what the value of s2 was after the code executes.  What is the value of s1?
   :feedback_c: Strings are immutable, meaning they don't change.  Any function that changes a string returns a new string.  So s1 never changes unless you set it to a different string. 

   What is the value of s1 after the following code executes?
   
   :: 

     s1 = "HEY"
     s2 = s1.lower()
     s3 = s2.capitalize()


