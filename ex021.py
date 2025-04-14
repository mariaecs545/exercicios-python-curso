# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
# Antes de iniciar, deve colar um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load('nome do arquivo mp3')
pygame.mixer.music.play()
pygame.event.wait()
