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
	:prefix: 7-8-

Chapter 7 Exercises
--------------------

#. 

    .. tabbed:: ch7ex1t

        .. tab:: Question
            
            Complete lines 1 and 2 below to create the code to add up all the numbers from 1 to 5 and print the sum. 

            .. activecode:: ch7ex1q
                :nocodelens:

                sum =    
                thingsToAdd = 
                for number in thingsToAdd:
    	            sum = sum + number
                print(sum)                

        .. tab:: Answer
        
            Set the sum to 0 in line 1.  Create a list ``[1,2,3,4,5]`` in line2.    

            .. activecode:: ch7ex1a
                :nocodelens:

                sum = 0  # Start out with nothing
                thingsToAdd = [1,2,3,4,5]
                for number in thingsToAdd:
    	            sum = sum + number
                print(sum) 

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch7ex1q
                
#. 
   
    .. tabbed:: ch7ex2t

        .. tab:: Question

           Change the code below into a function that returns the sum of a list of numbers.  Pass the list of numbers as a parameter and print the result of calling the function.
           
           .. activecode::  ch7ex2q
                :nocodelens:

                sum = 0  # Start out with nothing
                thingsToAdd = [1,2,3,4,5]
                for number in thingsToAdd:
    	            sum = sum + number
                print(sum) 


        .. tab:: Answer
        
            Create a function as shown below that takes a list of numbers as input. Return the sum.  Call the function with a list of numbers from 1 to 5 and print the result to test the function.
            
            .. activecode::  ch7ex2a
                :nocodelens:
                
                def sumNums(numList):
                    sum = 0
                    for number in numList:
                        sum = sum + number
                    return sum

                aList = [1,2,3,4,5]
                print(sumNums(aList))
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex2q

#. 

    .. tabbed:: ch7ex3t

        .. tab:: Question

           Fill in the missing code on lines 3 and 4 to loop through the list of numbers and calculate the product.  Add a line at the end to print the value in ``product``.  
        
           .. activecode::  ch7ex3q
                :nocodelens:
                
                product = 1  # Start out with nothing
                numbers = [1,2,3,4,5]
                for in numbers:
    	            product = product *
         

        .. tab:: Answer
        
            Change line 3 to create a variable ``number`` that will take on the next value in the list each time through the loop.  Set ``product`` in line 4 to ``product * number``.  Print the result when the loop has finished.  
            
            .. activecode::  ch7ex3a
                :nocodelens:

                product = 1  # Start out with nothing
                numbers = [1,2,3,4,5]
                for number in numbers:
    	            product = product * number
                print(product)
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch7ex3q
                
#. 

    .. tabbed:: ch7ex4t

        .. tab:: Question

           Modify the code below to create a function that calculates the product of a list of numbers and returns it. Have the function take a list of numbers as a parameter.  Call the function to test it and print the result of calling the function.   
           
           .. activecode::  ch7ex4q
                :nocodelens:

                product = 1  # Start out with 1
                numbers = [1,2,3,4,5]
                for number in numbers:
    	            product = product * number
                print(product)
          
        .. tab:: Answer
        
            Define the function and create a parameter to take a list of numbers called ``numbers``.  Print the result of calling the function with a list of numbers.  
            
            .. activecode::  ch7ex4a
                :nocodelens:

                def calculateProduct(numbers):
                    product = 1  # Start out with 1
                    for number in numbers:
    	                product = product * number
                    return(product)
                
                numbers = [1,2,3,4,5]
                print(calculateProduct(numbers))
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex4q
   
#. 

    .. tabbed:: ch7ex5t

        .. tab:: Question

           Fill in the code below on lines 2, 4, and 6 to correctly add up and print the sum of all the even numbers from 0 to 10 (inclusive).
           
           .. activecode::  ch7ex5q
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR 
                sum =   # Start out with nothing
                # STEP 2: GET DATA
                numbers = range()
                # STEP 3: LOOP THROUGH THE DATA
                for number in numbers:
    	            # STEP 4: ACCUMULATE
    	           sum = sum +
                # STEP 5: PROCESS RESULT
                print(sum)

        .. tab:: Answer
        
            Initialize the sum to 0.  Create a range from 0 to 11 with a step of 2.  Set the sum to the current value of sum plus the value of number.
            
            .. activecode::  ch7ex5a
                :nocodelens:

                # STEP 1: INITIALIZE ACCUMULATOR 
                sum = 0  # Start out with nothing
                # STEP 2: GET DATA
                numbers = range(0,11,2)
                # STEP 3: LOOP THROUGH THE DATA
                for number in numbers:
    	            # STEP 4: ACCUMULATE
    	            sum = sum + number
                # STEP 5: PROCESS RESULT
                print(sum)

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex5q
                
#. 

    .. tabbed:: ch7ex6t

        .. tab:: Question

           Define a function to calculate the sum of the even numbers from 0 to the passed number.  Return the sum from the function.  Call the function and print the result.
           
           .. activecode::  ch7ex6q
                :nocodelens: 
                
                # STEP 1: INITIALIZE ACCUMULATOR 
                sum = 0  # Start out with nothing
                # STEP 2: GET DATA
                numbers = range(0,21,2)
                # STEP 3: LOOP THROUGH THE DATA
                for number in numbers:
    	            # STEP 4: ACCUMULATE
    	           sum = sum + number
                # STEP 5: PROCESS RESULT
                print(sum)

        .. tab:: Answer
        
            Define a function that takes the ``lastNum`` as a parameter.  Get a list of the even numbers between 0 and lastNum using ``range(0,lastNum+1,2)``.  Return the sum.  Call the function and print the result.
            
            .. activecode::  ch7ex6a
                :nocodelens:
                
                def sumEvens(lastNum):
                    # STEP 1: INITIALIZE ACCUMULATOR 
                    sum = 0  # Start out with nothing
                    # STEP 2: GET DATA
                    numbers = range(0,lastNum+1,2)
                    # STEP 3: LOOP THROUGH THE DATA
                    for number in numbers:
    	                # STEP 4: ACCUMULATE
    	                sum = sum + number
                    # STEP 5: PROCESS RESULT
                    return(sum)

                print(sumEvens(20))
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex6q
                
#. 

    .. tabbed:: ch7ex7t

        .. tab:: Question

           Fix the code below to correctly calculate and return the product of all of the even numbers from 10 to 20. 
           
           .. activecode::  ch7ex7q
                :nocodelens: 
                
                # STEP 1: INITIALIZE ACCUMULATOR 
                product = 0  # init product
                # STEP 2: GET DATA
                numbers = range(10,20,2)
                # STEP 3: LOOP THROUGH THE DATA
                for number in numbers:
    	            # STEP 4: ACCUMULATE
    	           product = product + number
                # STEP 5: PROCESS RESULT
                print(product)         

        .. tab:: Answer
        
            Change line 2 to initialze ``product`` to 1 instead of 0.  Change line 4 to ``range(10,21,2)``.  Change line 8 to ``product = product * number``. 
            
            .. activecode::  ch7ex7a
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
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex7q
                
#. 

    .. tabbed:: ch7ex8t

        .. tab:: Question

           Create a procedure to calculate and return the sum of all of the odd numbers from 1 to a passed last number (inclusive).  Call the function to test and it print the result.
           
           .. activecode::  ch7ex8q
                :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch7ex8a
                :nocodelens:
                
                def sumOdd(lastNumber):
                    sum = 0
                    numList = range(1,lastNumber+1,2)
                    for num in numList:
                        sum = sum + num
                    return sum

                print(sumOdd(13))
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex8q
                
#. 

    .. tabbed:: ch7ex9t

        .. tab:: Question

           Create a function to calculate and return the product of all of the even numbers from 2 to the passed end number (inclusive).  Be sure to call the function to test it and print the result.
           
           .. activecode::  ch7ex9q
                :nocodelens:

        .. tab:: Answer
        
            Create the procedure and be sure to call it to test it.
            
            .. activecode::  ch7ex9a
                :nocodelens:
                
                def calculateProduct(lastNum):
                    total = 1
                    numList = range(2, lastNum + 1, 2)
                    for num in numList:
                        total = total * num
                    return total
                    
                print(calculateProduct(8))
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex9q
                
#. 

    .. tabbed:: ch7ex10t

        .. tab:: Question

           Write a function that will take a list of numbers and return the average.  Remember that the average is the sum of all of the numbers in the list divided by the number of items in the list.  You can get the length of a list using the ``len(list)`` function.
           
           .. activecode::  ch7ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create the function and be sure to call it to test it.
            
            .. activecode::  ch7ex10a
                :nocodelens:
                
                def getAverage(numList):
                    sum = 0
                    for num in numList:
                        sum = sum + num
                    return sum / len(numList)
                
                numberList = [90, 80, 75, 90, 83]
                print(getAverage(numberList))
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex10q



