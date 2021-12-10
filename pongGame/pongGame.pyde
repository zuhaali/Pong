def setup():
    global bg
    size(474,360)
    bg = loadImage("arcade.jpg")

def playButton():
    fill(255)
    rect(
def homeScreen():
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
    
def draw():
    background(bg)
    homeScreen()
    
    print(mouseX,mouseY)
