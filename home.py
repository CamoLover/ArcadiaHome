import pygame
from pygame import mixer
import subprocess
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

#starting the mixer for sfx and add background music
mixer.init()
mixer.music.load('/home/arcadia/Desktop/ArcadiaHome-main/music.wav')
mixer.music.play(-1)

# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size,)

# Set the caption for the window
pygame.display.set_caption("Arcadia")

# Load the background image and scale it to the size of the screen
background_image = pygame.image.load("/home/arcadia/Desktop/ArcadiaHome-main/backgroundImage.ppm").convert()
background_image = pygame.transform.scale(background_image, size)

# Load images for the games
pacman_image = pygame.image.load("/home/arcadia/Desktop/ArcadiaHome-main/PacMan.png").convert_alpha()
mario_image = pygame.image.load("/home/arcadia/Desktop/ArcadiaHome-main/smbNES.jpg").convert_alpha()
donkeykong_image = pygame.image.load("/home/arcadia/Desktop/ArcadiaHome-main/dkong.jpg").convert_alpha()

# Create a list of games
games = [("Pacman", pacman_image), ("Mario Nes", mario_image), ("DK Nes", donkeykong_image)]

# Set the font for the menu text
font = pygame.font.Font(None, 50)

# Set the initial selection to the first game
selected = 0

# Loop until the user clicks the close button
done = False
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("/home/arcadia/Desktop/ArcadiaHome-main/click.wav"), maxtime=600)
                # Move the selection to the left
                selected = max(selected - 1, 0)
            elif event.key == pygame.K_d:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("/home/arcadia/Desktop/ArcadiaHome-main/click.wav"), maxtime=600)
                # Move the selection to the right
                selected = min(selected + 1, len(games) - 1)
            elif event.key == pygame.K_RETURN:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("/home/arcadia/Desktop/ArcadiaHome-main/pickupGame.wav"), maxtime=600)
                # Launch the selected game
                game_name, game_image = games[selected]
                print(f"Launching {game_name}...")
                if game_name == "Pacman":
                    pacman = ('mednafen -fs 1 "/home/arcadia/Desktop/gamemednafen/pacman.zip"')
                    os.system(pacman)
                    print(f"{game_name} Launched with success")
                    #code to launch game
                    
                elif game_name == "Mario Nes":
                    smb = ('mednafen -fs 1 "/home/arcadia/Desktop/gamemednafen/smb.zip"')
                    os.system(smb)
                    print(f"{game_name} Launched with success")
                    
                    #code to launch game
                elif game_name == "DK Nes":
                    dkong = ('mednafen -fs 1 "/home/arcadia/Desktop/gamemednafen/dkong.zip"')
                    os.system(dkong)
                    print(f"{game_name} Launched with success")
                    
                    
                    #code to launch game
                else :
                    print(f"Error, no game selectionned")

    # --- Drawing code goes here ---
    
    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the games
    for i, game in enumerate(games):
        game_name, game_image = game
        x = 200 + (i * 450)
        y = 200
        # Draw the selection glow
        if i == selected:
            pygame.draw.rect(screen, GREEN, (x + 150, y + 150, 300, 300), 5)
        # Resize the game image to fit inside the selection glow
        game_image = pygame.transform.scale(game_image, (280, 280))
        # Draw the game image inside the selection glow
        screen.blit(game_image, (x + 160, y + 160))

    # Update the screen
    pygame.display.flip()

# Close the window and quit
pygame.quit()
