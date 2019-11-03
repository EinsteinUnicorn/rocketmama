#Ashley
#player:
#direction/ pick up/ drop off/ 
#customer
from cmu_112_graphics import *
from tkinter import *
from PIL import Image
import random
import copy

#MAKERS
class Aliens(object):
    def __init__(self, alienNum, x, y, app):
        self.app = app
        self.alienNum = alienNum
        self.spriteList = []
        for i in range (1,7):
            pngFile = Image.open(f'worker{i}.png')
            self.spriteList.append(pngFile)
        self.sprite = self.spriteList[self.alienNum-1]
        self.sprite = app.scaleImage(self.sprite,1/2)
        self.x = x
        self.y = y

    def drawAlienWorker(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))
        



class Player(object):
    def __init__(self, playerNum, mode):
        self.mode = mode
        self.playerNum = playerNum
        self.spriteList = []
        for i in range (1,5):
            pngFile = Image.open(f'player{i}.png')
            self.spriteList.append(pngFile)
        self.sprite = self.spriteList[self.playerNum-1]
        self.score = 0
        self.orderList = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
        self.holding = []
        self.x = mode.width//2
        self.y = mode.height//2
        self.charW = 8
        self.charH = 12
        #self.items = set([Wheel,Engine,ControlPanel,Shell,FuelTank])
        table = Table()
        self.tables = table.allTables
        self.lastKey = ''
    def drawPlayers(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))

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

#Tables
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


class PickupTable(object):
    def __init__(self,xPos,yPos,wid,hei):
        self.x = xPos
        self.y = yPos
        self.wid = wid
        self.hei = hei

class WheelTable(PickupTable):
    def __init__(self,xPos,yPos,wid,hei,item):
        super().__init__(x,y,wid,hei)
        self.item = Wheel()
        
class FuelTankTable(PickupTable):
    def __init__(self,xPos,yPos,wid,hei,item):
        super().__init__(x,y,wid,hei)
        self.item = FuelTank()
        
class EngineTable(PickupTable):
    def __init__(self,xPos,yPos,wid,hei,item):
        super().__init__(x,y,wid,hei)
        self.item = Engine()

class ControlPanelTable(PickupTable):
    def __init__(self,xPos,yPos,wid,hei,item):
        super().__init__(x,y,wid,hei)
        self.item = ControlPanel()

class ShellTable(PickupTable):
    def __init__(self,xPos,yPos,wid,hei,item):
        super().__init__(x,y,wid,hei)
        self.item = Shell()

class Table(object):
    def __init__(self):
        self.allTableTypes = set([WheelTable,FuelTankTable,EngineTable,
                                  ControlPanelTable,ShellTable,Trash,MakerTable])
        self.allTables = set()

    def addTable(self,table):
        self.allTables.add(table)

        

    


#MAKING
class Rocket(object):
    orderedItems = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
    def __init__(self, mode):
        self.mode = mode
        self.items = []

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
            #draw the assembled rocket
            pass
        else:
            #draw the semi-assembled robot
            pass 
        pass

class Wheels(object):
    def __init__(self, mode):
        self.mode = mode
        pass
    def __repr__(self):
        return 'wheels'
    def draw(self, canvas):
        pass

class FuelTank(object):
    def __init__(self,mode):
        self.mode = mode
        self.tankFilled = False
        pass
    def __repr__(self):
        return f'fuel tank {self.tankFilled}'
    def fillTank(self):
        if self.tankFilled == False:
            self.tankFilled = True
        else:
            print('You already filled this tank')
    def draw(self, canvas):
        pass
class Engine(object):
    def __init__(self, mode, engineNum):
        self.mode = mode
        self.engineNum = engineNum
        self.shape = None

    def selectShape(self, shape):
        self.shape = shape

    def draw(self, event):
        if self.shape == 'triangle':
            #draw a triangle
            pass
        elif self.shape == 'circle':
            #draw a circle
            pass
        elif self.shape == 'square':
            #draw a square
            pass

class ControlPanel(object):
    def __init__(self, mode):
        self.mode = mode
        self.wired = False
    def wire(self):
        if self.wired == False:
            print('wired!')
        else:
            print("I'm already wired")

class Shell(object):
    def __init__(self, mode):
        self.mode = mode
        self.color = None
    def selectColor(self, color):
        self.color = color
    def draw(self, canvas):
        pass

    




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
        #aliens
        mode.alien1 = Aliens(1,100,600,mode)
        mode.alien2 = Aliens(2,400,100,mode)
        mode.alien3 = Aliens(3,800,100,mode)
        mode.alien4 = Aliens(4,1200,300,mode)
        mode.alien5 = Aliens(5,1200,700,mode)
        #players
        mode.player1 = Player(1,mode)
        
    def timerFired(mode):
        mode.spriteCount += 1

    def redrawAll(mode,canvas):
        mode.alien1.drawAlienWorker(canvas)
        mode.alien2.drawAlienWorker(canvas)
        mode.alien3.drawAlienWorker(canvas)
        mode.alien4.drawAlienWorker(canvas)
        mode.alien5.drawAlienWorker(canvas)
        
        mode.player1.drawPlayers(canvas)


class CookingRocket(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.setActiveMode(app.splashScreenMode)

CookingRocket(width=1320,height=870)
