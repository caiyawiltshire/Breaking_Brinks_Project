mBlock_y = 550
rect_width = 120
rect_height = 20
block1_x = 0
block1_y = 0
block2_x = 120
block2_y = 0
block3_x = 240
block3_y = 0
block4_x = 360
block4_y = 0
block5_x = 480
block5_y = 0
ball_x = 100
ball_y = 100
y_speed = 5
x_speed = 5

ball_red = 0
ball_green = 0
ball_blue = 0

block1 = True
block2 = True
block3 = True
block4 = True
block5 = True

def setup():
    size (600,600)
    background (255,255,255)
    
def draw(): 
    global ball_y
    global ball_x
    global y_speed
    global x_speed
    global mBlock_x
    global mBlock_y
    global rect_width
    global rect_height 
    global block1
    global block1_x
    global block1_y
    global block2
    global block2_x 
    global block2_y
    global block3
    global block3_x
    global block3_y
    global block4
    global block4_x 
    global block4_y
    global block5
    global block5_x 
    global block5_y
    global ball_red
    global ball_green 
    global ball_blue 
    background (255,255,255)

    fill(ball_red,ball_green, ball_blue)
    ellipse (ball_x,ball_y,20,20)
    fill (255, 251, 133) #bottom block
    rect (mouseX,mBlock_y,rect_width,rect_height)
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed
    
    #Ball hits moving block
    if  ball_x <= mouseX + 100 and ball_x >= mouseX and ball_y >= mBlock_y and ball_y <= mBlock_y + rect_height: 
        y_speed = -y_speed
        ball_red = random(0,255)
        ball_green = random(0,255)
        ball_blue = random(0,255)
    
    if  ball_x >= 595:
        x_speed = -x_speed
    if  ball_x <= 5:
        x_speed = -x_speed
        
        #DISAPPEARING BLOCKS
    if  block1 == True:
        fill(255, 145, 211)
        rect (block1_x,block1_y,rect_width,rect_height)
    if  ball_x <= block1_x + 120 and ball_x >= block1_x and ball_y <= rect_height : 
        y_speed = -y_speed
        block1 = False
        
    if  block2 == True:
        fill(255, 145, 211)
        rect (block2_x,block2_y,rect_width,rect_height)
    if  ball_x <= block2_x + 120 and ball_x >= block2_x and ball_y <= rect_height : 
        y_speed = -y_speed
        block2 = False
        
    if  block3 == True:
        fill(255, 145, 211)
        rect (block3_x,block3_y,rect_width,rect_height)
    if  ball_x <= block3_x + 120 and ball_x >= block3_x and ball_y <= rect_height: 
        y_speed = -y_speed
        block3 = False
        
    if  block4 == True:
        fill(255, 145, 211)
        rect (block4_x,block4_y,rect_width,rect_height)
    if  ball_x <= block4_x + 120 and ball_x >= block4_x and ball_y <= rect_height : 
        y_speed = -y_speed
        block4 = False
        
    if  block5 == True:
        fill(255, 145, 211)
        rect (block5_x,block5_y,rect_width,rect_height)
    if  ball_x <= block5_x + 120 and ball_x >= block5_x and ball_y <= rect_height: 
        y_speed = -y_speed
        block5 = False
        
        #YOU WON!!!
    if block1 == False and block2 == False and block3 == False and block4 == False and block5 == False:
        textSize (30)
        fill (0,0,255)
        text ("YOU WON!", 220,300)
        x_speed = 0
        y_speed = 0
        
        #Game Over!
    if ball_y > mBlock_y + 10:
        textSize (30)
        fill (0,0,0)
        text ("GAME OVER", 200,300)
