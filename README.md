# traffic_light
Interactive Traffic light code

Traffic Light Simulator (Tkinter)
# Overview

This project is an interactive Traffic Light Simulator built using Python and the Tkinter GUI library. The program visually represents a traffic light and allows users to switch between red, yellow, and green lights using radio buttons. Selecting a button updates the displayed light in real time.

The project demonstrates event-driven programming, GUI layout design, and basic state management in Python.

# Features

Interactive radio buttons to select traffic light states
Visual traffic light displayed using a Tkinter Canvas
Real-time updates when a new light is selected
Clear separation between UI setup and logic

# How It Works

The interface displays three radio buttons: Red, Yellow, and Green.
A shared variable (IntVar) tracks which option is selected.
When a radio button is clicked, a callback function updates the canvas.
Only one light is illuminated at a time, mimicking real traffic light behavior.

# Technologies Used

Python 3

Tkinter (Python’s built-in GUI library)

# How to Run the Program

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.

# Run the program:

# Mac / Linux
python3 traffic_light.py

# Windows
python traffic_light.py

The Traffic Light window will open automatically.

# File Structure

traffic_light.py — Main Python file containing the GUI and logic

# Learning Outcomes

This project demonstrates:

GUI development with Tkinter
Event handling using radio buttons
Canvas drawing and item updates
Basic object-oriented programming in Python

# Future Improvements
1. Add automatic light cycling with timers
2. Include pedestrian signals
3. Improve visual styling and layout
4. Add keyboard controls
