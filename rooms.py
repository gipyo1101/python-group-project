#gipyo
import pygame

def get_centre_floor(floor):
    floor_background = pygame.Surface((1280,720), pygame.SRCALPHA)
    for x in range(0, 700, 44):
        for y in range(0,400,20):
           floor_background.blit(floor, (x,y))

    for x in range(135,155,44):  
        for y in range(400,440, 20):
            floor_background.blit(floor, (x, y))

    for x in range(535,555,44):
        for y in range(400,440,20):
            floor_background.blit(floor, (x,y))
    
    return floor_background 

def get_A_room_floor(floor):
    A_floor_background = pygame.Surface((1280,720), pygame.SRCALPHA)
    for x in range(0,500,44):
        for y in range(0,400,20):
            A_floor_background.blit(floor,(x,y))
    
    for x in range(245,275,44):  
        for y in range(400,440,20):
            A_floor_background.blit(floor,(x, y))

    for x in range(500,550,44):
        for y in range(160,220,20):
            A_floor_background.blit(floor,(x,y))
    
    return A_floor_background

def get_exit_floor(floor):
    exit_floor_background = pygame.Surface((1280,720),pygame.SRCALPHA)
    for x in range(700,800,44):
        for y in range(100,280,20):
           exit_floor_background.blit(floor,(x,y))
    return exit_floor_background

def get_centre_wall(wall):
    wall_background = pygame.Surface((1000,80),pygame.SRCALPHA)
    for x in range(0,700,44):
        wall_background.blit(wall,(x,0))
    return wall_background

def get_A_room_wall(wall):
    A_wall_background =  pygame.Surface((1000,80),pygame.SRCALPHA)
    for x in range(0,500,44):
        A_wall_background.blit(wall,(x,0))
    return A_wall_background

def get_exit_wall(wall):
    exit_wall_background = pygame.Surface((1000,180),pygame.SRCALPHA)
    for x in range(704,800,44):
        for y in range(100,280,20):
            exit_wall_background.blit(wall,(x,100))
    return exit_wall_background

# Fajr
def get_B_room_floor(floor):
    B_floor_background = pygame.Surface((1280,720), pygame.SRCALPHA)

    for x in range(0,500,44):
        for y in range(0,400,20):
            B_floor_background.blit(floor,(x,y))

    for x in range(245,275,44):
        for y in range(400,440,20):
            B_floor_background.blit(floor,(x,y))

    for x in range(500,550,44):
        for y in range(160,220,20):
            B_floor_background.blit(floor,(x,y))

    return B_floor_background
def get_B_room_wall(wall):
    B_wall_background = pygame.Surface((1000,80), pygame.SRCALPHA)

    for x in range(0,500,44):
        B_wall_background.blit(wall,(x,0))

    return B_wall_background

def get_C_room_floor(floor):
    C_room_floor = floor.copy()
    return C_room_floor

#gipyo
class A_room():
    def __init__(self,floor, wall, bookshelf, diary, fireplace):
        self.floor = floor
        self.wall = wall
        self.bookshelf = bookshelf
        self.diary = diary
        self.fireplace = fireplace
        
        self.books = [("Fantasy", 1995), ("History", 1978),("Science Fiction", 2004),("Romance", 1982)]
        self.diary_open = False
        self.diary_page = 0
        self.diary_texts = ['I loved reading books in the library.',
               'Reading about the Second World War\nwas helpful for my history class at school.',
               'I wished I could use spells and magic\nlike the wizards in Harry Potter.', 
               'I often wondered what it would be like to\ntravel through space and discover new planets.',
               'I cried after reading tragic romance stories\nlike Romeo and Juliet. It broke my heart.',
               'My grandfather always told me,\n"The order of the years hides the truth."']
        self.diary_rect = pygame.Rect((600,340,30,20))
        self.inventory = []
    
    def event(self,event,character):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if character.player.colliderect(self.diary_rect):
                    self.diary_open = True
                
            if self.diary_open == True:
                if event.key == pygame.K_e:
                    self.diary_page += 1
                    if self.diary_page >= len(self.diary_texts):
                        self.diary_page = len(self.diary_texts) - 1
                if event.key == pygame.K_q:
                    self.diary_page -= 1
                    if self.diary_page < 0:
                        self.diary_page = 0

            if event.key == pygame.K_ESCAPE:
                self.diary_open = False
                self.diary_page = 0

    def A_room_screen(self,screen,character,diary_font):
        screen.blit(self.floor,(350,160))
        screen.blit(self.wall,(350,80))
        screen.blit(self.bookshelf,(330,200))
        screen.blit(self.bookshelf,(630,200))
        screen.blit(self.diary,(600,350))
        screen.blit(self.fireplace,(565,110))
        character.movement()
        character.graphic(screen)
        if self.diary_open == True:
            pygame.draw.rect(screen, 'white', (420, 120, 400, 400))
            self.diary_story = diary_font.render(self.diary_texts[self.diary_page], True, 'black')
            screen.blit(self.diary_story, (440,160))