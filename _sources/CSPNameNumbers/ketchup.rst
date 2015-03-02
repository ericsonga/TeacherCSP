..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |teachernote| image:: Figures/apple.jpg
    :width: 30px
    :align: top
    :alt: teacher note
    
.. |bigteachernote| image:: Figures/apple.jpg
    :width: 50px
    :align: top
    :alt: teacher note

.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |codelensfirst| image:: Figures/codelens-first.png
    :height: 20px
    :align: top
    :alt: move to first button

.. |codelensback| image:: Figures/codelens-back.png
    :height: 20px
    :align: top
    :alt: back button

.. |codelensfwd| image:: Figures/codelens-forward.png
    :height: 20px
    :align: top
    :alt: forward (next) button

.. |codelenslast| image:: Figures/codelens-last.png
    :height: 20px
    :align: top
    :alt: move to last button
    
.. 	qnum::
	:start: 1
	:prefix: csp-3-6-

.. highlight:: java
   :linenothreshold: 4

Following the Ketchup Ooze
====================================

Let's compute how long it would take ketchup to ooze down a table.  Imagine that you tilted a four foot table, and poured ketchup at the top.  How long would it take to get to the bottom of the table?  We're going to ignore physics and the angle of the table, and just start from the average speed of ketchup as .028 miles per hour.

.. figure:: Figures/ketchup.jpg
    :width: 200px
    :align: center
    :alt: A picture of ketchup dripping from a bottle
    :figclass: align-center

    Figure 2: Ketchup dripping speed

.. codelens:: Ketchup_Speed

   dripMPH = .028
   FPM = 5280.0
   dripFPH = dripMPH * FPM
   MPH = 60
   dripFPM = dripFPH / MPH
   print("Ketchup speed in feet per minute:")
   print(dripFPM)
   print("Ketchup speed to move 4 feet in minutes:")
   print(4 / dripFPM)

   
The next type of problem is new.  It shows correct code in code blocks on the left side, but the order is mixed up.  You need to drag the blocks to the right side in the right order.  Please watch the video below for a demonstration.
   
**Click on the right arrow below to play the following video.**
   
.. video:: parsons
   :controls:
   :thumb: ../_static/MixedUpCodeVideoThumb.png

   http://ice-web.cc.gatech.edu/ce21/1/static/video/MixedUpCode.mov
   http://ice-web.cc.gatech.edu/ce21/1/static/video/MixedUpCode.webm

.. parsonsprob:: 3_6_1_Ketchup_Speed

   The following program figures out the ketchup speed in feet per <i>seconds</i>.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   dripMPH = .028
   FPM= 5280.0
   dripFPH = dripMPH * FPM
   =====
   MPH = 60
   dripFPM = dripFPH / MPH
   =====
   SPM = 60
   dripFPS = dripFPM / SPM
   =====
   print("Ketchup speed:")
   print(ketchupFPS)



