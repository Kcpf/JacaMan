import assets
import variable
import pygame
import funcoes

class Fixed_wall(pygame.sprite.Sprite):
    def __init__(self, assets, spawn_point):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['square_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_point[0] + (variable.WIDTH_SQUARE/2)
        self.rect.centery = spawn_point[1] + (variable.HEIGHT_SQUARE/2)


class Character(pygame.sprite.Sprite):
    def __init__(self, player_sheet):
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (variable.WIDTH_SQUARE*4,variable.HEIGHT_SQUARE*4))

        # Define sequências de sprites de cada animação
        spritesheet = funcoes.load_spritesheet(player_sheet, 4, 4)
        
        self.animations = {
            # variable.STILL: player_sheet[4],
            variable.RIGHT: spritesheet[0:4],
            variable.DOWN: spritesheet[4:8],
            variable.LEFT: spritesheet[8:12],
            variable.UP: spritesheet[12:15],
        }
        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = variable.UP
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Ponto de spwan
        self.rect.centerx = variable.RESOLUTION[0]/variable.DIVISIONS[0]
        self.rect.bottom = variable.RESOLUTION[1] - 40
        self.speedx = 0
        self.speedy = 0

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 10

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > variable.RESOLUTION[0] - variable.WIDTH_SQUARE:
            self.rect.right = variable.RESOLUTION[0] - variable.WIDTH_SQUARE
        if self.rect.left < variable.WIDTH_SQUARE:
            self.rect.left = variable.WIDTH_SQUARE
        if self.rect.top < variable.HEIGHT_SQUARE:
            self.rect.top = variable.HEIGHT_SQUARE
        if self.rect.bottom > variable.RESOLUTION[1] - variable.HEIGHT_SQUARE:
            self.rect.bottom = variable.RESOLUTION[1] - variable.HEIGHT_SQUARE

        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center