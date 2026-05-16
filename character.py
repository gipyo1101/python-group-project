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
#gipyo

    #Hashim
    def set_position(self,x,y):
        self.x = x
        self.y = y
        self.player.x = round(self.x)
        self.player.y = round(self.y)
    
    def feet_hitbox(self):
        return pygame.Rect( round(self.x) + 12,
            round(self.y) + 34, 21, 9)
    
    def movement(self, walkable = None, barriers = None):
        if walkable is None:
            walkable = []

        if barriers is None:
            barriers = []

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]: 
            dx -= self.speed # arrow keys
        if keys[pygame.K_RIGHT]: 
            dx += self.speed
        if keys[pygame.K_DOWN]: 
            dy += self.speed
        if keys[pygame.K_UP]: 
            dy -= self.speed

        def position_is_allowed():
            feet = self.feet_hitbox()

            if walkable:
                on_floor = False

                for area in walkable:
                    if area.collidepoint(feet.center):
                        on_floor = True

                if not on_floor:
                    return False

            for barrier in barriers:
                if feet.colliderect(barrier):
                    return False

            return True
        
        # x axis movement
        old_x = self.x
        self.x += dx
        self.player.x = round(self.x)

        if not position_is_allowed():
            self.x = old_x
            self.player.x = round(self.x)

        # y axis movement
        old_y = self.y
        self.y += dy
        self.player.y = round(self.y)

        if not position_is_allowed():
            self.y = old_y
            self.player.y = round(self.y)
    #Hashim
    
    #gipyo
    def graphic(self,screen):
        screen.blit(self.character, self.player) 
    #gipyo