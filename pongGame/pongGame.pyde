scene=0

def setup():
    global bg
    size(474,360)
    bg = loadImage("arcade.jpg")

def playButton():
    fill(255)
    rect(110,271, 80, 40, 25)
    fill(0,0,0)
    textSize(25)
    text("Play!", 130, 300)
    
def ratingButton():
    fill(255)
    rect(289,271, 80, 40, 25)
    fill(0,0,0)
    textSize(25)
    text("Rate Us!", 297, 300)
    
def backButton(): 
    fill(255)
    rect(289,48, 80, 40, 25)
    fill(0,0,0)
    textSize(25)
    text("Go Back!", 297, 79)
    
def homeScreen():
    global scene
    scene=0
    background(bg)
    fill(255) 
    f = loadFont("AgencyFB-Reg-48.vlw")
    textFont(f)
    textSize(50)
    text("Welcome To Pong!", 95,87)
    stroke(255)
    noFill()
    rect(109, 108, 254, 155)
    textSize(30)
    text("Instructions", 175, 135)
    textSize(15)
    text("1- Control the paddle while the ball automatically \n moves", 114, 150)
    text("2- Your goal is to hit the ball with the paddle", 114, 185)
    text("3- Each time you miss the ball, you lose a life", 114, 200)
    text("4- Each time you hit the ball, you gain a point", 114, 220)
    text("5- Game ends either when the user loses all lives \n or gains 10 points",114, 240)
    playButton()
    ratingButton()
    if mousePressed and mouseX>110 and mouseX<190 and mouseY>271 and mouseY<311 and scene==0:
        scene=1
    if mousePressed and mouseX>289 and mouseX<369 and mouseY>271 and mouseY<311 and scene==0:
        scene=2
    

def playScreen(): 
    global scene
    scene=1
    background(bg)
    fill(0)
    text("hello", 200, 200)
    
def ratingScreen():
   global scene
   scene=2
   background(bg)
   fill(0)
   text("rate", 200, 200) 
   backButton()
   if mousePressed and mouseX>289 and mouseX<369 and mouseY>48 and mouseY<88 and scene==2:
        scene=0
    
def draw():
    if scene==0:
        homeScreen()
    elif scene==1:
        playScreen()
    elif scene==2:
        ratingScreen()
    print(mouseX,mouseY)
