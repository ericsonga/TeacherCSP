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
	:prefix: 17-8-

Chapter 17 Exercises
---------------------

#.

    .. tabbed:: ch17ex1t

        .. tab:: Question

            Fix 6 syntax errors in the code below so that the code runs correctly.  It will print a story.

            .. activecode:: ch17ex1q
                :nocodelens:

                # initialize the variables
                firstName = "Pat'
                lastName = "Smith"
                gender = girl"
                address = "65 Elm Street
                verb = "eat"

                # create the story
                start = "Once there was a "  gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at "  address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstname + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print (next3
                print(ending)

        .. tab:: Answer

            Change the first ``'`` to a ``"`` in line 2. Add a ``"`` before ``girl`` in line 4.  Add a ``"`` at the end of line 5.  Add a ``+`` before ``gender`` in line 9.  Change ``firstname`` to ``firstName`` in line 13.  Add a ``)`` at the end of line 19.

            .. activecode:: ch17ex1a
                :nocodelens:

                # initialize the variables
                firstName = "Pat"
                lastName = "Smith"
                gender = "girl"
                address = "65 Elm Street"
                verb = "eat"

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print (next3)
                print(ending)


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch17ex1q

#.

    .. tabbed:: ch17ex2t

        .. tab:: Question

            Fix the errors so that it prints the first and last name only.

            .. activecode::  ch17ex2q
                :nocodelens:

                # create the input
                input = "Pat,Smith,girl,65 Elm Street,eat'

                # split on the comma
                pieces = input.split(,)

                # print the values
                print("First name is:" + pieces)
                print("Last name is:" + pieces[2])


        .. tab:: Answer

            Fix the quotation mark in the second line. In the fifth line add quotations around the comma. Print ``pieces[0]`` and  ``pieces[1]``.

            .. activecode::  ch17ex2a
                :nocodelens:

                # create the input
                input = "Pat,Smith,girl,65 Elm Street,eat"

                # split on the comma
                pieces = input.split(",")

                # print the values
                print("First name is:" + pieces[0])
                print("Last name is:" + pieces[1])

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex2q

#.

    .. tabbed:: ch17ex3t

        .. tab:: Question

           Fix the 6 syntax errors in the code below so that it runs.  It will print a story.

           .. activecode::  ch17ex3q
                :nocodelens:

                # create the input
                input = "Pat,Smith girl,65 Elm Street,eat"

                # split at the comma
                pieces = input.split(",)

                # initialize the variables
                firstName = pieces[0]
                lastName = pieces[1
                gender = pieces[2]
                address = pieces[3]
                verb = pieces[4]

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the "  lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print next1
                print(next2)
                print(next3)
                print(ending)


        .. tab:: Answer

            Add a comma before ``girl`` on line 2.  Add a ``"`` before the ``)`` on line 5.  Add a ``]`` at the end of line 9.  Add a ``+`` in line 17.  Add a ``(`` and a ``)`` on line 23.

            .. activecode::  ch17ex3a
                :nocodelens:

                # create the input
                input = "Pat,Smith,girl,65 Elm Street,eat"

                # split at the comma
                pieces = input.split(",")

                # initialize the variables
                firstName = pieces[0]
                lastName = pieces[1]
                gender = pieces[2]
                address = pieces[3]
                verb = pieces[4]

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex3q

#.

    .. tabbed:: ch17ex4t

        .. tab:: Question

            Complete the code on lines 8 - 12 to initialize the variables correctly according to the order of the input.

            .. activecode::  ch17ex4q
                :nocodelens:

                # create the input
                input = "eat, Elm Street, girl, Pat, Smith"

                # split at the comma
                pieces = input.split(",")

                # initialize the variables
                firstName =
                lastName =
                gender =
                address =
                verb =

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Answer

            .. activecode::  ch17ex4a
                :nocodelens:

                # create the input
                input = "eat, Elm Street, girl, Pat, Smith"

                # split at the comma
                pieces = input.split(",")

                # initialize the variables
                firstName = pieces[3]
                lastName = pieces[4]
                gender = pieces[2]
                address = pieces[1]
                verb = pieces[0]

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex4q

#.

    .. tabbed:: ch17ex5t

        .. tab:: Question

           Indent 6 lines and fix the call to the procedure so that it works correctly.  It will print a story.

           .. activecode::  ch17ex5q
                :nocodelens:

               def witchStory (firstName, lastName, gender, address, verb):

               # create the story
               start = "Once there was a " + gender + " named " + firstName + "."
               next1 = "A good " + gender + " living at " + address + "."
               next2 = "One day, a wicked witch came to the " + lastName + " house."
               next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
               ending = "But " + firstName + " was smart and avoided the wicked witch."

                   # print the story
                   print(start)
                   print(next1)
                   print(next2)
                   print(next3)
                   print(ending)

               # call the procedure
               witchStory("boy", "Abe" "Brown", "1313 Maple Lane", "trick")

        .. tab:: Answer

            Indent lines 3-8.  Add a ``,`` between the first name and the last name on the call on line 18.  Move ``"boy"`` to after the last name in the call on line 18.

            .. activecode::  ch17ex5a
                :nocodelens:

                def witchStory (firstName, lastName, gender, address, verb):

                    # create the story
                    start = "Once there was a " + gender + " named " + firstName + "."
                    next1 = "A good " + gender + " living at " + address + "."
                    next2 = "One day, a wicked witch came to the " + lastName + " house."
                    next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                    ending = "But " + firstName + " was smart and avoided the wicked witch."

                    # print the story
                    print(start)
                    print(next1)
                    print(next2)
                    print(next3)
                    print(ending)

                # call the procedure
                witchStory("Abe", "Brown", "boy", "1313 Maple Lane", "trick")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex5q

#.

    .. tabbed:: ch17ex6t

        .. tab:: Question

            The input is a list of strings, add code below it (and fix indentation and variable names if needed) so that the code will print a story for each string in the list.

            .. activecode::  ch17ex6q
                :nocodelens:

                # create the input
                input = ["Pat,Smith,girl,65 Elm Street,eat", "John,Doe,Boy,25,123 Candy Lane, tickle"]

                # split at the comma
                pieces = input.split(",")

                # initialize the variables
                firstName = pieces[0]
                lastName = pieces[1]
                gender = pieces[2]
                address = pieces[3]
                verb = pieces[4]

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Answer

            Add a for loop, fix the indentation to put everything besides input in the body of the for loop, and change pieces to equal ``i.split(",")`` where i is each element in the string list.

            .. activecode::  ch17ex6a
                :nocodelens:

                # create the input
                input = ["Pat,Smith,girl,65 Elm Street,eat", "John,Doe,Boy,25,123 Candy Lane, tickle"]

                for i in input:

                    # split at the comma
                    pieces = i.split(",")

                    # initialize the variables
                    firstName = pieces[0]
                    lastName = pieces[1]
                    gender = pieces[2]
                    address = pieces[3]
                    verb = pieces[4]

                    # create the story
                    start = "Once there was a " + gender + " named " + firstName + "."
                    next1 = "A good " + gender + " living at " + address + "."
                    next2 = "One day, a wicked witch came to the " + lastName + " house."
                    next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                    ending = "But " + firstName + " was smart and avoided the wicked witch."

                    # print the story
                    print(start)
                    print(next1)
                    print(next2)
                    print(next3)
                    print(ending)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex6q

#.

    .. tabbed:: ch17ex7t

        .. tab:: Question

           Change 4 lines in the code below so that runs correctly without any errors.  It will print a poem.

           .. activecode::  ch17ex7q
                :nocodelens:

                input = "Roses,Violets,Sugar,Sue"
                pieces = input.split(",")
                flower1 = pieces[1]
                flower2 = pieces[2]
                spice = pieces[3]
                name = pieces[4]
                line1 = flower1 + " are red"
                line2 = flower2 + " are blue"
                line3 = spice + " is sweet"
                line4 = "And so it " + name
                print(line1)
                print(line2)
                print(line3)
                print(line4)

        .. tab:: Answer

            Fix the indices on lines 3-6 as shown below.

            .. activecode::  ch17ex7a
                :nocodelens:

                input = "Roses,Violets,Sugar,Sue"
                pieces = input.split(",")
                flower1 = pieces[0]
                flower2 = pieces[1]
                spice = pieces[2]
                name = pieces[3]
                line1 = flower1 + " are red"
                line2 = flower2 + " are blue"
                line3 = spice + " is sweet"
                line4 = "And so it " + name
                print(line1)
                print(line2)
                print(line3)
                print(line4)


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch17ex7q

#.

    .. tabbed:: ch17ex8t

        .. tab:: Question

            Fix the 6 errors so that the code prints the story properly.

            .. activecode::  ch17ex8q
                :nocodelens:

                # create the input
                input = "Abe,Brown,boy,1313 Maple Lane,trick"

                # split at the comma
                pieces = input.split(,)

                # initialize the variables
                firstName = pieces[1]
                lastName = pieces[2]
                gender = pieces[3]
                address = pieces[5]
                verb = pieces[-1]

                # create the story
                start = "Once there was a "  gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print("start")
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Answer

            On line 5, add quotations around the comma. On lines 8 - 11, fix the index positions. On line 15, add a plus sign before "gender".

            .. activecode::  ch17ex8a
                :nocodelens:

                # create the input
                input = "Abe,Brown,boy,1313 Maple Lane,trick"

                # split at the comma
                pieces = input.split(",")

                # initialize the variables
                firstName = pieces[0]
                lastName = pieces[1]
                gender = pieces[2]
                address = pieces[3]
                verb = pieces[-1]

                # create the story
                start = "Once there was a " + gender + " named " + firstName + "."
                next1 = "A good " + gender + " living at " + address + "."
                next2 = "One day, a wicked witch came to the " + lastName + " house."
                next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                ending = "But " + firstName + " was smart and avoided the wicked witch."

                # print the story
                print(start)
                print(next1)
                print(next2)
                print(next3)
                print(ending)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex8q

#.

    .. tabbed:: ch17ex9t

        .. tab:: Question

           Turn the following code into a function. It finds the name in a string and prints it.  Pass in the string and return the name if it is found and "Unknown" if not.  Be sure to call the function to test it.  Test it both when the name is there and when it isn't.

           .. activecode::  ch17ex9q
                :nocodelens:

                namePart = "name: Anu Gao"
                posName = namePart.find("name:")
                if (posName > -1):
                    name = namePart[posName+6:len(namePart)]
                else:
                    name = "Unknown"
                print(name)


        .. tab:: Answer

            Define the function as shown below.  Be sure to call the function to test it.  Test it both when the name is there and when it isn't.

            .. activecode::  ch17ex9a
                :nocodelens:

                def getName(namePart):

                    posName = namePart.find("name:")
                    if (posName > -1):
                        name = namePart[posName+6:len(namePart)]
                    else:
                        name = "Unknown"
                    return name

                print(getName("The name: Jasmine Brown"))
                print(getName("Jasmine Brown"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex9q

#.

    .. tabbed:: ch17ex10t

        .. tab:: Question

            The procedure below takes a string and splits it to create a story. Change it so that it takes multiple strings, so it creates the story without having to use split.

            .. activecode::  ch17ex10q
                :nocodelens:

                def witchStory (input):

                    # split at the comma
                    pieces = input.split(",")

                    # initialize the variables
                    firstName = pieces[0]
                    lastName = pieces[1]
                    gender = pieces[2]
                    address = pieces[3]
                    verb = pieces[4]

                    # create the story
                    start = "Once there was a " + gender + " named " + firstName + "."
                    next1 = "A good " + gender + " living at " + address + "."
                    next2 = "One day, a wicked witch came to the " + lastName + " house."
                    next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                    ending = "But " + firstName + " was smart and avoided the wicked witch."

                    # print the story
                    print(start)
                    print(next1)
                    print(next2)
                    print(next3)
                    print(ending)

                # call the procedure
                witchStory("Abe,Brown,boy,1313 Maple Lane,trick")

        .. tab:: Answer

            Create the procedure as shown below.

            .. activecode::  ch17ex10a
                :nocodelens:

                def witchStory (firstName, lastName, gender, address, verb):

                    # create the story
                    start = "Once there was a " + gender + " named " + firstName + "."
                    next1 = "A good " + gender + " living at " + address + "."
                    next2 = "One day, a wicked witch came to the " + lastName + " house."
                    next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
                    ending = "But " + firstName + " was smart and avoided the wicked witch."

                    # print the story
                    print(start)
                    print(next1)
                    print(next2)
                    print(next3)
                    print(ending)

                # call the procedure
                witchStory("Abe", "Brown", "boy", "1313 Maple Lane", "trick")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex10q

#.

    .. tabbed:: ch17ex11t

        .. tab:: Question

           Change the following code into a function that prints a crazy headline.  It should take the values as parameters. Be sure to call the function to test it.

           .. activecode::  ch17ex11q
                :nocodelens:

                input = "Elvis, alien, blue"
                pieces = input.split(",")
                name = pieces[0]
                thing = pieces[1]
                color = pieces[2]
                headline = name + " was abducted by a " + color + " " + thing + "."
                print(headline)


        .. tab:: Answer

            Define a function that takes a list and then call the function and pass in the list.  Print the result.

            .. activecode::  ch17ex11a
                :nocodelens:

                def getHeadline(name, thing, color):
                   return name + " was abducted by a " + color + " " + thing + "."

                print(getHeadline("Elvis", "alien", "blue"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex11q

#.

    .. tabbed:: ch17ex12t

        .. tab:: Question

            Fix the 3 errors to make the code print out the age.

            .. activecode::  ch17ex12q
                :nocodelens:

                agePart = "Their age: 17"
                posAge = agePart.find("age:")
                if (posAge < 0):
                    age = agePart[posAge:len(agePart)]
                else:
                    age = "Unknown"
                print(age)

        .. tab:: Answer

            In the if clause, check if the ``posAge > -1``. In the body of the if clause, set the substring to be ``posAge + 6:len(agePart_)``.

            .. activecode::  ch17ex12a
                :nocodelens:

                agePart = "Their age: 17"
                posAge = agePart.find("age:")
                if (posAge > -1):
                    age = agePart[posAge+5:len(agePart)]
                else:
                    age = "Unknown"
                print(age)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex12q

#.

    .. tabbed:: ch17ex13t

        .. tab:: Question

           Change the following into a procedure that prints the following story.  Pass in the values that can change.

           .. activecode::  ch17ex13q
                :nocodelens:

                input = "Jay,shoes"
                pieces = input.split(",")
                name = pieces[0]
                item = pieces[1]
                print("One day " + name + " went shopping.")
                print("He wanted to buy " + item + ".")
                print("But, he didn't like any.")
                print("So, " + name + " went home.")


        .. tab:: Answer

            Define the procedure and call it.  Be sure to pass the name and item.

            .. activecode::  ch17ex13a
                :nocodelens

                def tellStory(name, item):

                    print("One day " + name + " went shopping.")
                    print("He wanted to buy " + item + ".")
                    print("But, he didn't like any.")
                    print("So, " + name + " went home.")

                tellStory("Blake", "pants")


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex13q

#.

    .. tabbed:: ch17ex14t

        .. tab:: Question

            Change the following into a procedure that takes one string in the format "name: Bob, age: 10". The procedure should print the name and age.

            .. activecode::  ch17ex14q
                :nocodelens:

                agePart = "Their age: 17"
                posAge = agePart.find("age:")
                if (posAge > -1):
                    age = agePart[posAge+5:len(agePart)]
                else:
                    age = "Unknown"
                print(age)

                namePart = "name: Anu Gao"
                posName = namePart.find("name:")
                if (posName > -1):
                    name = namePart[posName+6:len(namePart)]
                else:
                    name = "Unknown"
                print(name)

        .. tab:: Answer

            Define procedure as shown below.

            .. activecode::  ch17ex14a
                :nocodelens:

                def aProcedure(aString):
                    aList = aString.split(",")
                    agePart = aList[1]
                    namePart = aList[0]

                    posAge = agePart.find("age:")
                    if (posAge > -1):
                        age = agePart[posAge+5:len(agePart)]
                    else:
                        age = "Unknown"
                    posName = namePart.find("name:")
                    if (posName > -1):
                        name = namePart[posName+6:len(namePart)]
                    else:
                        name = "Unknown"
                    print(name + "," + age)

                aProcedure("name: Bob,age: 10")
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex14q

#.

    .. tabbed:: ch17ex15t

        .. tab:: Question

           Write a personalized story.  It should start with a string of input and split that string to get the parts it needs for the story.  For example, define a name, animal, animal name, and animal adjective and create a story from that.

           .. activecode::  ch17ex15q
                :nocodelens:


        .. tab:: Answer

           Here is one example.  Look for a string with values separated with a comma.  Look for use of the ``split`` function.  Look for getting the values out of the list.

            .. activecode::  ch17ex15a
                :nocodelens:

                input = "Barb, horse, Sport, tall"
                pieces = input.split(",")
                name = pieces[0]
                animal = pieces[1]
                animalName = pieces[2]
                description = pieces[3]
                line1 = "Once upon a time there was a girl named, " + name + "."
                line2 = "She had a " + description + " " + animal + " named " + animalName + "."
                print(line1)
                print(line2)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex15q

#.

    .. tabbed:: ch17ex16t

        .. tab:: Question

            Write a procedure that takes in a string with 2 adjectives, a noun, and a verb separated by a comma (ex: "crazy,blue,banana,runs") in that order and prints a sentence using all 4 words.

            .. activecode::  ch17ex16q
                :nocodelens:

        .. tab:: Answer

            Define a procedure similar to the one below.

            .. activecode::  ch17ex16a
                :nocodelens:

                def aProcedure(aString):
                    pieces = aString.split(",")
                    adj1 = pieces[0]
                    adj2 = pieces[1]
                    noun = pieces[2]
                    verb = pieces[3]
                    sentence = "The " + adj1 + " and " + adj2 + " " + noun + " " + verb + "."
                    print(sentence)
                aProcedure("crazy,blue,banana,runs")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex16q

#.

    .. tabbed:: ch17ex17t

        .. tab:: Question

           Write a procedure that prints a personalized story.  It should take as input the items that will allow you to personalize a story.

           .. activecode::  ch17ex17q
                :nocodelens:

        .. tab:: Answer

            The example below is one possible procedure.  Be sure to call it to test it.

            .. activecode::  ch17ex17a
                :nocodelens:

                def tellAnimalStory(name, animal, animalName, description):

                    line1 = "Once upon a time there was a girl named, " + name + "."
                    line2 = "She had a " + description + " " + animal + " named " + animalName + "."
                    print(line1)
                    print(line2)

                tellAnimalStory("Barb","horse","Sport","handsome")


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex17q

#.

    .. tabbed:: ch17ex18t

        .. tab:: Question

            Write a procedure that takes in a name, age, and 2 verbs. If the age is less than 10, print a sentence using the name, age, and first verb. Otherwise print a sentence using the name, age, and second verb.

            .. activecode::  ch17ex18q
                :nocodelens:

        .. tab:: Answer

            Define a procedure similar to the one below.

            .. activecode::  ch17ex18a
                :nocodelens:

                def aSentence(name, age, verb1, verb2):
                    if age < 10:
                        print(name + " who is " + str(age) + " " + verb1)
                    else:
                        print(name + " who is " + str(age) + " " + verb1)
                aSentence("John", 10, "runs", "sleeps")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex18q

#.

    .. tabbed:: ch17ex19t

        .. tab:: Question

           Write a procedure that prints a personalized story.  It should take as input the items that will allow you to personalize a story.  It should also take a gender and vary the story based on the gender.

           .. activecode::  ch17ex19q
               :nocodelens:

        .. tab:: Answer

            Here is one example.  Look for a conditional with two options (if and else).

            .. activecode::  ch17ex19a
                :nocodelens:

                def tellAnimalStory(name, gender, animal, animalName, description):

                    if (gender.find("female") > -1):
                        line1 = "Once upon a time there was a girl named, " + name + "."
                        line2 = "She had a " + description + " " + animal + " named " + animalName + "."
                    else:
                        line1 = "Once upon a time there was a boy name, " + name + "."
                        line2 = "He had a " + description + " " + animal + " named " + animalName + "."

                    print(line1)
                    print(line2)

                tellAnimalStory("Barb", "female", "horse","Sport","handsome")
                tellAnimalStory("Mark", "male", "dog","Baxter","funny")


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex19q

#.

    .. tabbed:: ch17ex20t

        .. tab:: Question

            Create a procedure that takes in a string like "name: Bob,age: 10,verb: dance" and prints out a sentence with just the name, age, and verb.

            .. activecode::  ch17ex20q
                :nocodelens:

        .. tab:: Answer

            Define a procedure similar to below.

            .. activecode::  ch17ex20a
                :nocodelens:

                def aProcedure(aString):
		    aList = aString.split(",")
		    agePart = aList[1]
		    namePart = aList[0]
		    verbPart = aList[2]
		
		    posName = namePart.find("name:")
		    posAge = agePart.find("age:")
		    posVerb = verbPart.find("verb:")
		    
		    if (posName > -1):
		        name = namePart[posName+6:len(namePart)]
		    else:
		        name = "Unknown"
		    
		    if (posAge > -1):
		        age = agePart[posAge+5:len(agePart)]
		    else:
		        age = "Unknown"
		    
		    if (posVerb > -1):
		        verb = verbPart[posVerb+6:len(verbPart)]
		    else:
		        verb = "Unknown"
		
		    print(name + " who is " + age + " likes to " + verb)

		aProcedure("name: Bob,age: 10,verb: dance")
                
        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex20q
