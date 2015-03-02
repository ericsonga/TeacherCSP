..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

..  shortname:: Chapter 1: What a computer can do
..  description:: This is what a computer can do.

	
Ability #3: A computer can make decisions
===========================================

..	index::
	pair: if; statements
	single: logical expression
	single: posterizing

The first thing that a computer can do is to move information around and do arithmetic on the values.  The second thing a computer can do is to make decisions.  More specifically, (1) a computer can *test data* and (2) a computer can *execute some instruction* based on that test.  The ability to test data and take actions on the result is what allows the computer to deal with data input from the user and take action on it (e.g., `if creditCardValue == 'valid'`), or deal with data from the world around (e.g., `if signColor == 'red'`).

In Python, we do these two steps using an *if* statement.  An `if` statement includes a *logical expression* which is the 'test.'  It is followed by a *block* which are instructions to execute if the test is true.  If the test isn't true, the next statement *after* the `if` is executed.

Here's an example using an `if` statement.  We can make *decisions* about red, green, and blue values when computing an image.  Let's say that if we have a little bit of each of red, green, and blue, we want to make each of them zero.  If we have more, we set them to a mid-range value like 120.  This is called *posterizing* because it reduces all the colors in a picture to a small number of colors -- like the ones you might use if you were making a poster.

.. activecode:: csp_images_posterize

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          if r < 120:
             r = 0
          if r >= 120:
             r = 120
          if g < 120:
             g = 0
          if g >= 120:
             g = 120
          if b < 120:
             b = 0
          if b >= 120:
             b = 120
          newcolor = color(r,b,g)
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)

 run()

.. mchoicemf:: csp_images_posterizeQ
   :answer_a: 8
   :answer_b: 3
   :answer_c: 120
   :answer_d: 256 * 256 * 256
   :correct: a
   :feedback_a: Right -- two possible values of each of red, green, and blue makes for 8 colors
   :feedback_b: No, two values of each of red, green, and blue is more than 3.
   :feedback_c: No, far fewer
   :feedback_d: No, that's the total number of colors possible.  But this function reduces that.
   
   How many colors will be in our image when we are done?


Here's another example using an `if` statement.  Let's compute the gross and net pay for an hourly worker getting $7.50.  Let's say that if he works less than or equal to 35 hours a week, his tax rate is 15%, but if it's over 35, the tax rate is 18%.  We can imagine changing the `hours` variable before running the program.

.. codelens:: firstif

  hours = 25
  hourlyRate = 7.50
  if hours <= 35:
    taxRate = 0.15
  if hours > 35:
    taxRate = 0.18
  grossPay = hours * hourlyRate
  tax = grossPay * taxRate
  netPay = grossPay - tax
  print(netPay)

Try running this version with different values for `hours` worked -- edit the code above and change the first line so that `hours` has a different value. 

In this second version, we set a `taxRate` as a *default*, then change it only on the special condition. Does it work the same as the above example?

.. activecode:: firstifActive

   hours = 25
   hourlyRate = 7.50
   taxRate = 0.18
   if hours <= 35:
     taxRate = 0.15
   grossPay = hours * hourlyRate
   tax = grossPay * taxRate
   netPay = grossPay - tax
   print(netPay)

.. mchoicemf:: firstIfEquivalent
  :answer_a: No, they're always the same.
  :answer_b: Yes, they're different if hours is exactly 35.
  :answer_c: Yes, they're different if the hourlyRate is over 100.
  :correct: a
  :feedback_a: The end result is the same.
  :feedback_b: No, because "<=" is true if the value is less than or equal to.
  :feedback_c: No, the hourlyRate doesn't matter at all here.

   Are there values for hours and hourlyRate that make the two programs above result in different netPay?

The basic form of an `if` statement is the word **if** followed by a logical expression, and then a colon.  All the statements that are indented beneath the `if` are executed *IF AND ONLY IF* the logical express is `true`.

Some logical expressions include:

+------------+---------------------------------------------------------+
| Expression | Logical meaning                                         |
+------------+---------------------------------------------------------+
| a < b      | True if a is less than b                                |
+------------+---------------------------------------------------------+
| a <= b     | True if a is less than or equal to b                    |
+------------+---------------------------------------------------------+
| a > b      | True if a is greater than b                             |
+------------+---------------------------------------------------------+
| a >= b     | True if a is greater than or equal to b                 |
+------------+---------------------------------------------------------+
| a == b     | True if a is equal to b.                                | 
|            | (Two equals signs, to distinguish it from assignment)   |
+------------+---------------------------------------------------------+
| a != b     | True if a is *not* equal to b.                          | 
+------------+---------------------------------------------------------+

.. 	index::
	single: and
	single: or
	pair: logical operators; and
	pair: logical operators; or
	
We can also use the conjunctions `and` and `or`.  An `or` means that if *either* side is true, the whole expression is true.  An `and` means that only if *both* sides are true, the whole express is true.  A 'not' reverses the logical value that it precedes.

====================        ================
Expression                  Meaning
====================        ================
(a < b) or (c < d)          The whole express is true if a is less than b or c is less than d. 
--------------------        ----------------
(a < b) and (c < d)         The whole express is true if a is less than b **AND** *ALSO* c is less than d.  
--------------------        ----------------
not a < b                   Only true if a is actually greater than or equal to b.  `not a < b` is the same as `a >= b`.
====================        ================

The version of the below programs is broken in a subtle way.  For one value of `hours`, the `taxRate` will not receive any value, so the calculation of `grossPay` will fail with an `undefined variable`.  This is why professional programmers will assign *some* value to a variable like `taxRate` at the beginning of the program, so that errors like this won't happen.Can you figure out what value of `hours` will result in an error?

.. activeCode:: firstifbroken

  hours = 25
  hourlyRate = 7.50
  if hours < 35:
    taxRate = 0.15
  if hours > 35:
    taxRate = 0.18
  grossPay = hours * hourlyRate
  tax = grossPay * taxRate
  netPay = grossPay - tax
  print(netPay)

Try different values for `hours` then answer the below:

.. fillintheblank:: brokenrange
  :correct: \\b35\\s*\\+
  :blankid: brokenrange1
 
  What value for hours will result in an error complaining that the taxRate is undefined?  :textfield:`brokenrange1::mini`

It is certainly possible to have multiple `if` statements, and each one can match (or not match) the data.  Imagine a more complicated tax code, where hours decide some aspects of `taxRate` but there is a `secondaryTax` that depends on how much gross pay is.

.. activeCode:: secondaryTax

  hours = 25
  hourlyRate = 7.50
  if hours <= 35:
    taxRate = 0.15
  if hours > 35:
    taxRate = 0.18
  grossPay = hours * hourlyRate
  tax = grossPay * taxRate
  secondaryTax = 0
  if grossPay > 100:
    secondaryTax = grossPay * 0.05
  if grossPay > 500:
    secondaryTax = grossPay * 0.075
  netPay = grossPay - tax - secondaryTax
  print(netPay)

.. mchoicemf:: secondaryTax
  :answer_a: $6 an hour, e.g., hourlyRate = 6
  :answer_b: $2.50 an hour, e.g., hourlyRate = 2.5
  :answer_c: $2.51 an hour, e.g., hourlyRate = 2.51
  :answer_d: $12.51 an hour, e.g., hourlyRate = 12.51
  :correct: c
  :feedback_a: No -- $6/hour would incur secondaryTax, but that's not the smallest amount to do so.
  :feedback_b: No, because that would be exactly $100 grossPay. The test is <
  :feedback_c: Right -- it's a little more than $100 gross pay, but we can't increment less than a penny an hour.
  :feedback_d: $12.51 would trigger both secondaryTax if statements.

   Assuming a 40 hour work week, what is the smallest `hourlyRate` that would incur a secondary tax?

If the `grossPay` is over 500, it's also over 100.  So *both* `if` statements would be triggered.  But that's okay.  Trace the program to convince yourself that we don't end up taking *double* secondary tax.

.. codeLens:: secondaryTax

  hours = 40
  hourlyRate = 27.50
  if hours <= 35:
    taxRate = 0.15
  if hours > 35:
    taxRate = 0.18
  grossPay = hours * hourlyRate
  tax = grossPay * taxRate
  secondaryTax = 0
  if grossPay > 100:
    secondaryTax = grossPay * 0.05
  if grossPay > 500:
    secondaryTax = grossPay * 0.075
  netPay = grossPay - tax - secondaryTax
  print(netPay)


Teacher's Note: Avoiding the `else`
_______________________________________________

..	index::
   	pair: if; else

Most professional programmers would write this code:

.. sourcecode:: python

	hours = 25
	hourlyRate = 7.50
	if hours <= 35:
  		taxRate = 0.15
	if hours > 35:
  		taxRate = 0.18

Like this:

.. sourcecode:: python

  	hours = 25
	hourlyRate = 7.50
	if hours <= 35:
		taxRate = 0.15
	else:
		taxRate = 0.18

An `else` is an additional phrase on an `if` statement.  IF AND ONLY IF the *test* in the `if` is **false** does the block of statements after the `else` get executed.  Using an `if` with an `else` makes sure that *either* the 'if' block is executed *or* the 'else' block is executed, but **never** both.  

It is easy to write an `if` where you want *exactly* one block to execute, but you accidentally create a "hole" -- a condition when neither block executes.  That's what happened in this example:

.. activeCode:: firstifbroken2

  hours = 35
  hourlyRate = 7.50
  if hours < 35:
    taxRate = 0.15
  if hours > 35:
    taxRate = 0.18
  grossPay = hours * hourlyRate
  tax = grossPay * taxRate
  netPay = grossPay - tax
  print(netPay)

So why not teach `else` right away?  Because it actually makes code **much** harder for students to *read*.  Studies show that making the test *explicit* makes it **ten times** easier for beginning students to read programs with `if` statements [#Sime]_.  Using an `else` hides away the condition when the `else` block would execute.  Beginning students are having enough trouble just reading the code and making sense of it.  Using an `else` hides away clues to how the program is working.

To do the same thing as the `else` and be sure that it's readable, use a `not`.

.. sourcecode:: python

  	hours = 25
	hourlyRate = 7.50
	if hours <= 35:
		taxRate = 0.15
	if not hours <= 35:
		taxRate = 0.18

Teacher's Note: Sneak up on `and` and `or`
_______________________________________________

Students have a difficult time with logical expressions.  It's probably just a matter of experience.  They do a lot with arithmetic expressions, but *expressions whose value is true or false* are much less common in mathematics.

In particular, expressions with *multiple* logical expressions, combined with `and` and `or`, are challenging for students.  There is some research that shows that the more logical expressions in the program, the more difficult (in terms of time to understand it, ability to read or modify the program) it is for students.

Don't ask students to do much with `and` and `or` to start.  Give them a lot of experience with simple logical expressions, before introducing `and` and `or`.

Notes
____________________________________________________

.. [#Sime]  M. E. Sime, A. T. Arblaster, T. R. G. Green. in *Journal of Occupational Psychology*, 50(3), 205-216. http://onlinelibrary.wiley.com/doi/10.1111/j.2044-8325.1977.tb00376.x/abstract 
