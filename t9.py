from pygame.locals import *
import random

pygame.init()

SCREEN_SIZE = 1440
screen = pygame.display.set_mode((SCREEN_SIZE, 120))

################################################################################
#                               Classes                                        #
################################################################################

class Alien(pygame.sprite.Sprite):
    
    def __init__(self, filename, x, y, index):
        super().__init__()
        self.rawimage = pygame.image.load(filename)
        self.image = self.rawimage
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = index
        
    def get_rawimage(self):
        return self.rawimage
        
    def update(self):
        screen.blit(self.image, self.rect)

class Blur(pygame.sprite.Sprite):
    
    def __init__(self, rawimage):
        super().__init__()
        self.rawimage = rawimage
        self.image = self.rawimage
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_SIZE-100)
        self.rect.y = random.randrange(50)
        self.angle = 0
        self.scale = 1
    
    '''
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.rawimage, angle)
    
    def scale(self, scale):
        self.image = pygame.transform.scale(self.rawimage, scale * self.rect.w, scale * self.rect.h)¶
    '''
    
    def rotozoom(self):
        self.angle += 5
        self.scale += 0.1
        self.image = pygame.transform.rotozoom(self.rawimage, self.angle, self.scale)
    
    def update(self):
        screen.blit(self.image, self.rect)
        if self.angle >= 90:
            self.kill()
    
    
alien_group = pygame.sprite.Group()
blur_group = pygame.sprite.Group()

for i in range(0,9):
    a = Alien('/Users/konoha/Desktop/VIS142/project1/alien.png', i*100+20, 20, i)
    alien_group.add(a)

clock = pygame.time.Clock()

################################################################################
#                               Main Loop                                      #
################################################################################

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEBUTTONDOWN:
            for a in alien_group:
                if a.rect.collidepoint(pygame.mouse.get_pos()):
                    print("mouse clicked")
                    b = Blur(a.get_rawimage())
                    blur_group.add(b)
    
    screen.fill((0,0,0))
    
    # show blur animation
    
    for b in blur_group:
        b.rotozoom()
        b.update()
    
    for a in alien_group:
        a.update()
    
    print("alien_group size:\t", len(alien_group))
    print("blur_group size:\t", len(blur_group))
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()    