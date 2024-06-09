import pygame

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background.jpg"), SIZE)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)


class Enemy(GameSprite):
    def update(self):
        ...






class Wall(GameSprite):
    def update(self):
        ...


class Player(GameSprite):
    def update(self):
        if self.rect.bottom <= 550:
            self.rect.y += 5
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_SPACE]:
            self.rect.y -= 10
    




main_character = Player("mario.png",(90,90),(100,530))
enemy_flower = Enemy("angryflower.png",(85,85),(300,530))

walls = [ Wall("wall.png",(300,150),(400,250)),
Wall("wall.png",(300,150),(400,250)),
#ll("wall.png",(300,150),(400,250)),
]

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background, (0,0))
    main_character.reset()
    main_character.update()
    enemy_flower.reset()
    for w in walls:
        w.reset()
        


    pygame.display.update()
    clock.tick(FPS)
