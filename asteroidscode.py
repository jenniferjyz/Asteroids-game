#render = draw for object
#OOP has no global variables
rot = 0 

import random
#Asteroid-----------------------------------------------------------------------------
class Asteroid():
    #Controlling asteroid
    def __init__(self):
        self.x = random.randint(0, 800) #asteroids can move across the 800 pixel screen (horizontal)
        self.y = random.randint(0, 600) #asteroids can move down the 600 pixel screen
        self.vel_y = random.randint(-3, 2) #random velocity between -3 to 5
        self.vel_x = random.randint(-3, 2)
    
    def move(self):
        #Moving asteroid
        #wrapping 
        if self.x>=width+50: #width is 800
            self.x = 0 #come back to edge
        elif self.x <= 50:
            self.x=width #asteroids stay inside
        self.x += self.vel_x #add a velocity from the random velocity range (give them speed)
        
        if self.y >= height + 50:
            self.y = 0
        elif self.y <= 50:
            self.y = height
        self.y += self.vel_y
        
    def render(self,ship): 
    #drawing and moving asteroids
        fill(255) 
        ellipse(self.x, self.y, 50, 50)
        #collision detection
        if self.checkAsteroidShipCollision(ship):
            noLoop() #stop game
            gameOver() #print gameover
        
    def checkAsteroidShipCollision (self,ship):
    #asteroids hit ship
        distance_x = (self.x - ship.x)**2 
        distance_y = (self.y - ship.y)**2
        distance = sqrt(distance_x + distance_y) #calculate distance between ship and asteroid
        if distance <= 30:
          return True
        else:
          return False 
        
#Ship-----------------------------------------------------------------------------
class Ship():
    '''Controlling ship'''
    def __init__(self):
        self.x = 400 #transformation
        self.y = 300
        
        self.rot = 0 
        self.vel = 5
        self.vel_x = 0
        self.vel_y = 0
        self.inertial_drift = False
        
    def move(self):
        '''Rotate triangle, acceleration, wrap ship'''
        self.vel_x = sin(radians(self.rot)) #makes triangle move in direction with angle rotated in 
        self.vel_y = -cos(radians(self.rot))
        
        self.x += self.vel * self.vel_x #acceleration

        if self.x>=width+100: #wrap ship
            self.x=0
        elif self.x<=-100:
            self.x=width
        self.y += self.vel * self.vel_y
        
        if self.y>=height+100:
            self.y=0
        elif self.y<=-100:
            self.y=height
        self.y += self.vel * self.vel_y 
    
    def friction(self):
        '''Controlling ship's friction'''
        self.vel_y *= 0.95 #slows down
        self.vel_x *= 0.95
        
        self.x += self.vel_x * self.vel
        self.y += self.vel_y * self.vel

    def render(self):
        '''Drawing and controlling rotation of ship'''
        pushMatrix() #lock transformation in place
    
        translate(self.x,self.y)
        rotate(radians(self.rot)) #rotate 5 radians
        
        triangle(0,-20,-10,10,10, 10) #undo transformations to get correct origin
        
        popMatrix()

ast = [] #empty list for asteroid
for n in range(5): #5 asteroids on screen
    ast.append(Asteroid()) #add asteroids to list
ship = Ship() #make the ship

def setup():
    '''Drawing background'''
    global rot
    size(800,600)
    background(119,158,203) #background colour
    
def draw():
    '''Rotation and friction with keyboard'''
    global rot, ast
    background(119,158,203) #so asteroids don't leave a trail of black
    for n in ast:
        n.move()
        n.render(ship)
    
    if key_p[0]:
        ship.move()
    if key_p[1]:
        ship.rot += 5 #if right is pressed then move 5 radians
        
    if key_p[2]:
        ship.rot -= 5 #if right is pressed then move 5 radians
    
    if not key_p[0]:
        ship.friction()
    
    ship.render() #ship move certain radians
   # if ship.inertial_drift:
     #   ship.vel*=0.95
    
key_p = [False, False, False] #set all as false first
#Keyboard Controls---------------------------------------------------------------------------
def keyPressed():
    global rot, key_p
    size(800,600)
    background(119,158,203) #background colour
    if keyCode == RIGHT:
        key_p[1] = True
    if keyCode == LEFT:
        key_p[2] = True
    if keyCode == UP:
        key_p[0] = True
       # ship.inertial_drift = False
        
def keyReleased():
    '''Built-in fn when key's released'''
    global key_p
    if key_p[0]:
        key_p[0] = False #it doesn't move when it isn't pressed
       # ship.inertial_drift = True
    if key_p[1]:
        key_p[1] = False
    if key_p[2]:
        key_p[2] = False

def gameOver(): #display game over text
    textAlign(CENTER);
    textSize(50)
    text("GAME OVER", width/2, height/2);
