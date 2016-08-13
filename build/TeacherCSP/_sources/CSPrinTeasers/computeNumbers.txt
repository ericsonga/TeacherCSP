..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

..  shortname:: Chapter: What You Can Do with a Computer
..  description:: Some tidbits of what you can do with a computer

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-1-3-


.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |teachernote| image:: Figures/apple.jpg
    :width: 26px
    :align: bottom
    :alt: teacher note

Compute with Numbers
=====================

We won't be using lots of math in this eBook, so don't worry if math isn't your favorite thing.  You will run and modify programs that work with words, turtles (virtual ones), and images as well as numbers.  The only math that you need to know is addition, subtraction, multiplication, and division. 

..	index::
	single: variable
	pair: programming; variable

Computers were first used for calculations. You may be used to doing calculations with a calculator, but calculations are often easier if you can *name* the numbers you are working with.  When you name a number, or the result of a calculation, you are creating a **variable**.  A **variable** is a name associated with computer memory that can hold a value and that value can change or vary.  One example of a **variable** is the score in a game.  The score starts off at 0 and increases as you play the game.

.. figure:: Figures/pongScore.png
    :width: 400px
    :align: center
    :alt: A game in Scratch with a score
    :figclass: align-center
    
    Figure 2: A pong game in `Scratch <http://scratch.mit.edu>`_ with a score shown in the upper left.

One thing that you might want to calculate is a **Body Mass Index**.    `Body Mass Index (BMI) <http://www.nhlbi.nih.gov/guidelines/obesity/BMI/bmicalc.htm>`_ is a measure of body fat that is useful in screening for health issues.  Generally speaking:

- A BMI of 18.5 or less is considered *underweight*.
- A BMI between 18.5 to 24.9 is considered *healthy*.
- A BMI between 25-29.9 is considered *overweight*.
- A BMI of 30 or over is considered *obese*.

To calculate a BMI, you need the height in inches and the weight in pounds.  You square the height (multiply the height in inches by itself), then divide the weight in pounds by the squared-height.  BMI is defined in terms of meters and kilograms, so to convert from pounds and inches multiply by 703.

In the box below is a computer program that calculates and prints the BMI for someone 60 inches tall (5 feet) and 110 pounds.  

Press the |runbutton| button below to make the computer execute these steps. The output from this program will be displayed to the right of the program.

Pres the |audiobutton| button below to bring up an "Audio Tour" that explains this program, line-by-line.

You can only use the *Save* and *Load* buttons if you are logged in. The *Save* button will save the current program and the *Load* button will load a saved program.

.. activecode:: BMI
    :tour_1: "Line-by-line Tour"; 1: BMI-line1; 2: BMI-line2; 3: BMI-line3; 4: BMI-line4; 5: BMI-line5; 6: BMI-line6; 7: BMI-line7; 
    :nocodelens:
    
    height = 60    # in inches (60 inches is 5 feet)
    weight = 110   # in pounds
    heightSquared = height * height
    BMI = weight / heightSquared
    BMImetric = BMI * 703
    print("BMI:")
    print(BMImetric)

Change the weight (in inches) and height (in pounds) in the program above, and press the *Run* button to calculate a new BMI.  

.. Note
   Notice how naming the values (using variables) for height and weight makes it easier to figure out what values need to be changed.  

.. mchoice:: 1_3_1_BMI_Q1
   :answer_a: 21.9
   :answer_b: 21.924704834
   :answer_c: 21
   :answer_d: 22
   :correct: b
   :feedback_a: Close, but the computer will give you more digits than that.
   :feedback_b: Yes!
   :feedback_c: No, the result will be a number with a decimal point and numbers after the decimal point.
   :feedback_d: No, the computer does not round the result.
   
   Imagine that you are 5 foot 7 inches and weighed 140 pounds.  What is your BMI?


