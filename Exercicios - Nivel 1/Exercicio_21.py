# Importando arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('your_music.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())