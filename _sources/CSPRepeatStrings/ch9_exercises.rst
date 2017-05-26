..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: 9-6-

Chapter 9 Exercises
--------------------

#.

    .. tabbed:: ch9ex1t

        .. tab:: Question

            Fix 5 errors in code below to correctly print: "Rubber baby buggy bumpers."

            .. activecode:: ch9ex1q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                Phrase = "Rubber baby buggy bumpers.
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase
                    # STEP 4: ACCUMULATE
                    newString = newString letter
                # STEP 5: PROCESS RESULT
                print(newString

        .. tab:: Answer

            Change ``Phrase`` to ``phrase`` and add a ``"`` at the end of the line.  Add a ``:`` at the end of line 6.  Add a ``+`` in line 8.  Add a ``)`` at the end of line 10.

            .. activecode:: ch9ex1a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "Rubber baby buggy bumpers."
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = newString + letter
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch9ex1q

#.

    .. tabbed:: ch9ex2t

        .. tab:: Question

            The code currently prints the reverse of a string. Change it so that it prints the string in the correct order, but every character is separated by a space (there should even be a space between a space and the next character).

            .. activecode::  ch9ex2q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "This is a string."
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Answer

            In line 3, ``newString`` should equal ``newString + letter + " "``. The order does matter.

            .. activecode::  ch9ex2a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "This is a string."
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = newString + letter + " "
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex2q

#.

    .. tabbed:: ch9ex3t

        .. tab:: Question

           Fix the indention on 4 lines below to correctly print the reverse of the string.  It should print: "!yadhtriB yppaH."

           .. activecode::  ch9ex3q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATORS
                newString = ""
                # STEP 2: GET DATA
                    phrase = "Happy Birthday!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                # STEP 4: ACCUMULATE
                newString = letter + newString
                # STEP 5: PROCESS RESULT
                    print(newString)


        .. tab:: Answer

            Change the indention on lines 4, 7, 8, and 10 as shown below.

            .. activecode::  ch9ex3a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATORS
                newString = ""
                # STEP 2: GET DATA
                phrase = "Happy Birthday!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString
                # STEP 5: PROCESS RESULT
                print(newString)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex3q

#.

    .. tabbed:: ch9ex4t

        .. tab:: Question

            Fix the errors in the code to correctly print the reverse of the string. It should print: "!gnirts a m'I ,kool yeH"

            .. activecode::  ch9ex4q
                :nocodelens:

                # STEP 2: GET DATA
                phrase = "Hey look, I'm a string!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    newString = ""
                    # STEP 4: ACCUMULATE
                    newString = newString + phrase
                    # STEP 5: PROCESS RESULT
                    print(phrase)

        .. tab:: Answer

            ``newString`` should be initialized outside of the for loop. Inside the for loop, it should equal ``letter + newString`` and the print statement should be outside the for loop and it should print the ``newString``

            .. activecode::  ch9ex4a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATORS
                newString = ""
                # STEP 2: GET DATA
                phrase = "Hey look, I'm a string!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex4q

#.

    .. tabbed:: ch9ex5t

        .. tab:: Question

           Fix 4 errors in the code below to correctly print the mirror of the text in phrase.  It should print: "tset a si sihTThis is a test."

           .. activecode::  ch9ex5q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString =
                # STEP 2: GET DATA
                phrase = "This is a test"
                # STEP 3: LOOP THROUGH THE DATA
                for l in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString  letter
                # STEP 5: PROCESS RESULT
                print()


        .. tab:: Answer

            Initialize ``newString`` to the empty string in line 2.  Change ``l`` to ``letter`` in line 6.  Add a ``+`` in line 8.  Add ``newString`` on line 10.

            .. activecode::  ch9ex5a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "This is a test"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString + letter
                # STEP 5: PROCESS RESULT
                print(newString)


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch9ex5q

#.

    .. tabbed:: ch9ex6t

        .. tab:: Question

            The code currently prints each letter of the string twice in a row. Change it so that it prints the mirror of the string. It should print: "!rorrim a ni gnikool ekil s'tIIt's like looking in a mirror!"

            .. activecode::  ch9ex6q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "It's like looking in a mirror!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = newString + letter + letter
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Answer

            Change line 4 to be ``newString = letter + newString + newString``

            .. activecode::  ch9ex6a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "It's like looking in a mirror!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString + letter
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex6q

#.

    .. tabbed:: ch9ex7t

        .. tab:: Question

           The code below is supposed to replace all 1's with i's, but it is in an infinite loop.  You can reload the page to stop the infinite loop.  Add a line to make the code work.  It should print: "This is a string."

           .. activecode::  ch9ex7q
                :nocodelens:

                str = "Th1s is a str1ng"
                pos = str.find("1")
                while pos >= 0:
                    str = str[0:pos] + "i" + str[pos+1:len(str)]
                print(str)

        .. tab:: Answer

            Add line 5 as shown below.

            .. activecode::  ch9ex7a
                :nocodelens:

                str = "Th1s is a str1ng"
                pos = str.find("1")
                while pos >= 0:
                    str = str[0:pos] + "i" + str[pos+1:len(str)]
                    pos = str.find("1")
                print(str)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex7q

#.

    .. tabbed:: ch9ex8t

        .. tab:: Question

            Fix the errors so that the code prints "I'm just a string."

            .. activecode::  ch9ex8q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = "  "
                # STEP 2: GET DATA
                phrase = "I'm just a string."
                # STEP 3: LOOP THROUGH THE DATA
                for phrase in letter
                    # STEP 4: ACCUMULATE
                    letter = letter + newString
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Answer

            newString should not be initialized with spaces. On line 3, it should be "for letter in phrase:". Line 4 should be "newString = newString + letter".

            .. activecode::  ch9ex8a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "I'm just a string."
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = newString + letter
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex8q

#.

    .. tabbed:: ch9ex9t

        .. tab:: Question

           The program below is supposed to encode the text in message, but it has 5 errors.  Fix the errors so that it prints: "nvvg.nv.zg.nrwmrtsg."

           .. activecode::  ch9ex9q
                :nocodelens:

                message = "meet me at midnight"
                str = "abcdefghijklmnopqrstuvwxyz.
                eStr = zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = message
                for letter in message
                    pos = str.find(letter)
                    encodedMessage = encodedMessage + eStr[pos:pos+1]
                print encodedMessage)

        .. tab:: Answer

            Change line 2 to end in ``"``.  Change line 3 to start the string with ``"``.  Change line 4 to set ``encodeMesage`` to the empty string to start.  Add ``:`` at the end of line 5.  Add ``(`` on line 8.

            .. activecode::  ch9ex9a
                :nocodelens:

                message = "meet me at midnight"
                str = "abcdefghijklmnopqrstuvwxyz. "
                eStr = "zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = ""
                for letter in message:
                    pos = str.find(letter)
                    encodedMessage = encodedMessage + eStr[pos:pos+1]
                print(encodedMessage)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex9q

#.

    .. tabbed:: ch9ex10t

        .. tab:: Question

            The code currently prints "This is a striniThis is a string". Fix the error so that it replaces every "1" with "i" and prints "This is a string".

            .. activecode::  ch9ex10q
                :nocodelens:

                str = "Th1s is a str1ng"
                pos = str.find("1")
                while pos >= 0:
                    pos = str.find("1")
            	    str = str[0:pos] + "i" + str[pos+1:len(str)]
                print(str)

        .. tab:: Answer

            At the end of the body of the while loop, make sure to find the "1" again.

            .. activecode::  ch9ex10a
                :nocodelens:

                str = "Th1s is a str1ng"
                pos = str.find("1")
                while pos >= 0:
                    str = str[0:pos] + "i" + str[pos+1:len(str)]
                    pos = str.find("1")
                print(str)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex10q

#.

    .. tabbed:: ch9ex11t

        .. tab:: Question

           Rewrite the following code to create a function that takes a string and returns the reverse of the string.  It should print: "!yadhtriB yppaH."

           .. activecode::  ch9ex11q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATORS
                newString = ""
                # STEP 2: GET DATA
                phrase = "Happy Birthday!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString
                # STEP 5: PROCESS RESULT
                print(newString)

        .. tab:: Answer

            Define the function as shown below.  Call the function and print the result.

            .. activecode::  ch9ex11a
                :nocodelens:

                def reverse(phrase):
                    # STEP 1: INITIALIZE ACCUMULATORS
                    newString = ""

                    # STEP 3: LOOP THROUGH THE DATA
                    for letter in phrase:

                       # STEP 4: ACCUMULATE
                       newString = letter + newString

                    # STEP 5: PROCESS RESULT
                    return(newString)

                print(reverse("Happy Birthday!"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex11q

#.

    .. tabbed:: ch9ex12t

        .. tab:: Question

            Fix the errors in the code so that it replaces the misspelled word "recieved" with the correct spelling "received"

            .. activecode::  ch9ex12q
                :nocodelens:

                str = "He recieved candy"
                pos = str.find("received")
                while pos >= 0:
                    str = str[0:pos+len("recieved")] + "received" + str[pos:len(str)]
                    pos = str.find("recieved")
                print(str)

        .. tab:: Answer

            In line 2, make sure to find the position of the misspelled word. In line 4, ``str = str[0:pos] + "received" + str[pos+len("recieved"):len(str)]``.

            .. activecode::  ch9ex12a
                :nocodelens:

                str = "He recieved candy"
                pos = str.find("recieved")
                while pos >= 0:
                    str = str[0:pos] + "received" + str[pos+len("recieved"):len(str)]
                    pos = str.find("recieved")
                print(str)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex12q

#.

    .. tabbed:: ch9ex13t

        .. tab:: Question

           Rewrite the following code to create a function that takes a string and returns the mirror of the string.  It should print: "!ssalC iHHi Class!".

           .. activecode::  ch9ex13q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                # STEP 2: GET DATA
                phrase = "This is a test"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                    newString = letter + newString + letter
                # STEP 5: PROCESS RESULT
                print(newString)


        .. tab:: Answer

            Define the function as shown below.  Call the function and print the result.

            .. activecode::  ch9ex13a
                :nocodelens:

                def mirror(phrase):

                    # STEP 1: INITIALIZE ACCUMULATOR
                    newString = ""
                    # STEP 3: LOOP THROUGH THE DATA
                    for letter in phrase:
                        # STEP 4: ACCUMULATE
                        newString = letter + newString + letter
                    # STEP 5: PROCESS RESULT
                    return(newString)

                print(mirror("Hi Class!"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex13q

#.

    .. tabbed:: ch9ex14t

        .. tab:: Question

            Complete the code to change all the periods to commas.

            .. activecode::  ch9ex14q
                :nocodelens:

                str = "I like to eat. sleep. learn. and code!"
                pos = str.
                while pos >= :
                    str = str[0:pos] +   + str[  :len(str)]
                    pos =
                print(str)

        .. tab:: Answer

            On line 2, use the find method to find the period. On line 3, ``pos`` should be greater than or equal to 0. Line 4 should be "str = str[0:pos] + "," + str[pos+len("."):len(str)]" and line 5 should find the next period.

            .. activecode::  ch9ex14a
                :nocodelens:

                str = "I like to eat. sleep. learn. and code!"
                pos = str.find(".")
                while pos >= 0:
                    str = str[0:pos] + "," + str[pos+len("."):len(str)]
                    pos = str.find(".")
                print(str)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex14q

#.

    .. tabbed:: ch9ex15t

        .. tab:: Question

           Modify the code below to create a function that will that will take a message and return an encoded message.  It should print: "nvvg.nv.zg.nrwmrtsg."

           .. activecode::  ch9ex15q
                :nocodelens:

                message = "meet me at midnight"
                str = "abcdefghijklmnopqrstuvwxyz. "
                eStr = "zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = ""
                for letter in message:
                    pos = str.find(letter)
                    encodedMessage = encodedMessage + eStr[pos:pos+1]
                print(encodedMessage)

        .. tab:: Answer

            Define the function as shown below and be sure to return the encoded string.  Call the function and print the result.

            .. activecode::  ch9ex15a
                :nocodelens:

                def encode(message):
                    str = "abcdefghijklmnopqrstuvwxyz. "
                    eStr = "zyxwvutsrqponmlkjihgfedcba ."
                    encodedMessage = ""
                    for letter in message:
                        pos = str.find(letter)
                        encodedMessage = encodedMessage + eStr[pos:pos+1]
                    return(encodedMessage)

                print(encode("The password is touchdown."))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex15q

#.

    .. tabbed:: ch9ex16t

        .. tab:: Question

            Rewrite and fix the errors in the code to be a procedure that takes in a string and prints the reverse of the string and the mirror of the string. Make sure to call the procedure.

            .. activecode::  ch9ex16q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                reverseString = ""
                mirrorString = " "
                # STEP 2: GET DATA
                phrase = "This is the string"
                # STEP 3: LOOP THROUGH THE DATA
                for phrase in phrase:
                    # STEP 4: ACCUMULATE
                    reverseString = reverseString + letter
                    mirrorString = letter + letter + reverseString
                # STEP 5: PROCESS RESULT
                print(reverseString)
                print(mirrorString)

        .. tab:: Answer

            ``mirrorString`` in line 2 should not be set equal to a string of a space. The for loop should be "for letter in phrase". ``reverseString`` should equal ``letter + reverseString`` and ``mirrorString`` should equal ``letter + mirrorString + letter``.

            .. activecode::  ch9ex16a
                :nocodelens:

                def aProcedure(phrase):
                    # STEP 1: INITIALIZE ACCUMULATOR
                    reverseString = ""
                    mirrorString = ""
                    # STEP 3: LOOP THROUGH THE DATA
                    for letter in phrase:
                        # STEP 4: ACCUMULATE
                        reverseString = letter + reverseString
                        mirrorString = letter + reverseString + letter
                    # STEP 5: PROCESS RESULT
                    print(reverseString)
                    print(mirrorString)

                phrase = "This is the string"
                aProcedure(phrase)
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex16q

#.

    .. tabbed:: ch9ex17t

        .. tab:: Question

           Modify the code below to create a function that returns the decoded input string.  It should print: "meet me at midnight."

           .. activecode::  ch9ex17q
                :nocodelens:

                message = ""
                str = "abcdefghijklmnopqrstuvwxyz. "
                eStr = "zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = "nvvg.nv.zg.nrwmrtsg"
                for letter in encodedMessage:
                    pos = eStr.find(letter)
                    message = message + str[pos:pos+1]
                print(message)

        .. tab:: Answer

            Define the function as shown below.  Be sure to return the decoded message.  Call the function and print the result.

            .. activecode::  ch9ex17a
                :nocodelens:

                def decode(eMessage):
                    message = ""
                    str = "abcdefghijklmnopqrstuvwxyz. "
                    eStr = "zyxwvutsrqponmlkjihgfedcba ."
                    for letter in eMessage:
                        pos = eStr.find(letter)
                        message = message + str[pos:pos+1]
                    return(message)

                print(decode("nvvg.nv.zg.nrwmrtsg"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex17q

#.

    .. tabbed:: ch9ex18t

        .. tab:: Question

            Finish the code so that it prints the mirror of the string with the correct way then the reverse. It should print: "This is a mirror!!rorrim a si sihT"

            .. activecode::  ch9ex18q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                aString = ""
                # STEP 2: GET DATA
                phrase = "This is a mirror!"

        .. tab:: Answer

            .. activecode::  ch9ex18a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR
                newString = ""
                aString = ""
                # STEP 2: GET DATA
                phrase = "This is a mirror!"
                # STEP 3: LOOP THROUGH THE DATA
                for letter in phrase:
                    # STEP 4: ACCUMULATE
                	newString = letter + newString
                for letter in newString:
                  	aString = letter + aString + letter
                # STEP 5: PROCESS RESULT
                print(aString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex18q

#.

    .. tabbed:: ch9ex19t

        .. tab:: Question

           Create another function that encodes a string.  Pass in both the string to be encoded *and* the string to use to encode the string as well.

           .. activecode::  ch9ex19q
               :nocodelens:

        .. tab:: Answer

            Create a function similar to the encode function above, but change it to take two input values.

            .. activecode::  ch9ex19a
                :nocodelens:

                def encode2(message, eStr):
                    str = "abcdefghijklmnopqrstuvwxyz. "
                    encodedMessage = ""
                    for letter in message:
                        pos = str.find(letter)
                        encodedMessage = encodedMessage + eStr[pos:pos+1]
                    return(encodedMessage)

                print(encode2("This is a test", "zyxwvutsrqponmlkjihgfedcba ."))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex19q

#.

    .. tabbed:: ch9ex20t

        .. tab:: Question

            Here's the code to encode a message. Write code underneath it to decode the encoded message and print it.

            .. activecode::  ch9ex20q
                :nocodelens:

                message = "meet me at midnight"
                str = "abcdefghijklmnopqrstuvwxyz. "
                eStr = "zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = ""
                for letter in message:
                    pos = str.find(letter)
                    encodedMessage = encodedMessage + eStr[pos:pos+1]
                print(encodedMessage)

        .. tab:: Answer

            Initialize decodedMessage and then iterate through encodedMessage and in the body of the for loop, just switch eStr and str from the encoded message.

            .. activecode::  ch9ex20a
                :nocodelens:

                message = "meet me at midnight"
                str = "abcdefghijklmnopqrstuvwxyz. "
                eStr = "zyxwvutsrqponmlkjihgfedcba ."
                encodedMessage = ""
                for letter in message:
                    pos = str.find(letter)
                    encodedMessage = encodedMessage + eStr[pos:pos+1]
                print(encodedMessage)

                decodedMessage = ""
                for letter in encodedMessage:
                    pos = eStr.find(letter)
                    decodedMessage = decodedMessage + str[pos:pos+1]
                print(decodedMessage)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch9ex20q
