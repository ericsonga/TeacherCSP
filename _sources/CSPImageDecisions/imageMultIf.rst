..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-15-4-
	
Multiple If's with Images
===========================

..	index::
	single: posterize

We can use multiple if's to reduce the number of colors in an image.  Let's say that if we have a little bit of each of red, green, and blue, we want to make each of them zero.  If we have more, we set them to a mid-range value like 120.  This is called *posterizing* because it reduces all the colors in a picture to a small number of colors -- like the ones you might use if you were making a poster.

.. raw:: html

    <img src="../_static/arch.jpg" id="arch.jpg">
    
.. activecode:: Posterize
    :tour_1: "Structural Tour"; 1: id3-line1; 4: id3-line4; 7-8: id3-line7-8; 9: id3-line9; 11-13: id3-line11-13; 16-17: id3-line16-17; 18-19: id3-line18-19; 20-21: id3-line20-21; 22-23: id3-line22-23; 24-25: id3-line24-25; 26-27: id3-line26-27; 30: id3-line30; 33: id3-line33; 36-37: id3-line35-36;
    :nocodelens:

    from image import *
    
    # CREATE AN IMAGE FROM A FILE
    img = Image("arch.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)
            
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()
            
            # VALUES FOR THE NEW COLOR
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
            
            # CREATE THE COLOR
            newPixel = Pixel(r,g,b)
            
            # CHANGE THE IMAGE
            img.setPixel(x, y, newPixel)
     
    # SHOW THE CHANGED IMAGE       
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)

.. mchoicemf:: 15_4_1_posterize1
   :answer_a: 8
   :answer_b: 3
   :answer_c: 120
   :answer_d: 16,777,216 (= 256 * 256 * 256) 
   :correct: a
   :feedback_a: Two possible values of each of red, green, and blue makes for 8 colors
   :feedback_b: Two values of each of red, green, and blue is more than 3.
   :feedback_c: Far fewer
   :feedback_d: That's the total number of colors possible.  But this code reduces that.
   
   How many different colors will be in our image when we are done?
   
Rewrite the code for posterizing an image using if and else rather than multiple if's.  Test that it still works correctly.  


.. note::  

   This is the end of chapter 15.  Readers who are part of the teacher study should go to `https://www.surveymonkey.com/s/TeacherQ1415 <https://www.surveymonkey.com/s/TeacherQ1415>`_ and take the post test for chapters 14 and 15 before continuing on to chapter 16.


       
