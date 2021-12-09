def setup():
    global bg
    size(474,360)
    bg = loadImage("arcade.jpg")

def homeScreen():
    f = loadFont("AgencyFB-Reg-48.vlw")
    textFont(f)
    textSize(50)
    text("Welcome To Pong!", 95,87)
    stroke(255)
    noFill()
    rect(109, 108, 254, 126)
    
def draw():
    background(bg)
    homeScreen()
    
    print(mouseX,mouseY)
