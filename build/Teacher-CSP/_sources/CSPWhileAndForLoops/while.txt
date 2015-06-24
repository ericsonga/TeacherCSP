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
	:prefix: csp-8-3-
	
.. highlight:: java
   :linenothreshold: 4


Looping When We Don't Know When We'll Stop
============================================

Now, how do we get the computer to do something only so many times, or until something happens that we want to happen?  We have to construct programs so that all the parts together make the logical expression true *until* we want it to be false.

Let's say that we want to find the square root of a number.  For some square roots, you're never going to be exact.  Let's say that we want to find a square root that, when multiplied by itself, is within `0.01` of the square we want.  How do we do it?  There's a really old process that we can apply here.

1. Start by guessing `2`.
2. Compute the guess squared.
3. Is the guess squared close to the target number?  If it's within `0.01`, we're done.  We'll take the absolute value of the difference, in case we overshoot. (In Python, ``abs`` is the absolute value function.)
4. If it's not close enough, we divide the target number by our guess, then average that value with our guess.
5. That's our new guess.  Square it, and go back to Step #3.

Here's a program that does exactly that.  Try different `target` values, and see how good it is at computing square roots.

.. activecode:: Square_Root
  :tour_1: "Line by line tour"; 1: sqR_line1; 2: sqR_line2; 3: sqR_line3; 4: sqR_line4; 5: sqR_line5; 6: sqR_line6; 7: sqR_line7; 8: sqR_line8;

  target = 6
  guess = 2
  guessSquared = guess * guess
  while abs(target-guessSquared) > 0.01:
      closer = target / guess
      guess = (guess + closer) / 2.0
      guessSquared = guess * guess
  print("Square root of", target,"is", guess)

.. mchoicemf:: 8_3_1_Square_Root_Q1
  :answer_a: No error, since we compute it inside the loop.
  :answer_b: We would get an error.
  :answer_c: We need the one before the while loop, but not the one afterward.
  :correct: b
  :feedback_a: We have to compute it before, or abs(target-guessSquared) > 0.01 would be an error.
  :feedback_b: A variable has to be declared (created) before it is used.
  :feedback_c: We need both.  The one before sets up the test.  The one inside the loop lets us update guessSquared.

   What would happen if we didn't compute ``guessSquared`` before the ``while`` loop?

Let's say that you wanted to figure out the square root of 6.  How many times would the body of the ``while`` loop be executed?  We could figure it out by tracing the program.  

.. video:: trace-squareroot
   :controls:
   :thumb: ../_static/squareRootTrace.png

   http://ice-web.cc.gatech.edu/ce21/1/static/video/square-root-trace.mov
   http://ice-web.cc.gatech.edu/ce21/1/static/video/square-root-trace.webm

.. mchoicemf:: 8_3_2_Count_Loops_Q1
  :answer_a: Just once.
  :answer_b: Twice.
  :answer_c: Three times.
  :answer_d: Four times
  :correct: c
  :feedback_a: The first time through the loop, guess is 2, and 2 * 2 is 4, which isn't 6.
  :feedback_b: The second time through the loop, guess is 2.5 (average of 3 and 2). But, 2.5 * 2.5 is still more than 0.01 away from 6.
  :feedback_c: The third time through the loop, guess is 2.45 which is a pretty good square root value for 6.
  :feedback_d: We don't get to a fourth time.  Guess is 2, then 2.5, then 2.45, and then we stop.

   How many times do we execute the body of the loop when ``target = 6`` (in the video)?

How about the square root of 25?  How about 2,356?  It's difficult to know ahead of time how many times the loop will execute.  That's where the ``while`` loop really shines, when you can specify an end condition (or rather, a *continue* condition).
