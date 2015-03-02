..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-15-2-

Combining Pictures
====================

We can use a conditional to copy just the non-white pixels from one picture to another picture.  We can take this tiny image of the women and put her by the Eiffel tower in Paris, France.  

.. raw:: html

    <img src="../_static/lady_tiny.png" id="lady_tiny.png">
    <img src="../_static/eiffel.jpg" id="eiffel.jpg">

.. activecode:: Copy_Non_White
    :tour_1: "Structural Tour"; 1: id2a-line1; 4-5: id2a-line4-5; 8-9: id2a-line8-9; 10: id2a-line10; 11-13: id2a-line11-13; 16: id2a-line16; 19: id2a-line19; 22-23: id2a-line21-22;
    :nocodelens:

    from image import *
    
    # CREATE THE IMAGES 
    img1 = Image("lady_tiny.png")
    img2 = Image("eiffel.jpg")

    # LOOP THROUGH ALL THE PIXELS IN IMG1
    for x in range(img1.getWidth()):
        for y in range(img1.getHeight()):
            p1 = img1.getPixel(x, y)
            r1 = p1.getRed()
            g1 = p1.getGreen()
            b1 = p1.getBlue()
  
            # CHECK IF THE PIXEL ISN'T WHITE
            if r1 < 250 and g1 < 250 and b1 < 250:
            
            	# COPY THE COLOR TO IMG2
            	img2.setPixel(x, y + 130, p1)
            
    # SHOW THE CHANGED IMAGE
    win = ImageWin(img2.getWidth(),img2.getHeight())
    img2.draw(win)

What would happen if ``img1`` was wider or taller than ``img2``?  Can you modify the program above to work even if that were true?