# Arcadia - High School "Chef d'oeuvre" Project 🕹️

## Introduction 🎮

Arcadia is a high school "Chef d'oeuvre" project – a nostalgic home menu created for an arcade setup. Crafted by a group of three students, this project simplifies the process of selecting and launching classic NES games. Written in Python, Arcadia offers a user-friendly interface for enjoying three timeless classics: Mario Bros, Pac-Man, and Donkey Kong.

## Features 🌟

- **Arcade Button Compatibility**: Arcadia smoothly integrates with arcade buttons, delivering an authentic gaming experience.

- **Game Launching**: Gamers can effortlessly choose and start their favorite game directly from the menu.

- **Custom Background Image**: The home menu flaunts a custom background image, elevating the arcade's visual appeal.

- **Raspberry Pi Integration**: Arcadia is fully compatible with Raspberry Pi, making it a perfect fit for your arcade setup.

## Requirements 📋

To set up and run Arcadia, make sure you have the following:

- [Python](https://www.python.org/downloads/)
- [Pygame](https://www.pygame.org/download.shtml)

## Usage 🚀

1. Clone this repository to your local machine.
2. Ensure you have the necessary game ROMs for Mario Bros, Pac-Man, and Donkey Kong.
3. Modify the file paths in the Python code to point to the correct ROM locations on your system.

```python
# Example: Change these paths to your ROM file locations
pacman = ('mednafen -fs 1 "/path/to/pacman.zip"')
smb = ('mednafen -fs 1 "/path/to/smb.zip"')
dkong = ('mednafen -fs 1 "/path/to/dkong.zip"')
```
Run the Python script, and the Arcadia home menu will spring to life.
How to Play 🎯
Use 'A' and 'D' keys to navigate through the game selection.
Press 'Enter' to launch the selected game.
Screenshots 📸
Screenshot


To-Do Checklist 📝
 - [x] Add more games to the menu.
 - [x] Enhance the user interface.
 - [x] Elevate sound effects and music.
 - [x] Document the code for easy customization.
 
Thank you for exploring Arcadia, a labor of love from our high school days! Enjoy your gaming adventures! 🚀🎮
