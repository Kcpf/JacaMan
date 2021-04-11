import variable
import pygame
import funcoes

class Wall(pygame.sprite.Sprite):
    def __init__(self, spawn_point):
        """Create an instance of a Wall

        Keyword arguments:
        spawn_point -- location of spawn (x, y)
        """

        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_point[0] + (variable.WIDTH_SQUARE/2)
        self.rect.centery = spawn_point[1] + (variable.HEIGHT_SQUARE/2)

class Fixed_wall(Wall):
    def __init__(self, assets, spawn_point):
        """Create an instance of Fixed walls

        Keyword arguments:
        assets -- image dictionary
        spawn_point -- location of spawn (x, y)
        """

        self.image = assets['square_img']
        Wall.__init__(self, spawn_point)


class Removable_wall(Wall):
    def __init__(self, assets, spawn_point):
        """Create an instance of Removable walls

        Keyword arguments:
        assets -- image dictionary
        spawn_point -- location of spawn (x, y)
        """

        self.image = assets['tijolo']
        Wall.__init__(self, spawn_point)


class Character(pygame.sprite.Sprite):
    def __init__(self, player_sheet, posx, posy):
        """Create an instance of the Player

        Keyword arguments:
        player_sheet -- player's spritesheet
        posx -- location of spawn (x)
        posy -- location of spawn (y)
        """

        pygame.sprite.Sprite.__init__(self)

        # Player animations
        player_sheet = pygame.transform.scale(
            player_sheet,
            (variable.WIDTH_SQUARE*4, variable.HEIGHT_SQUARE*4)
        )

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

        # Player position
        self.rect.centerx = posx
        self.rect.bottom = posy
        self.speedx = 0
        self.speedy = 0

        # Action times
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 10
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000

    def update(self):
        """Update player characteristics
        """

        # Movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Check if player is passing external fixed blocks
        if self.rect.right > variable.RESOLUTION[0] - variable.WIDTH_SQUARE:
            self.rect.right = variable.RESOLUTION[0] - variable.WIDTH_SQUARE
        if self.rect.left < variable.WIDTH_SQUARE:
            self.rect.left = variable.WIDTH_SQUARE
        if self.rect.top < variable.HEIGHT_SQUARE:
            self.rect.top = variable.HEIGHT_SQUARE
        if self.rect.bottom > variable.RESOLUTION[1] - variable.HEIGHT_SQUARE:
            self.rect.bottom = variable.RESOLUTION[1] - variable.HEIGHT_SQUARE

        # Walking animation
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
        """Drop bomb method

        Keyword arguments:
        assets -- image dictionary
        all_sprites -- All sprites group
        all_jacas -- All jackfruits group
        """

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:

            self.last_shot = now

            new_jaca = Jaca(assets, self.rect.centerx, self.rect.centery)
            all_jacas.add(new_jaca)


class Jaca(pygame.sprite.Sprite):
    def __init__(self, assets, px, py):
        """Create jackfruit instance

        Keyword arguments:
        assets -- image dictionary
        px -- Bomb position (x)
        py -- Bomb position (y)
        """

        pygame.sprite.Sprite.__init__(self)

        self.jaca_types = {
            "fechada": assets["jaca_fechada_img"],
            "aberta1": assets["jaca_aberta1_img"],
            "aberta2": assets["jaca_aberta2_img"],
            "aberta3": assets["jaca_aberta3_img"]}

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
        """Update bomb characteristics
        """

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        # Transform to open jackfruit
        if elapsed_ticks > self.frame_ticks:
            self.image = self.jaca_types['aberta1']
            self.mask = pygame.mask.from_surface(self.image)

        if elapsed_ticks > self.frame_ticks*2:
            self.image = self.jaca_types['aberta2']
            self.mask = pygame.mask.from_surface(self.image)

        if elapsed_ticks > self.frame_ticks*3:
            self.image = self.jaca_types['aberta3']
            self.mask = pygame.mask.from_surface(self.image)

        # Transform to explosion sprite
        if elapsed_ticks > self.frame_ticks*4:

            if elapsed_ticks > self.frame_ticks*4 + 250:
                self.assets['explosion_sound'].play()
                self.image = self.assets['explojaca1_img']


            if elapsed_ticks > self.frame_ticks*4 + 500:
                self.image = self.assets['explojaca2_img']

            # self.assets[EXPLOSION_SOUNDS].play()

            if elapsed_ticks > self.frame_ticks*4 + 750:
                self.image = self.assets['explojaca3_img']

            if elapsed_ticks > self.frame_ticks*4 + 1000:
                self.image = self.assets['explojaca4_img']

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.centerx = self.x
            self.rect.centery = self.y

        # Kill Sprite after ticks
        if elapsed_ticks > self.frame_ticks_exp:
            self.kill()
