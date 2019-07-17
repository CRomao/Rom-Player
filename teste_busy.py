import pygame

#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('c.mp3')
pygame.mixer.music.play()
print('tocando')


    if not pygame.mixer.music.get_busy():
    print('\n a musica está no buffer')

a = input('Tocar outra?')