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
    
.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. 	qnum::
	:start: 1
	:prefix: csp-9-4-
	
.. highlight:: java
   :linenothreshold: 4

Modifying Text
===============

We can loop through the string and modify it using ``find`` and slice (substring).  

Google has been digitizing books.  But, sometimes the digitizer makes a mistake and uses 1 for i.  The following program replaces ``1`` with ``i`` everywhere in the string.  Now you might not want to really replace every ``1`` with ``i``, but don't worry about that right now.  It uses a ``while`` loop since we don't know how many times it will need to loop.

.. codelens:: Change_Ones
    :question: What is the value of pos after the line with the red arrow executes?
    :breakline: 5
    :feedback: Remember that find returns the starting index if the target string is found and -1 if not.  
    :correct: globals.pos
	
    str = "Th1s is a str1ng"
    pos = str.find("1")
    while pos >= 0:
        str = str[0:pos] + "i" + str[pos+1:len(str)]
        pos = str.find("1")
    print(str)
    
You don't have to replace just one character.  You could replace every instance of a word with another word.  For example, what if you spelled a word wrong and wanted to change it everywhere?

.. codelens:: Change_Word
    :question: What is the value of pos after the line with the red arrow executes?
    :breakline: 6
    :feedback: Remember that find returns the starting index if the target string is found and -1 if not.  
    :correct: globals.pos
	
    str = "He wanted a peice of candy"
    str = str + " so he gave her a peice."
    pos = str.find("peice")
    while pos >= 0:
        str = str[0:pos] + "piece" + str[pos+len("peice"):len(str)]
        pos = str.find("peice")
    print(str)
    
Can you loop through and encode a string to hide the contents of the message?

.. codelens:: Encode_String
	
    message = "meet me at midnight"
    str = "abcdefghijklmnopqrstuvwxyz. "
    eStr = "zyxwvutsrqponmlkjihgfedcba ."
    encodedMessage = ""
    for letter in message:
        pos = str.find(letter)
        encodedMessage = encodedMessage + eStr[pos:pos+1]
    print(encodedMessage)


.. mchoice:: 9_4_1_replace_m
   :answer_a: a
   :answer_b: d
   :answer_c: w
   :answer_d: v
   :correct: d
   :feedback_a: The letter in str is replaced with the letter at the same position in eStr.
   :feedback_b: The letter in str is replaced with the letter at the same position in eStr.
   :feedback_c: Try counting the letters in str to figure out how many letters to count in eStr.
   :feedback_d: The letter e is at position 4 in str and will be replaced with the letter v at position 4 in eStr.

   What character is e replaced with when the message is encoded?

.. mchoice:: 9_4_2_encodeMess1
   :answer_a: ""
   :answer_b: "o"
   :answer_c: "n"
   :answer_d: "m"
   :correct: c
   :feedback_a: It starts out as the empty string, but a letter is added each time through the loop.
   :feedback_b: The letter in str is replaced with the letter at the same position in eStr.
   :feedback_c: The letter in eStr at the same position as the m in str is n.
   :feedback_d: Notice that we are adding the letter in eStr at pos not the letter in str at pos.

   What is the value of encodedMessage after the loop executes the first time?  

.. parsonsprob:: 9_4_3_Decode_String

   The program below decodes an encoded message, but the lines are mixed up.  Put the lines in the right order with the right indentation.
   -----
   message = ""
   str = "abcdefghijklmnopqrstuvwxyz. "
   eStr = "zyxwvutsrqponmlkjihgfedcba ."
   encodedMessage = "nvvg.nv.zg.nrwmrtsg"
   =====
   for letter in encodedMessage:
   =====
       pos = eStr.find(letter)
   =====
       message = message + str[pos:pos+1]
   =====
   print(message)