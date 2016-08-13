..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note
    
.. 	qnum::
	:start: 1
	:prefix: csp-16-1-


Working with Collections of Data
=================================

*Learning Objectives:*

- Use ``+`` to append strings and lists together.
- Use ``*`` to create multiples of strings.
- Introduce the ``len`` (length) function to get the number of characters in a string or the number of items in a list.
- Introduce a list as something that holds items in order.
- Use an index to get an item from a list.
- Introduce a for each loop, which loops through all the items in a list or string.
- Show how to reverse a list.
- Vary the change amount when creating a list using the ``range`` function.
- Generate a decreasing list with the ``range`` function.
- Introduce the rainfall problem.

.. index:: 
	single: arrays; lists; indexing; collections;

Computers can work with more than just single values like 34.2 or single words like ``Hi``. They can also store large collections of numbers and letters and other objects.  To manipulate the data, computers really just use the first three abilities that we have discussed: the ability to name things, the ability to repeat instructions, and the ability to make decisions.  That means that computers have to be able to get single values out of those collections of data, and put single values back into them.

The rest of this chapter will give examples of using two data *collections*: strings and lists.



