from cmu_112_graphics import *
from tkinter import *
from PIL import Image 
from player_trash_makertable import *
import random
import copy

class Rocket(object):
    orderedItems = []
    def __init__(self, mode, customer):
        self.mode = mode
        self.items = []
        self.customer = customer
        Rocket.orderedItems = self.customer.order

    def addItem(self, part):
        tempList = copy.copy(self.items)
        tempList.append(part)
        index = len(tempList) - 1
        if str(tempList[index]) == Rocket.orderedItems[index]:
            self.items.append(part)
            print('Part added!')
        else:
            if 'False' in  str(tempList[index]):
                print('You need to do something to this item!')
            else:
                print(f'You can not add that, you need {Rocket.orderedItems[index]}')

    def checkAssembly(self):
        tempList = []
        for item in self.items:
            tempList.append(str(item))
        return Rocket.orderedItems ==  tempList     

    def draw(self, canvas):
        assembled = checkAssembly()
        if assembled == True:
            pass

class Wheels(object):
    def __init__(self, app, player):
        self.mode = app
        self.player = player
        self.assembled = None #if this is None, this will not be draw 
        self.wheel =self.mode.scaleImage(self.mode.loadImage('wheel.png'), 1/4)

    def __repr__(self):
        return f'wheels {self.assembled}'

    def getWheel(self):
        self.assembled = True
         
    def draw(self, canvas):
        if 'wheels True' == self.player.inHand():
            canvas.create_image(self.player.x, self.player.y,image=ImageTk.PhotoImage(self.wheel))

class FuelTank(object):
    def __init__(self,app, player):
        self.mode = app
        self.player = player
        self.tankFilled = False
        self.tank = self.mode.scaleImage(self.mode.loadImage('tank.png'), 1/4)
    def __repr__(self):
        return f'fuel tank {self.tankFilled}'
    def fillTank(self):
        if self.tankFilled == False:
            self.tankFilled = True
        else:
            print('You already filled this tank')
    def draw(self, canvas):
        if 'fuel tank True' == self.player.inHand():
            canvas.create_image(self.player.x, self.player.y,image=ImageTk.PhotoImage(self.tank))

class Engine(object):
    def __init__(self, app, player):
        self.mode = app
        self.player = player
        self.shapes = ['triangle', 'square', 'circle']
        self.shape = self.shapes[random.randint(0, 2)]
        self.engineIn = False
    
    def __repr__(self):
        return 'engine {self.shape}'
    
    def getEngine(self):
        self.engineIn = True

    def selectShape(self, shape):
        self.shape = shape

    def draw(self, event):
        self.engine =self.mode.scaleImage(self.mode.loadImage(f'{self.shape}.png'), 1/4)
        if self.engineIn == True:
            if f'engine {self.shape}' in self.player.inHand():
                canvas.create_image(self.player.x, self.player.y,image=ImageTk.PhotoImage(self.engine))

class ControlPanel(object):
    def __init__(self, app, player):
        self.mode = app
        self.player = player
        self.wired = False
        self.acomputer = self.mode.scaleImage(self.mode.loadImage('acomputer.png'), 1/4)
        self.uacomputer = self.mode.scaleImage(self.mode.loadImage('uncomputer.png'), 1/4)

    def __repr__ (self):
        return f'control panel {self.wired}'
    def wire(self):
        if self.wired == False:
            print('wired!')
        else:
            print("I'm already wired")
    
    def draw(self, canvas):
        if 'control panel True' == self.player.inHand():
            canvas.create_image(self.player.x, self.player.y,image=ImageTk.PhotoImage(self.acomputer))
        elif 'control panel False' == self.player.inHand():
            canvas.create_image(self.player.x, self.player.y,image=ImageTk.PhotoImage(self.uacomputer))

class Shell(object):
    def __init__(self, app, player):
        self.mode = app
        self.player = player
        self.color = 'nocolor'

    def __repr__(self):
        return f'shell {self.color}'

    def selectColor(self, colorNum):
        colors = ['pink', 'orange', 'purple']
        self.color = colors[colorNum]

    def draw(self, canvas):
        self.shell = self.mode.scaleImage(self.mode.loadImage(f'{self.color}shell.png'), 1/4)
        if f'shell {self.color}' in self.player.inHand():
            canvas.create_image(self.player.x, self.player.y, image = ImageTk.PhotoImage(self.shell))
        

class Customer(object):
    def __init__(self):
        self.order = ['wheels True', 'fuel tank True', 'engine triangle', \
        'control panel True', 'shell pink']
    
