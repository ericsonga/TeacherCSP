.. qnum::
   :prefix: 2-5-
   :start: 1
   
Exam Questions for Chapters 1 and 2
-------------------------------------

The following questions test what you have learned in chapters 1 and 2. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch1a2ex
    
    .. mchoice:: e1a2_1
       :answer_a: dog
       :answer_b: fish
       :answer_c: cat
       :answer_d: bird
       :correct: a
       :feedback_a: The value of var3 is first set to "bird" but then changed to be the value of var1.  The value of var1 is first set to "cat" but later changed to the value of var2 which was set to "dog".
       :feedback_b: Only var2 has the value of fish.  When you assign the value of a variable to the value of another variable the value is copied to the new variable.  No relationship is created between the two variables.
       :feedback_c: The value of var3 is first set to "bird" but then changed to be the value of var1.  However, the value of var1 also is changed after it is originally set.
       :feedback_d: While var3 is originally set to "bird" the value is changed later.

       What is the value of var3 after the following code executes?
       
       ::
       
          var1 = "cat" 
          var2 = "dog"
          var3 = "bird"
          var1 = var2
          var3 = var1
          var2 = "fish"
           
    .. mchoice:: e1a2_2
       :answer_a: variable
       :answer_b: turtle
       :answer_c: string 
       :answer_d: program
       :correct: a
       :feedback_a: A variable is a name associated with space (computer memory) that holds a value.  That value can change or vary.
       :feedback_b: A turtle is an object that can move forward and turn.  As it moves it can draw with a pen.
       :feedback_c: A string is a sequence of characters.
       :feedback_d: A program is a set of instructions that a computer can execute.  

       A named space that can hold a value is which of the following?
           
    .. mchoice:: e1a2_3
       :answer_a: integer
       :answer_b: turtle
       :answer_c: string
       :answer_d: image
       :correct: c
       :feedback_a: An integer is a positive or negative whole number like -30 or 23028.  
       :feedback_b: A turtle is an object that can move forward and turn.  As it moves it can draw with a pen.
       :feedback_c: A string is a sequence of characters.
       :feedback_d: An image is a representation of a digital picture and you can get and change the color values at pixels in the image.

       The kind of data that can be letters, digits, and other characters inside a pair of single or double quotes is which of the following?
           
    .. mchoice:: e1a2_4
       :answer_a: 3
       :answer_b: 2
       :answer_c: 5
       :answer_d: 0
       :correct: b
       :feedback_a: That is the original value of var1.  What is the value of var2?
       :feedback_b: When var1 is assigned to have the same value as var2 the value from var2 is copied and not changed.
       :feedback_c: That is the original value of var3.  What is the value of var2?
       :feedback_d: When one variable (var1) is set to the value of another (var2) it copies the value from the other (var2).  It does't change the value in the other (var2).

       What is the value of var2 after the following code executes?
   
       ::
       
          var1 = 3 
          var2 = 2
          var3 = 5
          var1 = var2
           
    .. mchoice:: e1a2_5
       :answer_a: A square
       :answer_b: A rectangle that is taller than it is wide
       :answer_c: A diamond
       :answer_d: A rectangle that is wider than it is tall
       :correct: b
       :feedback_a: This would be true if all the forward amounts were the same.
       :feedback_b: Zari's heading is set to 90 which turns her to point due north.  So, the rectangle is taller than it is high.  
       :feedback_c: This would be true if all the forward amounts were the same and the heading was 45 to start.
       :feedback_d: Turtles start off facing east and setting the heading to 90 turns it to face north.

       What shape would the following code draw?
       
       ::
       
         from turtle import *        # use the turtle library
         space = Screen()            # create a turtle screen (space)
         zari = Turtle()             # create a turtle named zari
         zari.setheading(90)         
         zari.forward(100)           # tell zari to move forward by 100 units
         zari.right(90)              # turn by 90 degrees
         zari.forward(50)           # tell zari to move forward by 100 units
         zari.right(90)              # turn by 90 degrees
         zari.forward(100)           # tell zari to move forward by 100 units
         zari.right(90)              # turn by 90 degrees
         zari.forward(50)           # tell zari to move forward by 100 units
         zari.right(90)              # turn by 90 degrees
    

   