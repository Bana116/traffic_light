# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Student Name: <Asmaa Bana>
# Student Number: <1012819611>
# Supervisor: Dr. Maher Elshakankiri
#
#
# Tutorial 3, Problem 1
# Purpose: Traffic Light
# Date Created: <2025/11/06>
# Date Modified: <d2025/11/06>

from tkinter import * 

class TrafficLight: 
    def __init__(self):
        window = Tk()
        window.title("Traffic Light")
        
        #Frame for radio buttons
        frame1 = Frame(window)
        
        frame1.pack()
        
        #Shared variable for all radio buttons 
        self.color = IntVar() #0 means nothing selected 
        
        rbRed = Radiobutton(frame1, text="Red", variable=self.color, value=1, command=self.updated_light)
        rbYellow = Radiobutton(frame1, text="Yellow", variable=self.color, value=2, command=self.updated_light)
        rbGreen = Radiobutton(frame1, text="Green", variable=self.color, value=3, command=self.updated_light)
        
        rbRed.grid(row=0, column=0, padx=5, pady=5)
        rbYellow.grid(row=0, column=1, padx=5, pady=5)
        rbGreen.grid(row=0, column=2, padx=5, pady=5)
        
        #Canvas for lights 
        self.canvas = Canvas(window, width=150, height=300, bg="white")
        self.canvas.pack()
        
        #Create three circle outlines 
        self.red_light = self.canvas.create_oval(50, 20, 100, 70, fill="white", outline="black")
        self.yellow_light = self.canvas.create_oval(50, 100, 100, 150, fill="white", outline="black")
        self.green_light = self.canvas.create_oval(50, 180, 100, 230, fill="white", outline="black")
        
        window.mainloop()
        
    def updated_light(self): 
        # Turn all lights off
        self.canvas.itemconfig(self.red_light, fill="white")
        self.canvas.itemconfig(self.yellow_light, fill="white")
        self.canvas.itemconfig(self.green_light, fill="white")
        
        # Light up the selected one
        if self.color.get() == 1:
            self.canvas.itemconfig(self.red_light, fill="red")
        elif self.color.get() == 2:
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
        elif self.color.get() == 3:
            self.canvas.itemconfig(self.green_light, fill="green")
            
TrafficLight()