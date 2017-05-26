.. qnum::
   :prefix: 15-7-
   :start: 1
   
Exam Questions for Chapters 14 and 15
-------------------------------------

The following questions test what you have learned in chapters 14 and 15. Click the "Start" button when you are ready to begin the exam.  Click the "Pause" button to pause the exam (you will not be able to see the questions when the exam is paused).  It will show how much time you have used, but you have unlimited time. Click on the "Finish Exam" button at the end when you are done.  The number correct, number wrong, and number skipped will be displayed at the bottom of the page.  Feedback for each answer will also be shown as well as your answer.

You will not be able to change your answers after you hit the "Finish Exam" button.

.. timed:: ch14a15ex
    
    .. mchoice:: e14a15_1
       :answer_a: y % 1
       :answer_b: y % 2
       :answer_c: y % 3
       :answer_d: y % 4
       :correct: c
       :feedback_a: Since every value is evenly divisible by 1 this will always return 0.
       :feedback_b: This will return two possible values 0 if even and 1 if odd.
       :feedback_c: This will return 0, 1, or 2.  
       :feedback_d: This will return 0, 1, 2, or 3.

       Which of the following expressions gives you 3 possible results for all values of y?
           
    .. mchoice:: e14a15_2
       :answer_a: newPixel = image.Pixel(r, g, b)
       :answer_b: img.setPixel(x, y, newPixel)
       :answer_c: p = img.getPixel(x, y)
       :answer_d: win = ImageWin(img.getWidth(), img.getHeight())
       :correct: b
       :feedback_a: This creates a new pixel with the given red, green, and blue values.
       :feedback_b: This updates the pixel values in the image at x and y with the colors in the pixel.
       :feedback_c: This gets the pixel at the given x and y location.
       :feedback_d: This creates a window that can be used to display the image.

       Which of the following statements actually changes the image?
       
    .. mchoice:: e14a15_3
       :answer_a: The program removes all the red from the image
       :answer_b: The program changes all the red pixels to a single color
       :answer_c: The program changes all the pixels to have some red
       :answer_d: The program changes the image to only have 3 values of red
       :correct: d
       :feedback_a: This would be true if the red was always set to 0.
       :feedback_b: This would be true if the red was always set to the same value.
       :feedback_c: If r is less than 120 the red is removed (set to 0).
       :feedback_d: The red will be sets to 0, 200, or 255.  

       What does the following code do to the image?
       
       ::
       
          from image import *
          
          # CREATE AN IMAGE FROM A FILE
          img = Image("arch.jpg")

          # LOOP THROUGH ALL PIXELS
          for x in range(img.getWidth()):
              for y in range(img.getHeight()):
                  p = img.getPixel(x, y)
                  r = p.getRed()
                  g = p.getGreen()
                  b = p.getBlue()

                  # VALUES FOR THE NEW COLOR
                  if r < 120:
                      r = 0
                  elif r < 240:
                      r = 200
                  else:
                      r = 255

                  # CREATE THE COLOR
                  newPixel = image.Pixel(r,g,b)

                  # CHANGE THE IMAGE
                  img.setPixel(x, y, newPixel)

          win = ImageWin()
          img.draw(win)
              
    .. mchoice:: e14a15_4
       :answer_a: Vertical stripes that alternate between red and black and start with red.
       :answer_b: Vertical stripes that alternate between black and red and start with black.
       :answer_c: Horizontal stripes that alternate between red and black and start with red.
       :answer_d: Horizontal stripes that alternate between black and red and start with black.
       :correct: a
       :feedback_a: Sue turns left 90 so the stipes are vertical.  The first element in range(5) is 0 so the stripes start with red.  
       :feedback_b: This would be true if the color was set to black when index is even and red when index is odd.
       :feedback_c: This would be true if sue didn't turn left 90 degrees at the start.
       :feedback_d: This would be true if sue didn't turn left 90 degrees at the start and if the color was set to black when the index is even and red when it is odd.

       What does the following code draw?
       
       ::
       
          from turtle import *     
          space = Screen()        
          height = space.window_height()
          maxY = height / 2         
          sue = Turtle()              
          sue.pensize(10) 
          sue.left(90)       

          for index in range(5):      
          sue.penup()          
          if index % 2 == 0:     
              sue.color('red')        
          else:                     
              sue.color('black')      
          sue.goto(index * 10, -1 * maxY)
          sue.pendown()             
          sue.forward(height)
                   
    .. mchoice:: e14a15_5
       :answer_a: A random value between 10 and 20 
       :answer_b: A random value between 11 and 19 
       :answer_c: A random value between 11 and 20 
       :answer_d: A random value between 10 and 19  
       :correct: d
       :feedback_a: This would be true if it was random.randrange(10,21)
       :feedback_b: This would be true if it was random.randrange(11,20)
       :feedback_c: This would be true if it was random.randrange(11,21)
       :feedback_d: The randrange function returns a random value between the first parameter value and one less than the second parameter value.

       What does random.randrange(10,20) return?


   