import pygame
#from pygame.sprite import _Group

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

player = Soldier(200, 200, 0.2)  
player2 = Soldier(400, 200, 0.2)




run = True
while run:


    screen.blit(player.image,player.rect)
    screen.blit(player2.image,player2.rect)

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()


pygame.quit()