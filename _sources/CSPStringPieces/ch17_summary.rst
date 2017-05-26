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
	:prefix: csp-17-7-


Chapter 17 - Concept Summary
============================

Chapter 17 included the following concepts from computing.

..	index::
    single: find
    single: list
    single: index
    single: out of range error
    single: parameter
    single: slice
    single: split
    single: substring

- **List** - A list holds items in order.  An example of a list is ``[1, 2, 3]``.   
- **Index** - The index is the position of the item in a list or string.  In Python the first item is at index 0.  
- **Out of Range Error** - An out of range error will occur if you try to access an item in a list and give it an invalid index.  The first item in a list is at index 0 and the last is at one less than the length.
- **Parameter** - A parameter is input to a procedure or function that is specified when you define the procedure or function.  This is also called a **formal parameter**. The parameter will be assigned a value when the procedure or function is called.
- **Substring** - A substring is part of a string.  You can use the slice operator in Python to get a substring.

Summary of Python Keywords and Functions
------------------------------------------- 
- **Find** - The ``source.find(target)`` function returns the position of the target string in the source string if it is there or -1 if it is not.
- **Split** - The ``split`` function returns a list of strings separated by a specified character.  For example, if ``message = "Nora, Jones, 15"`` then ``message.split(",")`` would return ``['Nora', 'Jones', '15']``.
- **Slice** - The statement ``source[pos]`` returns the character at that position in the string.  This uses an index to get the character from the string at that index.  The statement ``source[start:end]`` returns the characters from start to one before end.  It uses two indices the start index (inclusive) and the end index (exclusive) to return a substring of the string from the start character to one before the end character.

.. note::  

   This is the end of chapter 17.   We would love it if you could give us some feedback on this chapter at https://www.surveymonkey.com/r/ch17-teacher-fb.  You might want to open this link in a new tab to make it easier for you to return to your place in this ebook.