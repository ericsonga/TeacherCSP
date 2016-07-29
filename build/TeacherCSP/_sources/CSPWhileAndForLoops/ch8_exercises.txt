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

            The following code will loop infinitely. Make one change that will make it loop only 5 times.

            .. activecode::  ch8ex2q
                :nocodelens:

                x = 5
                while x > 0:
                    print(x)
                    x = x + 1

        .. tab:: Answer

            Since, x is already greater than zero, it will keep looping. Change line 4 to be ``x = x - 1``.

            .. activecode::  ch8ex2a
                :nocodelens:

                x = 5
                while x > 0:
                    print(x)
                    x = x - 1

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex2q

#.

    .. tabbed:: ch8ex3t

        .. tab:: Question

           Make 5 changes to the code below to correctly print a count up from -10 to 0.

           .. activecode::  ch8ex3q
                :nocodelens:

                output = ""
                x = -10
                while x < 0
                    x = x - 1
                output = output + str(x) + " "
                print(output)


        .. tab:: Answer

            Change the ``while`` to less than or equal zero.  Add a ``:`` at the end.  Change it to ``x = x + 1`` and move it after ``output = output + str(x) + " "``.  Indent the ``output = output + str(x) + " "``.

            .. activecode::  ch8ex3a
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
                :identifier: teachercsp_ch8ex3q

#.

    .. tabbed:: ch8ex4t


        .. tab:: Question

            Fix the errors in the code below so that it uses 2 loops to print 8 lines of ``*``.

            .. activecode::  ch8ex4q
                :nocodelens:

                for x in range(1,2)
                while x in range(0,4):
                print("*")

        .. tab:: Answer

            The first loop should be from range 0 to 2 (or any two numbers that are 2 numbers apart). Line 1 should also have a colon at the end and line 2 should be indented and a for loop instead of a while. Line 3 should be indented 8 spaces.

            .. activecode::  ch8ex4a
                :nocodelens:

                for x in range(0,2):
                    while x in range(0,4):
                        print("*")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex4q

#.

    .. tabbed:: ch8ex5t

        .. tab:: Question

           Finish lines 1 and 5 so that the following code correct prints all the values from -5 to -1.

           .. activecode::  ch8ex5q
                :nocodelens:

                output =
                x = -5
                while x < 0:
                    output = output + str(x) + " "
                    x =
                print(output)


        .. tab:: Answer

            Change line 1 to set output to the empty string (``""``).  Change line 5 to ``x = x + 1``.

            .. activecode::  ch8ex5a
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
                :identifier: teachercsp_ch8ex5q

#.

    .. tabbed:: ch8ex6t

        .. tab:: Question

            Complete the code on lines 4 and 6 so that it prints the number 6.

            .. activecode::  ch8ex6q
                :nocodelens:

                x = 3
                i = 0
                while i < 3:
                    x =
                    i = i + 1
                print()

        .. tab:: Answer

            Line 4 should be ``x = x + 1`` and line 6 should print x.

            .. activecode::  ch8ex6a
                :nocodelens:

                x = 3
                i = 0
                while i < 3:
                    x = x + 1
                    i = i + 1
                print(x)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex6q

#.

    .. tabbed:: ch8ex7t

        .. tab:: Question

           The code below is supposed to print an estimate of the square root.  But, the indention is wrong on 4 lines.  Fix it.

           .. activecode::  ch8ex7q
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

            .. activecode::  ch8ex7a
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
                :identifier: teachercsp_ch8ex7q

#.

    .. tabbed:: ch8ex8t

        .. tab:: Question

            The function currently takes a start and stop argument and uses a for loop to find the sum of all the numbers between them (inclusive). Change the for loop to a while loop while still using the parameters.

            .. activecode::  ch8ex8q
                :nocodelens:

                def sumFunc(start, stop):
                    sum = 0
                    for num in range(start, stop + 1):
                        sum = sum + num
                    return sum

                print(sumFunc(1,10))

        .. tab:: Answer

            Initialize num to be equal to the start argument. Make the while loop check to see if num is less than or equal to the stop argument. In the body of the while loop, make sure to increment num by 1.

            .. activecode::  ch8ex8a
                :nocodelens:

                def sumFunc(start, stop):
                    sum = 0
                    num = start
                    while num <= stop:
                        sum = sum + num
                        num = num + 1
                    return sum
                print(sumFunc(1,10))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex8q

#.

    .. tabbed:: ch8ex9t

        .. tab:: Question

           The program below is supposed to print the times tables for 1 to 3, but there are 5 errors.  Fix the errors.

           .. activecode::  ch8ex9q
                :nocodelens:

                for x in range(1,3):
                     for y in range(1,10)
                         print(str(x) + " * " str(y) + " = " x*y)

        .. tab:: Answer

            Change line 1 to end the range at 4.  Change line 2 to end the range at 11 and add the ``:`` at the end.  Fill in the missing ``+`` between strings in line 3 and add ``str(x*y)``.

            .. activecode::  ch8ex9a
                :nocodelens:

                for x in range(1,4):
                     for y in range(1,11):
                         print(str(x) + " * " + str(y) + " = " + str(x*y))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex9q

#.

    .. tabbed:: ch8ex10t

        .. tab:: Question

            Rewrite the code for the multiplication table from 1 to 2 using a while loop and a for loop instead.

            .. activecode::  ch8ex10q
                :nocodelens:

                for x in range(1,4):
                     for y in range(1,11):
                         print(str(x) + " * " + str(y) + " = " + str(x*y))

        .. tab:: Answer

            Can do in either order, but make sure the variable is being incremented for the while loop in the correct place.

            .. activecode::  ch8ex10a
                :nocodelens:

                x = 1

                while x < 3:
                    for y in range(1,11):
                        print(str(x) + " * " + str(y) + " = " + str(x*y))
                    x += 1

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex10q

#.

    .. tabbed:: ch8ex11t

        .. tab:: Question

           Rewrite the following code to use a while loop instead of a for loop.

           .. activecode::  ch8ex11q
                :nocodelens:

                product = 1  # Start out with nothing
                numbers = range(1,11)
                for number in numbers:
                    product = product * number
                print(product)

        .. tab:: Answer

            Change line 2 to create number and set it to 1.  Change line 3 to loop while the number is less than 11.  Add a line before the print statement to increment number.

            .. activecode::  ch8ex11a
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
                :identifier: teachercsp_ch8ex11q

#.

    .. tabbed:: ch8ex12t

        .. tab:: Question

            Fix the errors so that the code gets the average of the numbers from 1 to 10.

            .. activecode::  ch8ex12q
                :nocodelens:

                sum = 10
                x = 0
                while x < 11:
                sum =  x
                x = x + 1
                average = sum / 2
                print(average)

        .. tab:: Answer

            Set sum equal to 0 and x equal to 1. Indent lines 4 and 5 and on line 4, sum should equal sum plus x. The average is equal to the sum divided by x.

            .. activecode::  ch8ex12a
                :nocodelens:

                sum = 0
                x = 1
                while x < 11:
                    sum = sum + x
                    x = x + 1
                average = sum / x
                print(average)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex12q

#.

    .. tabbed:: ch8ex13t

        .. tab:: Question

           Rewrite the following code to use a while loop instead of a for loop.

           .. activecode::  ch8ex13q
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

            .. activecode::  ch8ex13a
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
                :identifier: teachercsp_ch8ex13q

#.

    .. tabbed:: ch8ex14t

        .. tab:: Question

 	    The code below currently enters a loop where it keeps printing even. Fix the code so that it prints Even and Odd for numbers 0 to 9.
 	    
            .. activecode::  ch8ex14q
                :nocodelens:

		number = 0
		while number < 10:
		    while number % 2 == 0:
		        print("Even")
		    while number % 2 != 0:
		        print("Odd")
		    number += 1
		    
        .. tab:: Answer

	    You have to increment the counter in the body of each inner loop.
	    
            .. activecode::  ch8ex14a
                :nocodelens:

		number = 0
		while number < 10:
		    while number % 2 == 0:
		        print("Even")
		        number += 1
		    while number % 2 != 0:
		        print("Odd")
		        number += 1
		        
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex14q

#.

    .. tabbed:: ch8ex15t

        .. tab:: Question

           Modify the code below to create a function that will take numbers as input until you enter a negative number and then will return the average of the numbers.

           .. activecode::  ch8ex15q
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

            .. activecode::  ch8ex15a
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
                :identifier: teachercsp_ch8ex15q

#.

    .. tabbed:: ch8ex16t

        .. tab:: Question

            Fix and change the code so it prints a table of division instead of multiplication for -10 to -1.

            .. activecode::  ch8ex16q
                :nocodelens:

                for x in range(0,11)
                for y in range(0,11):
                print(str(x) + " * " + str(y) + " = " + str(x*y))

        .. tab:: Answer

            Change the range in line 1 from -10 to 0 and add the colon. Fix the indentation in the rest of the lines and in line 3 change the string and operator to reflect division

            .. activecode::  ch8ex16a
                :nocodelens:

                for x in range(-10, 0):
                    for y in range(0,11):
                        print(str(x) + " / " + str(y) + " = " + str(x/y))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex16q

#.

    .. tabbed:: ch8ex17t

        .. tab:: Question

           Create a function to calculate and return the sum of all of the even numbers from 0 to the passed number (inclusive) using a while loop.

           .. activecode::  ch8ex17q
                :nocodelens:

        .. tab:: Answer

            Create the function and be sure to call it to test it.

            .. activecode::  ch8ex17a
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
                :identifier: teachercsp_ch8ex17q

#.

    .. tabbed:: ch8ex18t

        .. tab:: Question
        
            Write a procedure that takes a user input and keeps asking for a user input until the input is "Hello". If the input is not hello, it should print "This is you n wrong try." where n is the number of times they have put an input in. If they type "Hello", the procedure should print "Success!". Hint: ``!=`` means does not equal

            .. activecode::  ch8ex18q
                :nocodelens:


        .. tab:: Answer

            In the procedure, get an input and initialize the count. Then create the while loop with the condition that the input does not equal "Hello". Increment count first in the loop if count was initialized as 0. Increment it last if count was initialized as 1. Ask for input again in the body of the while loop.
            
            .. activecode::  ch8ex18a
                :nocodelens:

                def inputFunc():
                    userInput = input("Give me a string")
                    count = 0
                    while userInput != "Hello":
                        count += 1
                        print("This is your " + count + " wrong try.")
                        userInput = input("Give me a string")
                    print("Success!")

                inputFunc()
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex18q

#.

    .. tabbed:: ch8ex19t

        .. tab:: Question

           Create a procedure to print stars and spaces in a roughly square pattern and have it take as input the number of stars on a side.  Use a nested loop to do this.

           .. activecode::  ch8ex19q
               :nocodelens:

        .. tab:: Answer

            Create the procedure and be sure to call it to test it.

            .. activecode::  ch8ex19a
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
                :identifier: teachercsp_ch8ex19q

#.

    .. tabbed:: ch8ex20t

        .. tab:: Question

            Write a procedure that takes an int argument and uses a while loop to create a right-triangle like shape out of ``*``. The first row should have 1 star and the last should have n stars where n is the argument passed.

            .. activecode::  ch8ex20q
                :nocodelens:


        .. tab:: Answer

            Assign a counter variable to 1 and increment it in the body of the while loop.

            .. activecode::  ch8ex20a
                :nocodelens:

                def triangleDraw(n):
                    x = 1
                    while x <= n:
                        print("*" * x)
                        x += 1

                triangleDraw(6)
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch8ex20q
