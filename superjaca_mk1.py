import assets
import pygame
from funcoes import *
from classes import *
from variable import *

pygame.init()

# Define screen settings
window = pygame.display.set_mode((RESOLUTION))
pygame.display.set_caption('Super Jaca Man')

# Load all assets
assets = assets.load_assets()
char_pos = [[RESOLUTION[0]/DIVISIONS[0], RESOLUTION[1] - 40],
            [RESOLUTION[0] - 40, 80]]

# Set initial player settings
p1 = Character(assets["ash_img"], char_pos[0][0], char_pos[0][1])
p2 = Character(assets["pacman_img"], char_pos[1][0], char_pos[1][1])
    
# All sprite groups 
all_sprites = pygame.sprite.Group()
all_jacas = pygame.sprite.Group()
fixed_wall_sprites = pygame.sprite.Group()
all_explosions = pygame.sprite.Group()
all_players = pygame.sprite.Group()
removable_wall_sprites = pygame.sprite.Group()
all_walls = pygame.sprite.Group()

all_sprites.add(p1)
all_sprites.add(p2)

all_players.add(p1)
all_players.add(p2)


# Create fixed walls and the removable brick
all_sprites, fixed_wall_sprites, all_walls, removable_wall_sprites = build_walls(
    assets,
    all_sprites,
    fixed_wall_sprites,
    all_walls,
    removable_wall_sprites
)

game = True
clock = pygame.time.Clock()
FPS = 7
pygame.mixer.music.play(loops=-1)

# Start game loop 
while SCREEN == 0:
    # Start screen loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()  
        if event.type == pygame.KEYDOWN:
            SCREEN = 4
        
    window.blit(assets['initialScreen_img'], (0,0))
    pygame.display.update()

lista_sprite = [
    assets["ash_img"], 
    assets["pacman_img"],
    assets["rgb_img"],
    assets["ghost_img"],
    assets["link_img"],
    assets["bomberman_img"]
]

cord_lis = [
    [RESOLUTION[0]/DIVISIONS[0] + 1, RESOLUTION[1]/3 + 17],
    [RESOLUTION[0]/DIVISIONS[0]+127, RESOLUTION[1]/3 + 17],
    [RESOLUTION[0]/DIVISIONS[0]+337, RESOLUTION[1]/3 + 17],
    [RESOLUTION[0]/DIVISIONS[0]+463,RESOLUTION[1]/3 + 17]
]

pos_circle =  [int(RESOLUTION[0]/DIVISIONS[0]+1),int(RESOLUTION[1]/3 + 17)]
selection1 = ""

while SCREEN == 4:
    # Start screen loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

    window.blit(assets['choosescreen_img'], (0,0))

    for j, i in enumerate(lista_sprite):
        img = load_spritesheet(i, 4, 4)[4]
        img =  pygame.transform.scale(img, (HEIGHT_SQUARE + 15, WIDTH_SQUARE+ 15))
        if j == 0:
            window.blit(img, cord_lis[0])
            window.blit(img, cord_lis[2])
        elif j == 1:
            window.blit(img, cord_lis[1])
            window.blit(img, cord_lis[3])
        elif j == 2:
            window.blit(img, (cord_lis[0][0], cord_lis[0][1]+90))
            window.blit(img, (cord_lis[2][0], cord_lis[2][1]+90))
        elif j == 3:
            window.blit(img, (cord_lis[1][0], cord_lis[1][1]+90))
            window.blit(img, (cord_lis[3][0], cord_lis[3][1]+90))
        elif j == 4:
            window.blit(img, (cord_lis[0][0], cord_lis[0][1]+180))
            window.blit(img, (cord_lis[2][0], cord_lis[2][1]+180))
        elif j == 5:
            window.blit(img, (cord_lis[1][0], cord_lis[1][1]+180))
            window.blit(img, (cord_lis[3][0], cord_lis[3][1]+180))
    
    if buttonClick(cord_lis[0][0], cord_lis[0][1], HEIGHT_SQUARE + 15, WIDTH_SQUARE+ 15):
        pygame.draw.circle(window, (0, 0, 0), pos_circle, 10)
    
        
    pygame.display.update()



while SCREEN == 1:
    # Main game screen loop
    clock.tick(FPS) 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit() 

        if event.type == pygame.KEYDOWN:
            # Event player 1
            if event.key == pygame.K_l:
                p1.drop_bomb(assets, all_sprites, all_jacas)
                
            if event.key == pygame.K_LEFT:
                p1.state = LEFT
                p1.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_RIGHT:
                p1.state = RIGHT
                p1.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_UP:
                p1.state = UP
                p1.speedy -= WIDTH_SQUARE
                
            if event.key == pygame.K_DOWN:
                p1.state = DOWN
                p1.speedy += WIDTH_SQUARE
                

            # Event player 2
            if event.key == pygame.K_e:
                p2.drop_bomb(assets, all_sprites, all_jacas)
            if event.key == pygame.K_a:
                p2.state = LEFT
                p2.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_d:
                p2.state = RIGHT
                p2.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_w:
                p2.state = UP
                p2.speedy -= WIDTH_SQUARE
                
            if event.key == pygame.K_s:
                p2.state = DOWN
                p2.speedy += WIDTH_SQUARE
                    

        if event.type == pygame.KEYUP:

            # Event player 1
            if event.key == pygame.K_LEFT:
                p1.state = STILL
                p1.speedx += WIDTH_SQUARE

            if event.key == pygame.K_RIGHT:
                p1.state = STILL
                p1.speedx -= WIDTH_SQUARE

            if event.key == pygame.K_UP:
                p1.state = STILL
                p1.speedy += WIDTH_SQUARE

            if event.key == pygame.K_DOWN:
                p1.state = STILL
                p1.speedy -= WIDTH_SQUARE

            # Event player 2
            if event.key == pygame.K_a:
                p2.state = STILL
                p2.speedx += WIDTH_SQUARE
                
            if event.key == pygame.K_d:
                p2.state = STILL
                p2.speedx -= WIDTH_SQUARE
                
            if event.key == pygame.K_w:
                p2.state = STILL
                p2.speedy += WIDTH_SQUARE
                    
            if event.key == pygame.K_s:
                p2.state = STILL
                p2.speedy -= WIDTH_SQUARE
                

    all_sprites.update()
    all_jacas.update()

    # Detect collisions with Walls
    for player in all_players:
        for wall in all_walls:
            if cant_pass(player, wall):
                player.rect.y -= player.speedy
                player.rect.x -= player.speedx
                break

    # Detect collisions with bomb
    for player in all_players:
        
        for jaca in pygame.sprite.spritecollide(player, all_jacas, False, pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta1"] and jaca.image != jaca.jaca_types["fechada"] and jaca.image != jaca.jaca_types["aberta2"] and jaca.image != jaca.jaca_types["aberta3"]:
                if player == p1:
                    SCREEN = 2
                if player == p2:
                    SCREEN = 3
                
                player.kill()
                break
            else:
                # mover o cant_passs para dentro da classe player
                if cant_pass(player, jaca):
                    player.rect.y -= player.speedy
                    player.rect.x -= player.speedx

    # Check if removable walls were exploded
    for wall in removable_wall_sprites:
        for jaca in pygame.sprite.spritecollide(wall, all_jacas, False, pygame.sprite.collide_mask):
            if jaca.image != jaca.jaca_types["aberta1"] and jaca.image != jaca.jaca_types["fechada"] and jaca.image != jaca.jaca_types["aberta2"] and jaca.image != jaca.jaca_types["aberta3"]:
                wall.kill()
                
    window.fill((155, 220, 72))
    all_jacas.draw(window)
    all_sprites.draw(window)

    pygame.display.update() 

# Game over loops 
if SCREEN == 2:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        window.blit(assets['pe_na_jaca2'], (0,0))  
        pygame.display.update()
        
if SCREEN == 3:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        window.blit(assets['pe_na_jaca1'], (0,0))
        pygame.display.update()
