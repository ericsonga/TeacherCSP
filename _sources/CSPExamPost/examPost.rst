.. qnum::
   :prefix: 24-1-
   :start: 1
   
Post Exam
-------------

The following questions test what you have learned in this ebook. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch18a19ex
    
    .. mchoice:: ePost_1_25
       :answer_a: The turtle in this example draws a pentagram.
       :answer_b: This code will generate an error.
       :answer_c: The turtle draws four lines of length 5, 11, 16, and 21
       :answer_d: The turtle draws a square.
       :correct: d
       :feedback_a: This only loops 4 times, so how can it draw a pentagram?
       :feedback_b: This will not cause an error.
       :feedback_c: This would be true if it was sue.forward(sides)
       :feedback_d: This will loop 4 times and each time draw a line of length 100 so this will be a square.
    
       What is the output from the program below?
       
       ::
       
          from turtle import * 
          space = Screen() 
          sue = Turtle() 
          sue.setheading(90) 
          for sides in [5,11,16,21]: 
              sue.forward(100) 
              sue.right(90)
    
    .. mchoice:: ePost_2_18
       :answer_a: Normal
       :answer_b: Hypertensive Crisis
       :answer_c: High Blood Pressure B
       :answer_d: Prehypertension
       :answer_e: High Blood Pressure A
       :correct: e
       :feedback_a: This would be true if check_systolic returned 0 and check_diastolic returned 0.  
       :feedback_b: This would be true if check_systolic returned 3 or check_diastolic returned 3.  
       :feedback_c: This would be true if check_systolic returned 2 and check_diastolic returned something other than 3. 
       :feedback_d: This would be true if check_systolic returned 1 and check_diastolic returned 1.  
       :feedback_e: The function check_systolic(135) returns 1 and the function check_diastolic(100) returns 2 so this will print "High Blood Pressure A"

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
          else:
              print ("High Blood Pressure B")
              
    .. mchoice:: ePost_3_20
       :answer_a: [-5, 5, 0]  [3, 1, 3, 5]
       :answer_b: [10, 5, 0]  [3, 1, 3, 100]
       :answer_c: [-5, 5, 0]  [3, 1, 3, 100]
       :answer_d: [10, -5, 0]  [3, 1, 3, 100]
       :answer_e: [10, -5, 0]  [3, 1, 3, 5]
       :correct: d
       :feedback_a: This would be true if the first index in an array was 1 not 0. 
       :feedback_b: This would be true if it was a[1] = 5 not a[1] = -5
       :feedback_c: This would be true if it was a[0] = -5.  
       :feedback_d: The value of a at index 1 is changed to -5.  The variable val is set to 0.  Then the value of a is printed.  Then b is set to [3,1,3,0].  Then the value at index 3 in b is set to 100.  Then it prints the value of b. 
       :feedback_e: This would be true if it was var = a[1] before a[1] was changed. 

       What is the output from the program below?  
       
       ::
       
          a = [10,5,0]
          a[1] = -5
          val = a[2]
          print (a)
          b = [3,1,3,val]
          b[3] = 100
          print (b)
           
    
    .. mchoice:: ePost_4_16
       :answer_a: a = 7, b = 5, c = 0
       :answer_b: a = 5, b = 7, c = 7
       :answer_c: a = 5, b = 0, c = 7
       :answer_d: a = 5, b = 7, c = 0
       :answer_e: a = 5, b = 5, c = 7
       :correct: b
       :feedback_a: The variable a is set to 7 initially, but it is changed to the value of b which is 5.
       :feedback_b: While a starts at 7, b starts at 5 and c starts at 0, c is set to a copy of a's value, then a is set to a copy of b's value, and b is set to a copy of c's value.
       :feedback_c: Since b is set to 0 and c starts out a 0 this may seem right, but c is changed to a copy of the value in a before that.
       :feedback_d: Did you miss that c is set to a copy of the value in a?
       :feedback_e: Did you miss that b is set to a copy of the value in c and c is set to a copy of the value in a?  

       What will be the values in a, b, and c after the following lines of code execute?
       
       ::
       
          a = 7;
          b = 5;
          c = 0;
          c = a;
          a = b;
          b = c;
           
    .. mchoice:: ePost_5_21
       :answer_a: It will print "Hello Fred"
       :answer_b: It will print "Good-bye Fred"
       :answer_c: It will print "Hello name"
       :answer_d: It will print hello + " " + name
       :correct: b
       :feedback_a: Even though the variable is called hello it contains "Good-bye".
       :feedback_b: Yes, this is what it will print.
       :feedback_c: It prints the value in name which has been set to "Fred".
       :feedback_d: It will print the value of hello and then a space and the value of name.

       Given the following code segment, which of the below statements is true?
       
       ::
       
          hello = "Good-bye"
          fred = "name"
          name = "Fred"
          message = hello + " " + name
          print (message)
          
    .. mchoice:: ePost_6_22
       :answer_a: The printed result will be odd with a decimal point.
       :answer_b: The printed result will be even with a decimal point.
       :answer_c: The printed result will be odd without a decimal point.
       :answer_d: The printed result will be even without a decimal point.
       :correct: d
       :feedback_a: This would true if there was an odd numer of items in aList and at least one of the numbers had a decimal point.
       :feedback_b: This would true if at least one of the numbers had a decimal point.
       :feedback_c: This would true if there was an odd numer of items in aList.
       :feedback_d: Since you are adding up an even number of odd numbers the answer will be even. Since all numbers are integers (don't have a decimal point) the answer won't have a decimal point either.  

       Given the following code segment, which of the below statements is the most true?
       
       ::
       
          sum = 0                                           
          aList = [1,3,7,19,21,131]
          for number in aList:
              sum = sum + number
          print (sum)

          
    .. mchoice:: ePost_7_17
       :answer_a: Error
       :answer_b: Error and 250.0 on the next line
       :answer_c: 250.0
       :answer_d: 1000 / 4
       :answer_e: Error and 250 on the next line
       :correct: c
       :feedback_a: This would be true if x was initialized to 0.
       :feedback_b: This would be true if the if and else statements weren't there.
       :feedback_c: Since x is initialized to 4 it will print the result of 1000 divided by 4 which is 250.0.  
       :feedback_d: This would be true if it was print ("1000 / x") instead.
       :feedback_e: This would be true if the if and else statements weren't there and if 1000 / 4 gave an integer result.

       What is the output from the program below?
       
       ::

          x = 4
          if x == 0:
              print ("Error")
          else:
              print (1000 / x)
              
    .. mchoice:: ePost_8_24
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
              
    .. mchoice:: ePost_9_19
       :answer_a: 6          [3, 1, -2]         -2
       :answer_b: 6          [3, 1, -2]         -1
       :answer_c: 6          [3, 1, -2]          2
       :answer_d: 10        [3, 1, -2]          1
       :answer_e: 10        [3, 1, -2]          2
       :correct: b
       :feedback_a: This would be correct if we hand't changed the value at index 2 in b.  
       :feedback_b: This will print the value at index 3 in a which is 6.  Then it will print b which has [3, 1, -2].  Then it adds one to the value at index 2 in b which is -2 so -2 + 1 is -1.  Then is prints the value at index 2 in b which is -1. 
       :feedback_c: This would be correct if the original value at index 2 in b was 1, but it was -2.
       :feedback_d: This would be correct if we had added 3 to the value at index 2 in b.  
       :feedback_e: This would be correct if we had added 4 to the value at index 2 in b.

       What is the output from the program below?
       
       ::

          a = [10,5,10,6]
          print (a[3])
          b = [3,1,-2]
          print b
          b[2] = b[2] + 1
          print (b[2])
          
    .. mchoice:: ePost_10_23
       :answer_a: The printed result will be odd with a decimal point.
       :answer_b: The printed result will be even with a decimal point.
       :answer_c: The printed result will be odd without a decimal point.
       :answer_d: The printed result will be even without a decimal point.
       :correct: c
       :feedback_a: This would be true if counter or sum had a decimal point.  
       :feedback_b: This would be true if this loop ran an even number of times and counter or sum had a decimal point.
       :feedback_c: Since counter starts with a value of 1 and increments by 2 each time it will always be odd.  Sum starts off at 0 and adds counter each time.  This will be odd when there it has added an odd number of values and even when it has added an even number of values.  Since this loops till counter is greater than 10 this will loop 5 times so the result is odd. 
       :feedback_d: This would be true if the loop ran an even number of times.

       Given the following code segment, which of the below statements is the most true?
       
       ::
       
          counter = 1
          sum = 0
          while counter <= 10:
              sum = sum + counter
              counter = counter + 2
          print (sum)
          
    .. mchoice:: ePost_11_26
       :answer_a: 182
       :answer_b: 181
       :answer_c: 153
       :answer_d: 29
       :correct: c
       :feedback_a: Check your addition.
       :feedback_b: This would be true if it was for number in range(1,len(numList))
       :feedback_c: This will add 1 + 7 + 131 which is 153
       :feedback_d: This would be true if it was for number in range(0,len(thingsToAdd),2)

       Given the following code segment, what will be printed?
       
       ::
       
          sum = 0                                                  
          numList = [1,3,7,19,21,131]
          for number in range(1,len(numList),2):
              sum = sum + numList[number]
          print(sum)
             

   
