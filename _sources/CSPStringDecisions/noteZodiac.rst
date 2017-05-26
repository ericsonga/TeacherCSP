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

..  qnum::
  :start: 1
  :prefix: csp-13-5-
  
.. highlight:: python
   :linenothreshold: 3

|bigteachernote| Teacher note: Group by Zodiac signs 
======================================================


This “unplugged” activity will give students practice on “tracing through” ``elif`` statements.

**Summary**


Twelve students stand in line side-by-side holding up signs with zodiac sign dates on them. The rest of the students start at one end of the line, and, for each sign, check to see if their birthday falls within that zodiac sign period. If it does, the student stops and stands behind that sign. At the end, all the students will be grouped according to their zodiac signs!

+-----------------+---------------------------+-----------------------------------------------------------------+
| **Zodiac Sign** | **Date**                  | **Sign characteristics**                                        |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Aries           | March 21 - April 19       | Active, Demanding, Determined, Effective, Ambitious             |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Taurus          | April 20 - May 20         | Security, Subtle strength, Appreciation, Instruction, Patience  |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Gemini          | May 21 - June 20          | Communication, Indecision, Inquisitive, Intelligent, Changeable |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Cancer          | June 21 - July 22         | Emotion, Diplomatic, Intensity, Impulsive, Selective            |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Leo             | July 23 - August 22       | Ruling, Warmth, Generosity, Faithful, Initiative                |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Virgo           | August 23 - September 22  | Analyzing, Practical, Reflective, Observation, Thoughtful       |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Libra           | September 23 - October 22 | Balance, Justice, Truth, Beauty, Perfection                     |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Scorpio         | October 23 - November 21  | Transient, Self-Willed, Purposeful, Unyielding                  |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Sagittarius     | November 22 - December 21 | Philosophical, Motion, Experimentation, Optimism                |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Capricorn       | December 22 - January 19  | Determination, Dominance, Perservering, Practical, Willful      |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Aquarius        | January 20 - February 18  | Knowledge, Humanitarian, Serious, Insightful, Duplicitous       |
+-----------------+---------------------------+-----------------------------------------------------------------+
| Pisces          | February 19 - March 20    | Fluctuation, Depth, Imagination, Reactive, Indecisive           |
+-----------------+---------------------------+-----------------------------------------------------------------+

from `<http://www.whats-your-sign.com/zodiac-sign-dates.html>`_

**To prepare**

-  1 ``if`` sign:

.. sourcecode:: python

    if birthday falls between March 21 to April 19:
        Your sign is Aries


-  10 ``elif`` signs (Taurus to Aquarius), leaving out the last one (Pisces): this will be your else condition. For example:

.. sourcecode:: python

    elif birthday falls between April 20 to May 20:
        Your sign is Taurus


And so on.
    
-  1 ``else`` sign:

.. sourcecode:: python

    else: 
        Your sign is Pisces

**Directions**

1. Have 12 volunteers line up side by side.
2. Give each volunteer a sign, making sure the leftmost student has the ``if`` sign, and the rightmost student has the ``else`` sign. It’s best to keep the ``elif`` signs in the correct order.
3. Have each student start at the ``if`` sign, to check if his birthday falls within the dates on the sign.
4. If it does, have that student stand behind the student holding the sign.
5. Otherwise, have the student step (right) to the next sign, to check if his birthday matches that one.
6. Let him keep going until he finds a sign that matches his birthday.

**Wrap up questions**

-  Ask the students how many steps they had to take to find their zodiac sign. Emphasize that for some cases, fewer ``elif`` conditions are checked than for others.
-  For the ``else`` sign, why was the zodiac sign dates for Pisces unnecessary? (It was the only option left)
-  Ask the students to rewrite the ``else`` sign so it becomes another ``elif`` sign. Point out that the ``else`` is optional.
