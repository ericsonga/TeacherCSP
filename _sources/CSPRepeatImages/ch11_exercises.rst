..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
    

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: 11-8-

Chapter 11 Exercises
---------------------

Below is a selection of images that you can use in the programs in this section.

.. raw:: html

   <table>
   <tr><td>beach.jpg</td><td>baby.jpg</td><td>vangogh.jpg</td><td>swan.jpg</td></tr>
   <tr><td><img src="../_static/beach.jpg" id="beach.jpg"></td><td><img src="../_static/baby.jpg" id="baby.jpg"></td><td><img src="../_static/vangogh.jpg" id="vangogh.jpg"></td><td><img src="../_static/swan.jpg" id="swan.jpg"></td></tr>
   </table>
   <table>
   <tr><td>puppy.jpg</td><td>kitten.jpg</td><td>girl.jpg</td><td>motorcycle.jpg</td></tr>
   <tr><td><img src="../_static/puppy.jpg" id="puppy.jpg"></td><td><img src="../_static/kitten.jpg" id="kitten.jpg"></td><td><img src="../_static/girl.jpg" id="girl.jpg"></td><td><img src="../_static/motorcycle.jpg" id="motorcycle.jpg"></td></tr>
   </table>
   <table>
   <tr><td>gal1.jpg</td><td>guy1.jpg</td><td>gal2.jpg</td></tr>
   <tr><td><img src="../_static/gal1.jpg" id="gal1.jpg"></td><td><img src="../_static/guy1.jpg" id="guy1.jpg"></td><td><img src="../_static/gal2.jpg" id="gal2.jpg"></td></tr>
   </table>

.. note::

   Remember that it can take a bit of time to process all the pixels in a picture!  Check for errors below the code if it is taking a long time, but if you don't see any errors just wait.

#. 

    .. tabbed:: ch11ex1t

        .. tab:: Question
            
            Fix 4 syntax errors in the code below so that it correctly sets the red in all pixels to 0.  

            .. activecode:: ch11ex1q
                :nocodelens:

                from image import 

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg"

                # LOOP THROUGH THE PIXELS
                pixelList = img.getPixels()
                for p in pixelList:

                    # SET THE RED TO 0
                    p.setRed()

                    # UPDATE THE IMAGE
                    img.updatePixel()

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
      	            
        .. tab:: Answer
        
            Add a ``*`` at the end of line 1.  Add a ``)`` at the end of line 4.  Change line 11 to ``(0)``.  Change line 14 to ``(p)``.
            
            .. activecode:: ch11ex1a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH THE PIXELS
                pixelList = img.getPixels()
                for p in pixelList:

                    # SET THE RED TO 0
                    p.setRed(0)

                    # UPDATE THE IMAGE
                    img.updatePixel(p)

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch11ex1q
                
#. 
   
    .. tabbed:: ch11ex2t

        .. tab:: Question

           Fix the indention below to correctly set the red to the green, the green to the blue, and the blue to the red.
           
           .. activecode::  ch11ex2q
                :nocodelens:

                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels()
                for p in pixels:

                # STEP 4: GET THE DATA
                r = p.getRed()
                g = p.getGreen()
                b = p.getBlue()

                # STEP 5: MODIFY THE COLOR
                p.setRed(g)
                p.setGreen(b)
                p.setBlue(r)

                # STEP 6: UPDATE THE IMAGE
                img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)




        .. tab:: Answer
        
            Change the indention on lines 11-22 as shown below.  
            
            .. activecode::  ch11ex2a
                :nocodelens:
                
                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels()
                for p in pixels:

                    # STEP 4: GET THE DATA
                    r = p.getRed()
                    g = p.getGreen()
                    b = p.getBlue()

                    # STEP 5: MODIFY THE COLOR
                    p.setRed(g)
                    p.setGreen(b)
                    p.setBlue(r)

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex2q

#. 

    .. tabbed:: ch11ex3t

        .. tab:: Question

           Fill in the missing code on lines 9, 12, and 18 below to set the red to half the original value in all pixels in the picture.
        
           .. activecode::  ch11ex3q
                :nocodelens:
                
                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p 

                    # STEP 4: GET THE DATA
                    r = p.

                    # STEP 5: MODIFY THE COLOR
                    p.setRed(r * 0.5);

                    # STEP 6: UPDATE THE IMAGE
                    img.

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)         
         

        .. tab:: Answer
        
            Add ``in pixels:`` to line 9.  Add ``getRed()`` to line 12.  Add ``updatePixel(p)`` to line 18.  
            
            .. activecode::  ch11ex3a
                :nocodelens:

                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    # STEP 4: GET THE DATA
                    r = p.getRed()

                    # STEP 5: MODIFY THE COLOR
                    p.setRed(r * 0.5);

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)



        .. tab:: Discussion 

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch11ex3q
                
#. 

    .. tabbed:: ch11ex4t

        .. tab:: Question

           Fix the indention in the code below so that it correctly increases the red in each pixel in the picture by 1.5.  
           
           .. activecode::  ch11ex4q
                :nocodelens:

                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                    # STEP 2: PICK THE IMAGE
                    img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    # STEP 4: GET THE DATA
                    r = p.getRed()

                # STEP 5: MODIFY THE COLOR
                p.setRed(r * 1.5);

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
          
        .. tab:: Answer
        
            Remove the indention on lines 4-5.  Add indention on lines 14-15.
            
            .. activecode::  ch11ex4a
                :nocodelens:
                
                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    # STEP 4: GET THE DATA
                    r = p.getRed()

                    # STEP 5: MODIFY THE COLOR
                    p.setRed(r * 1.5);

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex4q
   
#. 

    .. tabbed:: ch11ex5t

        .. tab:: Question

           Fix the code below to correctly set the green and blue values to 0.75 times their current values. 
           
           .. activecode::  ch11ex5q
                :nocodelens:

                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    p.setGreen(g * 0)
                    p.setBlue(b * 0)
                    g = p.getGreen()
                    b = p.getBlue()

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Answer
        
            Get the values into ``g`` and ``b`` before you try to use them.  Multiply the old values by ``0.75`` instead of ``0``.    
            
            .. activecode::  ch11ex5a
                :nocodelens:

                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    # STEP 4: GET THE DATA
                    g = p.getGreen()
                    b = p.getBlue()

                    # STEP 5: MODIFY THE COLOR
                    p.setGreen(g * 0.75)
                    p.setBlue(b * 0.75)

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex5q
                
#. 

    .. tabbed:: ch11ex6t

        .. tab:: Question

           Change the following code to set the red to 0 for all pixels in the left half of the picture.
           
           .. activecode::  ch11ex6q
                :nocodelens: 
                
                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH THE PIXELS
                for x in range(img.getWidth()):
    	            for y in range(img.getHeight()):
    	            
    	                # GET THE DATA
    	                p = img.getPixel(x, y)

                        # SET THE RED TO 0
                        p.setRed(0)

                        # UPDATE THE IMAGE
                        img.updatePixel(p)

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Answer
        
            Change line 7 to ``int(img.getWidth() / 2)):``.  
            
            .. activecode::  ch11ex6a
                :nocodelens:
                
                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH THE PIXELS
                for x in range(int(img.getWidth() / 2)):
    	            for y in range(img.getHeight()):
    	            
    	                # GET THE DATA
    	                p = img.getPixel(x, y)

                        # SET THE RED TO 0
                        p.setRed(0)

                        # UPDATE THE IMAGE
                        img.updatePixel(p)

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex6q
                
#. 

    .. tabbed:: ch11ex7t

        .. tab:: Question

           Change the code below to set the red value in the pixels in the bottom half of the picture to 0.  
           
           .. activecode::  ch11ex7q
                :nocodelens: 
                
                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH THE PIXELS
                for x in range(img.getWidth()):
    	            for y in range(img.getHeight()):
    	            
    	                # GET THE DATA
    	                p = img.getPixel(x, y)

                        # SET THE RED TO 0
                        p.setRed(0)

                        # UPDATE THE IMAGE
                        img.updatePixel(p)

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                
                

        .. tab:: Answer
        
            Change line 8 to ``(int(img.getHeight() / 2), img.getHeight())``.
            
            .. activecode::  ch11ex7a
                :nocodelens
                
                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH THE PIXELS
                for x in range(img.getWidth()):
    	            for y in range(int(img.getHeight() / 2), img.getHeight()):
    	            
    	                # GET THE DATA
    	                p = img.getPixel(x, y)

                        # SET THE RED TO 0
                        p.setRed(0)

                        # UPDATE THE IMAGE
                        img.updatePixel(p)

                # SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex7q
                
#. 

    .. tabbed:: ch11ex8t

        .. tab:: Question

           Change the following code into a procedure to keep only the green values in all pixels in a picture.
           
           .. activecode::  ch11ex8q
                :nocodelens:
                
                # STEP 1: USE THE IMAGE LIBRARY
                from image import *

                # STEP 2: PICK THE IMAGE
                img = Image("beach.jpg")

                # STEP 3: LOOP THROUGH THE PIXELS
                pixels = img.getPixels();
                for p in pixels:

                    # STEP 5: MODIFY THE COLOR
                    p.setRed(0)
                    p.setBlue(0)

                    # STEP 6: UPDATE THE IMAGE
                    img.updatePixel(p)

                # STEP 7: SHOW THE RESULT
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)


        .. tab:: Answer
        
            Define a procedure to keep only the green values (set the red and blue to 0) in an image.  Pass the image to the procedure.  Do the import, create the image, call the prodecure, and show the result.
            
            .. activecode::  ch11ex8a
                :nocodelens:
                
                def keepOnlyGreen(img): 

                    # loop through all the pixels
                    pixels = img.getPixels();
                    for p in pixels:

                        p.setRed(0)
                        p.setBlue(0)
        
                        # change the pixel color at the current location
                        img.updatePixel(p)
                
                from image import *
                img = Image("beach.jpg")
                keepOnlyGreen(img)
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex8q
                
#. 

    .. tabbed:: ch11ex9t

        .. tab:: Question

           Define a procedure to negate an image.  See Image_Negate_Quarter from Chapter 11 section 7 for how to create a negative of an image.  Pass the image to the procedure.  Do the import, create the image, call the prodecure, and show the result. 
           
           .. activecode::  ch11ex9q
                :nocodelens:

        .. tab:: Answer
        
            Define the procedure as shown below.  
            
            .. activecode::  ch11ex9a
                :nocodelens:
                
                def negate(img): 

                    # loop through all the pixels
                    for x in range(img.getWidth()):
    	                for y in range(img.getHeight()):

                            # get the red, green, and blue at the current pixel
                            p = img.getPixel(x, y)
                            r = p.getRed()
                            g = p.getGreen()
                            b = p.getBlue()
            
                            # create a new pixel with the negated color
                            newPixel = Pixel(255-r, 255-g, 255-b)
        
                            # change the pixel color at the current location
                            img.setPixel(x, y, newPixel)
                
                from image import *
                img = Image("vangogh.jpg")
                negate(img)
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                                
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex9q
                
#. 

    .. tabbed:: ch11ex10t

        .. tab:: Question

           Write a procedure to mirror an image from left to right around a vertical line in the middle of the image.  Pass the image to the procedure.  Do the import, create the image, call the prodecure, and show the result. 
           
           .. activecode::  ch11ex10q
               :nocodelens:

        .. tab:: Answer
        
            Create a procedure as shown below.  Call it to test it. 
            
            .. activecode::  ch11ex10a
                :nocodelens:
                
                def mirrorLeftToRight(img):
                
                    # loop through the pixels from 0 to half the width
                    for x in range(int(img.getWidth() / 2)):
                        for y in range(img.getHeight()):

                            p = img.getPixel(x, y)
                            img.setPixel(img.getWidth() - 1 - x, y, p)

                from image import *
                img = Image("vangogh.jpg")
                mirrorLeftToRight(img)
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)
                        
                                 
        .. tab:: Discussion 

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch11ex10q



