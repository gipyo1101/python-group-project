#gipyo
import pygame

class Character:
    def __init__(self,x,y,speed):
        game_character = pygame.image.load('images/game_character.png').convert_alpha() # because of transparency
        self.character_image = pygame.Surface((16,16), pygame.SRCALPHA)
        self.character_image.blit(game_character,(0,0),(0,16,16,16))
        self.character_image.set_colorkey((0,0,0))
        self.character = pygame.transform.scale(self.character_image, (40,40))
        self.x = x
        self.y = y
        self.speed = speed
        self.player = pygame.Rect(self.x,self.y,40,40)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.x -= self.speed # arrow keys
        if keys[pygame.K_RIGHT]: self.x += self.speed
        if keys[pygame.K_DOWN]: self.y += self.speed
        if keys[pygame.K_UP]: self.y -= self.speed

        #if self.player.colliderect(centre_up = pygame.Rect(300,50,700,50)):
            #self.player.x = self.x

        '''if self.x < 275: self.x = 275   # limits 
        if self.x > 935: self.x = 935
        if self.y < 140: self.y = 140
        if self.y > 515: self.y = 515'''
        
        self.player.x = self.x      # rect to collide
        self.player.y = self.y
        
        
    
    def graphic(self,screen):
        screen.blit(self.character, self.player)  