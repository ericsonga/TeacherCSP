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
	:prefix: 8-8-

Chapter 8 Exercises
--------------------

#. 

    .. tabbed:: ch8ex1t

        .. tab:: Question
            
            Fix the 5 syntax errors in the code below to print a countdown of the numbers from 10 to 0.  

            .. activecode:: ch8ex1q
                :nocodelens:

                counter = 10
                while Counter > 0:
                    Print(counter)
                    counter = Counter + 1                 

        .. tab:: Answer
        
            Change ``Counter`` to ``counter`` on lines 2 and 4.  Loop while ``counter`` is greater than or equal to 0.  Change the ``Print`` to ``print``.  Change the last line to subtract one rather than add it.

            .. activecode:: ch8ex1a
                :nocodelens:

                counter = 10
                while counter >= 0:
                    print(counter)
                    counter = counter - 1  

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch8ex1q
                
#. 
   
    .. tabbed:: ch8ex2t

        .. tab:: Question

           Make 5 changes to the code below to correctly print a count up from -10 to 0.  
           
           .. activecode::  ch8ex2q
                :nocodelens:

                output = ""
                x = -10
                while x < 0
                    x = x - 1
                output = output + str(x) + " "
                print(output)


        .. tab:: Answer
        
            Change the ``while`` to less than or equal zero.  Add a ``:`` at the end.  Change it to ``x = x + 1`` and move it after ``output = output + str(x) + " "``.  Indent the ``output = output + str(x) + " "``.
            
            .. activecode::  ch8ex2a
                :nocodelens:
                
                output = ""
                x = -10
                while x <= 0:
                    output = output + str(x) + " "
                    x = x + 1
                print(output)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex2q

#. 

    .. tabbed:: ch8ex3t

        .. tab:: Question

           Finish lines 1 and 5 so that the following code correct prints all the values from -5 to -1.  
        
           .. activecode::  ch8ex3q
                :nocodelens:
                
                output = 
                x = -5
                while x < 0:
                    output = output + str(x) + " "
                    x = 
                print(output)
         

        .. tab:: Answer
        
            Change line 1 to set output to the empty string (``""``).  Change line 5 to ``x = x + 1``.
            
            .. activecode::  ch8ex3a
                :nocodelens:

                output = ""
                x = -5
                while x < 0:
                    output = output + str(x) + " "
                    x = x + 1
                print(output)
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch8ex3q
                
#. 

    .. tabbed:: ch8ex4t

        .. tab:: Question

           The code below is supposed to print an estimate of the square root.  But, the indention is wrong on 4 lines.  Fix it.
           
           .. activecode::  ch8ex4q
                :nocodelens:

                target = 6
                    guess = 2
                guessSquared = guess * guess
                while abs(target-guessSquared) > 0.01:
                    closer = target / guess
                guess = (guess + closer) / 2.0
                        guessSquared = guess * guess
                    print("Square root of", target,"is", guess)
          
        .. tab:: Answer
        
            Don't indent line 2.  Indent line 6 under line 5.  Indent line 7 at the same level as line 5.  Don't indent line 8.
            
            .. activecode::  ch8ex4a
                :nocodelens:
                
                target = 6
                guess = 2
                guessSquared = guess * guess
                while abs(target-guessSquared) > 0.01:
                    closer = target / guess
                    guess = (guess + closer) / 2.0
                    guessSquared = guess * guess
                print("Square root of", target,"is", guess)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex4q
   
#. 

    .. tabbed:: ch8ex5t

        .. tab:: Question

           The program below is supposed to print the times tables for 1 to 3, but there are 5 errors.  Fix the errors.
           
           .. activecode::  ch8ex5q
                :nocodelens:

                for x in range(1,3):
                     for y in range(1,10)
                         print(str(x) + " * " str(y) + " = " x*y)

        .. tab:: Answer
        
            Change line 1 to end the range at 4.  Change line 2 to end the range at 11 and add the ``:`` at the end.  Fill in the missing ``+`` between strings in line 3 and add ``str(x*y)``.
            
            .. activecode::  ch8ex5a
                :nocodelens:

                for x in range(1,4):
                     for y in range(1,11):
                         print(str(x) + " * " + str(y) + " = " + str(x*y))

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex5q
                
#. 

    .. tabbed:: ch8ex6t

        .. tab:: Question

           Rewrite the following code to use a while loop instead of a for loop.
           
           .. activecode::  ch8ex6q
                :nocodelens: 
                
                product = 1  # Start out with nothing
                numbers = range(1,11)
                for number in numbers:
                    product = product * number
                print(product)

        .. tab:: Answer
        
            Change line 2 to create number and set it to 1.  Change line 3 to loop while the number is less than 11.  Add a line before the print statement to increment number.
            
            .. activecode::  ch8ex6a
                :nocodelens:
                
                product = 1  # Start out with nothing
                number = 1
                while number < 11:
                    product = product * number
                    number = number + 1
                print(product)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex6q
                
#. 

    .. tabbed:: ch8ex7t

        .. tab:: Question

           Rewrite the following code to use a while loop instead of a for loop. 
           
           .. activecode::  ch8ex7q
                :nocodelens: 
                
                # STEP 1: INITIALIZE ACCUMULATOR 
                product = 1  # init product to 1
                # STEP 2: GET DATA
                numbers = range(10,21,2)
                # STEP 3: LOOP THROUGH THE DATA
                for number in numbers:
    	            # STEP 4: ACCUMULATE
    	           product = product * number
                # STEP 5: PROCESS RESULT
                print(product) 
                        

        .. tab:: Answer
        
            Change line 4 to only create and initialize number.  Change line 6 to loop while number is less than 21.  Add a step 5 where the value of number is set to the current value plus 2.
            
            .. activecode::  ch8ex7a
                :nocodelens:
                
                # STEP 1: INITIALIZE ACCUMULATOR 
                product = 1  # init product to 1
                # STEP 2: INIT THE DATA
                number = 10
                # STEP 3: LOOP THROUGH THE DATA
                while number < 21:
    	            # STEP 4: ACCUMULATE
    	            product = product * number
    	            # STEP 5: change the number
    	            number = number + 2
                # STEP 6: PROCESS RESULT
                print(product) 
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex7q
                
#. 

    .. tabbed:: ch8ex8t

        .. tab:: Question

           Modify the code below to create a function that will take numbers as input until you enter a negative number and then will return the average of the numbers.  
           
           .. activecode::  ch8ex8q
                :nocodelens:
                
                sum = 0
                count = 0
                message = "Enter an integer or a negative number to stop"
                value = input(message)
                while int(value) > 0:
                    print("You entered " + value)
                    sum = sum + int(value)
                    count = count + 1
                    value = input(message)
                print("The sum is: " + str(sum) + 
                      " the average is: " + str(sum / count))

        .. tab:: Answer
        
            Define the function.  Return the sum divided by the count.  Call the function and print the result.
            
            .. activecode::  ch8ex8a
                :nocodelens:
                
                def calculateAverage():
                    sum = 0
                    count = 0
                    message = "Enter an integer or a negative number to stop"
                    value = input(message)
                    while int(value) > 0:
                        print("You entered " + value)
                        sum = sum + int(value)
                        count = count + 1
                        value = input(message)
                    return(sum / count)
                    
                print(calculateAverage())
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex8q
                
#. 

    .. tabbed:: ch8ex9t

        .. tab:: Question

           Create a function to calculate and return the sum of all of the even numbers from 0 to the passed number (inclusive) using a while loop.
           
           .. activecode::  ch8ex9q
                :nocodelens:

        .. tab:: Answer
        
            Create the function and be sure to call it to test it.
            
            .. activecode::  ch8ex9a
                :nocodelens:
                
                def calculateSum(lastNum):
                    sum = 0
                    num = 0
                    while (num <= lastNum):
                        sum = sum + num
                        num = num + 2
                    return sum
                    
                print(calculateSum(10))
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex9q
                
#. 

    .. tabbed:: ch8ex10t

        .. tab:: Question

           Create a procedure to print stars and spaces in a roughly square pattern and have it take as input the number of stars on a side.  Use a nested loop to do this.
           
           .. activecode::  ch8ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch8ex10a
                :nocodelens:
                
                def printSquare(numStars):
                    for x in range(0,numStars):
                        line = ""
                        for y in range(0,numStars):
                            line = line + ' *'
                        print(line)
                    
                printSquare(6)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex10q



