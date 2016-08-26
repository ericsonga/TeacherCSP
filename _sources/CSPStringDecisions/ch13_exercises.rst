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
	:prefix: 13-6-

Chapter 13 Exercises
---------------------

#.

    .. tabbed:: ch13ex1t

        .. tab:: Question

            Fix 7 problems in the code below so that it runs.

            .. activecode:: ch13ex1q
                :nocodelens:

                score = 20
                if score < 10
                print("You can do better.")
                if score > 10:
                print(Good job!")
                if score > 20
                print("Amazing"

        .. tab:: Answer

            Add ``:`` at the end of line 2.  Indent lines 3, 5, and 7.  Add a ``"`` after the ``(`` on line 5.  Add a ``:`` on line 6.  Add a ``)`` at the end of line 7.

            .. activecode:: ch13ex1a
                :nocodelens:

                score = 20
                if score < 10:
                    print("You can do better.")
                if score > 10:
                    print("Good job!")
                if score > 20:
                    print("Amazing")

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch13ex1q

#.

    .. tabbed:: ch13ex2t

        .. tab:: Question

            Fix the errors in the code so that it prints "Less than 5" when a number is less than 5 and "Greater than or equal to 5" when it is greater than or equal to 5.

            .. activecode::  ch13ex2q
                :nocodelens:

                x = 4
                if x > 5
                print("Less than 5")
                    if x =< 5
                    print("Greater than or equal to 5")

        .. tab:: Answer

            Fix indentation on lines 3 and 4. Add colons after the if statements. Fix the conditions to match the words.

            .. activecode::  ch13ex2a
                :nocodelens:

                x = 4
                if x < 5:
                    print("Less than 5")
                if x >= 5:
                    print("Greater than or equal to 5")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex2q

#.

    .. tabbed:: ch13ex3t

        .. tab:: Question

           Fix 6 errors in the code below so that it works correctly.

           .. activecode::  ch13ex3q
                :nocodelens:

                print(You are in front of a creepy door in a hallway.")
                prin("What do you want to do?")
                action = input ("Type: in, left, or right. Then click OK or press enter)
                if action == "in"
                    print("You choose to go in.")
                    print("The room is pitch black.")
                if action == "left":
                print("You choose to turn left.")
                    print("A ghost appears at the end of the hall.")
                if action == "right":
                    print("You choose to turn right.")
                print("A greenish light is visible in the distance.")

        .. tab:: Answer

            Add a ``"`` after the ``(`` on line 1.  Change line 2 to ``print``.  Add a ``"`` before the ``)`` on line 3.  Add a ``:`` at the end of line 4.  Indent lines 8 and 12.

            .. activecode::  ch13ex3a
                :nocodelens:

                print("You are in front of a creepy door in a hallway.")
                print("What do you want to do?")
                action = input ("Type: in, left, or right. Then click OK or press enter")
                if action == "in":
                    print("You choose to go in.")
                    print("The room is pitch black.")
                if action == "left":
                    print("You choose to turn left.")
                    print("A ghost appears at the end of the hall.")
                if action == "right":
                    print("You choose to turn right.")
                    print("A greenish light is visible in the distance.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex3q

#.

    .. tabbed:: ch13ex4t

        .. tab:: Question

            Complete the code to get user input, and make choices based off the input. The input should either be "in", "left", or "right"; make sure the user knows that.

            .. activecode::  ch13ex4q
                :nocodelens:

                print("You are in front of a creepy door in a hallway.")
                print("What do you want to do?")
                userInput =
                if
                    print("You choose to go in.")
                    print("The room is pitch black.")
                if
                    print("You choose to turn left.")
                    print("A ghost appears at the end of the hall.")
                if
                    print("You choose to turn right.")
                    print("A greenish light is visible in the distance.")

        .. tab:: Answer

            Complete the question asking for user input and complete the if statements.

            .. activecode::  ch13ex4a
                :nocodelens:

                print("You are in front of a creepy door in a hallway.")
                print("What do you want to do?")
                userInput = input("Type: in, left, or right. Then click OK or press enter)
                if userInput == "in":
                    print("You choose to go in.")
                    print("The room is pitch black.")
                if userInput == "left":
                    print("You choose to turn left.")
                    print("A ghost appears at the end of the hall.")
                if userInput == "right":
                    print("You choose to turn right.")
                    print("A greenish light is visible in the distance.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex4q

#.

    .. tabbed:: ch13ex5t

        .. tab:: Question

           Fix the code below to assign grades correctly using elif and else. You can assume the numbers are all correct.

           .. activecode::  ch13ex5q
                :nocodelens:

                score = 80
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

            Change lines 4, 6, and 8 to ``elif``.  Change line 10 to ``else:``.

            .. activecode::  ch13ex5a
                :nocodelens:

                score = 80
                if score >= 90:
                    grade = "A"
                elif score >= 80:
                    grade = "B"
                elif score >= 70:
                    grade = "C"
                elif score >= 60:
                    grade = "D"
                else:
                   grade = "E"
                print(grade)



        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch13ex5q

#.

    .. tabbed:: ch13ex6t

        .. tab:: Question

            The following code prints both statements, change it so that it only prints the first one when the age is less than 6.

            .. activecode::  ch13ex6q
                :nocodelens:

                age = 4
                if age < 6:
                    print("You're in kindergarten")
                if age < 11:
                    print("You're in elementary school")


        .. tab:: Answer

            Use ``elif`` clause for the second one.
            
            .. activecode::  ch13ex6a
                :nocodelens:

                age = 4
                if age < 6:
                    print("You're in kindergarten")
                elif age < 11:
                    print("You're in elementary school")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex6q

#.

    .. tabbed:: ch13ex7t

        .. tab:: Question

           Change the code below to use elif and else rather than several ifs.  Also fix it to print "Good job!" if the score is greater than 10 and less than or equal to 20 and "Amazing" if the score is over 20.

           .. activecode::  ch13ex7q
                :nocodelens:

                score = 22
                if score < 10:
                    print("You can do better.")
                if score > 10:
                    print("Good job!")
                if score > 20:
                    print("Amazing")


        .. tab:: Answer

            Change line 4 to ``elif score > 10 and score <= 20:`` and change line 6 to ``else:``.

            .. activecode::  ch13ex7a
                :nocodelens:

                score = 22
                if score < 10:
                    print("You can do better.")
                elif score > 10 and score <= 20:
                    print("Good job!")
                else:
                    print("Amazing")


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex7q

#.

    .. tabbed:: ch13ex8t

        .. tab:: Question

            Complete the code so that it iterates through the list of numbers and prints positive, negative, or neither based off the integer.

            .. activecode::  ch13ex8q
                :nocodelens:

                numbers = [-1,0,1]
                for x in numbers:
                    if
                        print("positive")
                    elif
                        print(
                    else:
                        print(

        .. tab:: Answer

            Should check if x is greater than, less than, or equal to 0, and print the appropriate response.

            .. activecode::  ch13ex8a
                :nocodelens:

                numbers = [-1,0,1]
                for x in numbers:
                    if x > 0:
                        print("positive")
                    elif x < 0:
                        print("negative")
                    else:
                        print("neither")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex8q

#.

    .. tabbed:: ch13ex9t

        .. tab:: Question

           Change the code below to use ``elif`` and ``else``.

           .. activecode::  ch13ex9q
                :nocodelens:

                num = input ("Type a number from 1 to 5. Then click OK or press enter")
                if num == "1":
                    print("You will get a treat.")
                if num == "2":
                    print("You will lose something.")
                if num == "3":
                    print("You will meet a new friend.")
                if num == "4":
                    print("You will catch a cold.")
                if num == "5":
                    print("You will ace a test.")

        .. tab:: Answer

            Change lines 4, 6, and 8 to ``elif`` and change line 10 to ``else``.

            .. activecode::  ch13ex9a
                :nocodelens:

                num = input ("Type a number from 1 to 5. Then click OK or press enter")
                if num == "1":
                    print("You will get a treat.")
                elif num == "2":
                    print("You will lose something.")
                elif num == "3":
                    print("You will meet a new friend.")
                elif num == "4":
                    print("You will catch a cold.")
                else:
                    print("You will ace a test.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex9q

#.

    .. tabbed:: ch13ex10t

        .. tab:: Question

            Fix the errors in the code and change it to use elif's and else so that if the user's score is greater than the high score, it prints "Good job!", if it's lower, print "Try again.", and if it's the same print "You tied the high score".

            .. activecode::  ch13ex10q
                :nocodelens:

                highScore = 10
                userInput = Input("What's your score? (Give a number 1 - 20)")
                userInput = int(userInput)
                if userInput < 10
                    print(Good job!)
                    if userInput > 10
                    print("Try again.")
                        if userInput = 10
                            print("You tied the high score.")

        .. tab:: Answer

            Fix indentation and add colons after the if clauses. Add quotes to strings, lowercase "input", and fix the signs in the conditionals. Also replace the second and third conditions with elif and else.

            .. activecode::  ch13ex10a
                :nocodelens:

                highScore = 10
                userInput = input("What's your score? (Give me a number 1 -20)")
                userInput = int(userInput)
                if userInput > 10:
                    print("Good job!")
                elif userInput < 10:
                    print("Try again.")
                else:
                    print("You tied the high score.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex10q

#.

    .. tabbed:: ch13ex11t

        .. tab:: Question

           Change the following code to use ``elif`` and ``else`` instead.

           .. activecode::  ch13ex11q
                :nocodelens:

                team1 = 20
                team2 = 20
                if (team1 < team2):
                    print("team1 won")
                if (team2 > team1):
                    print("team2 won")
                if (team2 == team1):
                    print("team1 and team2 tied")

        .. tab:: Answer

            Change line 5 to ``elif`` and line 7 to ``else``.

            .. activecode::  ch13ex11a
                :nocodelens:

                team1 = 20
                team2 = 20
                if (team1 < team2):
                    print("team1 won")
                elif (team2 > team1):
                    print("team2 won")
                else:
                    print("team1 and team2 tied")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex11q

#.

    .. tabbed:: ch13ex12t

        .. tab:: Question

            Add statements to the code, so that if the user gives a number less than 5, you ask for the input again, and have another set of decision statements based off if the number is greater than, less than, or equal to 3.

            .. activecode::  ch13ex12q
                :nocodelens:

                user = input("Give me a number")
                number = int(user)
                if number < 5:
                    user2 =
                    number2 = int(user2)
                    if
                        print("I love CS")
                    elif
                        print("CS is the best")
                    else:
                        print("I like CS better than food")
                else:
                    print("Who else loves CS?")

        .. tab:: Answer

            Complete as shown below.

            .. activecode::  ch13ex12a
                :nocodelens:

                user = input("Give me a number")
                number = int(user)
                if number < 5:
                    user2 = input("Give me a number")
                    number2 = int(user2)
	            if number2 > 3:
	                print("I love CS")
	            elif number2 < 3:
	                print("CS is the best")
	            else:
	                print("I like CS better than food")
                else:
                    print("Who else loves CS?")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex12q

#.

    .. tabbed:: ch13ex13t

        .. tab:: Question

           Change the code below to use only 1 ``if``, 1 ``elif``, and 1 ``else``.

           .. activecode::  ch13ex13q
                :nocodelens:

                state = "Georgia"
                if state == "Georgia":
                    print("It's hot")
                if state == "Florida":
                    print("It's hot")
                if state == "Alaska":
                    print("It's cold")
                else:
                    print("I don't know the weather")


        .. tab:: Answer

            Combine the first 2 ``if`` statements by using an ``or``. Change the third ``if`` statement into an ``elif``.

            .. activecode::  ch13ex13a
                :nocodelens

                state = "Georgia"
                if state == "Georgia" or state == "Florida":
                    print("It's hot")
                elif state == "Alaska":
                    print("It's cold")
                else:
                    print("I don't know the weather")




        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex13q

#.

    .. tabbed:: ch13ex14t

        .. tab:: Question

            Fix the code and change the statements so there are three sets of if and else and 2 elifs.

            .. activecode::  ch13ex14q
                :nocodelens:

                if bikes > people:
                print("We should take the bikes.")
                if bikes < people:
                print("We should not take the bikes.")
                if bikes == people:
                print("We can't decide.")

                if vans > bikes:
                print("That's too many vans.")
                if vans < bikes:
                print("Maybe we could take the vans.")
                if vans == bikes:
                print("We still can't decide.")

                if people > vans:
                print("Alright, let's just take the vans.")
                if people <= vans:
                print("Fine, let's stay home then.")

        .. tab:: Answer


            .. activecode::  ch13ex14a
                :nocodelens:

                people = 30
                bikes = 40
                vans = 15


                if bikes > people:
                    print("We should take the bikes.")
                elif bikes < people:
                    print("We should not take the bikes.")
                else:
                    print("We can't decide.")

                if vans > bikes:
                    print("That's too many vans.")
                elif vans < bikes:
                    print("Maybe we could take the vans.")
                else:
                    print("We still can't decide.")

                if people > vans:
                    print("Alright, let's just take the vans.")
                else:
                    print("Fine, let's stay home then.")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex14q

#.

    .. tabbed:: ch13ex15t

        .. tab:: Question

           Change the code below into a procedure that takes a number as a parameter and prints the quartile.  Be sure to test each quartile.

           .. activecode::  ch13ex15q
                :nocodelens:

                x = .25
                if x <= .25:
                    print("x is in the first quartile - x <= .25")
                if x <= .5 and x > .25:
                    print("x is in the second quartile - .25 < x <= .5")
                if x <= .75 and x > .5:
                    print("x is in the third quartile - .5 < x <= .75")
                if x > .75:
                    print("x is in the fourth quartile - .75 < x <= 1")

        .. tab:: Answer

            Create the procedure and pass the number.  Test the procedure for each quartile.

            .. activecode::  ch13ex15a
                :nocodelens:

                def printQuartile(x):
                    if x <= .25:
                        print("x is in the first quartile - x <= .25")
                    if x <= .5 and x > .25:
                        print("x is in the second quartile - .25 < x <= .5")
                    if x <= .75 and x > .5:
                        print("x is in the third quartile - .5 < x <= .75")
                    if x > .75:
                        print("x is in the fourth quartile - .75 < x <= 1")


                printQuartile(.25)
                printQuartile(0.3)
                printQuartile(0.5)
                printQuartile(0.75)
                printQuartile(0.8)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex15q

#.

    .. tabbed:: ch13ex16t

        .. tab:: Question

            Fix the code so that it prints only 1 thing for each age group and uses elif and else.

            .. activecode::  ch13ex16q
                :nocodelens:

                age = 10
                if age >= 18:
                    print("adult")
                if age < 18:
                    print("teen")
                if age < 13:
                    print("pre-teen")
                if age < 10:
                    print("kid")
                if age < 5:
                    print("toddler")
                if age < 2:
                    print("baby")

        .. tab:: Answer

            Flip the order of the statments, and substitute elif and else clauses for everything but the first statement.

            .. activecode::  ch13ex16a
                :nocodelens:

                age = 10
                if age < 2:
                    print("baby")
                elif age < 5:
                    print("toddler")
                elif age < 10:
                    print("kid")
                elif age < 13:
                    print("pre-teen")
                elif age < 18:
                    print("teen")
                else:
                    print("adult")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex16q

#.

    .. tabbed:: ch13ex17t

        .. tab:: Question

           Write a function that will take a number as input and return a fortune as a string.  Ask the user to pick a number to get the fortune before you call the function.  Have at least 5 different fortunes.  Use ``if``, ``elif``, and ``else``.

           .. activecode::  ch13ex17q
                :nocodelens:

        .. tab:: Answer

            Define the function as shown below and be sure to test it.

            .. activecode::  ch13ex17a
                :nocodelens:

                def getFortune(num):
                    if num == "1":
                        return("You will ace a test")
                    elif num == "2":
                        return("You will get hurt.")
                    elif num == "3":
                        return("You will meet a new friend.")
                    elif num == "4":
                        return("You will find a penny.")
                    else:
                        return("You will lose something.")

                num = input ("Type a number from 1 to 5. Then click OK or press enter")
                print(getFortune(num))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex17q

#.

    .. tabbed:: ch13ex18t

        .. tab:: Question

            Write a function that takes in a list of grades and returns the letter grade of the average (A is 90+, B is 80-89, C is 70-79, D is 60-69, F is 59 and below). Call the function and print the result.

            .. activecode::  ch13ex18q
                :nocodelens:


        .. tab:: Answer

            Iterate through the list to find the average then use if, elif, and else statements to determine the letter grade.

            .. activecode::  ch13ex18a
                :nocodelens:

                def gradeAverage(aList):
                    sum = 0
                    for x in aList:
                        sum = sum + x
                    avg = sum / len(aList)
                    if avg >= 90:
                        grade = "A"
                    elif avg >= 80:
                        grade = "B"
                    elif avg >= 70:
                        grade = "C"
                    elif avg >= 60:
                        grade = "D"
                    else:
                       grade = "F"
                    return grade

                print(gradeAverage([80,90,90,80,100]))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex18q

#.

    .. tabbed:: ch13ex19t

        .. tab:: Question

           Write a procedure to tell an interactive story and let the user choose one of at least 3 options.

           .. activecode::  ch13ex19q
               :nocodelens:

        .. tab:: Answer

            Create a procedure as shown below.  Call it to test it and print the result.

            .. activecode::  ch13ex19a
                :nocodelens:

                def story():

                    print("You are in front of a creepy door in a hallway.")
                    print("What do you want to do?")
                    action = input ("Type: in, left, or right. Then click OK or press enter")
                    if action == "in":
                        print("You choose to go in.")
                        print("The room is pitch black.")
                    if action == "left":
                        print("You choose to turn left.")
                        print("A ghost appears at the end of the hall.")
                    if action == "right":
                        print("You choose to turn right.")
                        print("A greenish light is visible in the distance.")

                story()


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex19q

#.

    .. tabbed:: ch13ex20t

        .. tab:: Question

            Write code that iterates through number 1 - 20 and prints "Fizz" if it's a multiple of 3, "Buzz" if it's a multiple of 5, "FizzBuzz" if it's a multiple of 3 and 5, and the number if it's not a multiple of 3 or 5. It should only print one statement per number.

            .. activecode::  ch13ex20q
                :nocodelens:


        .. tab:: Answer

            Order of the first statement is important. Look below.

            .. activecode::  ch13ex20a
                :nocodelens:

                for x in range (1,21):
                    if x % 3 == 0 and x % 5 == 0:
                        print("FizzBuzz")
                    elif x % 3 == 0:
                        print("Fizz")
                    elif x % 5 == 0:
                        print("Buzz")
                    else:
                        print(x)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch13ex20q
