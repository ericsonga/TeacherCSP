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
    
.. tabbed:: tab_combine

    .. tab:: Copy_Non_White_Exercize
    
       Run the program below.  What would happen if ``img1`` was wider or taller than ``img2``, like if we tried to do this with the apple (see below) as img1 and gal2 (see below) as img2?  Can you modify the program below to work even if that were true?  One thing you might need to know is that the function ``min(value1,value2)`` will return the smaller of the two values.  If you have trouble figuring out a solution click on the Answer tab to see one way to do this.

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
         
    .. tab:: Copy_Non_White_Answer
    
       Here is one way to make sure that the codes till works even if img1 is wider or taller than img2.
       
       .. activecode:: Copy_Non_White_Answer
          :tour_1: "Structural Tour"; 1: id2a-line1; 4-5: id2a-line4-5; 8-9: id2a-line8-9; 10: id2a-line10; 11-13: id2a-line11-13; 16: id2a-line16; 19: id2a-line19; 22-23: id2a-line21-22;
          :nocodelens:

          from image import *
    
          # CREATE THE IMAGES 
          img1 = Image("apple.jpg")
          img2 = Image("gal2.jpg")
          width1 = img1.getWidth()
          height1 = img1.getHeight()
          width2= img2.getWidth()
          height2 = img2.getHeight()
          maxWidth = min(width1,width2)
          maxHeight = min(height1,height2)

          # LOOP THROUGH THE PIXELS
          for x in range(maxWidth):
              for y in range(maxHeight):
                  p1 = img1.getPixel(x, y)
                  r1 = p1.getRed()
                  g1 = p1.getGreen()
                  b1 = p1.getBlue()
  
                  # CHECK IF THE PIXEL ISN'T WHITE
                  if r1 < 250 and g1 < 250 and b1 < 250:
            
            	      # COPY THE COLOR TO IMG2
            	      img2.setPixel(x, y, p1)
            
          # SHOW THE CHANGED IMAGE
          win = ImageWin(img2.getWidth(),img2.getHeight())
          img2.draw(win)
          
    .. tab:: Discussion

       .. disqus::
           :shortname: cslearn4u
           :identifier: teachercsp_ch15combine
          
    Below is a selection of images that you can use in the programs in this section.

    

          
Here are a couple of other pictures that we can also use.  The first is apple.jpg and the second is gal2.jpg.  The apple is 500 wide by 334 high and gal2 is 248 wide by 240 high.

.. raw:: html

    <img src="../_static/apple.jpg" id="apple.jpg">
    <img src="../_static/gal2.jpg" id="gal2.jpg">

