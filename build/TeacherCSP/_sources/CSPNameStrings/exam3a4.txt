.. qnum::
   :prefix: 4-8-
   :start: 1
   
Exam Questions for Chapters 3 and 4
-------------------------------------

The following questions test what you have learned in chapters 3 and 4. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch3a4ex
    
    .. mchoice:: e3a4_1
       :answer_a: namewords
       :answer_b: name + words
       :answer_c: John Smith + likes to play outside.
       :answer_d: John Smith likes to play outside.
       :correct: d
       :feedback_a: This would be true if it was print ("name" + "words"), but name and words are not in quotes so the value of each will be printed.
       :feedback_b: This would be true if it was print ("name + words").
       :feedback_c: The would be true if it was print (name + " +" + words).
       :feedback_d: When you use a variable name in a print statement the value of the variable is printed.  The + sign is used to join strings together.  

       What is printed after the following code is run?
       
       ::

          name = "John Smith"
          words = " likes to play outside." 
          print (name + words)
           
    .. mchoice:: e3a4_2
       :answer_a: Tests to see if the values on each side of the expression are equal
       :answer_b: Assigns the name on the left to the value on the right
       :answer_c: Copies the value from the right to the left
       :answer_d: Creates two new objects, one named cat and one named meow
       :correct: b
       :feedback_a: This would be true if it was cat == "meow"
       :feedback_b: A name on the left and a value on the right creates a variable with that name and that value.
       :feedback_c: This would be true if it was a variable name on the right instead of a string.
       :feedback_d: This creates a variable and sets its value.  It doesn't create an object.

       In the following code, what does the "=" do?
       
       ::
       
          cat = "meow"
           
    .. mchoice:: e3a4_3
       :answer_a: I only
       :answer_b: II only 
       :answer_c: III only
       :answer_d: all of them
       :correct: b
       :feedback_a: There are no quotes around the string so this gives an error.  
       :feedback_b: When you use '+' it appends the strings together so this will print the correct string
       :feedback_c: Answer III will not work since there is no variable called Morrissey.
       :feedback_d: Answer II will work, but not answer I or answer III.  Number I has no quotes around the string. In III there is no variable called Morrissey.

       Which of the following line(s) of code will print out "My name is Morrissey"?
       
       ::
       
          I.   print (My name is Morrissey)
          II.  var1 = "My name is " 
               var2 = "Morrissey" 
               var3 = var1 + var2 
               print (var3)
          III. M = "M" 
               orrissey = "orrissey" 
               print ("My name is " + Morrissey)
           
    .. mchoice:: e3a4_4
       :answer_a: 0
       :answer_b: 2
       :answer_c: 5
       :answer_d: 1
       :correct: d
       :feedback_a: This would be true if it was 4 % 2 since 2 goes in evenly into 4.
       :feedback_b: This would be true if you were trying to divide 5 by a number that was larger than 5.  
       :feedback_c: This would be true if it was 5 % 3.  
       :feedback_d: 2 goes into 5 2 times with a remainder of 1.

       What is printed after the following executes?
   
       ::
       
          result = 5 % 2
          print(result)
           
    .. mchoice:: e3a4_5
       :answer_a: 3
       :answer_b: 10
       :answer_c: 18
       :answer_d: 0 
       :correct: b
       :feedback_a: While var2 starts out set to 3 it changes when it is set to a copy of the value in var1.
       :feedback_b: While var2 starts out set to 3 it changes to a copy of the value in var1 which is 10.
       :feedback_c: This is the value of var1 after the code executes.
       :feedback_d: You would have to set var2 to 0 at some point for this to be true.

       What is the value of var2 after the following code executes?
       
       ::
       
          var2 = 3
          var1 = 10
          var2 = var1
          var3 = var2
          var1 = 18
          
    .. mchoice:: e3a4_6
       :answer_a: THIS IS A TEST
       :answer_b: this is a test
       :answer_c: This is a test
       :answer_d: This is a test, really!
       :correct: a
       :feedback_a: Strings are immutable.  Any change to a string returns a new string.
       :feedback_b: This would be true if the question asked for the value of better.
       :feedback_c: This would be true if the question asked for the value of betterStill 
       :feedback_d: This would be true if the question asked for the value of more.

       What is the value of sentence after the following code executes?
   
       ::
       
          sentence = "THIS IS A TEST"
          better = sentence.lower()
          betterStill = better.capitalize() + "."
          more = sentence + ", really!"


   