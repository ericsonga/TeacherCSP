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

.. 	qnum::
	:start: 1
	:prefix: csp-6-7-
	
.. highlight:: java
   :linenothreshold: 4


Using an Image Library
========================

Similarly, in the image processing example, we used ``from image import *``.  That made the functions ``getPixels()`` and ``getRed()`` accessible.  We could also define a new function that returns a new color, or a new procedure that changes the image.  

.. raw:: html

    <img src="../_static/arch.jpg" id="arch.jpg" >
    
.. activecode:: Image_Functions
    :tour_1: "Important Lines Tour"; 1,4,7,11,15,18: timg2-line1_4_7_11_15_18; 2: timg2-line2; 5: timg2-line5; 8-9: timg2-line8-9; 12-13: timg2-line12-13; 16: timg2-line16; 19-20: timg2-line19-20;
    :nocodelens:

    # USE THE IMAGE LIBRARY 
    from image import *
    
    # CREATE AN IMAGE FROM A FILE
    img = Image("arch.jpg")

    # LOOP THROUGH THE PIXELS
    pixels = img.getPixels()
    for p in pixels:
        
        # MODIFY THE PIXEL COLOR
        r = p.getRed()
        p.setRed(r * 0.5)
            
        # UPDATE THE IMAGE
        img.updatePixel(p)
            
    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    
The ``for p in pixels`` on line 9 let's us loop through all of the pixels in the image and change the red value for each pixel.  We'll talk more about looping (repeating steps) in the next chapter.

.. mchoice:: 6_7_1_Image_Functions_Q1
   :answer_a: It sets the red value in the current pixel to half the red of the original.  
   :answer_b: It sets the red value in the current pixel to twice the red of the original.
   :answer_c: It sets the red value in the current pixel to 5 times the red of the original.
   :answer_d: It sets the red value in the current pixel to 0.5.  
   :correct: a
   :feedback_a: Multiplying by 0.5 is the same as dividing by 2.  
   :feedback_b: This would be true if it was r * 2, instead of r * 0.5
   :feedback_c: This would be true if it was r * 5, instead of r * 0.5
   :feedback_d: This would be true if it was 0.5 instead of r * 0.5
   
   What does the line ``p.setRed(r * 0.5)`` do?


This ability to name functions and procedures, and sets of functions and procedures, and absolutely anything and any set of things in a computer is very powerful.  It allows us to create **abstractions** that make the computer easier to program and use.  More on that in a future chapter.

