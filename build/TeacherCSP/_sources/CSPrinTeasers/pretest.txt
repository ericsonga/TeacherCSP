.. qnum::
   :prefix: 1-2-
   :start: 1
   
Pretest
-------------------------------------

The following is a pretest to test what you already know about programming in Python. Don't worry if you don't understand the questions yet.  We don't expect you to.  Just answer the questions to the best of your ability or pick "I don't know". 

Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.  Answers are saved on the computer you are working on by your username so we recommend logging in before starting.

.. timed:: preTest
    
    .. mchoice:: pre_1
       :answer_a: x = 7, y = 5, z = 0
       :answer_b: x = 5, y = 7, z = 7
       :answer_c: x = 5, y = 7, z = 0
       :answer_d: x = 5, y = 5, z = 7
       :answer_e: I don't know
       :correct: b
       :feedback_a: Those are the original values, but they change.
       :feedback_b: x is set to 7 but changed to the value of y which is 5.  y is set to 5 originally, but is changed to the value of z but after z has been set to the value of x which is 7.  z was set to 0 originally but changes to the the value of x which is 7.
       :feedback_c: This would be true if setting y to z reset z to 0, but that is not what happens.
       :feedback_d: y was set to 5 originally, but the value was changed.
       :feedback_e: That is okay.  We do not expect you to know this.

       What will be the values in x, y, and z after the following lines of code execute?

       ::
       
          x = 7;
          y = 5;
          z = 0;
          z = x;
          x = y;
          y = z;
         
           
    .. mchoice:: pre_2
       :answer_a: Mere morals cannot divide by zero.
       :answer_b: 1000 / 4
       :answer_c: 250.0
       :answer_d: Mere mortals cannot divide by zero. 250.
       :answer_e: I don’t know
       :correct: c
       :feedback_a: The sentence prints only if denominator is equal to 0, but it is not.  
       :feedback_b: It will print the result of the division.
       :feedback_c: It only prints the result of dividing 1000 by 4 which is 250.0.  
       :feedback_d: The sentence prints only if denominator is equal to 0, but it is not. 
       :feedback_e: That is okay.  We do not expect you to know this.

       What is the output from the program below?
       
       ::

          denominator = 4
          if denominator == 0:
              print ("Mere mortals cannot divide by zero.")
          else:
              print (1000 / denominator)
           
    .. mchoice:: pre_3
       :answer_a: Normal
       :answer_b: Hypertensive Crisis
       :answer_c: High Blood Pressure A
       :answer_d: Prehypertension
       :answer_e: I don’t know
       :correct: c
       :feedback_a: This will only print when both check_systolic and check_diastolic return 0 which is when check_systolic is passed a number less than 120 and check_diastolic is passed a number less than 80.
       :feedback_b: This will only print when either check_systolic or check_diastolic return 3 which is when check_systolic is passed a number greater or equal to 180 and check_diastolic is passed a number greater than or equal to 110.
       :feedback_c: This will print when check_systolic was 1 and check_diastolic was greater than 1 (but not 3).  
       :feedback_d: This will print when check_systolic was 1 and check_diastolic was less than or equal to 1.  
       :feedback_e: That is okay.  We do not expect you to know this.

       What is the output from the program below?
       
       ::

          def check_systolic(num1):
              if num1 < 120:
                  return 0
              elif num1 < 140:
                  return 1
              elif num1 < 180:
                  return 2
              else:
                  return 3

          def check_diastolic(num2):
              if num2 < 80:
                  return 0
              elif num2 < 90:
                  return 1
              elif num2 < 110:
                  return 2
              else:
                  return 3

          syst = 135
          dias = 100
          if check_systolic(syst) == 0 and check_diastolic(dias) == 0:
              print ("Normal")
          elif check_systolic(syst) == 3 or check_diastolic(dias) == 3:
              print ("Hypertensive Crisis")
          elif check_systolic(syst) == 1:
              if check_diastolic(dias) > 1:
                  print ("High Blood Pressure A")
              else:   
                  print ("Prehypertension")

           
    .. mchoice:: pre_4
       :answer_a: 10        [3, 1, -2]          -1
       :answer_b: 6          [3, 1, -2]          2
       :answer_c: 6          [3, 1, -2]         -1
       :answer_d: 6          [3, 1, -2]         -2
       :answer_e: I don’t know
       :correct: c
       :feedback_a: This would print 10 first if lists started at index 0, but they start at index 1.
       :feedback_b: Remember that lists start at index 0.
       :feedback_c: Lists start at index 0.  You can modify the value at an index.  
       :feedback_d: Notice that second[2] is incremented.
       :feedback_e: That is okay.  We do not expect you to know this.

       What is the output from the program below?
       
       ::
 
          first = [10,5,10,6]
          print (first[3])
          second = [3,1,-2]
          print (second)
          second[2] = second[2] + 1
          print (second[2])
           
    .. mchoice:: pre_5
       :answer_a: [-5, 5, 0]  [3, 1, 3, 5]
       :answer_b: [10, 5, 0]  [3, 1, 3, 100]
       :answer_c: [10, -5, 0]  [3, 1, 3, 5]
       :answer_d: [10, -5, 0]  [3, 1, 3, 100]
       :answer_e: I don’t know
       :correct: d
       :feedback_a: The first value in first doesn't change.  first[1] refers to the second item in the list.
       :feedback_b: The second item (the one at index 1) is the first list is changed to -5.  
       :feedback_c: The last item in the second list is changed to 100.  
       :feedback_d: The second item (the one at index 1) is the first list is changed to -5.  The last item in the second list is changed to 100. 
       :feedback_e: That is okay.  We do not expect you to know this.

       What is the output from the program below?  
       
       ::

          first = [10,5,0]
          first[1] = -5
          value = first[2]
          print (first)
          second = [3,1,3,value]
          second[3] = 100
          print (second)
          
    .. mchoice:: pre_6
       :answer_a: It will print "Hello Roger" 
       :answer_b: It will print "Hello name"
       :answer_c: It will print "Good-bye Roger"
       :answer_d: It will print hello + " " + name
       :answer_e: I don’t know
       :correct: c
       :feedback_a: It prints the value of hello which is "Good-bye".
       :feedback_b: It prints the value of hello which is "Good-bye".
       :feedback_c: It prints the value of hello which is "Good-bye" and the value of name which is "Roger" with a space between.
       :feedback_d: It prints the value of the variables.  
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, which of the following statements is true?
       
       ::

          hello = "Good-bye"
          roger = "name"
          name = "Roger"
          greeting = hello+" "+name
          print (greeting)
          
    .. mchoice:: pre_7
       :answer_a: The printed result will be even and will have a decimal point.
       :answer_b: The printed result will be odd and will have a decimal point.
       :answer_c: The printed result will be even and will not have a decimal point.
       :answer_d: The printed result will be odd and will not have a decimal point.
       :answer_e: I don’t know
       :correct: c
       :feedback_a: Adding up an even number of odd numbers results in an even sum, but there won't be a decimal point.
       :feedback_b: Adding up an even number of odd numbers results in an even sum.
       :feedback_c: Adding up an even number of odd numbers results in an even sum and there won't be a decimal point.
       :feedback_d: Adding up an even number of odd numbers results in an even sum.
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, which of the following is true?
       
       ::

          sum = 0 # Start out with nothing
          thingsToAdd = [1,3,7,19,21,131]
          for number in thingsToAdd:
              sum = sum + number
          print (sum)
          
    .. mchoice:: pre_8
       :answer_a: The printed result will be even and will have a decimal point.
       :answer_b: The printed result will be odd and will have a decimal point.
       :answer_c: The printed result will be even and will not have a decimal point.
       :answer_d: The printed result will be odd and will not have a decimal point.
       :answer_e: I don’t know
       :correct: d
       :feedback_a: Adding up an odd number of odd numbers results in an odd sum.  
       :feedback_b: Adding up an odd number of odd numbers results in an odd sum. But, another answer is also true.
       :feedback_c: This would be true if any of the numbers being added had a decimal point.
       :feedback_d: Since none of the numbers have a decimal point in them the answer will not have a decimal point. But, another answer is also true.
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, which of the following is true?
       
       ::
       
          counter = 1
          sum = 0
          while counter <= 10:
              sum = sum + counter
              counter = counter + 2
          print (sum)


          
    .. mchoice:: pre_9
       :answer_a: The printed result will only contain vowels.
       :answer_b: The printed result will only contain consonants.
       :answer_c: It will print the empty string.
       :answer_d: The printed result will include "y"
       :answer_e: I don't know
       :correct: a
       :feedback_a: This only adds the letter if it is a vowel.
       :feedback_b: This only adds the letter if it is a vowel.
       :feedback_c: No, it will add vowels to newString and print that.
       :feedback_d: The letter must be in "aeiou" to be added to newString.
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, which of the statements below is true?
       
       ::

          newString = ""
          phrase = "Rubber baby buggy bumpers."
          for letter in phrase:
              if letter in "aeiou":
                  newString = newString + letter
          print (newString)
          
    .. mchoice:: pre_10
       :answer_a: The turtle in this example draws a pentagram.
       :answer_b: The turtle draws four lines of length 5, 11, 16, and 21
       :answer_c: The turtle draws a square.
       :answer_d: This code will generate an error.
       :answer_e: I don’t know
       :correct: c
       :feedback_a: It loops 4 times, how can that be a pentagram?
       :feedback_b: It always moves forward by 100.
       :feedback_c: It draws a square with a side length of 100.
       :feedback_d: No error will be generated.
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, which of the statements below is true?
       
       ::

          from turtle import * 
          space = Screen() 
          alisha = Turtle() 
          alisha.setheading(90) 
          for sides in [5,11,16,21]: 
              alisha.forward(100) 
              alisha.right(90)
              
    .. mchoice:: pre_11
       :answer_a: 29
       :answer_b: 182
       :answer_c: 153
       :answer_d: 181
       :answer_e: I don't know
       :correct: c
       :feedback_a: This adds up every other number starting with the one at index 1 (second in list).
       :feedback_b: This adds up every other number starting with the one at index 1 (second in list).
       :feedback_c: This adds up every other number starting with the one at index 1 (second in list).
       :feedback_d: This adds up every other number starting with the one at index 1 (second in list).
       :feedback_e: That is okay.  We do not expect you to know this.

       Given the following code segment, what will be printed?
       
       ::

          sum = 0 # Start out with nothing
          thingsToAdd = [1,3,7,19,21,131]
          for number in range(1,len(thingsToAdd),2):
              sum = sum + thingsToAdd[number]
          print(sum)


       
      

   