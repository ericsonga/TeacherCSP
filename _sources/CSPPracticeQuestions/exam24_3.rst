.. qnum::
   :prefix: 24-3-
   :start: 1
   
Set #3
-------------------------------------

The following questions make up Set #3 of the Practice Exam Questions. The questions resemble, both in format and substance, what you might see on the AP CS Principles exam. You should finish these questions within 17 minutes to satisfy the time constraints of the AP exam. You may refer to the official AP CS Reference Sheet during the exam, provided by the College Board, which can be found |link|.

.. |link| raw:: html

   <a href="https://secure-media.collegeboard.org/digitalServices/pdf/ap/ap-computer-science-principles-course-and-exam-description.pdf#page=121" target="_blank">here</a>

Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time.  Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch24_3ex
    
    .. mchoice:: e24_3_1
       :answer_a: sample.com
       :answer_b: sample.org.biz
       :answer_c: enter.sample.org
       :answer_d: sample.org/help
       :correct: c
       :feedback_a: Incorrect. This is a completely different website unrelated to sample.org.
       :feedback_b: Incorrect. sample.org is a subdomain of biz in this answer choice.
       :feedback_c: Correct. The subdomain is always on the left of the domain name.
       :feedback_d: Incorrect. Subdomains are always on the left side of the domain and use a "." instead of a "/".

       Which of the following would be a subdomain of the domain sample.org according to the guidelines of the Domain Name System (DNS)?
    
    .. mchoice:: e24_3_2
       :answer_a: Algorithm A always calculates the correct average, but Algorithm B may not.
       :answer_b: Algorithm B always calculates the correct average, but Algorithm A may not.
       :answer_c: Both Algorithm A and Algorithm B always calculate the correct average.
       :answer_d: Neither Algorithm A nor Algorithm B always calculate the correct average.
       :correct: a
       :feedback_a: Correct. Algorithm A correctly calculates the average, while Algorithm B does not.
       :feedback_b: Incorrect. Algorithm B would calculate the average if the groups of four took an average of their scores.
       :feedback_c: Incorrect. Algorithm B would calculate the average if the groups of four took an average of their scores.
       :feedback_d: Incorrect. Algorithm A correctly calculates the average.

       There are 16 students standing in a classroom. Each student is given back his or her graded homework. Students decide to find out the class’s average score on the homework. Two different algorithms are given for finding the average score.
       
       ::
       
       
        Algorithm A
        Step 1: All students stand.
        Step 2: A randomly selected student writes his or her score on the whiteboard
        and is seated.
        Step 3: A randomly selected standing student adds his or her score to the value 
        on the whiteboard, records the new value on the whiteboard, and is seated. 
        The previous value on the whiteboard is erased.
        Step 4: Repeat step 3 until no students remain standing.
        Step 5: The value on the whiteboard is divided by 16.

        Algorithm B
        Step 1: All students stand.
        Step 2: Students form groups of 4.
        Step 3: In each group, the students with the lowest and highest scores return 
        to their seats.
        Step 4: Repeat steps 1 and 2 until only two students remain standing.
        Step 5: Add the remaining two students’ numbers and divide the sum by two. 

       Which of the following statements is true?

    .. mchoice:: e24_3_3
       :answer_a: How does the temperature fluctuate from day to night?
       :answer_b: Is there a correlation between air temperature and precipitation?
       :answer_c: What is the average annual precipitation?
       :answer_d: What is the average daily temperature? 
       :correct: c
       :feedback_a: Incorrect. The meteorologists have temperature data from days and nights so they can compare the differences between them.
       :feedback_b: Incorrect. The meteorologists have temperature and precipitation data, so they can compare them and determine if there is a correlation.
       :feedback_c: Correct. The meteorologists only have data from one year, so they cannot calculate the average annual precipitation.
       :feedback_d: Incorrect. The meteorologists have temperature data for an entire year, so they can find the average of daily temperatures across that time range.

       Meteorologists record atmospheric data to predict future weather conditions. Suppose that a meteorological lab in Atlanta takes hourly measurements of air temperature and precipitation in the city for a total period of 12 months. Note that the lab also records the exact time and date for each measurement. 

       Which of the following questions about the city’s weather could NOT be accurately answered using only the data collected by the lab?
       
    .. mchoice:: e24_3_4
       :answer_a: How does wind speed fluctuate from day to night?
       :answer_b: During which hour of the day does it rain the most on average?
       :answer_c: Is there a correlation between air pressure and precipitation?
       :answer_d: Is there a correlation between Atlanta’s daily average temperature and Chicago’s daily average temperature?
       :correct: b
       :feedback_a: Incorrect. The meteorologists do not have wind speed data.
       :feedback_b: Correct. The meteorologists have precipitation data for a year, so they can calculate this.
       :feedback_c: Incorrect. The meteorologists do not have air pressure data.
       :feedback_d: Incorrect. The meteorologists do not have data for Chicago's temperature.

       Meteorologists record atmospheric data to predict future weather conditions. Suppose that a meteorological lab in Atlanta takes hourly measurements of air temperature and precipitation in the city for a total period of 12 months. Note that the lab also records the exact time and date for each measurement.       
       
       Which of the following questions about Atlanta’s weather can be accurately answered using only the data collected by the lab?
       
    .. mchoice:: e24_3_5
       :answer_a: 8
       :answer_b: 7
       :answer_c: 5
       :answer_d: 3
       :correct: d
       :feedback_a: Incorrect. This would be true for a hexadecimal value of 38.
       :feedback_b: Incorrect. This would be true for a hexadecimal value of 37.
       :feedback_c: Incorrect. This would be true for a hexadecimal value of 35.
       :feedback_d: Correct. The ASCII value would be '51'.

       ASCII is a character-encoding scheme that uses numeric values in decimal (base 10)  to represent alphanumeric and special characters. For example, the uppercase letter ‘A’ is represented by the decimal value ‘65’. Digits from ‘0’ - ‘9’ also have a corresponding ASCII value. The digit ‘0’ has an ASCII value of ‘48’, ‘1’ has an ASCII value of ‘49’ and so on.We can represent the ASCII value of digits as hexadecimal  numbers (base 16) as well. Which digit has a hexadecimal value of ‘33’? 
       
    .. mchoice:: e24_3_6
       :answer_a: The long data type can store 2^48 times as many distinct values as the short data type
       :answer_b: The long data type can store 2^64 times as many distinct values as the short data type
       :answer_c: The long data type can store 2^16 times as many distinct values as the short data type
       :answer_d: The short data type can store 4 times as many distinct values as the long data type
       :correct: a
       :feedback_a: Correct. It can store 2^(64 - 16) as many distinct values.
       :feedback_b: Incorrect. That is how many total values the long data stores.
       :feedback_c: Incorrect. That is how many total values the short data stores.
       :feedback_d: Incorrect. While long data is 4 times as long as the short, the question asks for the difference in distinct values the data type can hold.

       Imagine there is a programming language which uses two different data types to store integers - a 16-bit short data type and a 64-bit long data type. Then which of the following statements is true about the two data types?
       
    .. mchoice:: e24_3_7
       :answer_a: I,III
       :answer_b: II, III
       :answer_c: I, IV
       :answer_d: I, II, III, IV
       :correct: c
       :feedback_a: Incorrect. Option III will not give them the maximum pay, and won't give them any bonus.
       :feedback_b: Incorrect. Both of these options are incorrect.
       :feedback_c: Correct. Both of these options correctly calculate each employee's pay.
       :feedback_d: Incorrect. Options II and III both incorrectly calculate the employee's pay.

        At a company, n number of employees are given the same bonus of $5,000 on top of their salary.  However, each person can only get a maximum of $100,000 a year, so if adding the bonus causes the employee’s total pay to surpass $100,000, the employee will receive the maximum pay of $100,000.  Each employee’s original annual salary is stored in a list entitled employeeList, indexed from 1 to n.
        
        ::
        
        
          PROCEDURE addBonuses(employeeList) 
          {
            i ← n
            REPEAT n TIMES
            {
               <MISSING CODE>
               i ← i + 1
            }
            RETURN employeeList
          }
        
       Which of the following code segments can be placed in the <MISSING CODE> area to make the program work as expected?

       (The min(a,b) and max(a,b) functions return the lesser and greater values of the inputs, respectively.)
       
       Option I. 
            
            ::
               
               employeeList[i] ← min (employeeList [i] + 5000, 100000)
       
       Option II.
            
            ::
               
               employeeList [i] ← max (employeeList [i] + 5000, 100000)
       
       Option III.
            
            ::
            
               employeeList[i] ← employeeList [i] + 5000 
               IF (employeeList [i] > 100000) 
               { 
                  employeeList [i] ← employeeList [i] - 5000 
               }
       
       Option IV.
            
            ::
            
               employeeList[i] ← employeeList [i] + 5000 
               IF (employeeList [i] > 100000) 
               { 
                  employeeList [i] ← 100000 
               } 
              
               
       
    .. mchoice:: e24_3_8
       :answer_a: I, IV
       :answer_b: I, III, IV
       :answer_c: II, III
       :answer_d: I, II, III, IV
       :correct: d
       :feedback_a: Incorrect. SMS and Email have also increased the availability of distant communication and collaboration.
       :feedback_b: Incorrect. SMS has also increased the availability of distant communication and collaboration.
       :feedback_c: Incorrect. Social Media websites and Video Conferencing have also increased the availability of distant communication and collaboration.
       :feedback_d: Correct. All of these utilities have increased the availability of distant communication and collaboration.

       Which of the following have increased the availability of communication and collaboration between people at a distance?
       
        | I. Social Media
        | II. SMS
        | III. Email
        | IV. Video Conferencing
       
    .. mchoice:: e24_3_9
       :answer_a: I, II
       :answer_b: I, III
       :answer_c: I, II, III
       :answer_d: None of the options
       :correct: b
       :feedback_a: Incorrect. Option II is incorrect. Some problems require algorithms that do not run in reasonable time.
       :feedback_b: Correct. Both of these statements regarding algorithms are true.
       :feedback_c: Incorrect. Option II is incorrect. Some problems require algorithms that do not run in reasonable time.
       :feedback_d: Incorrect. An algorithm that runs in reasonable time refers to a polynomial function of the input size.

       Which of the following statements are true about algorithms?
       
         | I. If an algorithm runs in reasonable time, the number of steps the algorithm takes is a polynomial function (constant, linear, squared, etc.) of the size of the input.
         | II. All problems can be solved using an algorithm that runs in reasonable time.
         | III. If a problem cannot be solved in reasonable time, a heuristic approach is helpful to solve the problem.
 
       
    .. mchoice:: e24_3_10
       :answer_a: (3,3)
       :answer_b: (1,3)
       :answer_c: (5,3)
       :answer_d: (1,1)
       :correct: b
       :feedback_a: Incorrect. Notice that n is changed to n/2 after the inner loop.
       :feedback_b: Correct. By following the code, you can see that the triangle ends up in (1,3).
       :feedback_c: Incorrect. The triangle only turns right throughout the enter code segment.
       :feedback_d: Incorrect. Did you miss the TURN_RIGHT call after the inner loop?

       The red triangle in the grid below is currently located at the position (5, 1) (5th row down and 1st column across), and is facing upward.
       
       .. image:: Figures/triangle.png
          :height: 250px
          :width: 250px
       
       If the following code is run, which position will the red triangle end up on?
       ::
      
         n ← 4
         REPEAT UNTIL n = 1
         {
            REPEAT n TIMES
        	   {
        	      MOVE_FORWARD
        	   }
        	   TURN_RIGHT
        	   n ← n/2
         }
       
