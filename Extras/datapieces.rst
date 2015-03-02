..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. |teachernote| image:: Figures/teachernote.png
    :width: 25px
    :align: top
    :alt: teachernote


Ability #5: A computer can take data apart
=============================================

.. index:: 
	single: arrays; lists; indexing; collections; len

Computers can store more than just single values like 34.2 or the words `"Hello World!"`  They can also store banks of data, large collections of numbers and letters and other objects.  To manipulate those data, computers really just use those first three abilities: Move values around and do arithmetic on them, make decisions, and repeat instructions.  That means that computers have to be able to get single values out of those banks of data, and put single values back into them.

Here are some examples of data banks (called *collections*):

- A *string* is a collection of characters, in a sequence.  `"My name is Mark."` is a string with 16 characters in it. Spaces and periods are separate characters.
  Strings start with single quotes or double quotes.  You can actually do some simple "arithmetic" with strings. You can get the length of any collection with `len`.

.. codelens:: simpleStrings
  :showoutput:

  name = "Mark"
  start = 'My name is '
  combined = start + name
  print(len(combined))
  print(combined)
  print(name * 3)

.. mchoicema:: simpleStringsCombined
		  :answer_a: start+name
		  :answer_b: start+name+name+name
		  :answer_c: start + (3 * name)
		  :answer_d: start + 3 * name
		  :correct: b,c,d
		  :feedback_a: No, this just generates: My name is Mark
		  :feedback_b: Yes, this will work. Could you use multiplication?
		  :feedback_c: Yes, this will work, but multiplication is processed before addition, so you do not have to have parentheses.
		  :feedback_d: Yes, this will work just fine.

	   	  If we wanted to add one line to the above to print "My name is MarkMarkMark", which one of these would do it? Choose all that are correct.

- A *list* can hold any number of items, of any type.  You create and end lists with square brackets, and separate elements with commas.
  Again, `len` will tell you the number of items in the list.  You can do "arithmetic" with lists, too.  Multiplication makes copies.  We can
  add two lists together, even if one of the lists only has a single item in it.


.. codelens:: simpleLists
  :showoutput:

  myFirstList = [12,"apples",13,"bears"]
  print len(myFirstList)
  print myFirstList * 3
  mySecondList = myFirstList + [321.4]
  print mySecondList

To access individual items in a collection, we can use an *index number*.  Each item in a collection has a number associated with it -- think of it as the item's address in the collection.  The first item in a collection has index number `0`, the next one `1`, and so on.  We use square brackets to access items of the list, e.g., `myList[0]` will always return the first item in the list.

You can access individual items of a list just like they were variables.  They can give you values on the right side of an assignment, or they can be names on the left side.

.. codelens:: itemsAsVariables
  :showoutput:

  items = [2,4,6,8]
  items[0]="First item"
  items[1] = items[0]
  items[2] = items[2] + 1
  print(items)

.. mchoicemf:: itemsAsVariablesQ
	:answer_a: items[0]
	:answer_b: items[1]
	:answer_c: items[2]
	:answer_d: items[3]
	:correct: d
	:feedback_a: Originally, items[0] was 2, but then we set it to the string: First item
	:feedback_b: No, we set items[1] to be the same as items[0]: First item
	:feedback_c: No, we increment items[2]
	:feedback_d: Yup, it stays 8.

	Of the four items in the list named `items`, which one is not changed in the above program?
		  
If you try to access an index that isn't in the collection, you get an error **index out of range**.  That means that you have tried to access an item that isn't there. Try running the example below to see what that error looks like

.. activeCode:: indexError

  items = [2,4,6,8]
  print("The number of items is", len(items))
  items[0]="First item"
  items[1] = items[0]
  items[2] = items[2] + 1
  items[4] = "Last item"
  print(items)

Why would the programmer who wrote `items[4] = "Last item"` be trying to do?  Maybe trying to *add* an additional item to the list, "Last item."

.. mchoicema:: itemsAsVariablesQ
	:answer_a: items.append("Last item")
	:answer_b: items = items + ["Last item"]
	:answer_c: items.addIndex(4)
	:answer_d: items = items + "Last item"
	:correct: a,b
	:feedback_a: Yes -- append is a *method* that lists understand.
	:feedback_b: Yup, we know that we can add two lists together, and that's what we're doing here.
	:feedback_c: That does not actually work.  A programmer could add the ability for lists to understand addIndex, though.
	:feedback_d: No, you would get an error because you cannot add a list (items) to a string (Last item)
	
	Which of these lines *would* actually add "Last item" to the end of the `items` list? (Hint: Go ahead and try them above!) 

Whatever the length of the collection (the number of items in the collection), the highest *index* is one *less* than the length.  (Since the first item in the collection is index `0`.)  You have probably figured out why the `range` in the `for` loop stops one less than the last value.  If you access the `range` based on the `len` of the collection, you get exactly the right thing. We want to be able to do something like this:

.. activecode:: rangeLen

  myString = "This is a long string"
  for index in range(0,len(myString)):
     print(myString[index])

**Programming Challenge**: Complete the program below to print out each item in the list `myList`, one per line.

.. activecode:: allItems
  
  myList = ["this",1,"can","do", 2]
  # You fill in here

**An easier `for` loop**:  Because it is so common to use a `for` loop to touch each of the elements of a collection, we can do it even without using a `range` and indexing.

.. activecode:: foreach
  
  myList = [0,1,2,3,"end"]
  for item in myList:
    print(item)
  myString = "Abraham Lincoln"
  for character in myString:
    print(character)

This isn't actually a different `for` loop.  The function `range` actually creates a list of numbers, and the index just steps through each of those items one at a time.

.. activecode:: foreachRange
  
  myString = "Abraham Lincoln"
  myList = range(0,len(myString))
  for index in myList:
    print(myString[index])

.. mchoicemf:: foreachRangeQ
			  :answer_a: We would get an error for doing math in a range function
			  :answer_b: We would get an error because len(myString)/2 is 7.5
			  :answer_c: We would get "A b r a h a m" printing, one character per line
			  :answer_d: We would get "A b r a h a m " printing, one character per line (plus space)
			  :correct: c
			  :feedback_a: No, that is completely okay.
			  :feedback_b: No, though that could happen in some languages. Instead, we just get 7.
			  :feedback_c: Yup, exactly.
			  :feedback_d: No, 7.5 gets truncated to 7, not rounded to 8.

			   What would happen if we changed line 2 to `myList = range(0,len(myString)/2)`? (Hint: You could try it)

**Indexing the elements of the collection**: We can use the looping ability of computers, plus the indexing ability, to manipulate lists in interesting and even surprising ways. In the below program, we introduce the idea of an *accumulator*.  We start out the list `sofar` as being empty -- just a list with nothing in it.  As the program does on, it appends items from the `source` list into the `sofar` list.  

.. activecode:: revlistForward

  source = ["This","is","a","list"]
  sofar = []
  for index in range(0,len(source)):
    sofar = [source[index]] + sofar
    print sofar

.. mchoicemf:: reversinglist
		  :answer_a: Because we started at 0 and went to len(source)
		  :answer_b: Because we added up the elements into sofar, but put the new element ahead of the others so-far
		  :answer_c: Because of the square brackets around source[index]
		  :correct: b
		  :feedback_a: No, that is the normal way of accessing each element, one at a time.
		  :feedback_b: Yes -- if we had done sofar = sofar + [source[index]], sofar would have just duplicated the list, in order
		  :feedback_c: No, we need those in order to be add elements into the list.  You can only add a list to a list.

		   Why did we end up reversing the list?
		
.. index:: accumulator

There is a version of `range` that takes an *increment amount*, so that you can go up by steps more than two, or down by a negative number.  Try it out!

.. codelens:: justTheEvens
   :showoutput:

  numbers = [0,1,2,3,4,5,6,7,8,9,10]
  evens = []
  for index in range(0,len(numbers),2):
     evens = evens + [numbers[index]]
  print evens

.. activecode:: justTheEvensActive
   :showoutput:

  numbers = [0,1,2,3,4,5,6,7,8,9,10]
  evens = []
  for index in range(0,len(numbers),2):
     evens = evens + [numbers[index]]
  print evens

.. mchoicema:: justtheEvensQ
		  :answer_a: Start with numbers=[1,2,3,4,5,6,7,8,9,10]
		  :answer_b: Change the range to range(1,len(numbers),2)
		  :answer_c: Change the range to range(0,len(numbers),1)
		  :answer_d: Change the range to range(0,len(numbers),3)
		  :correct: a,b
		  :feedback_a: Yes, that would work, but there's an easier way
		  :feedback_b: Yes, just by starting at 1, then skipping 2 each time, we'd collect the odds
		  :feedback_c: No, that would collect all the numbers in evens
		  :feedback_d: No, that would result in 0,3,6,9 in evens

		   Which of these changes to the program would you give you just the odds? (Again: Try it!)

**Rainfall Problem**: Let's imagine that you have a list that contains amounts of rainfall, collected by a meteorologist.  Her rain gathering equipment occasionally makes a mistake and reports a negative amount.  We have to ignore those.  We need to write a program to (a) add up all the positive integers (and only positive integers), (b) count the number of positive integers (we will count with "1.0" so that our average can have a decimal point), and (c) print out the average at the end.  If there are *no* positive integers, don't try to print an average.

.. parsonsprob:: rainfall
   
  Construct a program that correctly solves the rainfall problem
  -----
  rain = [0,5,1,0,-1,6,7,-2,0]
  sumrain = 0
  count = 0
  =====
  for day in rain:
  =====
    if day >= 0:
  =====
      sumrain = sumrain + day
      count = count + 1.0
  =====
  if count > 0:
  =====
      ave = sumrain / count
      print("Average",ave)
  =====
  if not count > 0:
  =====
      print("No rain found.")

Type the program here and try it.  Does it work like you thought it would?

.. activecode:: rainfallActive

  rainfall = [0,.05,1.2,0,-1,.06,.07,-2,0]
  sumRainfall = 0
  countRainfall = 0
  # Your code goes here

**Reversing and accumulating**: Here's a program we saw earlier, but changing the `range` to something even more unusual.

.. activecode:: buildupstring

  source = ["This","is","a","list"]
  slowly = []
  for index in range(len(source)-1,-1,-1):
    slowly = [source[index]] + slowly
    print slowly

.. mchoicemf:: lenMinusOne
	  :answer_a: If we started with len(source), we would get an error for indexing past the end of the list
	  :answer_b: It is a mistake and should be len(source)
	  :answer_c: Because we have -1 in the other two spots
	  :correct: a
	  :feedback_a: Right -- the end element is at index len(source)-1
	  :feedback_b: No -- if accessed len(source) as an index, we would be going past the end of the list
	  :feedback_c: We have -1 in the end position because we want to stop at zero, and we have an increment of -1 (last position)
	
	   Why do we start at `len(source)-1` in this program?

Can you figure out what this program does?

.. sourcecode:: python

  source = "United States of America"
  slowly = ""
  for index in range(len(source)-1,-1,-1):
    slowly = slowly + source[index]
    print slowly

Try to figure out what this program does, then try this question.

.. mchoicemf:: reversed
			  :answer_a: <image src="../_static/reversal.png"/>
			  :answer_b: <image src="../_static/build-up-rightway.png"/>
			  :answer_c: <image src="../_static/build-up-missed-one.png"/>
			  :correct: a
			  :feedback_a: Yup, this takes letters from the end of the string forward, and adds them to the end
			  :feedback_b: No, this one is adding up letters in the forward direction
			  :feedback_c: No, this one ends at 0 (or rather, 1)

		   	  Which one of these is the output of that program?

Teacher's Note: The Rainfall Problem
_________________________________________________________

|teachernote| The Rainfall Problem is perhaps the most famous problem in computer science education research.  Elliot Soloway invented it and had students at Yale University try it in 1983.  Only 14% of students in week 10 of their first semester could solve the problem correctly.  Only 36% of the students in the second course could do it.  Only 69% of Juniors and Seniors could do it.  Every study of this problem in the last 30 years has come up with the same result -- students find this to be a very hard problem.

Why?  Thinking about that gives us insights into what students find hard about programming:

- There are several different kinds of tests going on here.  Did we see a negative number?  Did we read any positive integers at all?  In the full version of the problem, students also have to check if they have reached the end of the data.

- There are two accumulators (a sum and a count), and they have to be used together -- and **only** if the integer is positive.

So that gives you a sense for what pace to expect from your students.  Two accumulators and three `if` conditionals is enough that only 14% of Ivy League students can write the program after 10 weeks of undergraduate computer science class.  Notice how we dealt with the problem here -- we asked you to *assemble* the program out of *pieces* we already gave you.  That's already an easier task.  

Start out slow with what you ask students to write.