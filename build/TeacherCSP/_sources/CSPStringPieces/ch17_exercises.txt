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

           Fix the 6 syntax errors in the code below so that it runs.  It will print a story.
           
           .. activecode::  ch17ex2q
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
            
            .. activecode::  ch17ex2a
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
                :identifier: teachercsp_ch17ex2q
                
#. 

    .. tabbed:: ch17ex3t

        .. tab:: Question

           Indent 6 lines and fix the call to the procedure so that it works correctly.  It will print a story.
           
           .. activecode::  ch17ex3q
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

    .. tabbed:: ch17ex4t

        .. tab:: Question

           Change 4 lines in the code below so that runs correctly without any errors.  It will print a poem. 
        
           .. activecode::  ch17ex4q
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
            
            .. activecode::  ch17ex4a
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
                :identifier: teachercsp_ch17ex3q
                
#. 
                
    .. tabbed:: ch17ex5t

        .. tab:: Question

           Turn the following code into a function. It finds the name in a string and prints it.  Pass in the string and return the name if it is found and "Unknown" if not.  Be sure to call the function to test it.  Test it both when the name is there and when it isn't. 
           
           .. activecode::  ch17ex5q
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
            
            .. activecode::  ch17ex5a
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
                :identifier: teachercsp_ch17ex4q
                
                
#. 

    .. tabbed:: ch17ex6t

        .. tab:: Question

           Change the following code into a function that prints a crazy headline.  It should take the values as parameters. Be sure to call the function to test it.
           
           .. activecode::  ch17ex6q
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
            
            .. activecode::  ch17ex6a
                :nocodelens:
                
                def getHeadline(name, thing, color):
                   return name + " was abducted by a " + color + " " + thing + "."
                   
                print(getHeadline("Elvis", "alien", "blue"))
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch17ex6q
                
#. 

    .. tabbed:: ch17ex7t

        .. tab:: Question

           Change the following into a procedure that prints the following story.  Pass in the values that can change.
           
           .. activecode::  ch17ex7q
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
            
            .. activecode::  ch17ex7a
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
                :identifier: teachercsp_ch17ex7q
                
#. 

    .. tabbed:: ch17ex8t

        .. tab:: Question

           Write a personalized story.  It should start with a string of input and split that string to get the parts it needs for the story.  For example, define a name, animal, animal name, and animal adjective and create a story from that.
           
           .. activecode::  ch17ex8q
                :nocodelens:
                
                
        .. tab:: Answer
        
           Here is one example.  Look for a string with values separated with a comma.  Look for use of the ``split`` function.  Look for getting the values out of the list.  
            
            .. activecode::  ch17ex8a
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
                :identifier: teachercsp_ch17ex8q
                
#. 

    .. tabbed:: ch17ex9t

        .. tab:: Question

           Write a procedure that prints a personalized story.  It should take as input the items that will allow you to personalize a story.  
            
           .. activecode::  ch17ex9q
                :nocodelens:

        .. tab:: Answer
        
            The example below is one possible procedure.  Be sure to call it to test it.
            
            .. activecode::  ch17ex9a
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
                :identifier: teachercsp_ch17ex9q
                
#. 

    .. tabbed:: ch17ex10t

        .. tab:: Question

           Write a procedure that prints a personalized story.  It should take as input the items that will allow you to personalize a story.  It should also take a gender and vary the story based on the gender.  
           
           .. activecode::  ch17ex10q
               :nocodelens:

        .. tab:: Answer
        
            Here is one example.  Look for a conditional with two options (if and else).  
            
            .. activecode::  ch17ex10a
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
                :identifier: teachercsp_ch17ex10q



