.. qnum::
   :prefix: 24-1-
   :start: 1
   
Set #1
-------------------------------------

The following questions make up Set #1 of the Practice Exam Questions. The questions resemble, both in format and substance, what you might see on the AP CS Principles exam. You should finish these questions within 17 minutes to satisfy the time constraints of the AP exam. You may refer to the official AP CS Reference Sheet during the exam, provided by the College Board, which can be found |link|.

.. |link| raw:: html

   <a href="https://secure-media.collegeboard.org/digitalServices/pdf/ap/ap-computer-science-principles-course-and-exam-description.pdf#page=121" target="_blank">here</a>

Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch24ex
    
    .. mchoice:: e24_1_1
       :answer_a: I. and III. only
       :answer_b: I. and II. only
       :answer_c: II. and III. only
       :answer_d: I., II. and III.
       :correct: a
       :feedback_a: Correct
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Incorrect

       Which of the following statements are true regarding compressing files?

          | I. If lossless compression is applied, every single bit of data that was originally in the file remains after the file is uncompressed.
          | II. No matter what compression technique is used, once a data file is compressed, it cannot be restored to its original state.
          | III. The amount of data reduction possible using lossy compression is often much higher than through lossless techniques.
           
    .. mchoice:: e24_1_2
       :answer_a: Abstraction requires users to understand the low-level details of a system.
       :answer_b: Abstraction reduces information and detail to facilitate focus on relevant concepts.
       :answer_c: Abstraction increases the complexity of the software system.
       :answer_d: Abstraction compresses a program file to reduce file size.
       :correct: b
       :feedback_a: Incorrect
       :feedback_b: Correct
       :feedback_c: Incorrect
       :feedback_d: Incorrect
   
       Which of the following statements about abstraction is true?

    .. mchoice:: e24_1_3
       :answer_a: Yes, the code correctly switches the values of 'a' and 'b'.
       :answer_b: No, but it will work correctly if statements 1. and 3. are switched.
       :answer_c: No, but it will work correctly if statements 2. and 3. are switched.
       :answer_d: No, but it will work correctly if statements 1. and 2. are switched.
       :correct: c
       :feedback_a: Incorrect
       :feedback_b: Incorrect
       :feedback_c: Correct
       :feedback_d: Incorrect
       
       A programmer is writing code to switch the values of two integer variables, namely ``a`` and ``b``, using a temporary integer variable, ``temp``. This is the pseudo-code that the programmer has come up with:
       ::

        temp ← a  # statement 1.
        b ← temp  # statement 2.
        a ← b     # statement 3.

       Will the pseudo-code correctly perform the required task (assume that ``a`` and ``b`` are never numerically equal)?

    .. mchoice:: e24_1_4
       :answer_a: X = 155, Y = 1555
       :answer_b: X = 20, Y = 20
       :answer_c: X = 15, Y = 5
       :answer_d: X = 20, Y = 25
       :correct: d
       :feedback_a: Incorrect
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Correct 

       What is the final value of the integers ``X`` and ``Y`` after the following statements are executed?
       ::

         X ← 15
         Y ← 5
         X ← X + Y
         Y ← X + Y

    .. mchoice:: e24_1_5
       .. mchoice:: e24_1_5
       :answer_a: The baby duck picture appears as intended.
       :answer_b: The baby duck picture appears as 4 out of order images.
       :answer_c: The baby duck picture is distorted.
       :answer_d: The baby duck picture won’t load on the user’s smartphone.
       :correct: a
       :feedback_a: Correct
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Incorrect

       A user’s smartphone makes a request to a server for 4 packets that represent the image of a baby duck. The server sends the 4 packets but they arrive at the user’s smartphone out of order. How does the smartphone interpret the packets that form the image?

       .. figure:: Figures/duckpacket.jpg
       

    .. mchoice:: e24_1_6
       :answer_a: Cloud Computing
       :answer_b: Global Positioning System
       :answer_c: Short Message Service
       :answer_d: Data Mining
       :correct: a
       :feedback_a: Correct
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Incorrect 

       Which of the following technologies allows its users to store, manage and access files remotely over the Internet?

    .. mchoice:: e24_1_7
       :answer_a: a ≥ c and c ≥ b
       :answer_b: a ≥ c and b ≥ c
       :answer_c: c ≥ a and c ≥ b
       :answer_d: c ≥ b and c ≥ a
       :correct: a
       :feedback_a: Correct
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Incorrect 

       Consider the following incomplete pseudo-code to print the largest of three integer variables, namely ``a``, ``b`` and ``c``:
       ::

         IF (a ≥ b)
         {
            IF (*incomplete_1*)
            {
                DISPLAY(a)
            }
            ELSE
            {
                DISPLAY(c)
            }
         }
         ELSE
         {
            IF (*incomplete_2*)
            {
                DISPLAY(c)
            }
            ELSE
            {
                DISPLAY(b)
            }
         }
       
       Which of the following options can be substituted for *incomplete_1* and *incomplete_2*, respectively, for the code to work as intended?

    .. mchoice:: e24_1_8
       :answer_a: 4
       :answer_b: 8
       :answer_c: 16
       :answer_d: 32
       :correct: c
       :feedback_a: Incorrect
       :feedback_b: Incorrect
       :feedback_c: Correct
       :feedback_d: Incorrect 
        
       Trace the value of an integer variable ``n`` in the following code.
       ::

         i ← 1
         n ← 2
         REPEAT until i = 4 
         {
            n ← n * 2
            i ← i + 1
         }

       What is the value of ``n`` after the above code executes?

    .. mchoice:: e24_1_9
       :answer_a: Sorting students by grade
       :answer_b: Deleting a student’s record
       :answer_c: Searching for a student’s name
       :answer_d: Adding bonus points to grades of all students
       :correct: d
       :feedback_a: Incorrect
       :feedback_b: Incorrect
       :feedback_c: Incorrect
       :feedback_d: Correct 

       A professor uses an automated computer system to manage the student records of his classes. The time the system takes to perform various tasks for different class sizes is shown in the table below:

       +---------------------+---------------------------+----------------------------+----------------------------+
       | Task ↓       Size → | Small class (25 students) | Medium class (50 students) | Large class (100 students) |
       +=====================+===========================+============================+============================+
       | Sorting students by | 10 seconds                | 40 seconds                 | 160 seconds                |
       | grade               |                           |                            |                            |
       +---------------------+---------------------------+----------------------------+----------------------------+
       | Deleting a student’s| 2 seconds                 | 4 seconds                  | 8 seconds                  |
       | record              |                           |                            |                            |
       +---------------------+---------------------------+----------------------------+----------------------------+
       | Searching for a     | 1 second                  | 2 seconds                  | 4 seconds                  |
       | student’s name      |                           |                            |                            |
       +---------------------+---------------------------+----------------------------+----------------------------+
       | Adding bonus points | 3 seconds                 | 6 seconds                  | 9 seconds                  |
       | to grades of all    |                           |                            |                            |
       | students            |                           |                            |                            |
       +---------------------+---------------------------+----------------------------+----------------------------+

       Based on the information in the table, which of the following tasks is likely to take the least amount of time if the computer system is used for a class of 400 students? 

    .. mchoice:: e24_1_10
       :answer_a: Because hexadecimal is a lower level of abstraction than binary.
       :answer_b: Because hexadecimal can be represented with fewer total digits than binary.
       :answer_c: Because numbers greater than 1 must be used for certain forms of digital data.
       :answer_d: Because hexadecimal is easier to convert to decimal form.
       :correct: b
       :feedback_a: Incorrect
       :feedback_b: Correct
       :feedback_c: Incorrect
       :feedback_d: Incorrect 

       Why is digital data often represented in hexadecimal as opposed to binary?
