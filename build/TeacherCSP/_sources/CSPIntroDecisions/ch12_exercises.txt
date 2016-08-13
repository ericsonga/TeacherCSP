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
	:prefix: 12-10-

Chapter 12 Exercises
---------------------

#. 

    .. tabbed:: ch12ex1t

        .. tab:: Question
            
            Fix 3 syntax errors in the code below so that it correctly prints "x is less than 3" and then "All done" when x is less than 3.

            .. activecode:: ch12ex1q
                :nocodelens:

                x = 0
                if x < 3
                print ("x is less than 3")
                print ("All done)
      	            
        .. tab:: Answer
        
            Add a ``:`` at the end of line 2.  Indent line 3.  Add a ``"`` before the ``)`` in line 4.  
            
            .. activecode:: ch12ex1a
                :nocodelens:

                x = 0
                if x < 3:
                    print ("x is less than 3")
                print ("All done")

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch12ex1q
                
#. 
   
    .. tabbed:: ch12ex2t

        .. tab:: Question

           Fix the indention in the code below to use a price of 1.45 if the weight is less than 1 and a price of 1.15 otherwise.  There is also one syntax error.
           
           .. activecode::  ch12ex2q
                :nocodelens:

                weight = 0.5
                if weight < 1:
                price = 1.45
                if weight >= 1
                price = 1.15
                total = weight * price
                print(weight)
                print(price)
                print(total)




        .. tab:: Answer
        
            Change the indention on lines 3 and 5 and add a ``:`` at the end of line 4.  
            
            .. activecode::  ch12ex2a
                :nocodelens:
                
                weight = 0.5
                if weight < 1:
                    price = 1.45
                if weight >= 1:
                    price = 1.15
                total = weight * price
                print(weight)
                print(price)
                print(total)

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex2q

#. 

    .. tabbed:: ch12ex3t

        .. tab:: Question

           Fix 3 errors with indention in the code below to correctly set the price to 1.5 if the weight is less than 2 and otherwise set it to 1.3.  
        
           .. activecode::  ch12ex3q
                :nocodelens:
                
                weight = 0.5
                numItems = 5
                if weight < 2:
                price = 1.50
                if weight >= 2: 
                price = 1.30
                total = weight * price
                print(weight)
                    print(price)
                print(total)         
         

        .. tab:: Answer
        
            Indent lines 4 and 6.  Remove the indention on line 9.  
            
            .. activecode::  ch12ex3a
                :nocodelens:

                weight = 0.5
                numItems = 5
                if weight < 2:
                    price = 1.50
                if weight >= 2: 
                    price = 1.30
                total = weight * price
                print(weight)
                print(price)
                print(total)



        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch12ex3q
                
#. 

    .. tabbed:: ch12ex4t

        .. tab:: Question

           Fix 4 errors in the code below to print "x is a number from 	1 to 10" when x is greater than or equal to 1 and less than or equal to 10.   
           
           .. activecode::  ch12ex4q
                :nocodelens:

                x = 3
                if x > 1 and x <= 10
                print ("x is a number from 1 to 10")
                    print ("All done")
          
        .. tab:: Answer
        
            Change line 2 to ``x >= 1`` and add a ``:`` at the end of the line.  Indent line 3.  Remove the indent on line 4.  
            
            .. activecode::  ch12ex4a
                :nocodelens:
                
                x = 3
                if x >= 1 and x <= 10:
                    print ("x is a number from 1 to 10")
                print ("All done")
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex4q
   
#. 

    .. tabbed:: ch12ex5t

        .. tab:: Question

           Finish the conditional on line 3 to print "You can go out!" if either cleanedRoom or finishedHomework is true (not 0). It should always print "All done" as well.
           
           .. activecode::  ch12ex5q
                :nocodelens:

                cleanedRoom = 1
                finishedHomework = 0
                if 
                    print ("You can go out!")
                print ("All done")

        .. tab:: Answer
        
            Add ``cleanedRoom or finishedHomework:`` to line 3.  
            
            .. activecode::  ch12ex5a
                :nocodelens:

                cleanedRoom = 1
                finishedHomework = 0
                if cleanedRoom or finishedHomework:
                    print ("You can go out!")
                print ("All done")

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex5q
                
#. 

    .. tabbed:: ch12ex6t

        .. tab:: Question

           Fix 5 errors in the following code to set the price to 1.45 if the weight is less than or equal to 1 and otherwise set it to 1.15.
           
           .. activecode::  ch12ex6q
                :nocodelens: 
                
                weight = 0.5
                if weight < 1:
                price = 1.45
                if weight > 1:
                price = 1.15
                total = weight * price
                print(weigh)
                print(Price)
                print(total)

        .. tab:: Answer
        
            Indent lines 3 and 5.  Change line 2 to ``<=``.  Change line 7 to ``weight``.  Change line 8 to ``price``.
            
            .. activecode::  ch12ex6a
                :nocodelens:
                
                weight = 0.5
                if weight <= 1:
                    price = 1.45
                if weight > 1:
                    price = 1.15
                total = weight * price
                print(weight)
                print(price)
                print(total)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex6q
                
#. 

    .. tabbed:: ch12ex7t

        .. tab:: Question

           Change 3 lines in the code below to correctly set the grade so that a 90 and above is an A, 80-89 is a B, 70 - 79 is a C, 60-69 is a D and below 60 is an E.  
           
           .. activecode::  ch12ex7q
                :nocodelens: 
                
                score = 93
                if score >= 90:
                    grade = "A"
                if score >= 80:
                    grade = "B"
                if score >= 70:
                    grade = "C"
                if score >= 60:
                    grade = "D"
                if score < 60:
                   grade = "E"
                print(grade)
                
                

        .. tab:: Answer
        
            Change lines 4, 6, and 8 as shown below.
            
            .. activecode::  ch12ex7a
                :nocodelens
                
                score = 93
                if score >= 90:
                    grade = "A"
                if score >= 80 and score <= 89:
                    grade = "B"
                if score >= 70 and score <= 79:
                    grade = "C"
                if score >= 60 and score <= 69:
                    grade = "D"
                if score < 60:
                   grade = "E"
                print(grade)
                
                
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex7q
                
#. 

    .. tabbed:: ch12ex8t

        .. tab:: Question

           Fix 5 errors in the following code to set price to 1.45 if weight is less than 1 and otherwise set it to 1.15.  
           
           .. activecode::  ch12ex8q
                :nocodelens:
                
                weight = 0.5
                if weight < 1
                price = 1.45
                else
                price = 1.15
                total = weight * price
                print(weight)
                print(price
                print(Total)

        .. tab:: Answer
        
            Add ``:`` at the end of lines 2 and 4.  Indent lines 3 and 5.  Add a ``)`` at the end of line 8.  Change line 9 to ``total``.  
            
            .. activecode::  ch12ex8a
                :nocodelens:
                
                weight = 0.5
                if weight < 1:
                    price = 1.45
                else:
                    price = 1.15
                total = weight * price
                print(weight)
                print(price)
                print(total)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex8q
                
#. 

    .. tabbed:: ch12ex9t

        .. tab:: Question

           Write a procedure that will print out "even" if the passed value is even and "odd" if the passed value is odd.  Test both possibilities.  
           
           .. activecode::  ch12ex9q
                :nocodelens:

        .. tab:: Answer
        
            Define the procedure as shown below and be sure to test it.
            
            .. activecode::  ch12ex9a
                :nocodelens:
                
                def printIfEvenOrOdd(x):
                    if x % 2 == 0:
                        print("x is even")
                    else: 
                        print("x is odd")
                        
                printIfEvenOrOdd(92)
                printIfEvenOrOdd(5)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex9q
                
#. 

    .. tabbed:: ch12ex10t

        .. tab:: Question

           Write a function that takes a number for a grade and returns a string grade.  It should return E for any value below 60, D for 61 to 69, C for 70 to 79, B for 80 to 89 and A for 90 and above.  Write code to test each grade range.
           
           .. activecode::  ch12ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create a function as shown below.  Call it to test it and print the result.
            
            .. activecode::  ch12ex10a
                :nocodelens:
                
                def getGrade(x):
                    if x >= 90:
                       return "A"
                    if x >= 80 and x < 90:
                       return "B"
                    if x >= 70 and x < 80:
                       return "C"
                    if x >= 60 and x < 70:
                       return "D"
                    if x < 60:
                       return "E"
                        
                print(getGrade(95))
                print(getGrade(90))
                print(getGrade(85))
                print(getGrade(80))
                print(getGrade(75))
                print(getGrade(70))
                print(getGrade(65))
                print(getGrade(60))
                print(getGrade(55))
                print(getGrade(50))
                print(getGrade(0))
                
        
                        
                                 
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch12ex10q



