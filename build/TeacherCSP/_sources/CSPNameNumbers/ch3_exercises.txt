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
	:prefix: csp-3-12-

Chapter 3 Exercises
----------------------

#. 

    .. tabbed:: ch3ex1t

        .. tab:: Question
            
            Write down what you think each of these would print, then use
            the active code window to check your results:

            #. ``9 * 5``
            #. ``2 / 5``
            #. ``5 % 2``
            #. ``9 % 5``
            #. ``6 % 6``
            #. ``2 % 7``
            #. ``3 / 0``

            .. activecode:: ch3_ex1
                :nocodelens:

               print(9 * 5)

        .. tab:: Answer

            #. ``9 * 5 = 45``
            #. ``2 / 5 = 0.4``
            #. ``5 % 2 = 1``
            #. ``9 % 5 = 4``
            #. ``6 % 6 = 0``
            #. ``2 % 7 = 2``
            #. error - you can't divide by zero

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch3ex1q
                
#. 
   
    .. tabbed:: ch3ex2t

        .. tab:: Question

           
           Add a set of parentheses to the expression  ``x = 6 * 1 - 2`` so that the code below prints -6 instead of 4.
           
           .. activecode::  ch3ex2q
               :nocodelens:

               x = 6 * 1 - 2
               print(x)  

        .. tab:: Answer
        
            Add the parentheses around the ``1 - 2`` as shown below.
            
            .. activecode::  ch3ex2a
                :nocodelens:
                
                x = 6 * (1 - 2)
                print(x)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex2q

#. 

    .. tabbed:: ch3ex3t

        .. tab:: Question

           Complete the code on lines 3 and 5 below to print the cost of a car trip of 500 miles when the car gets 26 miles per gallon and gas costs 3.45 a gallon.  It should print 66.3461538462.
        
           .. activecode::  ch3ex3q
               :nocodelens:

               miles = 500
               milesPerGallon = 26
               numGallons = 
               pricePerGallon = 3.45
               total = 
               print(total)

        .. tab:: Answer
        
            Calculate ``numGallons`` as the ``miles / milesPerGallon``.  Calculate ``total`` as ``numGallons * pricePerGallon``. 
            
            .. activecode::  ch3ex3a
                :nocanvas:

                miles = 500
                milesPerGallon = 26
                numGallons = miles / milesPerGallon
                pricePerGallon = 3.45
                total = numGallons * pricePerGallon
                print(total)
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch3ex3q
                
#. 

    .. tabbed:: ch3ex4t

        .. tab:: Question

           Complete the code on lines 4 and 5 to print how many miles you can drive on $25 if your car gets 40 miles per gallon and the price of gas is $3.65 a gallon.  It should print 273.97260274. 
           
           .. activecode::  ch3ex4q
               :nocodelens:

               funds = 25
               milesPerGallon = 40
               pricePerGallon = 3.65
               numGallons = 
               numMiles = 
               print(numMiles)
          

        .. tab:: Answer
        
            Calculate ``numGallons`` as ``funds / pricePerGallon``.  Calculate ``numMiles`` as ``milesPerGallon * numGallons``.  
            
            .. activecode::  ch3ex4a
                :nocodelens:

                funds = 25
                milesPerGallon = 40
                pricePerGallon = 3.65
                numGallons = funds / pricePerGallon
                numMiles = milesPerGallon * numGallons
                print(numMiles)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex4q
   
#. 

    .. tabbed:: ch3ex5t

        .. tab:: Question

           Complete the code on lines 3 and 7 to print the final cost for an item that is priced $68, but is 40% off the original price and you have a coupon to take an additional 20% of the sale price.  It should print 32.64.  
           
           .. activecode::  ch3ex5q
                :nocodelens:

                price = 68
                amountOff = 0.4
                saleReduction = 
                salePrice = price - saleReduction
                amountOff = 0.2
                couponReduction = salePrice * amountOff
                couponPrice = 
                print(couponPrice)

        .. tab:: Answer
        
            Calculate ``saleReduction`` as ``price * amountOff``.  Calculate ``couponPrice`` as ``salePrice - couponReduction``.  
            
            .. activecode::  ch3ex5a
                :nocodelens:

                price = 68
                amountOff = 0.4
                saleReduction = price * amountOff
                salePrice = price - saleReduction
                amountOff = 0.2
                couponReduction = salePrice * amountOff
                couponPrice = salePrice - couponReduction
                print(couponPrice)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex5q
                
#. 

    .. tabbed:: ch3ex6t

        .. tab:: Question

           Finish the code on lines 4 and 5 to print how many wings you can buy if you have 5 people and they each can spend $4 a person and the wings are $0.50 a wing. It should print 40.0.  
           
           .. activecode::  ch3ex6q
                :nocodelens:

                numPeople = 5
                amountPerPerson = 4
                price = 0.5
                total = 
                numWings =  
                print(numWings)   

        .. tab:: Answer
        
            Calculate ``total`` as ``numPeople * amountPerPerson``.  Calculate ``numWings`` as ``total / price``.  
            
            .. activecode::  ch3ex6a
                :nocodelens:

                numPeople = 5
                amountPerPerson = 4
                price = 0.5
                total = numPeople * amountPerPerson
                numWings = total / price
                print(numWings)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex6q
                
#. 

    .. tabbed:: ch3ex7t

        .. tab:: Question

           Finish the code on lines 2 and 3 in the code below to print how many hours and minutes you have been waiting when you have been waiting a total of 270 minutes.  Remember that there are 60 minutes in an hour. It should print 4.0 and then 30.  
           
           .. activecode::  ch3ex7q
                :nocodelens:

                totalMinutes = 270
                numMinutes =
                numHours = 
                print(numHours)
                print(numMinutes)  

        .. tab:: Answer
        
            Calculate ``numMinutes`` as ``totalMinutes % 60``.  Calculate ``numHours`` as ``(totalMinutes - numMinutes) / 60``.  
            
            .. activecode::  ch3ex7a
                :nocodelens:

                totalMinutes = 270
                numMinutes = totalMinutes % 60
                numHours = (totalMinutes - numMinutes) / 60
                print(numHours)
                print(numMinutes)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex7q
                
#. 

    .. tabbed:: ch3ex8t

        .. tab:: Question

           Fix the syntax errors in the code below so that it calculates and prints the number of hours you will need to work if you earn $8 an hour and want to earn $100.  It should print 12.5.
           
           .. activecode::  ch3ex8q
                :nocodelens:

                8 = payPerHour
                amount = 100
                amount / payPerHour = numHours
                print(numHours)  

        .. tab:: Answer
        
            Change the first line to ``payPerHour = 8``.  Change the third line to ``numHours = amount / payPerHour``. 
            
            .. activecode::  ch3ex8a
                :nocodelens:
                
                payPerHour = 8
                amount = 100
                numHours = amount / payPerHour 
                print(numHours) 
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex8q
                
#. 

    .. tabbed:: ch3ex9t

        .. tab:: Question

           Finish lines 5 and 6 in the code below to print how many apples you can buy when apples cost 0.60 and you want to get 3 pears and they cost $1.2 each and you have $8.00.  It should print 7.33333333333.  Since you can't buy 7.333 apples can you also figure out how to make it print just 7?  
           
           .. activecode::  ch3ex9q
                :nocodelens:

                pricePerApple = 0.6
                numPears = 3
                pricePerPear = 1.2
                funds = 8
                fundsAfterPears = 
                numApples = 
                print(numApples) 

        .. tab:: Answer
        
            Calculate ``fundsAfterPears`` as ``funds - (pricePerPear * numPears)``.  Calculate ``numApples`` as ``fundsAfterPears / pricePerApple``.  You can throw away the fractional part using ``int(num)``.  
            
            .. activecode::  ch3ex9a
                :nocodelens:
                
                pricePerApple = 0.6
                numPears = 3
                pricePerPear = 1.2
                funds = 8
                fundsAfterPears = funds - (pricePerPear * numPears)
                numApples = fundsAfterPears / pricePerApple
                print(numApples)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex9q
                
#. 

    .. tabbed:: ch3ex10t

        .. tab:: Question

           Write the code to calculate and print how many *miles* you can drive if your car holds 10 gallons and you have a quarter of a tank left and your car gets 32 miles per gallon.  It should print 80.
           
           .. activecode::  ch3ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create variables to hold each value.  Calculate ``numGallons`` as ``tankCapacity * 0.25``.  Calculate ``numMiles`` as ``numGallons * milesPerGallon``.  Be sure to print the result.
            
            .. activecode::  ch3ex10a
                :nocodelens:
                
                tankCapacity = 10
                numGallons = tankCapacity * 0.25
                milesPerGallon = 32
                numMiles = numGallons * milesPerGallon 
                print(numMiles)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch3ex10q



