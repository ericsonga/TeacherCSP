..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-19-1-


Computer Abilities
================================================

Is that really all that a computer can do: name things, repeat steps, make decisions, and manipulate data? 

Yes, really -- that's it.  Everything else that a computer can do is just combinations of the those abilities:

- Naming values, moving them around, and doing arithmetic on them.

- Naming anything, including names for steps, names for names.

- Repeating instructions.

- Doing tests (using conditionals) and doing something because of the result.

- Accessing parts of a data collection.

.. index::
  single: abstraction

This is enough to build a Turing Machine.  In fact, everything that possibly *can* be computed, can be computed with just these four abilities, combined in different and sometimes surprising ways.  Probably the most powerful way is called **abstraction**.  An example of **abstraction** is when you create a function or procedure.  Others can then use that function or procedure without knowing or caring out the details of how it works.  

Now if you think about what you know that people do with a computer, the claim that these four abilities is all that you need to do *everything* may seem far-fetched.  How does a computer interface with a human or another computer?  All connections to the world outside of the computer appear as memory (special variable values) to a computer.

- *"What about reading from a keyboard or a mouse?"* Keyboards or mice get connected to a computer as if they were a special memory location.  Think about a variable named ``lastKeyPressed`` that would return a character that was the last key typed on the keyboard, or ``mousePosition`` that shows where the mouse cursor should now be.  The computer could run a loop, checking for new keys pressed or new mouse positions, and update the display accordingly.

- *"What about graphics?"*  Changing the display is just about changing memory (variables).  You can think about the display as a much of little dots (pixels) laid out along a horizontal axis and a vertical axis.  Each dot has three parts to it -- a red part, a green part, and a blue part.  To turn on the red to maximum at horizontal 100 dots from the right and 200 dots from the top can be thought of as ``display[100][200].red = 255``. 

- *"What about robots?  I've made a robot motor turn on, and I've read sensor data from a robot."*  Again, it's all about memory.  We can think about a special memory location that controls the motor, ``robotMotor = 0`` might turn it off, and ``robotMotor = 1`` might turn it on.  Sensor data might be available as a number read from a special variable, e.g., ``touchingBumper = readRobotPressureSensor``.

Now, think about all the wonderful things that computers can do, from web searches over billions of sites, to massive data analysis to track far away stars, to sharing messages among billions of on-line friends.  *All* of those can be understood in terms of these four abilities.  

Computers today are fast.  A typical computer today might execute a single assignment statement in one *billionth* of a second.  It is very difficult to write a program that will even take a full second to execute.  Mostly what a computer does today is *wait* -- wait on data coming in from the network (which the computer sees as, you guessed it, another memory location), or waiting on the user to type a key or move a mouse.

.. index::
  single: Halting Problem

We know that there are some limits to what we can compute.  For example, we know that we can't write a computer program that can test all other computer programs.  The problem is called *The Halting Problem*.  Imagine a program as one big long string.  We know that we can look at parts of that string using indexing.  We know that we can make decisions using ``if`` statements.  Can we write a program that can read other programs as strings, and tell us whether or not they will work?  Alan Turing, the same brilliant mathematician who defined computers for us, also wrote the mathematical proof that such a program is *impossible*. We can't write a general "program checker."

But we don't know the limits of computing with respect to ourselves.  Are we computable?  Is our intelligence just a really big and complicated program, with millions of conditions and hundreds of loops and billions of variables?  Is it possible to write a program that *is* intelligent?  We don't know the answers to those questions yet, but it's a fascinating problem to see how far we can push Alan Turing's machine.


