.. qnum::
   :prefix: 13-7-
   :start: 1
   
Exam Questions for Chapters 12 and 13
-------------------------------------

The following questions test what you have learned in chapters 12 to 13. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch12a13ex
    
    .. mchoice:: e12a13_1
       :answer_a: 5 to 20
       :answer_b: 6 to 20
       :answer_c: 5 to 19
       :answer_d: 6 to 19
       :correct: c
       :feedback_a: This would be true if it was if x >= 5 and x <= 20:
       :feedback_b: This would be true if it was if x > 5 and x <= 20:
       :feedback_c: It will print "condition true" when x is greater than or equal to 5 and less than 20.  
       :feedback_d: This would be true if it was if x > 5 and x < 20:

       Given the code below, what describes the values of x that will cause the code to print "condition true"? 
       
       ::

          if x >= 5 and x < 20:
              print ("condition true")
          print ("All done")
           
    .. mchoice:: e12a13_2
       :answer_a: A
       :answer_b: B
       :answer_c: C
       :answer_d: D
       :answer_e: E
       :correct: b
       :feedback_a: This would be true if the score was greater than or equal to 90
       :feedback_b: Since the score is less than 90 and greater than or equal to 80 "B" will print.
       :feedback_c: This would be true if the score was less than 80 and greater than or equal to 70.
       :feedback_d: This would be true if the score was less than 70 and greater than or equal to 60.
       :feedback_e: This would be true if the score was less than 60.  

       What is printed when the following code executes?
       
       ::
       
          score = 88
          if score >= 90:
              grade = "A"
          elif score >= 80:
              grade = "B"
          elif score >= 70:
              grade = "C"
          elif score >= 60:
              grade = "D"
          else:
              grade = "E"
          print(grade)
          
    .. mchoice:: e12a13_3
       :answer_a: 3
       :answer_b: 25
       :answer_c: 45
       :answer_d: 10
       :correct: c
       :feedback_a: This will print several things.
       :feedback_b: This will only print "You will ace a test"
       :feedback_c: This will only print "You will meet a new friend"
       :feedback_d: This will only print "You will catch a cold"

       For what value of num will the following print only "You will meet a new friend."?
       
       ::
       
          if num < 5 or num > 50:
              print("You will get a treat.")
          if num == 5 or num < 0:
              print("You will lose something.")
          if num < 10 or num > 40:
              print("You will meet a new friend.")
          if num < 20 or num > 60:
              print("You will catch a cold.")
          if num >= 20 and num <= 30:
              print("You will ace a test.")
              
    .. mchoice:: e12a13_4
       :answer_a: I
       :answer_b: II
       :answer_c: III
       :answer_d: IV
       :correct: c
       :feedback_a: This would always set x to 0 but if x was 1 in the original code it would not change.
       :feedback_b: If x is greater than 4 it is reset to 0 in the original code.
       :feedback_c: Anytime x is greater than 2 it will be set to 0 in the original code.
       :feedback_d: What if x is negative in the original code?  

       Which of the following is equivalent to the code segment below?
       
       ::
       
          if x > 2:
              x = x * 2
          if x > 4:
              x = 0
              
          I.   x = 0
          II.  if x > 2:
                   x = x * 2
          III. if x > 2:
                   x = 0
          IV.  if x > 2: 
                   x = 0
               else:
                   x = x * 2
                   
    .. mchoice:: e12a13_5
       :answer_a: A
       :answer_b: B
       :answer_c: C
       :answer_d: D
       :answer_e: E
       :correct: d
       :feedback_a: This would be true if the 2nd - 4th if were elif instead.
       :feedback_b: This would be true if the score was 83 and the 2nd - 4th if were elif instead.
       :feedback_c: This would be true if the score was 73 and the 2nd - 4th if were elif instead.
       :feedback_d: Since it is true that 93 is greater than 60 this will set grade to "D"
       :feedback_e: This would be true if score was less than 60.  

       What is the value of grade when the following code executes and score is 93?
       
       ::
       
          if score >= 90:
              grade = "A"
          if score >= 80:
              grade = "B"
          if score >= 70:
              grade = "C"
          if score >= 60:
              grade = "D"
          else 
              grade = "E"
     


   