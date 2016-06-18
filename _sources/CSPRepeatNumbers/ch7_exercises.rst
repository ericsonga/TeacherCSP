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

            Fix the errors in the code so that it prints the sum of all the numbers 1 to 10.

            .. activecode::  ch7ex2q
                :nocodelens:

                sum = 0
                numList = range(1,10)
                for number in numList:
                    sum = number
                print(sum)

        .. tab:: Answer

            On line 2, the range has to be (1,11) because the second number is not inclusive. Also, the sum has to be equal to the sum plus the new number. Otherwise the sum would just be the last number in the iteration.

            .. activecode::  ch7ex2a
                :nocodelens:

                sum = 0
                numList = range(1,11)
                for number in numList:
                	sum = sum + number
                print(sum)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex2q

#.

    .. tabbed:: ch7ex3t

        .. tab:: Question

           Change the code below into a function that returns the sum of a list of numbers.  Pass the list of numbers as a parameter and print the result of calling the function.

           .. activecode::  ch7ex3q
                :nocodelens:

                sum = 0  # Start out with nothing
                thingsToAdd = [1,2,3,4,5]
                for number in thingsToAdd:
    	            sum = sum + number
                print(sum)


        .. tab:: Answer

            Create a function as shown below that takes a list of numbers as input. Return the sum.  Call the function with a list of numbers from 1 to 5 and print the result to test the function.

            .. activecode::  ch7ex3a
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
                :identifier: teachercsp_ch7ex3q

#.

    .. tabbed:: ch7ex4t

        .. tab:: Question

            Fix the errors in the code so that it prints the product of every 5 numbers between 5 and 25.

            .. activecode::  ch7ex4q
                :nocodelens:

                product = 0
                numbers = len(4,25,5)
                for number in numbers:
                	product = product + number
                print(product)

        .. tab:: Answer

            Product should be initialized to equal 1 on line 1. On line 2, it should be the range function, and it should be ``range(5,26,5)`` because the first number is inclusive and the second is exclusive.

            .. activecode::  ch7ex4a
                :nocodelens:

                product = 1
                numbers = range(5,26,5)
                for number in numbers:
                	product = product * number
                print(product)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex4q

#.

    .. tabbed:: ch7ex5t

        .. tab:: Question

           Fill in the missing code on lines 3 and 4 to loop through the list of numbers and calculate the product.  Add a line at the end to print the value in ``product``.

           .. activecode::  ch7ex5q
                :nocodelens:

                product = 1  # Start out with nothing
                numbers = [1,2,3,4,5]
                for in numbers:
    	            product = product *


        .. tab:: Answer

            Change line 3 to create a variable ``number`` that will take on the next value in the list each time through the loop.  Set ``product`` in line 4 to ``product * number``.  Print the result when the loop has finished.

            .. activecode::  ch7ex5a
                :nocodelens:

                product = 1  # Start out with nothing
                numbers = [1,2,3,4,5]
                for number in numbers:
    	            product = product * number
                print(product)


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch7ex5q

#.

    .. tabbed:: ch7ex6t

        .. tab:: Question

            Fix the errors in the code so that it prints the sum of all the odd numbers 1 through 20.

            .. activecode::  ch7ex6q
                :nocodelens:

                sum = 1
                numbers = range(1,21,1)
                for numbers in number:
                sum = sum + number
                print(sum)

        .. tab:: Answer

            In line 1, sum should be initialized to equal 0. In line 2, the third argument of the range function should be 2 because it is the step size.

            .. activecode::  ch7ex6a
                :nocodelens:

                sum = 0
                numbers = range(1,21,2)
                for number in numbers:
                	sum = sum + number
                print(sum)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex6q

#.

    .. tabbed:: ch7ex7t

        .. tab:: Question

           Modify the code below to create a function that calculates the product of a list of numbers and returns it. Have the function take a list of numbers as a parameter.  Call the function to test it and print the result of calling the function.

           .. activecode::  ch7ex7q
                :nocodelens:

                product = 1  # Start out with 1
                numbers = [1,2,3,4,5]
                for number in numbers:
    	            product = product * number
                print(product)

        .. tab:: Answer

            Define the function and create a parameter to take a list of numbers called ``numbers``.  Print the result of calling the function with a list of numbers.

            .. activecode::  ch7ex7a
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
                :identifier: teachercsp_ch7ex7q

#.

    .. tabbed:: ch7ex8t

        .. tab:: Question

            Fix the error in the code so that it takes each string in the list and prints out the sentence "I like to eat pizza".

            .. activecode::  ch7ex8q
                :nocodelens:

                aString = ""
                aList = ["I", "like", "to", "eat", "pizza"]
                for word in aList:
                	aString = word
                	print(aString)

        .. tab:: Answer

            On line 4, aString should be equal to itself plus the new word.

            .. activecode::  ch7ex8a
                :nocodelens:

                aString = ""
                aList = ["I", "like", "to", "eat", "pizza"]
                for word in aList:
                	aString = aString + word
                print(aString)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex8q

#.

    .. tabbed:: ch7ex9t

        .. tab:: Question

           Fill in the code below on lines 2, 4, and 6 to correctly add up and print the sum of all the even numbers from 0 to 10 (inclusive).

           .. activecode::  ch7ex9q
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

            .. activecode::  ch7ex9a
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
                :identifier: teachercsp_ch7ex9q

#.

    .. tabbed:: ch7ex10t

        .. tab:: Question

            Write code that prints the square of each number 1 through 10 in the format "1 * 1 = 1", etc.

            .. activecode::  ch7ex10q
                :nocodelens:


        .. tab:: Answer

            You need to get a list of the numbers using ``range(1,11)`` and then iterate through the list and multiply each number by itself.

            .. activecode::  ch7ex10a
                :nocodelens:

                numbers = range(1, 11)
                for number in numbers:
                	numString = number
                	square = str(number * number)
                	print(numString + " * " + numString + " = " + square)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex10q

#.

    .. tabbed:: ch7ex11t

        .. tab:: Question

           Define a function to calculate the sum of the even numbers from 0 to the passed number.  Return the sum from the function.  Call the function and print the result.

           .. activecode::  ch7ex11q
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

            .. activecode::  ch7ex11a
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
                :identifier: teachercsp_ch7ex11q

#.

    .. tabbed:: ch7ex12t

        .. tab:: Question

            Create a function that returns the factorial of a passed number and call the function and print the result.

            .. activecode::  ch7ex12q
                :nocodelens:


        .. tab:: Answer

            Use the range function from 1 to n + 1 where n is the parameter given to get a list of the numbers. Then get the product of the product times the number.

            .. activecode::  ch7ex12a
                :nocodelens:

                def factorial(n):
            	product = 1
            	numbers = range(1, n+1)
            	for number in numbers:
            		product = product * number
            	return product
                print(factorial(5))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex12q

#.

    .. tabbed:: ch7ex13t

        .. tab:: Question

           Fix the code below to correctly calculate and return the product of all of the even numbers from 10 to 20.

           .. activecode::  ch7ex13q
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

            .. activecode::  ch7ex13a
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
                :identifier: teachercsp_ch7ex13q

#.

    .. tabbed:: ch7ex14t

        .. tab:: Question

            Create a list of all odd numbers from 1 to 20 and find the average. Then create a list of numbers from 1 to 100 using the average as the increment and print the product of those numbers.

            .. activecode::  ch7ex14q
                :nocodelens:

        .. tab:: Answer
            Use the range function with from 1 to 20 (21 would work too) and a step size of 2. Get the sum of all those numbers and use the length of the list to find the average. Then use the range function again with a step size of the average and find the product of all the numbers in the new list.

            .. activecode::  ch7ex14a
                :nocodelens:

                sum = 0
                numbers = range(1,20,2)
                for number in numbers:
                  	sum = sum + number
                average = sum / len(numbers)
                product = 1
                numbers2 = range(1,101, average)
                for number in numbers2:
                	product = product * number
                print(product)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex14q

#.

    .. tabbed:: ch7ex15t

        .. tab:: Question

           Create a procedure to calculate and return the sum of all of the odd numbers from 1 to a passed last number (inclusive).  Call the function to test and it print the result.

           .. activecode::  ch7ex15q
                :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch7ex15a
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
                :identifier: teachercsp_ch7ex15q

#.

    .. tabbed:: ch7ex16t

        .. tab:: Question

            Complete the code for a function that takes a list of letters and combines them into a word. It should print "Hi".

            .. activecode::  ch7ex16q
                :nocodelens:

                def letterCombiner( ):
                	tempString =
                	for  in letterList:
                		tempString = tempString + letter
                	return

                aList = ["H", "i"]
                print(letterCombiner( ))

        .. tab:: Answer

            On line 1, you have to put ``letterList`` as a parameter. On line 2, ``tempString`` has to equal an empty string. Line 3 should read ``for letter in letterList``. Line 5 should return the ``tempString`` and Line 8 should take aList as an argument.

            .. activecode::  ch7ex16a
                :nocodelens:

                def letterCombiner(letterList):
                	tempString = ""
                	for letter in letterList:
                		tempString = tempString + letter
                	return tempString

                aList = ["H", "i"]
                print(letterCombiner(aList))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex16q

#.

    .. tabbed:: ch7ex17t

        .. tab:: Question

           Create a function to calculate and return the product of all of the even numbers from 2 to the passed end number (inclusive).  Be sure to call the function to test it and print the result.

           .. activecode::  ch7ex17q
                :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch7ex17a
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
                :identifier: teachercsp_ch7ex17q

#.

    .. tabbed:: ch7ex18t

        .. tab:: Question

            Write a function that takes two inputs, a start and stop for a range (inclusive). Find the product and the sum of all the numbers and return the average between those two numbers. make a call to the function where you print the result

            .. activecode::  ch7ex18q
                :nocodelens:


        .. tab:: Answer

            The function should use the range from parameter 1 to parameter 2 + 1 in order to make it inclusive of the given stop argument. Don't forget to initialize the product variable as 1 and the sum as 0.

            .. activecode::  ch7ex18a
                :nocodelens:

                def aFunc(start, stop):
                	sum = 0
                	product = 1
                	numbers = range(start, stop + 1)
                	for number in numbers:
                		sum = sum + number
                		product = product * number
                	average = (sum + porduct) / 2
                	return average
                print(aFunc(1, 10))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex18q

#.

    .. tabbed:: ch7ex19t

        .. tab:: Question

           Write a function that will take a list of numbers and return the average.  Remember that the average is the sum of all of the numbers in the list divided by the number of items in the list.  You can get the length of a list using the ``len(list)`` function.

           .. activecode::  ch7ex19q
               :nocodelens:

        .. tab:: Answer

            Create the function and be sure to call it to test it.

            .. activecode::  ch7ex19a
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
                :identifier: teachercsp_ch7ex19q

#.

    .. tabbed:: ch7ex20t

        .. tab:: Question

            Create a function that takes one integer parameter and gets a list of all the odd numbers in that range and all the even numbers in that range. Find the product of all the even numbers, the sum of all the odd numbers, and then return the difference of the product by the sum and divide by the average of the two. Call the function and print the result.

            .. activecode::  ch7ex20q
                :nocodelens:


        .. tab:: Answer

            You have to use the range function twice and do two different for loops.

            .. activecode::  ch7ex20a
                :nocodelens:

                def aFunc(stop):
                	evens = range(0, stop + 1, 2)
                	odds = range( 1, stop + 1, 2)
                	product = 1
                	sum = 0
                	for n in evens:
                		product = produt * n
                	for n in odds:
                		sum = sum + n
                	difference = product - sum
                	average = (product + sum) / 2
                	return difference/ average
                print(aFunc(10))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch7ex20q
