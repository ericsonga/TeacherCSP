..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. 	qnum::
	:start: 1
	:prefix: csp-7-5-
	
.. highlight:: java
   :linenothreshold: 4


There's a Pattern Here!
=====================================

There's a pattern in these programs, a pattern that is common when processing data.  We call this the **Accumulator Pattern**.  In the first program above, we *accumulated* the values into the variable ``sum``.  In the last few programs, we *accumulated* a product into the variable ``product``.

Here are the five steps in this pattern.

1. Set the accumulator variable to its initial value.  This is the value we want if there is no data to be processed.
2. Get all the data to be processed.
3. Step through all the data using a ``for`` loop so that the variable takes on each value in the data.
4. Combine each *piece* of the data into the accumulator.
5. Do something with the result.

Using the Accumulator Pattern
=====================================

What is the sum of all the numbers between 0 and 100?  We can answer that easily using our pattern.

.. activecode:: Numbers_Sum
    :tour_1: "Code tour"; 2: accum_line2; 4: accum_line4; 6: accum_line6; 8: accum_line8; 10: accum_line10;
	
    # STEP 1: INITIALIZE ACCUMULATOR 
    sum = 0  # Start out with nothing
    # STEP 2: GET DATA
    numbers = range(101)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
    	# STEP 4: ACCUMULATE 
    	sum = sum + number
    # STEP 5: PROCESS RESULT
    print(sum)
    
.. parsonsprob:: 7_5_1_Sum_100

   The following is the correct code for printing the sum of all the odd numbers from 1 to 100 using the accumulator pattern, but it is mixed up. Drag the blocks from the left and put them in the correct order on the right.  <b>Remember that the statements in the body of a loop must be indented!</b>  To indent a block drag it further right. Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0  
   =====
   numbers = range(1,100,2)
   =====
   for number in numbers:
   =====
       sum = sum + number
   =====
   print(sum)

The `range` function has one more version that we can use here.  By providing *three* input numbers, we can specify the *start* value, the *ending* value (which is one more than the *last* value), and the *step* -- how much to skip *between* numbers.

.. activecode:: Range_Examples

  print range(10)
  print range(1,11)
  print range(0,11,2)
  print range(1,11,3)

Now let's answer a slightly harder question: What is the sum of all the *even* numbers between 0 and 100?  It's easy with our pattern.
  
.. activecode:: Numbers_Sum_Even
    :tour_1: "Code tour"; 2: accE_line2; 4: accE_line4; 6: accE_line6; 8: accE_line8; 10: accE_line10;
	
    # STEP 1: INITIALIZE ACCUMULATOR 
    sum = 0  # Start out with nothing
    # STEP 2: GET DATA
    numbers = range(0,101,2)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
    	# STEP 4: ACCUMULATE 
    	sum = sum + number
    # STEP 5: PROCESS RESULT
    print(sum)

.. mchoicemf:: 7_5_2_Numbers_Even_Q1
   :answer_a: Because we started at 0
   :answer_b: Because we want to include 100
   :answer_c: Because the computer only understands 1s and 0s
   :answer_d: Because we're using a step of 2
   :correct: b
   :feedback_a: We would want to include 100.
   :feedback_b: If we stop BEFORE 101, we include 100.
   :feedback_c: Internally, yes, but in Python, all decimal digits are allowed.
   :feedback_d: That doesn't really matter.

   Why do we stop at 101 in the above program?

.. mchoicemf:: 7_5_3_Numbers_Even_Q2
   :answer_a: Because if we started with 1, we would get all odd numbers
   :answer_b: Because all lists start with zero
   :answer_c: Because we end with 101
   :correct: a
   :feedback_a: This gives us [0,2,4,6...98,100].
   :feedback_b: They don't have to start at 0.  
   :feedback_c: That is true, but is not relevant here.

   Why do we START with zero?

How do we know what's really going on in this program?  How do we know that *number* is taking on all of the even values from 0 to 100?  One way we can tell is by using a CodeLens on a smaller problem from 0 to 20.  We can step through the program line-by-line, or race to the end by clicking the *Last* button and then step backwards.

.. codelens:: Numbers_Sum_Step
	
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

.. mchoicemf:: 7_5_4_Numbers_Add_Odds_Q1
   :answer_a: Changed the range step from 2 to 3
   :answer_b: Changed the range end from 101 to 100
   :answer_c: Changed the range end from 101 to 99
   :answer_d: Changed the range start from 0 to 1
   :correct: d
   :feedback_a: That would give us [0,3,6,9,12...99].
   :feedback_b: That would give us the even numbers from 0 to 98.
   :feedback_c: That would give us the even numbers from 0 to 98.
   :feedback_d: That would give us [1,3,5,...99].

   Change the program above (in ActiveCode 7) to add up all the ODD numbers including up to 99.  You should run it to get 2500. What change did you make to the program?
   
.. parsonsprob:: 7_5_5_Sum_From_50

   The following is the correct code for printing the sum of all the even numbers from 50 to 100 using the accumulator pattern, but it is mixed up. Drag the blocks from the left and put them in the correct order on the right.  Don't forget to indent blocks in the body of the loop.  Just drag the block further right to indent.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0  
   =====
   numbers = range(50,101,2)
   =====
   for number in numbers:
   =====
       sum = sum + number
   =====
   print(sum)
   =====
   numbers = range(50,100,2) #distractor




