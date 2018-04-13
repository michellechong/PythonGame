from gamelib import *
game = Game(800,600,"Endless Road") # game name and screen size
#graphics variables
#Background        
bk = Animation("roadsprite1.jpg", 26, game, 2495/5, 1689/6) #animation
bk.resizeTo(800,610) #make the background fit the game screen
game.setBackground(bk) #set the background


#Car
car = Image("car.png",game)
car.resizeBy(-20)
car.moveTo(400,550) #move the car to (600,600)

#Cow
cow = Animation("cow_front.png", 4, game, 512/4, 128, use_alpha=False) #cow is an animatio
cow.moveTo(300,450) #move the cow
cow.setSpeed(6,180) #set the speed and angle so the cow can move

#Cow1
cow1 = Animation("cow_front1.png", 4, game, 512/4, 128, use_alpha=False)
cow1.moveTo(250, 150)

#Ending 1
congratulation = Image("congratulations.png", game) #part of the ending screen when game is completed
congratulation.moveTo(300,100)

#Exploding
explosion = Animation("explosion.png",48,game,2048/8, 1536/6) #when car collided with an object
explosion.resizeBy(-70)
explosion.visible = False 

#Fuel
fuel = []
for index in range(50):
    fuel.append( Image("fuel.png",game)) #add fuels into the list
for index in range(50):
    x = randint(100,750)
    y = randint(100,4000)
    s = randint(5,10)
    fuel[index].moveTo(x,-y) #random x and y values, the fuels will occur at different location
    fuel[index].setSpeed(s, 180) #Set a random speed for the fuels
    fuel[index].resizeBy(-90) #make the size of fuels smaller

#Fuel1
fuel1 = Image("fuel1.png",game)
fuel1.resizeBy(-90)
fuel1.moveTo(250, 50)

#gameover screen
gameover = Image("gameover.png", game)

#Home
home = Image("destination.png",game) #part of the ending screen where player completed the game
home.resizeBy(-10)
home.moveTo(400,325) 

#Logo 
logo = Image("logo.png",game) #import logo
#logo.resizeBy(10) #enlarged logo
logo.moveTo(400,200) #moved the logo to a place

#pothole
pothole = []
for index in range(50):
    pothole.append( Image("pot_hole.png",game))
for index in range(20):
    x = randint(100,700)
    y = randint(100,4000)
    s = randint(5,10)
    pothole[index].moveTo(x,-y) #random locations
    pothole[index].setSpeed(s, 180) #random speed
    pothole[index].resizeBy(-40) #potholes are smaller

#Pothole 1
pothole1 = Image("pot_hole1.png",game)
pothole1.resizeBy(-60)
pothole1.moveTo(250, 250)

#stop sign
stopsign = []
for index in range(50):
    stopsign.append( Image("stopsign.png",game))
for index in range(20):
    x = randint(100,750)
    y = randint(100,4000)
    s = randint(9,12)
    stopsign[index].moveTo(x,-y) #random locations
    stopsign[index].setSpeed(s, 180) #random speed
    stopsign[index].resizeBy(-40) #stop sign are smaller

#stop sign 1
stopsign1 = Image("stopsign1.png", game)
stopsign1.resizeBy(-60)
stopsign1.moveTo(250, 350)

#Story
story = Image("story.png", game) #Import story

#Sound Files
collectfuel = Sound ("collectfuel.wav",1)
collide = Sound("collide.wav",2)
over = Sound("over1.wav",3)
win = Sound("win.wav",4)
game.setMusic("Triumph.mp3")
game.playMusic()

#title screen
while not game.over:
    game.processInput() # Process the inputs

    #draw graphics
    bk.draw()
    logo.draw()

    #Texts
    game.drawText("Press [Space] to Start",325,550)
    game.drawText("Press and Hold [i] to look at story",275,400)
    game.drawText("Press and Hold [H] for more information",275,450)
    game.drawText("Please Use the Arrow Keys on the Keyboard to Control the Car",200,500)

    #play the game
    if keys.Pressed[K_SPACE]: #start the game
        game.over = True

    #Story
    if keys.Pressed[K_i]: 
        game.clearBackground(black)
        story.draw()
        game.drawText("Release [i] to Return",350,500)

    #How to play   
    if keys.Pressed[K_h]: 
        game.clearBackground(black)
        fuel1.draw()
        game.drawText(" = Fuel(Collect This!!)", 300,50)

        cow1.draw()
        game.drawText(" = Cow(AVOID THIS!!)", 300,150)

        stopsign1.draw()
        game.drawText(" = STOP sign(AVOID THIS!!)", 300,350)

        pothole1.draw()
        game.drawText(" = Pothole(AVOID THIS!!)", 300,250)
        
        game.drawText("Release [H] to Return",300,500)
        
    game.update(30)

game.over = False


#Level 1
fuelcount = 0
while not game.over:
    game.processInput() # Process the inputs
    game.clearBackground()
    
    bk.draw()
    game.drawText("Level 1",10,10)
    
    
    #Car settings    
    car.draw()
    if keys.Pressed[K_LEFT]:
        car.x -= 20
    if keys.Pressed[K_RIGHT]:
        car.x += 20
    if keys.Pressed[K_UP]:
        car.resizeBy(-10)
    if keys.Pressed[K_DOWN]:
        car.resizeBy(10)

    explosion.draw(False)



    # Potholes setup
    for index in range(20):
        pothole[index].move()

        #make the pothole invisible until it reach after 470 (y-value)
        if pothole[index].y < 470:
            pothole[index].visible = False
        else:    
            pothole[index].visible = True


        #if car hit potholes...
        if pothole[index].collidedWith(car):
            car.health -= 1
            collide.play()
            explosion.moveTo(pothole[index].x,pothole[index].y)
            explosion.visible = True

        if car.health <1: #game ends when car's health is 0
            game.over = True
            over.play()


    #Fuel setup
    for index in range(50):
        fuel[index].move()
        #if car collect the fuels...
        if fuel[index].collidedWith(car):
            car.health += 5
            fuelcount += 1
            collectfuel.play()
            fuel[index].visible = False
            
    #Player move to next level
    if fuelcount >= 15 :
        game.over = True

    #Texts
    game.drawText("Collect 15 fuels to proceed.",10,25)       
    game.drawText("Car Health: " + str(car.health), 10, 40) 
    game.drawText("Fuels Collected: " + str(fuelcount),10,55)

    game.update(60)
game.over = False


#Level 2
fuelcount = 0
while not game.over:
    game.processInput() # Process the inputs
    game.clearBackground()
    bk.draw()
    game.drawText("Level 2",10,10)

    cow.move(False)
    if cow.isOffScreen("bottom"):
        x = randint(100,750)
        cow.moveTo(x,470)

    if cow.collidedWith(car):
        car.health -= 1
        explosion.moveTo(cow.x,cow.y)
        explosion.visible = True
                
    #car setup    
    car.draw()
    if keys.Pressed[K_LEFT]:
        car.x -= 20
    if keys.Pressed[K_RIGHT]:
        car.x += 20
    if keys.Pressed[K_UP]:
        car.resizeBy(-10)
    if keys.Pressed[K_DOWN]:
        car.resizeBy(10)

    
    explosion.draw(False)

    #pothole setup        
    for index in range(30):
        pothole[index].move()
        if pothole[index].y < 440:
            pothole[index].visible = False
        else:    
            pothole[index].visible = True


        if pothole[index].collidedWith(car):
            car.health -= 5
            collide.play()
            explosion.moveTo(pothole[index].x,pothole[index].y)
            explosion.visible = True

        if car.health <1:
            game.over = True
            over.play()
    #sign setup
    for index in range(10):
        stopsign[index].move()
        if stopsign[index].y < 450:
            stopsign[index].visible = False
        else:    
            stopsign[index].visible = True


        if stopsign[index].collidedWith(car):
            car.health -= 5
            collide.play()
            explosion.moveTo(stopsign[index].x,stopsign[index].y)
            explosion.visible = True

        if car.health <1:
            game.over = True
            over.play()
    #fuel setup
    for index in range(50):
        fuel[index].move()
        if fuel[index].collidedWith(car):
            car.health += 5
            fuelcount += 1
            collectfuel.play()
            fuel[index].visible = False


    #Texts    
    game.drawText("Car Health: " + str(car.health), 10, 25) 
    game.drawText("Fuels Collected: " + str(fuelcount),10,40)          
    game.drawText("Collect 10 fuels to get to your destination",10,55)


    #game completedd screen
    if fuelcount >= 10:
        game.clearBackground(black)
        bk.draw()
        bk.stop()
        home.draw()
        win.play()
        congratulation.draw()
        game.drawText("Press [SPACE] to Quit",10,10)   

        if keys.Pressed[K_SPACE]:
            game.over = True


    game.update(60)
game.over = False

#over Screen
game.clearBackground(black)
gameover.draw()
game.drawText("Press [SPACE] to Quit",400,500)
game.update(300)
game.wait(K_SPACE)

game.over = False


game.quit()
