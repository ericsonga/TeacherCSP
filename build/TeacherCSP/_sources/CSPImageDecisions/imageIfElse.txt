..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-15-3-

If and Else with Images
===========================

..	index::
	single: sqrt
	single: square root
	pair: math; sqrt

What if we want to identify objects in a picture?  For example we might want to find the swan in the following picture. One way to get started looking for an object is to find the points where the color changes substantially from one pixel to the next.  This is called **edge detection** and it is an important step in image processing.  

.. raw:: html

    <img src="../_static/swan.jpg" id="swan.jpg">

To look for substantial color changes calculate the average color for the current pixel and the one to the the right of it. You can calculate the average as the sum of the red, green, and blue values divided by 3 (the number of values).  Then compare the absolute value of the difference in the averages and if it is greater than some amount set the current pixel to black, otherwise set it to white.  This will result in what looks like a simple pencil sketch of the picture.  Try larger and smaller values than 10 in line 21 to see how they change the result.

.. activecode:: Edge_Detection
    :tour_1: "Structural Tour";  1: id2b-line1; 4: id2b-line4; 7-8: id2b-line7-8; 9: id2b-line9; 10: id2b-line10; 11-13: id2b-line11-13; 14: id2b-line14; 15-17: id2b-line15-17; 18: id2b-line18; 21-22: id2b-line21-22; 23-24: id2b-line23-24; 27: id2b-line27; 30-31: id2b-line29-30;
    :nocodelens:

    from image import *
    
    # CREATE AN IMAGE FROM A FILE
    img = Image("swan.jpg")

    # LOOP THROUGH ALL BUT LAST COLUMN
    for x in range(img.getWidth() - 1):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)
            p2 = img.getPixel(x + 1, y)
            r1 = p.getRed()
            g1 = p.getGreen()
            b1 = p.getBlue()
            average1 = (r1 + g1 + b1) / 3
            r2 = p2.getRed()
            g2 = p2.getGreen()
            b2 = p2.getBlue()
            average2 = (r2 + g2 + b2) / 3
          
            # VALUES FOR THE NEW COLOR
            if abs(average2 - average1) > 10:
            	newPixel = Pixel(0, 0, 0)
            else:
            	newPixel = Pixel(255, 255, 255)
            
            # CHANGE THE IMAGE
            img.setPixel(x, y, newPixel)
        
    # SHOW THE CHANGED IMAGE  
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    
Notice that the code above loops from 0 to the width - 1 as the last value through the loop (remember that range doesn't include the last value).  This is necessary since we are comparing the current pixel's average color with the average color in the pixel to the right.  There is no pixel to the right of the last pixel in a row so we have to stop after processing the one before the last one.
    
Try other ways to detect big changes in color from one pixel to another.  
    
.. mchoice:: 15_3_1_Edge
   :answer_a: 0
   :answer_b: 2
   :answer_c: 256
   :answer_d: 16,777,216 (= 256 * 256 * 256) 
   :correct: b
   :feedback_a: Black and white are colors.
   :feedback_b: This image will only have black or white pixels in all columns except the rightmost one.  The pixel colors in the rightmost column will not be changed. 
   :feedback_c: This would be true if we were only using shades of gray, but we are only using two colors.  
   :feedback_d: This would be true if we were using all color values, but we are only using black and white.
   
   How many different colors will be in our image (except the last column) when we are done?

