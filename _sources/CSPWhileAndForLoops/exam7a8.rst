.. qnum::
   :prefix: 8-9-
   :start: 1
   
Exam Questions for Chapters 7 and 8
-------------------------------------

The following questions test what you have learned in chapters 7 and 8. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch7a8ex
    
    .. mchoice:: e7a8_1
       :answer_a: Number: 10
       :answer_b: Number: number
       :answer_c: Number: 0
       :answer_d: Number: 11
       :correct: a
       :feedback_a: Since this while loop continues while number is less than or equal to 10 the last time in the loop it will print Number: 10.
       :feedback_b: This would be true if it was print ("Number: ", "number").  But since there are no quotes around number it will print the value of number.
       :feedback_c: While number is set to 0 to start it increments each time inside the loop.
       :feedback_d: This would be true if the print statement was after number was incremented by 1, but it is before.

       What is the last thing printed when the following code is run? 
       
       ::

          number = 0 
          while number <= 10: 
              print ("Number: ", number) 
              number = number + 1
           
    .. mchoice:: e7a8_2
       :answer_a: 1
       :answer_b: 2
       :answer_c: 3
       :answer_d: 4
       :correct: c
       :feedback_a: This would be true if the print was outside of the loop, but it is in the loop.
       :feedback_b: This would be true if it was range(1,3)
       :feedback_c: The range(1,4) returns a list with the values 1, 2, and 3.  So this will print hello 3 times.
       :feedback_d: This would be true if it was range(1,5).  Remember that it includes the first value and ends before the second value.

       When the following code is run, how many times is hello printed?
       
       ::
       
          helloArray = range(1,4) 
          for x in helloArray: 
              print ("hello")
          
           
    .. mchoice:: e7a8_3
       :answer_a: The program will loop indefinitely
       :answer_b: The value of number will be printed exactly 1 time
       :answer_c: The while loop will never get executed
       :answer_d: The value of number will be printed exactly 5 times
       :correct: a
       :feedback_a: This code loops while number is less than or equal to 5 and number only increments if it is less than 5 and it is originally set to 5 so number never changes.
       :feedback_b: This would be true if it was if number <= 5.
       :feedback_c: This would be true if number was set to a number larger than 5 to start.
       :feedback_d: This would be true if number was set to 1 to start.

       What is the result of executing the following code?
       
       ::
       
          number = 5 
          while number <= 5: 
              if number < 5: 
                  number = number + 1 
              print(number)
           
    .. mchoice:: e7a8_4
       :answer_a: 4
       :answer_b: 0
       :answer_c: 7
       :answer_d: 16
       :correct: d
       :feedback_a: This would be true if it was sum = sum + 1
       :feedback_b: This would be true if sum never changed, but each time through the loop number is added to the current sum.
       :feedback_c: This would be true if it printed the number.
       :feedback_d: This adds up the numbers in values and prints the sum.

       What will be printed by the following code when it executes?
   
       ::
       
          from turtle import * 
          sum = 0                                                  
          values = [1,3,5,7]
          for number in values:
              sum = sum + number
          print (sum)
           
    .. mchoice:: e7a8_5
       :answer_a: 12
       :answer_b: 9
       :answer_c: 7
       :answer_d: 8
       :correct: b
       :feedback_a: This would be true if counter started off with a value of 0.  
       :feedback_b: This loop executes 3 times.  After the first loop sum = 1 and counter = 3, after the second loop sum = 4 and counter = 5, and after the third loop sum = 9 and counter = 7.
       :feedback_c: This is the value of counter, but this code prints the value of sum.
       :feedback_d: This would be the value of counter after the loop if counter started at 0.

       What will the following code print?
       
       ::
       
          counter = 1
          sum = 0
          while counter <= 6:
              sum = sum + counter
              counter = counter + 2
          print (sum)
             

   