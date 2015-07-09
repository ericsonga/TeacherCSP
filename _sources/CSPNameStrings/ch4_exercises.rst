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
	:prefix: 4-6-

Chapter 4 Exercises
--------------------

#. 

    .. tabbed:: ch4ex1t

        .. tab:: Question
            
            There are errors in the following code.  Fix it to print correctly without errors.  

            .. activecode:: ch4ex1q
                :nocodelens:

                color = "red'
                name = 'Carly'
                print("Your name is " + name + 
                      and your favorite color is" + color + ".")

        .. tab:: Answer

            .. activecode:: ch4ex1a
                :nocodelens:

                color = "red"
                name = 'Carly'
                print("Your name is " + name + 
                      " and your favorite color is " + color + ".")

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch4ex1q
                
#. 
   
    .. tabbed:: ch4ex2t

        .. tab:: Question

           There are errors in the following code.  Fix it to print correctly without errors.  
           
           .. activecode::  ch4ex2q
               :nocodelens:

                age = 5
                name = 'Carly'
                print("Your name is" + name + 
                      "and your age is" + age + ".")

        .. tab:: Answer
            
            .. activecode::  ch4ex2a
                :nocodelens:
                
                age = 5
                name = 'Carly'
                print("Your name is " + name + 
                      " and your age is " + str(age) + ".")
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex2q

#. 

    .. tabbed:: ch4ex3t

        .. tab:: Question

           There are errors in the following code.  Fix it to print correctly without errors.  
        
           .. activecode::  ch4ex3q
               :nocodelens:

               age = input("How old are you?")
               name = input ("What is your first name?")
               print ("Your name is " + Name 
                      " and you are "  age "years old.")

        .. tab:: Answer
            
            .. activecode::  ch4ex3a
                :nocanvas:

                age = input("How old are you?")
                name = input ("What is your first name?")
                print ("Your name is " + name +
                       " and you are "  + age + " years old.")
                

        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch4ex3q
                
#. 

    .. tabbed:: ch4ex4t

        .. tab:: Question

           Modify line 6 to also print a string explaining the value being printed.  Include the funds value in the string.
           
           .. activecode::  ch4ex4q
               :nocodelens:

               funds = 25
               milesPerGallon = 40
               pricePerGallon = 3.65
               numGallons = funds / pricePerGallon
               numMiles = milesPerGallon * numGallons
               print(numMiles)
          

        .. tab:: Answer
            
            .. activecode::  ch4ex4a
                :nocodelens:

                funds = 25
                milesPerGallon = 40
                pricePerGallon = 3.65
                numGallons = funds / pricePerGallon
                numMiles = milesPerGallon * numGallons
                print("The number of miles you can drive on " + 
                       str(funds) + " dollars is " + str(numMiles) + ".")
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex4q
   
#. 

    .. tabbed:: ch4ex5t

        .. tab:: Question

           Modify line 6 to print out a string explaining the value that is printed.  Include the price of the wings, the number of people, and the amount each person has to spend.
           
           .. activecode::  ch4ex5q
                :nocodelens:

                numPeople = 5
                amountPerPerson = 4
                price = 0.5
                total = numPeople * amountPerPerson
                numWings =  total / price
                print(numWings) 

        .. tab:: Answer
            
            .. activecode::  ch4ex5a
                :nocodelens:

                numPeople = 5
                amountPerPerson = 4
                price = 0.5
                total = numPeople * amountPerPerson
                numWings = total / price
                print("You can order " + str(numWings) + " wings" + 
                      " when you have " + str(numPeople) + " people" +
                      " who can each spend " + str(amountPerPerson) + " dollars" + 
                      " and wings cost " + str(price) + " each.")
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex5q
                
#. 

    .. tabbed:: ch4ex6t

        .. tab:: Question

           Combine lines 4 and 5 in the code below to print how many hours and minutes 270 minutes is.  
           
           .. activecode::  ch4ex6q
                :nocodelens:

                totalMinutes = 270
                numMinutes = totalMinutes % 60
                numHours = (totalMinutes - numMinutes) / 60
                print(numHours)
                print(numMinutes)   

        .. tab:: Answer
            
            .. activecode::  ch4ex6a
                :nocodelens:

                totalMinutes = 270
                numMinutes = totalMinutes % 60
                numHours = (totalMinutes - numMinutes) / 60
                print(str(totalMinutes) + " is " + 
                      str(numHours) + " hours and " + 
                      str(numMinutes) + " minutes.")

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex6q
                
#. 

    .. tabbed:: ch4ex7t

        .. tab:: Question

           Complete the calculations on lines 2 and 4 and enter the items to be printed on line 5 to print the number of miles you can drive if you have a 10 gallon gas tank and are down to a quarter of a tank of gas and your car gets 32 miles per gallon.
           
           .. activecode::  ch4ex7q
                :nocodelens:

                tankCapacity = 10
                numGallons = 
                milesPerGallon = 32
                numMiles = 
                print()
                  

        .. tab:: Answer
            
            .. activecode::  ch4ex7a
                :nocodelens:

                tankCapacity = 10
                numGallons = tankCapacity * 0.25
                milesPerGallon = 32
                numMiles = numGallons * milesPerGallon 
                print("You can go " + str(numMiles) + " miles.")
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex7q
                
#. 

    .. tabbed:: ch4ex8t

        .. tab:: Question

           Write the code to get a color as input and print it out in all lowercase letters.  This can be helpful when you want to check for a particular color and want to compare the values with them both all lowercase.
           
           .. activecode::  ch4ex8q
                :nocodelens:

        .. tab:: Answer
            
            .. activecode::  ch4ex8a
                :nocodelens:
                
                color = input("Enter an color.")
                colorLower = color.lower()
                print("The color is " + colorLower)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex8q
                
#. 

    .. tabbed:: ch4ex9t

        .. tab:: Question

           Write the code below to calculate and print how many months it will take to save $200 if you earn $20 a week.
           
           .. activecode::  ch4ex9q
                :nocodelens:

        .. tab:: Answer
            
            .. activecode::  ch4ex9a
                :nocodelens:
                
                goal = 200
                weeklyEarning = 20
                totalWeeks = goal / weeklyEarning
                months = totalWeeks / 4
                print("It will take " + str(months) + " months to earn " + 
                       str(goal) + " if you make " + str(weeklyEarning) + 
                       " dollars a week.")
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex9q
                
#. 

    .. tabbed:: ch4ex10t

        .. tab:: Question

           Write the code below to gather at least 3 inputs and output a mad lib (which will use the input to tell a silly story).
           
           .. activecode::  ch4ex10q
               :nocodelens:

        .. tab:: Answer
            
            .. activecode::  ch4ex10a
                :nocodelens:
                
                place = input("Enter the name of a place.")
                verb = input("Enter a verb.")
                action = input("Enter an action.")
                color = input("Enter your favorite color.")
                animal = input("What is your favorite animal?")
                print("Once upon a time in " + place + ", I was " + 
                      verb + "ing and I " + action + " because a " + 
                      color + " " + animal + " was also " + verb + "ing.")
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex10q



