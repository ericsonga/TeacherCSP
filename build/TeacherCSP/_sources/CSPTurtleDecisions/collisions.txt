..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. 	qnum::
	:start: 1
	:prefix: csp-14-5-
     
Avoiding Collisions
======================

You can use conditionals to detect when two turtles are getting close to each other and then have the turtles take evasive action. In the code below they try both try to turn right just as ships do if they are heading straight for each other.    

.. tabbed:: tab_collision

    .. tab:: Avoid_Collision_Exercise

        Run the program below.  Notice that this code doesn't quite work as intended.  Both ``jaz`` and ``mia`` turn completely around.  How could you modify the code to fix it so that they turn to avoid each other, but don't end up turning completely around?  You might want turn only if the distance between the x values `and` the y values is less than some amount.  If you have trouble figuring out a solution, click on the tab to view one way to solve this.
   
       .. activecode:: td_avoid_collision
          :tour_1: "Structural Tour"; 1-2: td4-line1-2; 3-6: td4-line3-6; 7: td4-line7; 8-11: td4-line8-11; 12: td4-line12; 13-14: td4-line13-14; 15-17: td4-line15-17;
          :nocodelens:

          from turtle import *      
          space = Screen()          
          jaz = Turtle()           
          jaz.shape('turtle')     
          mia = Turtle()          
          mia.shape('turtle')      
          mia.color('red')         
          mia.penup()               
          mia.goto(100,0)         
          mia.pendown()      
          mia.right(180)           
          for x in range(20):    
    	      jaz.forward(10)         
    	      mia.forward(10)       
    	      if (mia.xcor() - jaz.xcor() < 40):  
        	      jaz.right(45)                    
        	      mia.right(45)                       

        
    .. tab:: Avoid_Collision_Answer
    
       Here is one solution.  
       
       .. activecode:: td_avoid_collision_answer
          :nocodelens:

          from turtle import *    
          space = Screen()         
          jaz = Turtle()           
          jaz.shape('turtle')      
          mia = Turtle()           
          mia.shape('turtle')       
          mia.color('red')         
          mia.penup()               
          mia.goto(100,0)          
          mia.pendown()          
          mia.right(180)          
          for x in range(20):     
    	      jaz.forward(10)    
    	      mia.forward(10)    
    	      if (mia.xcor() - jaz.xcor() < 40 and mia.ycor() - jaz.ycor() < 10): 
                  jaz.right(45)          
                  mia.right(45)   
                  
    .. tab:: Discussion

       .. disqus::
           :shortname: cslearn4u
           :identifier: teachercsp_ch14collision                