.. qnum::
   :prefix: 6-11-
   :start: 1
   
Exam Questions for Chapters 5 and 6
-------------------------------------

The following questions test what you have learned in chapters 5 and 6. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch5a6ex
    
    .. mchoice:: e5a6_1
       :answer_a: value
       :answer_b: Second
       :answer_c: parameter
       :answer_d: First
       :correct: b
       :feedback_a: When you print a variable it will print the value of the variable.
       :feedback_b: When you call myFunction("Second") the value of parameter is set to "Second".  This code prints the value of the variable called "value" which is set to the value of parameter.  
       :feedback_c: When value = parameter is executed the value of parameter is copied into the space called value.  
       :feedback_d: While value was first set to "First" it was changed to a copy of the value of parameter.

       What value is printed when the following code is executed?

       ::

          name = "John Smith"
          def myFunction(parameter): 
              value = "First" 
              value = parameter 
              print (value) 

          myFunction("Second")
           
    .. mchoice:: e5a6_2
       :answer_a: <img src="../_static/squarea.png" alt="A square with the first line in black and the next 3 in red" width="300">
       :answer_b: <img src="../_static/squareb.png" alt="A square with all lines in red" width="300">
       :answer_c: <img src="../_static/squarec.png" alt="A square with the first two lines in black and the last two in red" width="300">
       :answer_d: <img src="../_static/squared.png" alt="A square with the first three lines in black and the last one in red" width="300">
       :correct: c
       :feedback_a: This would be true if the alice.pencolor("red") was after the first forward.
       :feedback_b: This would be true if the alice.pencolor("red") was before the first forward.
       :feedback_c: Since the alice.pencolor("red") is after the second forward the first two lines will be black and the last two will be red.
       :feedback_d: This would be true if the alice.pencolor("red") was after the third forward.

       Which picture would the following code produce?
       
       ::
       
          from turtle import *
          screen = Screen()
          alice = Turtle()
          alice.forward(50)
          alice.left(90)
          alice.forward(50)
          alice.left(90)
          alice.pencolor("red")
          alice.forward(50)
          alice.left(90)
          alice.forward(50)
          
    .. mchoice:: e5a6_3
       :answer_a: bob.move(50)
       :answer_b: bob.left(50)
       :answer_c: bob.forward(50)
       :answer_d: bob.right(50)
       :correct: c
       :feedback_a: Turtles don't understand move.
       :feedback_b: The left procedure turns the turtle left by the specified amount.
       :feedback_c: Turtles have a forward procedure which moves the turtle in the direction it is facing by the specified amount.
       :feedback_d: The right procedure turns the turtle right by the specified amount.

       Given the following lines of code, which will move the turtle bob 50 units forward?
       
       ::
       
          from turtle import * 
          space = Screen() 
          bob = Turtle()
          
    .. mchoice:: e5a6_4
       :answer_a: definition
       :answer_b: procedure
       :answer_c: turtle
       :answer_d: function
       :correct: d
       :feedback_a: You use the def keyword to define a procedure or function.  
       :feedback_b: A procedure doesn't return anything.
       :feedback_c: Turtles have procedures and functions.  
       :feedback_d: A function returns a result.

       A named sequence of statements that returns a result is known as which of the following?
           
    .. mchoice:: e5a6_5
       :answer_a: <img src="../_static/checka.png" alt="Shorter line to south and then longer line to east" width="300">
       :answer_b: <img src="../_static/checkb.png" alt="Longer line to south and then shorter line to east" width="300">
       :answer_c: <img src="../_static/checkc.png" alt="Longer line to north and then shorter line to east" width="300">
       :answer_d: <img src="../_static/checkd.png" alt="Shorter line to north and then longer line to east" width="300">
       :correct: d
       :feedback_a: This would be true if it was right first and then left.
       :feedback_b: This would be true if it was right first and then left and if the first forward was 150 and the last was 75.
       :feedback_c: This would be true if it was the shorter line to the north and the longer to the east.
       :feedback_d: This will draw the shorter line to the north and then the longer one to the east.

       Which picture would the following code produce?
   
       ::
       
          from turtle import * 
          space = Screen() 
          sue = Turtle()
          sue.left(90)
          sue.forward(75)
          sue.right(90)
          sue.forward(150)
          
           
    .. mchoice:: e5a6_6
       :answer_a: Two squares connected with a straight line
       :answer_b: Two triangles connected with a straight line
       :answer_c: Two rectangles connected with a straight line
       :answer_d: Nothing
       :correct: b
       :feedback_a: This would be true if the right turns were 90 and there were four forwards
       :feedback_b: This procedure will draw a triangle and it is called twice so it draws two triangles
       :feedback_c: This would be true if the right turns were 90 and there were four forwards with two different forward amounts
       :feedback_d: This would be true if we only defined the procedure and didn't execute it.

       What will the following code draw?
       
       ::
       
          def shape(turtle): 
              turtle.left(60)
              turtle.forward(100)
              turtle.right(120)
              turtle.forward(100)
              turtle.right(120)
              turtle.forward(100)
              turtle.right(120)
              
          from turtle import *
          space = Screen()
          luis = Turtle()
          shape(luis)
          luis.forward(200)
          shape(luis)
          


   