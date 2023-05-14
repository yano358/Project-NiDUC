from tkinter import *
from PIL import ImageTk, Image
#GUI
import time

class DartBoard():
    shots = []
    roundCurr = 0

    def __init__(self, player, shots, maxRounds, maxShots):
        self.player = player
        self.shots = shots
        self.maxRounds = maxRounds
        self.maxShots = maxShots

    def run(self):
        self.top = Tk()
        self.top.geometry("420x480")
        self.top.title('Player ' + str(self.player))
        #todo labelll
        image = Image.open("DartBoard.png")
        self.bg_image = ImageTk.PhotoImage(image)

        self.canvas = Canvas(self.top, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack() 
    
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        self.roundLabel = Label(self.top, text = "Runda: " + str(self.roundCurr))
        self.roundLabel.pack()

        def button_click():
            self.roundCurr += 1

            if(self.roundCurr > self.maxRounds):
                self.top.destroy()
                return
            
            self.drawRound(self.roundCurr)
            

        button = Button(self.top, text="Następna runda:", width = 210, height = 30, command = button_click)
        button.pack()

        self.top.mainloop()


    def drawRound(self, round):
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        move = (round - 1) * self.maxShots

        for i in range (0, self.maxShots):
            self.takeShot(self.shots[ i + move ][0], self.shots[i + move ][1])


    def takeShot(self, xCord, yCord):
        circle_x = int((xCord * 210 / 5.0) + 210)  # X-coordinate of the circle's center
        circle_y =  int((yCord * -210 / 5.0) + 210)  # Y-coordinate of the circle's center
        circle_radius = 5  # Radius of the circle
        circle_color = "light blue"  # Color of the circle
        self.canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius,
                                circle_x + circle_radius, circle_y + circle_radius,
                                fill=circle_color)
        