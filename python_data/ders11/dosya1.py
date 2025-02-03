import pygame
from os import system

pygame.init() # Initialize pygame

icon = pygame.image.load("./file.png") # Load the icon image
pygame.display.set_icon(icon)

pygame.display.set_caption("My Game") # Set the title of the window
uygulama = pygame.display.set_mode((800, 600)) # Create the window

uygulama.fill((255, 255, 255)) # Fill the window with white color

zeminresmi = pygame.image.load("./image.jpg") # Load the background image

kontrol = True
while kontrol:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kontrol = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                kontrol = False
    uygulama.blit(zeminresmi, (0, 0)) # Draw the background image
    pygame.display.update() # Update the window

pygame.quit() # Quit pygame
system("clear") # Clear the terminal