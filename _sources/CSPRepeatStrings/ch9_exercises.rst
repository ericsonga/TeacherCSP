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

           Fix the indention on 4 lines below to correctly print the reverse of the string.  It should print: "!yadhtriB yppaH."
           
           .. activecode::  ch9ex2q
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
            
            .. activecode::  ch9ex2a
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
                :identifier: teachercsp_ch9ex2q

#. 

    .. tabbed:: ch9ex3t

        .. tab:: Question

           Fix 4 errors in the code below to correctly print the mirror of the text in phrase.  Is should print: "tset a si sihTThis is a test."  
        
           .. activecode::  ch9ex3q
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
            
            .. activecode::  ch9ex3a
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
                :identifier: teachercsp_ch9ex3q
                
#. 

    .. tabbed:: ch9ex4t

        .. tab:: Question

           The code below is supposed to replace all 1's with i's, but it is in an infinite loop.  You can reload the page to stop the infinite loop.  Add a line to make the code work.  It should print: "This is a string."
           
           .. activecode::  ch9ex4q
                :nocodelens:

                str = "Th1s is a str1ng"
                pos = str.find("1")
                while pos >= 0:
                    str = str[0:pos] + "i" + str[pos+1:len(str)]
                print(str)
          
        .. tab:: Answer
        
            Add line 5 as shown below.
            
            .. activecode::  ch9ex4a
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
                :identifier: teachercsp_ch9ex4q
   
#. 

    .. tabbed:: ch9ex5t

        .. tab:: Question

           The program below is supposed to encode the text in message, but it has 5 errors.  Fix the errors so that it prints: "nvvg.nv.zg.nrwmrtsg."
           
           .. activecode::  ch9ex5q
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
            
            .. activecode::  ch9ex5a
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
                :identifier: teachercsp_ch9ex5q
                
#. 

    .. tabbed:: ch9ex6t

        .. tab:: Question

           Rewrite the following code to create a function that takes a string and returns the reverse of the string.  It should print: "!yadhtriB yppaH."
           
           .. activecode::  ch9ex6q
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
            
            .. activecode::  ch9ex6a
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
                :identifier: teachercsp_ch9ex6q
                
#. 

    .. tabbed:: ch9ex7t

        .. tab:: Question

           Rewrite the following code to create a function that takes a string and returns the mirror of the string.  It should print: "!ssalC iHHi Class!".
           
           .. activecode::  ch9ex7q
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
            
            .. activecode::  ch9ex7a
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
                :identifier: teachercsp_ch9ex7q
                
#. 

    .. tabbed:: ch9ex8t

        .. tab:: Question

           Modify the code below to create a function that will that will take a message and return an encoded message.  It should print: "nvvg.nv.zg.nrwmrtsg."
           
           .. activecode::  ch9ex8q
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
            
            .. activecode::  ch9ex8a
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
                :identifier: teachercsp_ch9ex8q
                
#. 

    .. tabbed:: ch9ex9t

        .. tab:: Question

           Modify the code below to create a function that returns the decoded input string.  It should print: "meet me at midnight."
           
           .. activecode::  ch9ex9q
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
            
            .. activecode::  ch9ex9a
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
                :identifier: teachercsp_ch9ex9q
                
#. 

    .. tabbed:: ch9ex10t

        .. tab:: Question

           Create another function that encodes a string.  Pass in both the string to be encoded *and* the string to use to encode the string as well.  
           
           .. activecode::  ch9ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create a function similar to the encode function above, but change it to take two input values.  
            
            .. activecode::  ch9ex10a
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
                :identifier: teachercsp_ch9ex10q



