import pygame

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background.jpg"), SIZE)

pygame.font.init()
font = pygame.font.Font(None , 70)
text_lose = font.render("oh oh!", True, (255,0,0))


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


    
    def draw_wall(self):
        pygame.draw.rect(window,self.color, self.rect)



class Player(GameSprite):
    def update(self):


        
        keys = pygame.key.get_pressed()
        
        for w in walls:

            if  w.rect.colliderect(self.rect):
                
                break
            else:
                if self.rect.bottom <= 575:
                    self.rect.y += 5
                if keys[pygame.K_d]:
                    self.rect.x += 5
                if keys[pygame.K_a]:
                    self.rect.x -= 5
                if keys[pygame.K_SPACE]:
                    self.rect.y -= 10

        
                

       

    




main_character = Player("mario.png",(90,90),(100,530))

walls = [ Wall("wall.png",(300,150),(400,250)),
Wall("wall.png",(300,150),(400,250)),
Wall("wall.png",(300,150),(700,450)),
]

enemy_flowers = [Enemy("angryflower.png",(85,85),(300,530)),
Enemy("angryflower.png",(85,85),(700,355))

]

game_over = False
finish = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if not finish:
        window.blit(background, (0,0))
        main_character.reset()
        main_character.update()
        for f in enemy_flowers:
            f.reset()
        for w in walls:
            w.reset()
            
                
            
        
    
        


        pygame.display.update()
        clock.tick(FPS)
