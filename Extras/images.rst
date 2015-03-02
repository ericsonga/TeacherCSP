..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".
	

Loops and Patterns with Images
================================

.. |teachernote| image:: Figures/teachernote.png
    :width: 25px
    :align: bottom
    :alt: teachernote

.. index::
    single: pixel
	single: picture
	single: color

If Seymour Papert were starting kids out with computers today, he probably would also include bits of pictures (as well as bits of numbers and strings, and turtles) in his introduction.  Pictures on a computer are broken up into little bits called *pixels*, for *picture* (pix) *elements* (els).  These are laid out on a grid, from left to right (horizontal or **x** dimension) and top to bottom (vertical or **y** dimension).

Pixels are quite small.  Even this small picture below has 360 columns and 480 rows of pixels:

.. image:: Figures/arch.jpg

.. |audiobutton| image:: Figures/start-audio-tour.png


Each pixel has a color associated with it: An amount of redness, an amount of greenness, and an amount of blueness.
Let's remove the red from this picture.  Now, there are lot of lines in the program below, but fortunately, you can ignore most of them. The Audio Tour explains every line, but you really only care about 3-4 of these lines for most of our examples.  Press |audiobutton| to hear the audio tour explanation.

.. activecode:: csp_images_1
 :tour_1: Line-by-Line Tour; 1:imageline1 ;2:imageline2 ;4:imageline4 ;5:imageline5 ;6:imageline6 ;8:imageline8 ;9:imageline9 ;11:imageline11 ;12:imageline12 ;14:imageline14 ;15:imageline15 ;16-24:imageline16-24 ;16:imageline16 ;17-19:imageline17-19 ;22:imageline22 ;24:imageline24 ;26:imageline26 ;

 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # CAN CHANGE IMAGE HERE
    pict = loadImage('../_images/arch.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # BELOW IS PART YOU CARE ABOUT
    for x in range(pict.width):
      for y in range(pict.height):
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # For most effects
          # CHANGE THIS LINE FOR COLOR
          p = color(0,g,b)
          # CHANGE THIS LINE FOR POSITION
          set(x,y,p)

 run()

But we're not stuck using just the arch image.  We can use smaller images which will execute more quickly.

Teachers Notes: Understanding Image Representation
----------------------------------------------------
|teachernote| Understanding images requires understanding a nest of abstractions:

1. Pictures are made up of little pixels, laid out on an (x,y) grid.
2. Each pixel contains a color.
3. Each color has a red part, a green part, and a blue part.
4. Each color part is actually a number between 0 and 255.

There are some excellent CS Unplugged activities for undrestanding `image and color representation <http://csunplugged.org/image-representation>`_.

Your Library of Images
-----------------------

Because of the way that web page images work, you can only manipulate pictures here that have been pre-loaded to this web-server.  Play with these images by changing line 8 above, keeping the parentheses and the quotes.

.. |clocks| image:: Figures/clocks.jpg
    :width: 150px
    :align: top
    :alt: clocksjpg
	
.. |flowersthorns| image:: Figures/flowersthorns.jpg
    :width: 150px
    :align: top
    :alt: flowersthornsjpg
	
.. |shell| image:: Figures/shell.jpg
    :width: 150px
    :align: top
    :alt: shellpng
	
.. |statues| image:: Figures/statues.jpg
    :width: 150px
    :align: top
    :alt: statuesjpg
	
.. |vangogh| image:: Figures/vangogh.jpg
    :width: 150px
    :align: top
    :alt: vangoghjpg

.. table:: Images Library

   ===============================  ===============
       Filename
   ===============================  ===============
   **../_images/clocks.jpg**        |clocks|  
   **./_images/flowerthorns.jpg**   |flowersthorns|
   **../_images/shell.jpg**         |shell| 
   **../_images/statues.jpg**       |statues|
   **../_images/vangogh.jpg**       |vangogh|
   ===============================  ===============

.. |noredthorn| image:: Figures/redremovedthorns.jpg

You should try to modify the above program to try out the code on some additional images.

.. mchoicemf:: csp_images_swapfile
   :answer_a: ../_images/clocks.jpg
   :answer_b: ../_images/flowerthorns.jpg
   :answer_c: ../_images/shell.jpg
   :answer_d: ../_images/statues.jpg
   :correct: b
   :feedback_a: No, wrong image.
   :feedback_b: Yes!
   :feedback_c: No, wrong image.
   :feedback_d: No, wrong image.
   
   |noredthorn| This is an image created from the earlier program (removing red) from which of the library images?  Change line 8 in the earlier program to figure out which one of the above files was used for this image.
   
A Pattern for Image Processing
-------------------------------

As we have seen with turtles and words, there are some general patterns in the programs that we write.  With turtles, there was a polygon pattern (based on the Total Turtle Trip Theorem).  With words and numbers, there is the accumulator pattern.

The image processing pattern looks like this.  This program actually doesn't do anything to the image at all.  I'm just describing the pattern.

.. activecode:: csp_images_patterntemplate

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,g,b)
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)

 run()

Here are our six steps:

1. STEP 1: SET UP OUR IMAGE PROCESSING.  There is a bunch of code that we need to type in just to make image processing work.
2. STEP 2: PICK OUR IMAGE. We pick a particular image from our library by specifying it between quotes and between parentheses
3. STEP 3: SELECT OUR DATA. This example selects *every* pixel, that is "for all x in the width of the picture" and "for all y in the height of the picture".
4. STEP 4: GET OUR DATA.  You could *always* use the STEP 4 lines just as they are above, but you might be able to make it shorter if you wanted.  If you only needed red and were going to set the green and blue to zero, you don't have to get the green and blue.
5. STEP 5: CREATE OUR COLOR. This is the part that you will most often change.  Here's where you create a new color with red, green, and blue components.
6. STEP 6: CHANGE OUR DATA.  Normally, you put the color back at the same x and y coordinates.  But you might change that.



Changing Step 5: Increasing and decreasing color values
--------------------------------------------------------

First example: Let's change STEP 5, so that we decrease the red by 50%.

.. activecode:: csp_images_decreasered

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r*0.5,g,b)
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)

 run()

We can *increase* the red in a similar way. Let's change STEP 5, so that we increase the red by 150%.

.. activecode:: csp_images_increasered

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r*1.5,g,b)
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)

 run()

.. parsonsprob:: csp_words_palindrome

   Another way to get the a similar effect is to *decrease* the green and blue.  Figure out the right order of the program to do that.  Feel free to try it by modifying the above program.</p>
   -----
   # STEP 1: SET UP OUR IMAGE PROCESSING
   from processing import *
   pict = ''
   def setup():
     global pict
     size(360,480)
   =====
     # STEP 2: PICK OUR IMAGE
     pict = loadImage('../_images/flowerthorns.jpg')
   =====
     noLoop()
   =====
   def draw():
     image(pict,0,0)
   =====
     # STEP 3: SELECT OUR DATA
     for x in range(pict.width):
       for y in range(pict.height):
   =====
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
   =====
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,g*0.75,b*0.75)
   =====
          # STEP 6: CHANGE OUR DATA
          set(x,y,newcolor)
   =====
   run()


Changing Step 6: Changing where we put the colors
--------------------------------------------------------

Now, let's change Step 6.  Let's change *where* we put our new color.  Here is a subtle change from our original template -- look at Step 6 and compare it to other programs we have written here.

.. activecode:: csp_images_rotateflip

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,g,b)
          # STEP 6: CHANGE OUR DATA
          set(y,x,newcolor)

 run()

.. mchoicemf:: csp_images_rotate
   :answer_a: We rotated the image.
   :answer_b: We rotated and flipped the image.
   :answer_c: We flipped the image.
   :answer_d: No change.
   :correct: b
   :feedback_a: Compare the top and bottom. It's not really left and right.
   :feedback_b: Exactly -- it's like we rotated the picture behind itself
   :feedback_c: No, the image is rotated, too.
   :feedback_d: Compare this image to the original vangogh.jpg image.
   
   What happened when we swapped x and y when we stored the color back to the picture?

This one does a little math with the x and y.

.. activecode:: csp_images_flipped

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(pict.width):
      for y in range(pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,g,b)
          # STEP 6: CHANGE OUR DATA
          set(pict.width-x, pict.height-y, newcolor)

 run()

Changing Step 3: Changing which data we use
--------------------------------------------------------

We can also change which part of the picture we read and manipulate.

.. activecode:: csp_images_half

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/statues.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(0,int(pict.width/2)):
      for y in range(0,int(pict.height/2)):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(255-r,255-g,255-b)
          # STEP 6: CHANGE OUR DATA
          set(x, y, newcolor)

 run()

What happens if we skip every other x and y as we manipulate the colors?  Maybe make the green 255 and the blue 0? 

.. activecode:: csp_images_halfby2

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/statues.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    for x in range(0,pict.width,2):
      for y in range(0,pict.height,2):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,255,0)
          # STEP 6: CHANGE OUR DATA
          set(x, y, newcolor)

 run()

Let's try side-to-side copying.


.. activecode:: csp_images_flipvert

 # STEP 1: SET UP OUR IMAGE PROCESSING
 from processing import *
 pict = ''

 def setup():
    global pict
    size(360,480)
    # STEP 2: PICK OUR IMAGE
    pict = loadImage('../_images/vangogh.jpg')
    noLoop()

 def draw():
    image(pict,0,0)
    # STEP 3: SELECT OUR DATA
    halfway = int(pict.width/2)
    for x in range(0,halfway):
      for y in range(0,pict.height):
          # STEP 4: GET OUR DATA
          pixel = get(x,y)
          r = red(pixel)
          g = green(pixel)
          b = blue(pixel)
          # STEP 5: CREATE OUR COLOR
          newcolor = color(r,g,b)
          # STEP 6: CHANGE OUR DATA
          set(halfway + x, y, newcolor)

 run()

.. mchoicemf:: csp_images_mirrorq
   :answer_a: set(halfway - x, y, newcolor)
   :answer_b: set(x-halfway, y, newcolor)
   :answer_c: set(pict.width-x, y, newcolor)
   :answer_d: set(x-pict.width, y, newcolor)
   :correct: c
   :feedback_a: It does mirror, but only the left half
   :feedback_b: No effect
   :feedback_c: Yes, it looks like the woman is kissing herself
   :feedback_d: No, no effect.
   
   Try it: How would you mirror the image left-to-right?  Try changing line 26 to these.
