..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-18-7-

Most Populated and Least Populated States
======================================================

We're going to use another set of data (about the states) to give us insight into how we analyze the pollution data.

The top three largest states in population are:

==================   ============
State                Population
==================   ============
California           38,332,521
Texas                26,448,193
New York             19,651,127
==================   ============

And the three smallest are:

====================    ============
State                   Population
====================    ============
District of Columbia    646,449
Vermont                 626,630
Wyoming                 582,658
====================    ============


The three largest states in land area are Alaska, Texas, and California.  The three smallest are Connecticutt, Delaware, and Rhode Island.

The three *richest* states (by per capita income) are Maryland, Alaska, and New Jersey.  The three poorest are Arkansas, West Virginia, and Mississippi.

Do bigger or richer states have more pollution?
------------------------------------------------

What causes more pollution?
 
 - Maybe bigger states have more *stuff* and that leads to more pollution?
 - Maybe smaller states have more things crammed into a smaller place, and that leads to more pollution?
 - Maybe richer states have more industry, and that leads to more pollution?
 - Maybe more populous states have more people (so more cars and houses...) and that leads to more pollution?

Let's give you a way of asking these questions.  Let's write a program to get the average pollution **for a state**.


