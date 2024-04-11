import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 900))
surface = pygame.Surface((100,100), pygame.SRCALPHA)

done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True