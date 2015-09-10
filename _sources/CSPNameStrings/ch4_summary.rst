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
	:prefix: csp-4-6-


Chapter 4 - Summary
====================

Chapter 4 included the following concepts from computing.

..	index::
    single: append
    single: capitalize
	single: concatenate
	single: function
	single: immutable
	single: index
	single: object
	single: string
	single: substring

- **Append** - You can add two strings together using the ``+`` symbol.  This is also called **concatenate**.  
- **Capitalize** - The capitalize function returns a new string with the first character capitalized.
- **Concatenate** - You can use ``+`` to concatenate (append) two strings like this ``string3 = string1 + string2``.  This will create a new string called ``string3`` with all the characters from the first string, ``string1``, followed by all the characters in the second string, ``string2``.
- **Function** - A function returns a value.  Function can take input as well, but don't have to.  An example is the string ``lower()`` function that returns a string with all lowercase letters.
- **Immutable** - Immutable means that it does not change.  Strings are immutable in Python.  When you call a function that appears to change a string, it will actually return a new string.  
- **Index** - An index is a number associated with the position of a character in a string.  In Python the first character in a string is at index 0.  
- **Object** - An object can have behavior (things it can do).  For example a turtle object can go forward a specified amount. Strings and turtles are objects in Python.  
- **String** - A string is a sequence of characters.  You specify a string as characters inside a pair of single, double, or triple quotes. 
- **Substring** -  A substring is a part of a string.  One substring of "Hi there" would be "Hi".  

Summary of String Functions
----------------------------

..	index::
	single: find
	single: len
	single: lower
	single: slice
	
Chapter 4 also included the following string functions.

- **append** - You can add two strings together using the ``+`` symbol.  This is also called **concatenate**.  The result of ``"Happy" + " Birthday"`` is ``"Happy Birthday"``.
- **find** - The find function takes a string as input and returns the **index** of the first occurence of that string in the string the function is called on. The code ``"goodbye".find('bye')`` returns 4.  
- **len** - The len function that can take a string as input and returns the number of characters in the string including any spaces.  For example ``len("Hi there")`` will return 8.  
- **lower** - The lower string function returns a new string with only lowercase letters. For example ``"ALL CAPS".lower()`` returns ``"all caps"``.  
- **slice** - You can get part of a string which is also called a **substring** using [start] or [start:end] which will return a substring of the current string starting at the given start position and if an end position is given ending at the character before the end position.  For example ``"out"[1]`` will return ``"u"`` and ``"otter"[2:5]`` returns ``"ter"``.  

.. note::  

   This is the end of chapter 4.   We would love it if you could give us some feedback on this chapter at https://www.surveymonkey.com/r/ch4-teacher-fb.  You might want to open this link in a new tab to make it easier for you to return to your place in this ebook. 

