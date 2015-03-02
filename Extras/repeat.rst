..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/teachernote.png
    :width: 25px
    :align: top
    :alt: teachernote

	
Ability #4: A computer can repeat steps
---------------------------------------------------------------

..	index:
	single: while
	single: indefinite loop
	pair: statements; while
	pair: statements; for

A computer never gets tired.  It can do the same thing over-and-over without slipping up.  It will execute its program for as long as power holds out.  So, there must be a way to get a computer to do things over-and-over.

Turns out that that's the easy part. Getting a computer to repeat is simple.  Getting it to *stop* is the tricky part.  

The most flexible and simple way of getting a computer to repeat is to use a `while` statement.  A `while` statement includes a logical expression, and is followed by a block.  **AS LONG AS THE EXPRESSION IS TRUE**, the block of statements gets executed.

So, here's a program that loops forever.

.. sourcecode:: python

  	while 1 == 1:
		print("Looping")
		print("Forever")

Since `1` will always be equal to `1`, the two `print` statements will just be repeated over and over and over again.  (We call that "looping.") I ran this in a form of Python where I could stop the computer easily:

.. sourcecode:: python

 	>>> while 1==1:
	 		print ("Looping")
	 		print ("Forever")
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever
	Looping
	Forever

(I stopped the computer around this point.)

Now, how do we get the computer to do something only so many times, or until something happens that we want to happen?  We have to construct programs so that all the parts together make the logical expression true *until* we want it to be false.

Let's say that we want to find the square root of a number.  For some square roots, you're never going to be exact.  Let's say that we want to find a square root that, when multiplied by itself, is within `0.01` of the square we want.  How do we do it?  There's a really old process that we can apply here.

1. Start by guessing `2`.
2. Compute the guess squared.
3. Is the guess squared close to the target number?  If it's within `0.01`, we're done.  We'll take the absolute value of the difference, in case we overshoot. (In Python, `abs` is the absolute value function.)
4. If it's not close enough, we divide the target number by our guess, then average that value with our guess.
5. That's our new guess.  Square it, and go back to Step #3.

Here's a program that does exactly that.  Try different `target` values, and see how good it is at computing square roots.

.. activecode:: squareRoots

  target = 6
  guess = 2
  guessSquared = guess * guess
  while abs(target-guessSquared) > 0.01:
     closer = target / guess
     guess = (guess + closer) / 2.0
     guessSquared = guess * guess
  print("Square root of", target,"is", guess)

.. mchoicemf:: squareRootsBefore
  :answer_a: No error, since we compute it inside the loop.
  :answer_b: We would get an error because guessSquared wouldn't have a value at the logical expression for while.
  :answer_c: We need the one before the while loop, but not the one afterward.
  :correct: b
  :feedback_a: We have to compute it before, or abs(target-guessSquared) > 0.01 would be an error.
  :feedback_b: Absolutely right.
  :feedback_c: No, we need both.  The one before sets up the test.  The one inside the loop lets us update guessSquared.

   What would happen if we didn't compute `guessSquared` before the `while` loop?

Let's say that you wanted to figure out the square root of 6.  How many times would the body of the `while` loop be executed?  We could figure it out by tracing the program.  

.. video:: trace-squareroot
   :controls:
   :thumb: ../_static/video-tracing-square-root.png

   http://www.cc.gatech.edu/~mark.guzdial/videos/trace-squareroot.mov
   http://www.cc.gatech.edu/~mark.guzdial/videos/trace-squareroot.webm

.. mchoicemf:: countLoops
  :answer_a: Just once.
  :answer_b: Twice.
  :answer_c: Three times.
  :answer_d: Four times
  :correct: c
  :feedback_a: First time through the loop, guess is 2, and guess*guess is 4, which isn't 6.
  :feedback_b: Second time, guess is 2.5 (average of 3 and 2). Squared, that's more than 0.01 away from 6.
  :feedback_c: Yup, third time guess is 2.45 which is a pretty good square root value for 6.
  :feedback_d: No, we don't get to a fourth time.  Guess is 2, then 2.5, then 2.45, and then we stop.

   How many times do we execute the body of the loop when `target = 6` (in the video)?

How about the square root of 25?  How about 2,356?  It's hard to count exactly.  That's where the `while` loop really shines, when you can specify an end condition (or rather, a *continue* condition).

It's much easier (and more common) to have the computer repeat something for a specific number of times.  For example, we could have a computer count from 1 to 10 pretty easily.  We will use a `counter` variable that we will *increment* inside the loop.

.. codelens:: whileCounter
   :showoutput: 

   counter = 1
   while counter <= 10:
    print(counter)
    counter = counter + 1

.. mchoicemf:: incrementCounter
		  :answer_a: It increments the variable counter.  The value (counter + 1) is computed, and then named `counter`.
		  :answer_b: Since counter is in the test for the while loop, it has to change or it would be an infinite (never-ending) loop. 
		  :answer_c: It has to be after the print, so that the 10 gets printed before stopping.
		  :answer_d: All of the above.
		  :correct: d
		  :feedback_a: It is absolutely true -- but why is it in the loop?
		  :feedback_b: Right, but it is also incrementing.
		  :feedback_c: That is true. So what is the last value of counter?
		  :feedback_d: Yup -- all three statements are true.

	   	  Why is it important to have `counter = counter + 1` inside the loop?


.. mchoicemf:: whileCounterQ
	  :answer_a: 1.
	  :answer_b: 10.
	  :answer_c: 11.
	  :correct: c
	  :feedback_a: Counter gets incremented from 1.
	  :feedback_b: The last value to be printed is 10.
	  :feedback_c: Yup, counter gets incremented to 11 after printing, and then the while loop tests counter, finds counter > 10 and stops.

   	  When this program is done, what is the value of counter?

.. index::
	pair: statements; for
	single: definite loop

Because we count in a loop so often, there is a special loop just for *definite loops* (loops that have a definite number of iterations).  That's a `for` loop.  We have a counter variable that takes on values within a `range`.  A `for` loop is much simpler and much easier to use than a `while` loop.

.. codelens:: forCounterSimple
	:showoutput: 

	for counter in range(1,10):
	  print(counter)

Before tracing the above to the end, see if you figure out this question:

.. mchoicemf:: forCounterQ
		  :answer_a: 9.
		  :answer_b: 10.
		  :answer_c: 11.
		  :correct: a
		  :feedback_a: Yes, a range goes from a starting point to one *less* than the ending point. If we want to count to 10, range(1,11).
		  :feedback_b: Try it -- nope, never gets to 10.
		  :feedback_c: No. In fact, it doesn't even get to 10! Try it.

	   	  What is the last value to be printed here?

The body of any loop can include...another loop!  Here is a super-simple program that generates all the times tables from 0 to 10.

.. codelens:: timesTable
	:showoutput: 

	for x in range(0,11):
		for y in range(0,11):
		  print(x,"*",y,"=",x*y)
		

Here are two different ways to look at this program.  In the first one, we look at the *structure* of the program -- what you can understand by just *looking* at the program.

.. video:: timesTableStructure
		   :controls:
		   :thumb: ../_static/video-timestable-structure.png

		   http://www.cc.gatech.edu/~mark.guzdial/videos/timestable-structure.mov
		   http://www.cc.gatech.edu/~mark.guzdial/videos/timestable-structure.webm


In this video, we look at the *execution* of the program -- how it actually works when it's being *run* by the computer.

.. video:: timesTableTrace
		   :controls:
		   :thumb: ../_static/video-timestable-tracing.png

		   http://www.cc.gatech.edu/~mark.guzdial/videos/timestable-tracing.mov
		   http://www.cc.gatech.edu/~mark.guzdial/videos/timestable-tracing.webm

Teacher's Note: Confusing `while` and `if`
_______________________________________________

|teachernote| A `while` loop and an `if` loop **look** almost the same.  They each have a logical expression, and a block of instructions underneath them.  

Students often get them confused.  Some key distinctions to make to students:

- An `if` block executes only once.  It does the test, then executes the instructions indented underneath *once*.

- A `while` block executes **repeatedly** *as long as the expression is true*.  The body of the loop can be executed *many* times.

When you show students examples of `while` loops, make sure that you choose examples where the body of the loop gets executed several times, to show a difference from `if`.  When you trace the program, trace more than one iteration through the body of the loop, to emphasize the multiple times.

Teacher's Note: `for` loops are easier and more "natural"
_________________________________________________________

|teachernote| Several researchers have studied how people "naturally" describe programs.  In one study, students as young as middle school are shown videos of someone playing a game like "Pokemon" then asked:

	"Imagine that you are going to program a computer to make this video game.  What do you think you would say to the computer?"

Participants rarely specify iteration like in a `while` loop.  They often say things like "For all the folders, I would..." or "For each of the characters, do this..."  Doing something "for all" is pretty common.  As we'll see in the next section, we can use `for` loops just like that, e.g., *for all*.  In general, `for` loops are closer to how people naturally talk about looping.

But computer science students often make an economic argument to themselves.

	"A `while` loop can do everything that a `for` loop can, and is more flexible.  I'll just learn that."

I used to teach a 2nd year undergraduate course on *Object-oriented Design*.  I wanted to know how much programming they knew before we got started.  One year, I gave them the challenge of writing the program to print the times table, just as you just saw.  With a `for` loop, it's three lines of code.  Out of 75 students, only 15 used a `for` loop.  *Every* other student used a `while` loop.  Using a `while` loop is more lines of code, and more opportunities for error. (And many of the students did make errors.)  But *they were more comfortable with the `while` loop, because that's what they decided to focus on.*

Start out using the `for` loop in your classes.  It will be easier and more natural for students, and give them early success. 