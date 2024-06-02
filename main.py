import pygame

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("test_backgroundpng.png"), SIZE)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            ...
            self.rect.y -5




test_object = GameSprite("test.png",(100,100),(100,100))


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        window.blit(background, (0,0))
        test_object.reset()


    pygame.display.update()
    clock.tick(FPS)
