# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: Yuval Wainstein
Date: 8/8/18
"""
import turtle
import random #We'll need this later in the lab
color_snk = input('Choose a color: ')
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape('square')
snake.color(color_snk)
turtle.bgpic('wall.gif')
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for num_pieces in range (START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_1 = snake.stamp()
    stamp_list.append(stamp_1)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")
   
    


#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!



def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to left
    print("You pressed the left key!")
    
    


def right():
    global direction #snake direction is global (same everywhere)
    direction = RIGHT #Change direction to right
    print("You pressed the right key!")
   

def down():
    global direction #snake direction is global (same everywhere)
    direction = DOWN #Change direction to down 
    print("You pressed the down key!")
    



    


turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(food.pos())
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    #Grab pos of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print('You hit the right edge! GAME OVER!')
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print('You hit the left edge! GAME OVER!')
        quit ()
    elif new_y_pos >= UP_EDGE:
        print('You hit the uppper edge! GAME OVER!')
        quit ()
    elif new_y_pos <= DOWN_EDGE:
        print('You hit the lower edge! GAME OVER!')
        quit()
    global food_stamps, food_pos
    if len(food_stamps)<=6:
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
    if snake.pos() in pos_list:
        print('You ate yourself! GAME OVER')
        quit()
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    stamp_2 = snake.stamp()
    stamp_list.append(stamp_2)
    ######## SPECIAL PLACE - Remember it for Part 5
    
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food 
                                                   #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print('You have eaten the food!')
    else: 
        stamp_1 = stamp_list.pop(0)
        snake.clearstamp(stamp_1)
        pos_list.pop(0)
    
    #HINT: This if statement may be useful for Part 8
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    
        

   
    
        
    

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    
    
    
    ####WRITE YOUR CODE HERE!!




move_snake() #Update the snake drawing <- remember me later




