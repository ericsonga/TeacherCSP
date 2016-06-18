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
	:prefix: 4-7-

Chapter 4 Exercises
--------------------

#.

    .. tabbed:: ch4ex1t

        .. tab:: Question

            There are 3 syntax errors in the following code.  Fix it to print correctly without errors. It will print, "Your name is Carly and your favorite color is red".

            .. activecode:: ch4ex1q
                :nocodelens:

                color = "red'
                name = 'Carly'
                print("Your name is " + name +
                      and your favorite color is" + color + ".")

        .. tab:: Answer

            Change ``"red'`` to ``"red"``.  Add an ``"`` before ``and your favorite``.  Add a space after ``is``.

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

            Fix the syntax errors so it prints "My name is Sam and I am 12 years old."

            .. activecode::  ch4ex2q
                :nocodelens:

                name = Sam
                age = 12
                print("My name is name and I am" + age + "years old".)

        .. tab:: Answer

            ``Sam`` must be a string because otherwise it's a variable. Age must be converted to a string.

            .. activecode::  ch4ex2a
                :nocodelens:

                name = "Sam"
                age = 12
                print("My name is " + name +" and I am " + str(age) + " years old.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex2q

#.

    .. tabbed:: ch4ex3t

        .. tab:: Question

           You will get an error if you try to run the following code.  Fix the code to print correctly without errors.  It should print, "Your name is Carly and your age is 5."

           .. activecode::  ch4ex3q
               :nocodelens:

               age = 5
               name = 'Carly'
               print("Your name is" + name +
                     "and your age is" + age + ".")

        .. tab:: Answer

            Change ``age`` to ``str(age)``.

            .. activecode::  ch4ex3a
                :nocodelens:

                age = 5
                name = 'Carly'
                print("Your name is " + name +
                      " and your age is " + str(age) + ".")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex3q

#.

    .. tabbed:: ch4ex4t

        .. tab:: Question

            Using the variables given, modify the print statement to print ``"A car travelling at 70 mph takes 2 hours to go 140 miles."``
            
            .. activecode::  ch4ex4q
                :nocodelens:

                milesPerHour = 70
                distanceTravelled = 140
                timeTaken = milesPerHour / distanceTravelled
                print(timeTaken)

        .. tab:: Answer

            .. activecode::  ch4ex4a
                :nocodelens:

                milesPerHour = 70
                distanceTravelled = 140
                timeTaken = milesPerHour / distanceTravelled
                print("A car travelling at " + str(milesPerHour) + " mph takes " + str(timeTaken) + "hours to go " + str(distanceTravelled) + " miles.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex4q

#.

    .. tabbed:: ch4ex5t

        .. tab:: Question

           There are 3 syntax errors in the following code.  Fix it to print correctly without errors.  It will print your name and age.

           .. activecode::  ch4ex5q
               :nocodelens:

               age = input("How old are you?")
               name = input ("What is your first name?")
               print ("Your name is " + Name
                      " and you are "  age "years old.")

        .. tab:: Answer

            Change ``Name`` to ``name``.  Add a ``+`` at the end of line 3.  Add a ``+`` before and after ``age`` in line 4.

            .. activecode::  ch4ex5a
                :nocanvas:

                age = input("How old are you?")
                name = input ("What is your first name?")
                print ("Your name is " + name +
                       " and you are "  + age + " years old.")


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch4ex5q

#.

    .. tabbed:: ch4ex6t

        .. tab:: Question
            Fix the syntax errors so that the code prints ��The apple costs $5��

            .. activecode::  ch4ex6q
                :nocodelens:

                fruit = apple
                price = 5
                print("The" fruit "costs $" + "price")

        .. tab:: Answer


            .. activecode::  ch4ex6a
                :nocodelens:

                fruit = apple
                price = 5
                print("The " + fruit + " costs $" + str(price))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex6q


#.

    .. tabbed:: ch4ex7t

        .. tab:: Question

           Modify line 6 to print: "The number of miles you can drive on 25 dollars is 273.97260274."

           .. activecode::  ch4ex7q
               :nocodelens:

               funds = 25
               milesPerGallon = 40
               pricePerGallon = 3.65
               numGallons = funds / pricePerGallon
               numMiles = milesPerGallon * numGallons
               print(numMiles)


        .. tab:: Answer

            See line 6 below.  Be sure to use ``str(num)`` to convert a number to a string.

            .. activecode::  ch4ex7a
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
                :identifier: teachercsp_ch4ex7q

#.

    .. tabbed:: ch4ex8t

        .. tab:: Question

            Complete the code so that only "giant alligator" is printed.

            .. activecode::  ch4ex8q
                :nocodelens:

                sentence = "There is a giant alligator over there."
                s1 =
                print(s1)

        .. tab:: Answer

            You only want the substring from character 11 to character 26, but remember the stop sequence isn't inclusive.

            .. activecode::  ch4ex8a
                :nocodelens:

                sentence = "There is a giant alligator over there."
                s1 = sentence[11:27]
                print(s1)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex8q

#.

    .. tabbed:: ch4ex9t

        .. tab:: Question

           Modify line 6 to print: "You can order 40.0 wings when you have 5 people who can each spend 4 dollars and wings cost 0.5 each."

           .. activecode::  ch4ex9q
                :nocodelens:

                numPeople = 5
                amountPerPerson = 4
                price = 0.5
                total = numPeople * amountPerPerson
                numWings =  total / price
                print(numWings)

        .. tab:: Answer

            Change line 6 to include strings that explain the value that was calculated.  Be sure to use ``str(num)`` to convert a number to a string.

            .. activecode::  ch4ex9a
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
                :identifier: teachercsp_ch4ex9q

#.

    .. tabbed:: ch4ex10t

        .. tab:: Question

            Fix the code so that only "meow" is printed.

            .. activecode::  ch4ex10q
                :nocodelens:

                sentence = "The cat goes meow."
                s2 = [16:13]sentence
                print(s2)

        .. tab:: Answer

            Change line 2 to the proper syntax order for getting a substring, and change the start-stop bounds to 13 to 17.

            .. activecode::  ch4ex10a
                :nocodelens:

                sentence = "The cat goes meow."
                s2 = sentence[13:17]
                print(s2)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex10q

#.

    .. tabbed:: ch4ex11t

        .. tab:: Question

           Combine lines 4 and 5 in the code below to print: "270 is 4.0 hours and 30 minutes."

           .. activecode::  ch4ex11q
                :nocodelens:

                totalMinutes = 270
                numMinutes = totalMinutes % 60
                numHours = (totalMinutes - numMinutes) / 60
                print(numHours)
                print(numMinutes)

        .. tab:: Answer

           Combine lines 4 and 5 and use ``+`` to append strings.  Use ``str(num)`` to convert a number to a string so that it can be appended.

            .. activecode::  ch4ex11a
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
                :identifier: teachercsp_ch4ex11q

#.

    .. tabbed:: ch4ex12t

        .. tab:: Question

            Complete the code on lines 3 and 4 so that it prints "2" and then "22".

            .. activecode::  ch4ex12q
                :nocodelens:

                sentence = "This is his wish."
                sentence2 = "His only wish is this."
                pos =  .find("is")
                length = len( )
                print(length)

        .. tab:: Answer

            Line 3 should find "is" in sentence and line 4 should find the length of sentence 2

            .. activecode::  ch4ex12a
                :nocodelens:

                sentence = "This is his wish."
                sentence2 = "His only wish is this."
                pos = sentence.find("is")
                length = len(sentence2)
                print(length)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex12q

#.

    .. tabbed:: ch4ex13t

        .. tab:: Question

           Complete the calculations on lines 2 and 4 and enter the items to be printed on line 5 to print the number of miles you can drive if you have a 10 gallon gas tank and are down to a quarter of a tank of gas and your car gets 32 miles per gallon.  It should print: "You can go 80.0 miles."

           .. activecode::  ch4ex13q
                :nocodelens:

                tankCapacity = 10
                numGallons =
                milesPerGallon = 32
                numMiles =
                print()


        .. tab:: Answer

            Calculate ``numGallons`` as ``tankCapacity * 0.25``.  Calculate ``numMiles`` as ``numGallons * milesPerGallon``.  Use concatenation to print out an explanation and the value.  Be sure to use ``str(num)`` to convert a number to a string before you concatenate it.

            .. activecode::  ch4ex13a
                :nocodelens:

                tankCapacity = 10
                numGallons = tankCapacity * 0.25
                milesPerGallon = 32
                numMiles = numGallons * milesPerGallon
                print("You can go " + str(numMiles) + " miles.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex13q

#.

    .. tabbed:: ch4ex14t

        .. tab:: Question

            Fix line 2 so that it prints "Hi" instead of "hi".
            .. activecode::  ch4ex14q
                :nocodelens:

                s1 = "hi"
                s1.capitalize()
                print(s1)

        .. tab:: Answer

            You have to assign ``s1.capitalize()`` to ``s1`` to reflect the change

            .. activecode::  ch4ex14a
                :nocodelens:

                s1 = "hi"
                s1 = s1.capitalize()
                print(s1)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex14q


#.

    .. tabbed:: ch4ex15t

        .. tab:: Question

           Write code to get the name of a color from the user using the ``input`` function. Next convert the name of the color to all lowercase letters and print it.

           .. activecode::  ch4ex15q
                :nocodelens:

        .. tab:: Answer

            Use ``input("message")`` to get the color.  Use the ``lower()`` function to get the string as all lowercase letters.

            .. activecode::  ch4ex15a
                :nocodelens:

                color = input("Enter an color.")
                colorLower = color.lower()
                print("The color is " + colorLower)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex15q

#.

    .. tabbed:: ch4ex16t

        .. tab:: Question

            Write code to get the input of a user’s first name, then get only the first letter of their name, and print that letter lowercase.

            .. activecode::  ch4ex16q
                :nocodelens:

        .. tab:: Answer

            Get the user input and get the substring of only the first character.

            .. activecode::  ch4ex16a
                :nocodelens:

                name = input("What is your first name")
                firstInitial = name[0:1]
                print(firstInitial)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex16q

#.

    .. tabbed:: ch4ex17t

        .. tab:: Question

           Write the code below to calculate and print how many months it will take to save $200 if you earn $20 a week.  It should print: "It will take 2.5 months to earn 200 if you make 20 dollars a week."

           .. activecode::  ch4ex17q
                :nocodelens:

        .. tab:: Answer

            Name each of the values.  Calculate the ``totalWeeks`` it will take and the ``months`` and print the information.

            .. activecode::  ch4ex17a
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
                :identifier: teachercsp_ch4ex17q

#.

    .. tabbed:: ch4ex18t

        .. tab:: Question

            Write code to print out the statement "Hi my name is Bob and I am 2" using only string methods or string slicing. You must get every part of the new string from the given strings.

            .. activecode::  ch4ex18q
                :nocodelens:

                s1 = "hi"
                s2 = "My namesake is Bob, and he and I love to eat ham."

        .. tab:: Answer

            Use string slicing to get all the words and get the length of ``s1`` to get the number 2. Use methods like capitalize() and lower() to convert cases.

            .. activecode::  ch4ex18a
                :nocodelens:

                s3 = s1.capitalize()
                s4 = s2[0:7].lower()
                s5 = s2[12:18]
                s6 = s2[31:33]
                s7 = s2[46:48]
                s8 = len(s1)
                print(s3 + " " + s4 + " " + s5 + " " + s6 + s7 + " " + str(s8))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex18q

#.

    .. tabbed:: ch4ex19t

        .. tab:: Question

           Write code below to get at least 3 values from the user using the ``input`` function and output a mad lib (which will use the input to tell a silly story).

           .. activecode::  ch4ex19q
               :nocodelens:

        .. tab:: Answer

            Use ``input("message")`` to get the input.  Use string concatenation to print the mad lib.

            .. activecode::  ch4ex19a
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
                :identifier: teachercsp_ch4ex19q

#.

    .. tabbed:: ch4ex20t

        .. tab:: Question

            Write code that gets user input and print a string that states their input in all lowercase and gives the length of their string.

            .. activecode::  ch4ex20q
                :nocodelens:

        .. tab:: Answer

            Use the lower and length methods on the user input. Don't forget to convert the length to a string.
            
            .. activecode::  ch4ex20a
                :nocodelens:

                user = input("Type a sentence")
                user = user.lower()
                length = length(user)
                print("The length of " + user + " is" + str(length))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex20q
