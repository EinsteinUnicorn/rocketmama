from cmu_112_graphics import *
from tkinter import *
from PIL import Image 
import random
import copy
from player_trash_makertable import *
from rocket import *

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
        
        #items
        mode.wheel = Wheels(mode, mode.player1)
        mode.fuel = FuelTank(mode, mode.player1)
        mode.engine = Engine(mode, mode.player1)
        mode.controlPanel = ControlPanel(mode, mode.player1)
        mode.shell = Shell(mode, mode.player1)
        
    def timerFired(mode):
        mode.spriteCount += 1

    def redrawAll(mode,canvas):
        mode.alien1.drawAlienWorker(canvas)
        mode.alien2.drawAlienWorker(canvas)
        mode.alien3.drawAlienWorker(canvas)
        mode.alien4.drawAlienWorker(canvas)
        mode.alien5.drawAlienWorker(canvas)
        
        mode.player1.drawPlayers(canvas)

        if mode.player1.amtOfItems() > 0:
            mode.wheel.draw(canvas)
            #mode.fuel.draw(canvas)
            mode.engine.draw(canvas)
            mode.controlPanel.draw(canvas)
            mode.shell.draw(canvas)

class CookingRocket(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.setActiveMode(app.splashScreenMode)

CookingRocket(width=1320,height=870)
