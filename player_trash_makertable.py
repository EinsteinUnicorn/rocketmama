#Ashley
#player:
#direction/ pick up/ drop off/ 
#customer
from cmu_112_graphics import *
from tkinter import *
from PIL import Image
import random
import copy

class Aliens(object):
    def __init__(self, alienNum, x, y, app):
        self.app = app
        self.alienNum = alienNum
        self.spriteList = []
        for i in range (1,7):
            pngFile = Image.open(f'worker{i}.png')
            self.spriteList.append(pngFile)
        self.sprite = self.spriteList[self.alienNum-1]
        self.x = x
        self.y = y

    def drawAlienWorker(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))
        



class Player(object):
    def __init__(self, playerNum, mode):
        self.mode = mode
        self.playerNum = playerNum
        self.spriteList = [] #sprite list for players go here
        self.sprite = self.spriteList[self.playerNum-1]
        self.score = 0
        self.orderList = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
        self.holding = []
        self.x = mode.width//2
        self.y = mode.height//2
        self.charW = 8
        self.charH = 12
        self.items = set([Wheel,Engine,ControlPanel,Shell,FuelTank])
        self.tables = Tables() #table object class list?
        self.lastKey = ''
        

    def move(self,event):
        if (event.key == 'Right'):
            self.x += 10
            if self.x >= mode.width:
                self.x -= 10
            for table in self.tables:
                if isColliding(table):
                    self.x -= 10
            self.lastKey = 'Right'
            
        elif (event.key == 'Left'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if isColliding(table):
                    self.x += 10
            self.lastKey = 'Left'
            
        elif (event.key == 'Up'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if isColliding(table):
                    self.y += 10
            self.lastKey = 'Up'
                    
        elif (event.key == 'Down'):
            self.y += 10
            if self.y >= mode.height:
                self.y -= 10
            for table in self.tables:
                if isColliding(table):
                    self.y -= 10
            self.lastKey = 'Down'

            
    def isColliding(self, table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        #collide bottom right
        if (a <= (table.x + table.w) and\
            b >= (table.x + table.w)) and\
            (c <= (table.y + table.h) and\
            d >= (table.y + table.h)):
            return True
        #collide top right
        elif (a <= (table.x + table.w) and\
            b >= (table.x + table.w)) and\
            (c <= (table.y - table.h) and\
            d >= (table.y - table.h)):
            return True
        #collide bottom left
        elif (b >= (table.x - table.w) and\
            a <= (table.x - table.w)) and\
            (c <= (table.y + table.h) and\
            d >= (table.y + table.h)):
            return True
        #collide top left
        elif (b >= (table.x - table.w) and\
            a <= (table.x - table.w)) and\
            (c <= (table.y - table.h) and\
            d >= (table.y - table.h)):
            return True
        #collide top
        elif (a >= (table.x - table.w) and\
            b <= (table.x + table.w)) and\
            (c <= (table.y - table.h) and\
            d >= (table.y - table.h)):
            return True
        #collide bottom
        elif (a >= (table.x - table.w) and\
            b <= (table.x + table.w)) and\
            (c <= (table.y + table.h) and\
            d >= (table.y + table.h)):
            return True
        #collide left
        elif(a <= (table.x - table.w) and\
            b >= (table.x - table.w)) and\
            (c >= (table.y - table.h) and\
            d <= (table.y + table.h)):
            return True
        #collide right
        elif (a <= (table.x + table.w) and\
            b >= (table.x + table.w)) and\
            (c >= (table.y - table.h) and\
            d <= (table.y + table.h)):
            return True
        else:
            return False
        

    def pickDrop(self,event):
        for table in self.tables:
            if (event.key == 'd' and tableInFront(table) and\
                len(self.holding)>0) and (isinstance(table,Trash) or\
                isinstance(table,MakerTable)):
                item = self.holding.pop
                if isinstance(table,MakerTable) and\
                    self.orderList[len(makerTable1.progress)]==str(item):
                    makerTable1.progress.append(item)
                elif isinstance(table,MakerTable):
                    self.holding.append(item)
                    print("Can't drop here!")
                        
                
            elif (event.key == 'e' and tableInFront(table) and\
                len(self.holding)<2):
                self.holding.append(self.table.item)
            
            
    def tableInFront(self,table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        
        if self.lastKey == 'Right' and\
            (a <= (table.x + table.w) and\
            b >= (table.x + table.w)) and\
            (c >= (table.y - table.h) and\
            d <= (table.y + table.h)):
            return True
        elif self.lastKey == 'Left' and\
            (a <= (table.x - table.w) and\
            b >= (table.x - table.w)) and\
            (c >= (table.y - table.h) and\
            d <= (table.y + table.h)):
            return True
        elif self.lastKey == 'Up' and\
            (a >= (table.x - table.w) and\
            b <= (table.x + table.w)) and\
            (c <= (table.y + table.h) and\
            d >= (table.y + table.h)):
            return True
        elif self.lastKey == 'Down' and\
            (a >= (table.x - table.w) and\
            b <= (table.x + table.w)) and\
            (c <= (table.y - table.h) and\
            d >= (table.y - table.h)):
            return True


class ReceiveTable(object):
    def __init__(self,xPos,yPos,wid,hei):
        self.x = xPos
        self.y = yPos
        self.wid = wid
        self.hei = hei

class Trash(ReceiveTable):
    pass

class MakerTable(ReceiveTable):
    def __init__(self,xPos,yPos,wid,hei):
        super().__init__(x,y,wid,hei)
        self.progress = []

    




#ModalApp
class SplashScreenMode(Mode):
    def redrawAll(mode,canvas):
        canvas.create_text(mode.width/2, 200, text='This is a modal splash screen!')

    #for now keyPressed, but should change to mouse Press or sth
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def appStarted(mode):
        mode.spriteCount = 0
        mode.alien1 = Aliens(1,300,500,mode)
        
        
    def timerFired(mode):
        mode.spriteCount += 1

    def redrawAll(mode,canvas):
        mode.alien1.drawAlienWorker(canvas)


class CookingRocket(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.setActiveMode(app.splashScreenMode)

CookingRocket(width=1320,height=870)
