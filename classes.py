import variable
import pygame
import funcoes

#Classe das paredes 
class Fixed_wall(pygame.sprite.Sprite):
    def __init__(self, assets, spawn_point):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['square_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_point[0] + (variable.WIDTH_SQUARE/2)
        self.rect.centery = spawn_point[1] + (variable.HEIGHT_SQUARE/2)

class Removable_wall(pygame.sprite.Sprite):
    def __init__(self, assets, spawn_point):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['tijolo']
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_point[0] + (variable.WIDTH_SQUARE/2)
        self.rect.centery = spawn_point[1] + (variable.HEIGHT_SQUARE/2)

#Classe Principal, cria todas as caracteristicas do player
class Character(pygame.sprite.Sprite):
    def __init__(self, player_sheet,posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        #animacoes do personagem
        player_sheet = pygame.transform.scale(player_sheet, (variable.WIDTH_SQUARE*4,variable.HEIGHT_SQUARE*4))
        spritesheet = funcoes.load_spritesheet(player_sheet, 4, 4)
        self.animations = {
            variable.STILL: spritesheet[4:5],
            variable.RIGHT: spritesheet[0:4],
            variable.DOWN: spritesheet[4:8],
            variable.LEFT: spritesheet[8:12],
            variable.UP: spritesheet[12:15],
        }
        self.state = variable.STILL
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

        #posicao do personagem
        self.rect.centerx = posx
        self.rect.bottom = posy
        self.speedx = 0
        self.speedy = 0

        #updata as acoes 
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 10
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000

    def update(self):
        #movimento
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #impede que o personagem entre na parede
        if self.rect.right > variable.RESOLUTION[0] - variable.WIDTH_SQUARE:
            self.rect.right = variable.RESOLUTION[0] - variable.WIDTH_SQUARE
        if self.rect.left < variable.WIDTH_SQUARE:
            self.rect.left = variable.WIDTH_SQUARE
        if self.rect.top < variable.HEIGHT_SQUARE:
            self.rect.top = variable.HEIGHT_SQUARE
        if self.rect.bottom > variable.RESOLUTION[1] - variable.HEIGHT_SQUARE:
            self.rect.bottom = variable.RESOLUTION[1] - variable.HEIGHT_SQUARE
        
        #anima o andar do personagem
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            self.animation = self.animations[self.state]

            if self.frame >= len(self.animation):
                self.frame = 0
            center = self.rect.center

            self.image = self.animation[self.frame]

            self.rect = self.image.get_rect()
            self.rect.center = center


    def drop_bomb(self, assets, all_sprites, all_jacas):
        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:

            self.last_shot = now
            
            new_jaca = Jaca(assets, self.rect.centerx, self.rect.centery)
            # all_sprites.add(new_jaca)
            all_jacas.add(new_jaca)
    
    


class Jaca(pygame.sprite.Sprite):
    def __init__(self, assets, px, py):
        pygame.sprite.Sprite.__init__(self)

        self.jaca_types = {
            "fechada":assets["jaca_fechada_img"], 
            "aberta1":assets["jaca_aberta1_img"], 
            "aberta2":assets["jaca_aberta2_img"],
            "aberta3":assets["jaca_aberta3_img"]}

        self.image = self.jaca_types['fechada']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.assets = assets

        self.x = px
        self.y = py
        self.rect.centerx = px
        self.rect.centery = py
        
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 300
        self.frame_ticks_exp = 2500

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        #transfoma no sprite da jaca aberta
        if elapsed_ticks > self.frame_ticks:
            self.image = self.jaca_types['aberta1']
            self.mask = pygame.mask.from_surface(self.image)
        
        if elapsed_ticks > self.frame_ticks*2:
            self.image = self.jaca_types['aberta2']
            self.mask = pygame.mask.from_surface(self.image)

        if elapsed_ticks > self.frame_ticks*3:
            self.image = self.jaca_types['aberta3']
            self.mask = pygame.mask.from_surface(self.image)

        #transforma no sprite da bomba
        if elapsed_ticks > self.frame_ticks*4:

            if elapsed_ticks > self.frame_ticks*4 + 250:
                self.image = self.assets['explojaca1_img']
            
            if elapsed_ticks > self.frame_ticks*4 + 500:
                self.image = self.assets['explojaca2_img']
            
            if elapsed_ticks > self.frame_ticks*4 + 750:
                self.image = self.assets['explojaca3_img']
            
            if elapsed_ticks > self.frame_ticks*4 + 1000:
                self.image = self.assets['explojaca4_img']

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.centerx = self.x
            self.rect.centery = self.y

        #elimina o sprite
        if elapsed_ticks > self.frame_ticks_exp:
            self.kill()