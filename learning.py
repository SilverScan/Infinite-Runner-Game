import pygame
import pygame.locals as pyg
import math
import random
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
print(pygame.font.get_fonts())



screen = pygame.display.set_mode([1600,900])
screenColor = 0,0,0
running = True
pressed_keys = pygame.key.get_pressed()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.surface.Surface((100,50))
        self.surf.fill((60,60,60))
        self.rect = self.surf.get_rect(
            center = (800, 450)
        )
    def update(self, pressed_keys):
        if pressed_keys[pyg.K_w]:
            x=0
            y=-3
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_a]:
            x=-3
            y=0
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_s]:
            x=0
            y=3
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_d]:
            x=3
            y=0
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_UP]:
            x=0
            y=-3
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_LEFT]:
            x=-3
            y=0
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_DOWN]:
            x=0
            y=3
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)
        if pressed_keys[pyg.K_RIGHT]:
            x=3
            y=0
            if pressed_keys[pyg.K_SPACE]:
                x=x*2
                y=y*2
            self.rect.move_ip(x,y)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1600:
            self.rect.right = 1600
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 900:
            self.rect.bottom = 900
player = Player()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        size = random.randint(20,120)

        self.surf = pygame.Surface((size,size))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(1600+20,1600+100), random.randint(0,900)
            ) )
        self.speed = random.randint(1,6)
    
    def update(self):
        self.rect.move_ip(
            -(self.speed), 0)
        if self.rect.right < 0:
            self.kill()

def checkDeath():
    font2 = pygame.font.SysFont('Impact', 40)
    text2 = font2.render(
        "Final time: " + str(score) + '\nPress enter to restart', True, (255,255,255))
    textRect2 = text2.get_rect()
    textRect2.center = (800, 450)
    if alive == False:
        screen.blit(text2, textRect2)
    else:
        pass     
enemies = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(player)

score = 0
SCOREUP = pygame.USEREVENT + 2
ADDENEMY = pygame.USEREVENT + 1
alive = True
pygame.time.set_timer(ADDENEMY, 250)
pygame.time.set_timer(SCOREUP, 1000)


while running:
    for event in pygame.event.get():
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_RETURN:
                print(score)
                running = False
            elif event.key == pyg.K_p:
                screenColor = 255,255,255
                screen.fill((screenColor))
            elif event.key == pyg.K_o:
                screenColor = 130,130,130
                screen.fill((screenColor))
            elif event.key == pyg.K_i:
                screenColor = 0,0,0
                screen.fill((screenColor))
        elif event.type == ADDENEMY:
            newEnemy = Enemy()
            enemies.add(newEnemy)
            allSprites.add(newEnemy)
        elif event.type == SCOREUP:
            score += 1
    if alive == False:
        pygame.time.set_timer(ADDENEMY, 0)
        pygame.time.set_timer(SCOREUP, 0)


    
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    screen.fill((screenColor))
    screen.blit(player.surf, player.rect) 
    font = pygame.font.SysFont('Impact', 32)
    text = font.render(str(score), False, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (30, 30)
    screen.blit(text, textRect) 
    checkDeath()
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect) 
    if pygame.sprite.spritecollideany(player, enemies):
        alive = False
        player.kill()
        screenColor = 120,0,0       
    pygame.display.flip()
    clock.tick(90)


