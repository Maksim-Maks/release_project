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
text_win = font.render("YOU WIN!",True, (0,0,255))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,filename, size, coords):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)


class Enemy(GameSprite):
    def update(self):
        ...






class Wall(GameSprite):
    def __init__(self,filename, size, coords):
        super().__init__(filename, size, coords)
        self.hardness = 3
    def update(self):
        if self.hardness <= 0:
            self.kill()
        


    
    def draw_wall(self):
        pygame.draw.rect(window,self.color, self.rect)



class Player(GameSprite):
    def update(self,walls):
        global current_lvl
        if self.rect.left >= WIDTH:
            current_lvl += 1
            self.rect.x = 0
        elif self.rect.right <= 0:
            current_lvl -= 1
            self.rect.x = WIDTH

        

        pre_x = self.rect.x
        pre_y = self.rect.y



        
        keys = pygame.key.get_pressed()
        
        
        if self.rect.bottom <= 575:
            self.rect.y += 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_SPACE]:
            self.rect.y -= 10
        

        collided_walls = pygame.sprite.spritecollide(self,walls,False)
        if collided_walls:
            self.rect.x = pre_x
            self.rect.y = pre_y
            if self.rect.bottom <= collided_walls[0].rect.top:
                if keys[pygame.K_d]:
                    self.rect.x += 5
                if keys[pygame.K_a]:
                    self.rect.x -= 5
            if self.rect.top >= collided_walls[0].rect.bottom:
                collided_walls[0].hardness -= 1
                self.rect.y += 100


        
                

target = GameSprite("logo.png",(120,120),(WIDTH/2,HEIGHT/2))    

    




main_character = Player("mario.png",(90,90),(100,530))

walls_1 = pygame.sprite.Group(  Wall("wall.png",(300,150),(400,250)),
Wall("wall.png",(300,150),(400,250)),
Wall("wall.png",(300,150),(700,450)),
)
walls_2 = pygame.sprite.Group(Wall("wall.png",(300,150),(100,100)),
Wall("wall.png",(300,150),(350,200)),
Wall("wall.png",(300,150),(600,350)))

enemy_flowers1 = pygame.sprite.Group( Enemy("angryflower.png",(85,85),(300,530)),
Enemy("angryflower.png",(85,85),(700,355)))

enemy_flowers2 = pygame.sprite.Group( Enemy("angryflower.png",(85,85),(200,330)),
Enemy("angryflower.png",(85,85),(550,355)))



current_lvl = 1
game_over = False
finish = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if current_lvl == 1:
        walls = walls_1
        enemy_flowers = enemy_flowers1
    elif current_lvl == 2:
        walls = walls_2
        enemy_flowers = enemy_flowers2
    elif current_lvl >= 3:
        walls = pygame.sprite.Group()
        enemy_flowers = pygame.sprite.Group()
    if not finish:
        window.blit(background, (0,0))
        main_character.reset()
        pygame.draw.rect(window,(255,0,0),main_character.rect,1)
        main_character.update(walls)
        enemy_flowers.draw(window)
        walls.draw(window)
        walls.update()
        if pygame.sprite.spritecollide(main_character,enemy_flowers,False):
            finish = True
            window.blit(text_lose,(WIDTH/2,HEIGHT/2))

        if current_lvl == 3:
            target.reset()
            if pygame.sprite.collide_rect(main_character,target):
                window.blit(text_win,(WIDTH/2,HEIGHT/2))
                finish = True

            
        
    
        


        pygame.display.update()
        clock.tick(FPS)
