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
	:prefix: 15-6-

Chapter 15 Exercises
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

    .. tabbed:: ch15ex1t

        .. tab:: Question

            Make changes to 10 lines in the code below so that it runs.  It changes areas that look red in the original to green.

            .. activecode:: ch15ex1q
                :nocodelens:

                from  import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")

                # LOOP THROUGH ALL PIXELS
                for x in range(img.getWidth()):
                    for y in range(img.getHeight())
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

        .. tab:: Answer

            Add ``image`` after the ``from`` in line 1.  Add a ``:`` at the end of line 8.  Indent lines 14 - 21 four spaces to the right.

            .. activecode:: ch15ex1a
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


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch15ex1q

#.

    .. tabbed:: ch15ex2t

        .. tab:: Question

            Fix the code below so that the red in the picture gets changed to blue.

            .. activecode::  ch15ex2q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("girl.jpg")

                # LOOP THROUGH ALL PIXELS
                for x in range(img.getWidth()):
                for y in range(img.getHeight()):
                        p = img.getPixel(x, y)
                        r = p.getRed()
                        g = p.getGreen()
                        b = p.getBlue()

                        # VALUES FOR THE NEW COLOR
                        if r < 150 and g > 100 and b > 100:

                            # CREATE THE COLOR
                            newPixel = Pixel(0, 0, 0)

                            # CHANGE THE IMAGE
                            img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                    win = ImageWin(img.getWidth(),img.getHeight())
                    img.draw(win)

        .. tab:: Answer

            Fix the indentation like below and make sure the change occurs when the red value is greater than 150 and the green and blue values are less than 100. Fix the colors of the new pixel by setting it to (0,0,b).

            .. activecode::  ch15ex2a
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
                            newPixel = Pixel(0, 0, b)

                            # CHANGE THE IMAGE
                            img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex2q

#.

    .. tabbed:: ch15ex3t

        .. tab:: Question

           Fix the indention in the code below so that it runs correctly.  It does a primitive form of edge detection by getting all of the pixels (except for the last row) and all the pixels to the right of those and determining if the difference between the average of the rgb values for the pixel and the pixel to the right are substantially different.

           .. activecode::  ch15ex3q
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


        .. tab:: Answer

            Indent lines 9 to 24 as shown below.

            .. activecode::  ch15ex3a
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

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex3q

#.

    .. tabbed:: ch15ex4t

        .. tab:: Question

            Fix and change the code to change just the background color from white to gray.

            .. activecode::  ch15ex4q
                :nocodelens:

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
                if r > 0 and g > 0 and b > 0:

                # CREATE THE COLOR
                newPixel = Pixel(100, 100, 100)

                # CHANGE THE IMAGE
                img.setPixel(x, y, p)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Answer

            Fix the indentation like below and then make sure the if statement only works for r,g,b values greater than 200. Also, make sure you set the pixel to the new pixel.

            .. activecode::  ch15ex4a
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
                        if r > 200 and g > 200 and b > 200:

                            # CREATE THE COLOR
                            newPixel = Pixel(100, 100, 100)

                            # CHANGE THE IMAGE
                            img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex4q

#.

    .. tabbed:: ch15ex5t

        .. tab:: Question

           Fix the indention in the code below so that it runs correctly.  It posterizes a picture which means that it reduces all the colors in a picture to a small number of colors – like the ones you might use if you were making a poster..

           .. activecode::  ch15ex5q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

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

        .. tab:: Answer

            Indent lines 17, 19, 21, 23, 25, and 27 as shown below.

            .. activecode::  ch15ex5a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

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


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch15ex5q

#.

    .. tabbed:: ch15ex6t

        .. tab:: Question

            Fix the indentation so that the code puts the motorcycle on the beach. The code checks if the pixel isn't white in the first image, and if it's not, it places that pixel in the same location on the second image.

            .. activecode::  ch15ex6q
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image("motorcycle.jpg")
                img2 = Image("beach.jpg")
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

        .. tab:: Answer

            Indent like below.

            .. activecode::  ch15ex6a
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image("motorcycle.jpg")
                img2 = Image("beach.jpg")
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
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex6q

#.

    .. tabbed:: ch15ex7t

        .. tab:: Question

           Fix 5 errors in the code below. It will copy the non-white pixels from gal1.jpg to guy1.jpg.

           .. activecode::  ch15ex7q
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image("gal1.jpg")
                img2 = Image(guy1.jpg")

                # LOOP THROUGH ALL THE PIXELS IN IMG1
                for x in range(img1.getWidth():
                    for y in range(img1.getHeight())
                        p1 = img1.getPixel(x, )
                        r1 = p1.getRed()
                        g1 = p1.getGreen()
                        b1 = p1.getBlue()

                        # CHECK IF THE PIXEL ISN'T WHITE
                        if r1 < 250 and g1 < 250  b1 < 250:

                            # COPY THE COLOR TO IMG2
                            img2.setPixel(x, y, p1)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img2.getWidth(),img2.getHeight())
                img2.draw(win)


        .. tab:: Answer

            Add a ``"`` after the ``(`` on line 5.  Add another ``)`` before the ``:`` on line 8.  Add a ``:`` on line 9.  Add a ``y`` after the ``,`` on line 10.  Add an ``and`` on line 16.

            .. activecode::  ch15ex7a
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image("gal1.jpg")
                img2 = Image("guy1.jpg")

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
                            img2.setPixel(x, y, p1)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img2.getWidth(),img2.getHeight())
                img2.draw(win)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex7q

#.

    .. tabbed:: ch15ex8t

        .. tab:: Question

            Fix the 5 errors so that a swan in shown on a beach.

            .. activecode::  ch15ex8q
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image(swan.jpg)
                img2 = Image("beach.jpg")
                width1 = img1.getWidth()
                height1 = img1.getHeight()
                width2= img2.getWidth()
                height2 = img2.getHeight()
                maxWidth = min(width1,width2)
                maxHeight = min(height1,height2)

                # LOOP THROUGH THE PIXELS
                for x in range(maxWidth):
                  for y in range(maxHeight):
                    p1 = img1.getPixel()
                    r1 = p1.getRed
                    g1 = p1.getGreen()
                    b1 = p1.getBlue()

                    # CHECK IF THE PIXEL ISN'T WHITE
                    if r1 > 100 and g1 > 100 and b1 > 100

                      # COPY THE COLOR TO IMG2
                      img2.setPixel(x, y, pixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img2.getWidth(),img2.getHeight())
                img2.draw(win)

        .. tab:: Answer

            Add quotations around ``swan.jpg``. The ``getPixel()`` should be ``getPixel(x,y)``. It should be ``getRed()`` instead of ``getRed``. Add a colon after the if statement, and set the new pixel to ``(x,y,p1)``.

            .. activecode::  ch15ex8a
                :nocodelens:

                from image import *

                # CREATE THE IMAGES
                img1 = Image("swan.jpg")
                img2 = Image("beach.jpg")
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
                    if r1 > 100 and g1 > 100 and b1 > 100:

                      # COPY THE COLOR TO IMG2
                      img2.setPixel(x, y, p1)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img2.getWidth(),img2.getHeight())
                img2.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex8q

#.

    .. tabbed:: ch15ex9t

        .. tab:: Question

           Change the code below to use ``if`` and ``else`` rather than two ``if`` statements per color.  It posterizes an image.

           .. activecode::  ch15ex9q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

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

        .. tab:: Answer

            Change lines 18, 22, and 26 as shown below.

            .. activecode::  ch15ex9a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

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
                        else:
                            r = 120
                        if g < 120:
                            g = 0
                        else:
                            g = 120
                        if b < 120:
                            b = 0
                        else:
                            b = 120

                        # CREATE THE COLOR
                        newPixel = Pixel(r,g,b)

                        # CHANGE THE IMAGE
                        img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex9q

#.

    .. tabbed:: ch15ex10t

        .. tab:: Question

            Fix the indentation in the code and change it so that it edges the motorcycle but the background is black and the motorcycle edging will be white.

            .. activecode::  ch15ex10q
                :nocodelens:

                    from image import *

                    # CREATE AN IMAGE FROM A FILE
                    img = Image("motorcycle.jpg")

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

        .. tab:: Answer

            Fix the indentation like below and set the newPixel to be (255,255,255) if the absolute value of the difference of the averages is greater than 10. Otherwise the pixel should be (0,0,0).

            .. activecode::  ch15ex10a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("motorcycle.jpg")

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
                            newPixel = Pixel(255, 255, 255)
                        else:
                            newPixel = Pixel(0, 0, 0)

                        # CHANGE THE IMAGE
                        img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex10q

#.

    .. tabbed:: ch15ex11t

        .. tab:: Question

           Change the following code into a procedure. It posterizes an image. Be sure to call it to test it.

           .. activecode::  ch15ex11q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

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



        .. tab:: Answer

            Define the procedure and then import the library and create the image.  Pass the image to the posterize procedure.

            .. activecode::  ch15ex11a
                :nocodelens:

                def posterize(img):

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

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")
                posterize(img)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex11q

#.

    .. tabbed:: ch15ex12t

        .. tab:: Question

            Fix the 5 errors in the procedure so that it edges the motorcycle which means the image should only have 2 colors. The motorcycle should be one color, everything else should be the other color.

            .. activecode::  ch15ex12q
                :nocodelens:

                def edger(img):
                    # LOOP THROUGH ALL BUT LAST COLUMN
                    for x in range(img.getWidth() ):
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
                            if abs(average2 - average1) > 10
                                newPixel = Pixel(0, 0, 0)
                            else:
                                newPixel = Pixel(255, 255, 255)

                            # CHANGE THE IMAGE
                            img.setPixel(x, y, newPixel)

                            # SHOW THE CHANGED IMAGE
                            win = ImageWin(img.getWidth(),img.getHeight())
                            img.draw(win)

                    from image import *

                    # CREATE AN IMAGE FROM A FILE
                    img = Image(motorcycle.jpg)
                    edger(img)

        .. tab:: Answer

            The jpg file should be in quotations. You have to change line 3 to ``for x in range(img.getWidth() - 1):``. Add a ``:`` after the if statement. Take the 2 lines where you show the changed image outside of the body of both for loops.

            .. activecode::  ch15ex12a
                :nocodelens:

                def edger(img):
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

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("motorcycle.jpg")
                edger(img)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex12q

#.

    .. tabbed:: ch15ex13t

        .. tab:: Question

           Change the following into a procedure. It changes areas that are mostly red looking to green.  Be sure to call it to test it.

           .. activecode::  ch15ex13q
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



        .. tab:: Answer

            Define the procedure and then import the library and create the image.  Pass the image to the changeRedToGreen procedure.

            .. activecode::  ch15ex13a
                :nocodelens

                def changeRedToGreen(img):

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

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")
                changeRedToGreen(img)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex13q

#.

    .. tabbed:: ch15ex14t

        .. tab:: Question

            The code below currently makes the picture gray. Change it so that it posterizes (reduce the number of colors) the image instead.

            .. activecode::  ch15ex14q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("kitten.jpg")

                # LOOP THROUGH ALL PIXELS
                for x in range(img.getWidth()):
                    for y in range(img.getHeight()):
                        p = img.getPixel(x, y)

                        r = p.getRed()
                        g = p.getGreen()
                        b = p.getBlue()

                        # VALUES FOR THE NEW COLOR
                        if r < 120:
                            r = 150
                        if r >= 120:
                            r = 200
                        if g < 120:
                            g = 150
                        if g >= 120:
                            g = 200
                        if b < 120:
                            b = 150
                        if b >= 120:
                            b = 200

                        # CREATE THE COLOR
                        newPixel = Pixel(r,g,b)

                        # CHANGE THE IMAGE
                        img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Answer

            Set the values to the new color to 0 if the pixel color is less than 120 and 120 if it is greater than or equal to 120.

            .. activecode::  ch15ex14a
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

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex14q

#.

    .. tabbed:: ch15ex15t

        .. tab:: Question

           Write the code to posterize a picture but use 3 values for each color instead of 2.  Use 0 if the current value is less than 85, use 85 if the value is less than 170, else use 170.

           .. activecode::  ch15ex15q
                :nocodelens:


        .. tab:: Answer

            See the code in lines 16-33 for how to do this.

            .. activecode::  ch15ex15a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("beach.jpg")

                # LOOP THROUGH ALL PIXELS
                for x in range(img.getWidth()):
                    for y in range(img.getHeight()):
                        p = img.getPixel(x, y)

                        r = p.getRed()
                        g = p.getGreen()
                        b = p.getBlue()

                        # VALUES FOR THE NEW COLOR
                        if r < 85:
                            r = 0
                        elif r < 170:
                            r = 85
                        else:
                            r = 170
                        if g < 85:
                            g = 0
                        elif g < 170:
                            g = 85
                        else:
                            g = 170
                        if b < 85:
                            b = 0
                        elif b < 170:
                            b = 85
                        else:
                            b = 170

                        # CREATE THE COLOR
                        newPixel = Pixel(r,g,b)

                        # CHANGE THE IMAGE
                        img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex15q

#.

    .. tabbed:: ch15ex16t

        .. tab:: Question

            Fix the errors in the code and change the code to use if's and else's instead of just if's.

            .. activecode::  ch15ex16q
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("arch.jpg")

                # LOOP THROUGH ALL PIXELS
                for x in range(img.getWidth()
                    for y in range(img.getHeight()):
                        p = img.getPixels(x, y)

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

        .. tab:: Answer

            In line 7, add a ``)`` and ``:`` to the end. In line 9, it should be ``getPixel(x,y)`` not ``getPixels(x,y)``. The change the image line of code should be in the body of the inner for loop. Change all the second if clauses to else clauses.

            .. activecode::  ch15ex16a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("baby.jpg")

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
                        else:
                            r = 120
                        if g < 120:
                            g = 0
                        else:
                            g = 120
                        if b < 120:
                            b = 0
                        else:
                            b = 120

                        # CREATE THE COLOR
                        newPixel = Pixel(r,g,b)

                        # CHANGE THE IMAGE
                        img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex16q

#.

    .. tabbed:: ch15ex17t

        .. tab:: Question

           Write the code to do edge detection on a picture, but compare the curent pixel with the one below it rather than the one to the right.

           .. activecode::  ch15ex17q
                :nocodelens:

        .. tab:: Answer

            See the code below.  Only lines 7 trough 10 needed to change.  We now loop through all the columns and all but one of rows.  We compare the pixel at the current x and y to the one at the same x but y+1.

            .. activecode::  ch15ex17a
                :nocodelens:

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("swan.jpg")

                # LOOP THROUGH ALL BUT LAST ROW
                for x in range(img.getWidth()):
                    for y in range(img.getHeight() - 1):
                        p = img.getPixel(x, y)
                        p2 = img.getPixel(x, y + 1)
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

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex17q

#.

    .. tabbed:: ch15ex18t

        .. tab:: Question

            Write a procedure that takes an image as a parameter and edges it using the colors blue and white.

            .. activecode::  ch15ex18q
                :nocodelens:

        .. tab:: Answer

            Define a procedure similar to the one below.

            .. activecode::  ch15ex18a
                :nocodelens:

                from image import *

                def edgePicture(img):
                    img = Image(img)
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
                                newPixel = Pixel(0, 0, 255)
                            else:
                                newPixel = Pixel(255, 255, 255)

                            # CHANGE THE IMAGE
                            img.setPixel(x, y, newPixel)

                    # SHOW THE CHANGED IMAGE
                    win = ImageWin(img.getWidth(),img.getHeight())
                    img.draw(win)

                edgePicture("motorcycle.jpg")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex18q

#.

    .. tabbed:: ch15ex19t

        .. tab:: Question

           Write a procedure to remove the red on very red pixels (pixels that have a red value greater than 200 and a green and blue value of less than 100).

           .. activecode::  ch15ex19q
               :nocodelens:

        .. tab:: Answer

            Define the procedure and then import the library and create the image.  Pass the image to the removeVeryRed procedure.

            .. activecode::  ch15ex19a
                :nocodelens:

                def removeVeryRed(img):

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

                from image import *

                # CREATE AN IMAGE FROM A FILE
                img = Image("gal2.jpg")
                removeVeryRed(img)


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex19q

#.

    .. tabbed:: ch15ex20t

        .. tab:: Question

            Write a procedure that takes a picture as a parameter and converts all the red to grayscale.

            .. activecode::  ch15ex20q
                :nocodelens:

        .. tab:: Answer

            .. activecode::  ch15ex20a
                :nocodelens:

                from image import *

                def redToGray(aPic):
                    img = Image(aPic)

                    # LOOP THROUGH ALL PIXELS
                    for x in range(img.getWidth()):
                        for y in range(img.getHeight()):
                            p = img.getPixel(x, y)
                            r = p.getRed()
                            g = p.getGreen()
                            b = p.getBlue()
                            avg = (r + g + b) / 3
                            # VALUES FOR THE NEW COLOR
                            if r > 200 and g < 100 and b < 100:

                                # CREATE THE COLOR
                                newPixel = Pixel(avg,avg,avg)

                                # CHANGE THE IMAGE
                                img.setPixel(x, y, newPixel)

                    # SHOW THE CHANGED IMAGE
                    win = ImageWin(img.getWidth(),img.getHeight())
                    img.draw(win)

                redToGray("gal2.jpg")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch15ex20q
