.. qnum::
   :prefix: 17-9-
   :start: 1
   
Exam Questions for Chapters 16 and 17
-------------------------------------

The following questions test what you have learned in chapters 16 and 17. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch16a17ex
    
    .. mchoice:: e16a17_1
       :answer_a: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1204, 2048]
       :answer_b: [1, 4, 16, 64, 256, 1024]
       :answer_c: [2, 8, 32, 128, 512, 2048]
       :answer_d: [1, 8, 64, 512]
       :answer_e: out of range error
       :correct: d
       :feedback_a: This would be true if it was range(len(numbers))
       :feedback_b: This would be true if it was range(0,len(numbers),2):
       :feedback_c: This would be true it it was range(1,len(numbers),2):
       :feedback_d: This code adds the values at indicies that are evenly divisible by 3 to the new answer array and prints the contents of the array.
       :feedback_e: This would be true if range included the second parameter, but it does not.  This will stop at one before the length of the array which is the last valid index.

       What does the following code print?
       
       ::
       
          numbers = [1,2,4,8,16,32,64,128,256,512,1024,2048]
          answer = []
          for index in range(0,len(numbers),3):
              answer = answer + [numbers[index]]
          print (answer)
           
    .. mchoice:: e16a17_2
       :answer_a: Crfyro
       :answer_b: SC rof yarooH
       :answer_c: S o ao
       :answer_d: Hoa o C
       :answer_e: out of range error
       :correct: c
       :feedback_a: This would be true if it was range(len(source)-2,0,-2).
       :feedback_b: This would be true if it was range(len(source)-1,0,-1). 
       :feedback_c: This adds elements from source to answer starting at the last index and moving forward toward the front by 2 each time.  It stops before index reaches 0.   
       :feedback_d: This would be true if it was range(0,len(source),2)
       :feedback_e: This would be true if it was range(len(source),0,-2)

       What does the following code print?
       
       ::

          source = "Hooray for CS"
          answer = ""
          for index in range(len(source)-1,0,-2):
              answer = answer + source[index]
          print (answer)
       
    .. mchoice:: e16a17_3
       :answer_a: Charlie
       :answer_b: Brown
       :answer_c: football
       :answer_d: Charlie Brown
       :correct: d
       :feedback_a: This would be true if it was "Charlie Brown boy football" and we were splitting at the space characters.
       :feedback_b: This would be true if it was "Charlie Brown boy football" and we were splitting at the space characters and it was name = pieces[1]
       :feedback_c: This is the value of sport.  
       :feedback_d: The split function splits the string at the passed character which is a comma so the name is everything before the first comma.

       What is the value of name after executing the following code?
       
       ::
       
          from image import *
          def example (nameInput, ageInput):
              pieces = nameInput.split(",")
              name = pieces[0]
              gender = pieces[1]
              sport = pieces[2]
              age = ageInput

           example("Charlie Brown,boy,football", 8)
           
    .. mchoice:: e16a17_4
       :answer_a: yad ecin a si tI
       :answer_b: It is a nice day
       :answer_c: The empty string
       :answer_d: It will cause an error
       :correct: a
       :feedback_a: The for each loop will loop through each character and add it to the front of the result so this will reverse the string.
       :feedback_b: This would be true if it was resString = resString + char
       :feedback_c: While resString was initialized to the empty string it changes in the for each loop.
       :feedback_d: This is the correct syntax for the for each loop.

       What does the following code print?
       
       ::
       
          myString = "It is a nice day"
          resString = ""
          for char in myString:
             resString = char + resString
          print resString
          
    .. mchoice:: e16a17_5
       :answer_a: 10 and -1
       :answer_b: 5 and 2
       :answer_c: 10 and 4 
       :answer_d: 5 and 1
       :correct: b
       :feedback_a: This would be true if we were using index 2 everywhere instead of index 1.
       :feedback_b: Since arrays indicies start at 0 this will print the 2nd element of a which is 5 and then add one to the second element of b which is 1 and print it.
       :feedback_c: This would be true if we were using index 0 everywhere instead of index 1.
       :feedback_d: This would be true if we hand't added 1 to b[1] before printing it.
       
       What is the output from the code below?
       
       ::
       
          a = [10,5,10,6]
          print (a[1])
          b = [3,1,-2]
          b[1] = b[1] + 1
          print (b[1])
          
    .. mchoice:: e16a17_6
       :answer_a: The printed result will be even and will be printed with a decimal point
       :answer_b: The printed result will be odd and will be printed with a decimal point
       :answer_c: The printed result will be even and will be printed without a decimal point
       :answer_d: The printed result will be odd and will be printed without a decimal point
       :correct: c
       :feedback_a: When you add two odd numbers you get an even number, but it will be an integer and not a decimal.
       :feedback_b: This would be true if things had an odd number of items, but there are an even number.  Also the result will be an integer, not a decimal number.
       :feedback_c: When you add two odd numbers you get an even number that is an integer (no decimal point).
       :feedback_d: This would b true if things had an odd number of items, but it has an even number of items.

       Given the following code segment which of the below statements is the most true?
       
       ::
       
          t = 0                                                 
          things = [1,3,19,31]
          for number in things:
              t = t + number
          print (t)
          
    .. mchoice:: e16a17_7
       :answer_a: ueauue
       :answer_b: ueayuyue
       :answer_c: bbrbbybggybmprs
       :answer_d: Rbbr bb bgg bmprs.
       :correct: a
       :feedback_a: The letter is only added to newString when it is a vowel and the list does not include y as a vowel.
       :feedback_b: This would be true if y was in the list of things you were looking for as a vowel, but it is not.
       :feedback_c: This would be true if it was letter in "bcdfghjklmnpqrstvwxyz"
       :feedback_d: This would be true if it was letter not in "aeiou"

       What is printed when the following code executes?
       
       ::
       
          newString = ""
          phrase = "Rubber baby buggy bumpers."
          for letter in phrase:
              if letter in "aeiou":
                  newString = newString + letter
          print (newString)
             

   