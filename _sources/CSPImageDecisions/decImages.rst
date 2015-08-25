..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-15-1-

Using Decisions with Images
==============================

*Learning Objectives:*

- Show examples of using conditionals to modify images.
- Use conditionals to combine two pictures. 
- Use ``if`` and ``else`` with images. 
- Use multiple ``if`` statements with images.

.. raw:: html

    <img src="../_static/gal2.jpg" id="gal2.jpg">
	
We can create image effects by conditionally executing code.  In the code below we will try to change the color of the women's shirt.  We will clear the red value (set it to 0) for any pixel that has a red value greater than 200 and a green value of less than 100 and a blue value of less than 100.   

.. activecode:: Color_Replace
    :tour_1: "Structural Tour"; 1: id1-line1; 4: id1-line4; 7-8: id1-line7-8; 9: id1-line9; 10-12: id1-line10-12; 15: id1-line15; 18: id1-line18; 21: id1-line21; 24-25: id1-line23-24;
    :nocodelens:

    from image import *
    
    # CREATE AN IMAGE FROM A FILE
    img = Image("gal2.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()
          
            # VALUES FOR THE NEW COLOR
            if r > 200 and g < 100 and b < 100:
             
            	# CREATE THE COLOR
            	newPixel = Pixel(0, g, b)
            
               	# CHANGE THE IMAGE
               	img.setPixel(x, y, newPixel)
            
    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    
What happens if we only test if red is greater than 200? Change the code above to try it. 

Can you find values that work well to only change the shirt color and not anything else?  

Remember that white light is a combination of red, green, and blue light with each value at 255 for totally white light.  Try to change just the white background to green.  
