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
    def __init__(self, alienNum, x, y, mode):
        self.mode = mode
        self.alienNum = alienNum
        self.spriteList = []
        for i in range (1,7):
            pngFile = Image.open(f'worker{i}.png')
            self.spriteList.append(pngFile)
        self.sprite = self.spriteList[self.alienNum-1]
        self.sprite = mode.scaleImage(self.sprite,1/2)
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
        sprite = self.spriteList[self.playerNum-1]
        self.sprite = mode.scaleImage(sprite,1/2)
        self.score = 0
        self.orderList = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
        self.holding = []
        self.x = mode.width//2
        self.y = mode.height//2
        self.charW = 8
        self.charH = 10
        #self.items = set([Wheel,Engine,ControlPanel,Shell,FuelTank])
        table = Table()
        self.tables = table.allTables
        self.lastKey = ''
    def drawPlayers(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))

    def move(self,event):
        if (event.key == 'Right'):
            self.x += 10
            if self.x >= self.mode.width:
                self.x -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x -= 10
            self.lastKey = 'Right'
            
        elif (event.key == 'Left'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x += 10
            self.lastKey = 'Left'
            
        elif (event.key == 'Up'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y += 10
            self.lastKey = 'Up'
                    
        elif (event.key == 'Down'):
            self.y += 10
            if self.y >= self.mode.height:
                self.y -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y -= 10
            self.lastKey = 'Down'

            
    def isColliding(self, table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        #collide bottom right
        if (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide top right
        elif (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide bottom left
        elif (b >= (table.x - table.wid) and\
            a <= (table.x - table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide top left
        elif (b >= (table.x - table.wid) and\
            a <= (table.x - table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide top
        elif (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide bottom
        elif (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide left
        elif(a <= (table.x - table.wid) and\
            b >= (table.x - table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        #collide right
        elif (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        else:
            return False
            
    def tableInFront(self,table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        
        if self.lastKey == 'Right' and\
            (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Left' and\
            (a <= (table.x - table.wid) and\
            b >= (table.x - table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Up' and\
            (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Down' and\
            (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        return False

def pickDrop(player,event):
    for table in Table().allTables:
        if (event.key == 'd'):
            print('d pressed')
            print(Player.tableInFront(player,table))
            print(player.lastKey)
            if Player.tableInFront(player,table) and\
                len(player.holding)>0 and (isinstance(table,ReceiveTable)):
                item = player.holding.pop
                if isinstance(table,MakerTable) and\
                    player.orderList[len(makerTable1.progress)]==str(item):
                    makerTable1.progress.append(item)
                    print("dropped")
                elif isinstance(table,MakerTable):
                    player.holding.append(item)
                    print("Can't drop here!")
                        
        elif (event.key == 'e'):
            print('e pressed')
            if Player.tableInFront(player,table) and\
                (isinstance(table,PickupTable) and len(player.holding)<2):
                player.holding.append(player.table.item)
                print("picked up")


#Tables
class ReceiveTable(object):
    wid = 100
    hei = 50

class Trash(ReceiveTable):
    def __init__(self,xPos,yPos,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.x = xPos
        self.y = yPos
    pass

class MakerTable(ReceiveTable):
    def __init__(self,xPos,yPos,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.progress = []
        self.image = Image.open('makerTable.png')
        self.image = mode.scaleImage(self.image,1/2)
        
    def drawMakerTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class PickupTable(object):
    wid = 100
    hei = 50

class WheelTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = Wheels(mode)
        image = Image.open('wheelTable.png')
        self.image = mode.scaleImage(image,1/3)

    def __repr__(self):
        return 'WheelTable'

    def drawWheelTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

        
class FuelTankTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,item,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.rotated = rotated
        self.item = FuelTank(mode)
        image = Image.open('fuelTankTable.png')
        self.image = mode.scaleImage(sprite,1/2)

    def __repr__(self):
        return 'FuelTank'

    def drawFuelTankTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

        
class EngineTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,item,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.rotated = rotated
        self.item = Engine(mode)
        image = Image.open('engineTable.png')
        self.image = mode.scaleImage(sprite,1/2)

    def __repr__(self):
        return 'Engine'

    def drawEngineTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

class ControlPanelTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,item,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.rotated = rotated
        self.item = ControlPanel(mode)
        image = Image.open('controlPanelTable.png')
        self.image = mode.scaleImage(sprite,1/2)

    def __repr__(self):
        return 'ControlPanel'

    def drawControlPanelTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class ShellTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,item,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.rotated = rotated
        self.item = Shell(mode)
        image = Image.open('shellTable.png')
        self.image = mode.scaleImage(sprite,1/2)

    def __repr__(self):
        return 'Shell'

    def drawShellTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class Table(object):
    allTableTypes = set([WheelTable,FuelTankTable,EngineTable,
                                  ControlPanelTable,ShellTable,Trash,MakerTable])
    allTables = set()

    def addTable(self,table):
        Table.allTables.add(table)

    def __repr__(self):
        return Table.allTables

        

    


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

    
#other helper fx:
#from http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#cachingPhotoImages
#CachingPhotoImage for increased speed section   
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def getCachedPhotoImage(image):
    if ('cachedPhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage

# from www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
def getCellBounds(mode, row, col):
    gridWidth  = mode.width - 2*mode.margin
    gridHeight = mode.height - 2*mode.margin
    columnWidth = gridWidth / mode.cols
    rowHeight = gridHeight / mode.rows
    x0 = mode.margin + col * columnWidth
    x1 = mode.margin + (col+1) * columnWidth
    y0 = mode.margin + row * rowHeight
    y1 = mode.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)


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
        mode.margin = 5
        PickupTable()
        #floor
        mode.rows,mode.cols = 15,22
        mode.floor = make2dList(mode.rows,mode.cols)
        tile = Image.open('tile.png')
        mode.tile = mode.scaleImage(tile,1/4)

        for row in range(mode.rows):
            for col in range(mode.cols):
                mode.floor[row][col] = mode.tile
        
        #aliens
        mode.alien1 = Aliens(1,100,600,mode)
        mode.alien2 = Aliens(2,400,80,mode)
        mode.alien3 = Aliens(3,800,80,mode)
        mode.alien4 = Aliens(4,1200,300,mode)
        mode.alien5 = Aliens(5,1200,700,mode)
        
        #tables
        mode.wheelTable = WheelTable(400,160,False,mode)
        Table.addTable(Table,mode.wheelTable)
        
        mode.makerTable = MakerTable(mode.width/2-50,mode.height/2-25,mode)

        #players
        mode.player1 = Player(1,mode)
        mode.player2 = Player(2,mode)
        mode.player3 = Player(3,mode)
        mode.player4 = Player(4,mode)

        
    def timerFired(mode):
        mode.spriteCount += 1

    def keyPressed(mode,event):
        Player.move(mode.player1,event)
        pickDrop(mode.player1,event)
        Player.move(mode.player2,event)
        Player.move(mode.player3,event)
        Player.move(mode.player4,event)
        

    def redrawAll(mode,canvas):
        #floor
        for row in range(mode.rows):
            for col in range(mode.cols):
                (x0, y0, x1, y1) = getCellBounds(mode,row, col)
                cx, cy = (x0 + x1)/2, (y0 + y1)/2
                tile = mode.floor[row][col]
                photoImage = getCachedPhotoImage(tile)
                canvas.create_image(cx,cy,image=photoImage)
        
        #workers
        mode.alien1.drawAlienWorker(canvas)
        mode.alien2.drawAlienWorker(canvas)
        mode.alien3.drawAlienWorker(canvas)
        mode.alien4.drawAlienWorker(canvas)
        mode.alien5.drawAlienWorker(canvas)

        #tables
        mode.wheelTable.drawWheelTable(canvas)
        
        #players
        mode.player1.drawPlayers(canvas)
        #mode.player2.drawPlayers(canvas)
        #mode.player3.drawPlayers(canvas)
        #mode.player4.drawPlayers(canvas)


class CookingRocket(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.setActiveMode(app.splashScreenMode)

CookingRocket(width=1320,height=870)
