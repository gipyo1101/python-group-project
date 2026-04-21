import pygame
#from Game_assets import Character

pygame.init()
screen = pygame.display.set_mode((1280,720))
title_font = pygame.font.SysFont(None,100)
button_font = pygame.font.SysFont(None,60)
dialogue_font = pygame.font.SysFont(None,50)

# menu
start_button = pygame.Rect((410,300,400,100)) # (x,y,width,height)
quit_button = pygame.Rect((410,450,400,100))
menu_background = pygame.image.load('images/menu image1.jpeg').convert_alpha()
menu_background = pygame.transform.scale(menu_background, (1280, 720))

# rooms and rect
rooms = {'centre':['A','B','C','D','exit'], 'A':['centre','C'],
                'B':['centre','D'], 'C':['centre','A'], 'D':['centre','B'], 'exit':['centre']}
current_room = 'centre'
room_A = pygame.Rect(410, 78, 52, 63)
backroom_A = pygame.Rect((675, 835, 45, 45))
room_B = pygame.Rect(405,535,20,64)
room_C = pygame.Rect(415, 155, 22, 10)
room_D = pygame.Rect(415, 155, 22, 10)
centre_up = pygame.Rect(300,50,700,50)



# floor 
floor_wall = pygame.image.load('images/floors_LRK.png').convert_alpha()
floor = pygame.Surface((44,20), pygame.SRCALPHA)
floor.blit(floor_wall, (0,0), ((22,82,44,20)))
floor_background = pygame.Surface((1280,720),pygame.SRCALPHA)
A_floor_background = pygame.Surface((1280,720),pygame.SRCALPHA)
exit_floor = pygame.Surface((1280,720),pygame.SRCALPHA)
def centre_floor():
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
centre = centre_floor()

def A_room_floor():
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

A_floor = A_room_floor()

for x in range(700,800,44):
    for y in range(100,280,20):
        exit_floor.blit(floor,(x,y))
    

# wall
wall = pygame.Surface((44,80),pygame.SRCALPHA)
wall.blit(floor_wall,(0,0),(22,20,44,80))
wall = pygame.transform.scale(wall,(44,150))
wall_background = pygame.Surface((1000,80),pygame.SRCALPHA)
exit_wall = pygame.Surface((1000,180),pygame.SRCALPHA)
A_wall_background =  pygame.Surface((1000,80),pygame.SRCALPHA)

for x in range(0,700,44):
    wall_background.blit(wall,(x,0))

for x in range(704,800,44):
    exit_wall.blit(wall,(x,100))
    
    
def A_room_wall():
    for x in range(0,500,44):
        A_wall_background.blit(wall,(x,0))
    return A_wall_background

A_wall = A_room_wall()
    

# door
doors = pygame.image.load('images/doors_LRK.png').convert_alpha()
door = pygame.Surface((40,56),pygame.SRCALPHA)
door.blit(doors,(0,0),(102,16,40,56))
door = pygame.transform.scale(door,(52,64))


# furniture set
furniture_set = pygame.image.load('images/furniture set.png').convert_alpha()
diary = pygame.Surface((17,11),pygame.SRCALPHA)
diary.blit(furniture_set,(0,0),(327,115,17,11))
diary_scale = pygame.transform.scale(diary,(30,20))

bookshelf_set = pygame.image.load('images/bookshelf_LRK.png').convert_alpha()
bookshelf = pygame.Surface((134,126),pygame.SRCALPHA)
bookshelf.blit(bookshelf_set, (0, 0), (0, 0, 134, 126))
bookshelf_scale = pygame.transform.scale(bookshelf,(260,260))



class Character:
    def __init__(self,x,y,speed):
        game_character = pygame.image.load('images/game_character.png').convert_alpha() # because of transparency
        self.character_image = pygame.Surface((16,16), pygame.SRCALPHA)
        self.character_image.blit(game_character,(0,0),(0,16,16,16))
        self.character_image.set_colorkey((0,0,0))
        self.character = pygame.transform.scale(self.character_image, (45,45))
        self.x = x
        self.y = y
        self.speed = speed
        self.player = pygame.Rect(self.x,self.y,45,45)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.x -= self.speed # arrow keys
        if keys[pygame.K_RIGHT]: self.x += self.speed
        if keys[pygame.K_DOWN]: self.y += self.speed
        if keys[pygame.K_UP]: self.y -= self.speed

        if self.player.colliderect(centre_up):
            self.player.x = self.x

        '''if self.x < 275: self.x = 275   # limits 
        if self.x > 935: self.x = 935
        if self.y < 140: self.y = 140
        if self.y > 515: self.y = 515'''
        
        self.player.x = self.x      # rect to collide
        self.player.y = self.y
        
        
    
    def graphic(self,screen):
        screen.blit(self.character, self.player)     
girl = Character(580,320,0.7)
girl_A = Character(493,530,0.7)

story = ['I need to escape this house!','The exit is locked.', 'I should find the key to get out of here.']
story_index = 0
text_box = pygame.Rect((140,500,1000,120))
current_state = 'menu'
running = True

# room



while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse):
                current_state = 'story'
                story_index = 0
            if quit_button.collidepoint(mouse):
                running = False
            else:
                None          
        if current_state == 'story':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    story_index += 1
                    if story_index >= len(story):
                        current_state = 'game'
                else:
                    None
    if current_state == 'menu':
        screen.blit(menu_background,(0,0))
        pygame.draw.rect(screen, 'white', start_button)  #(x, y, width, height)
        pygame.draw.rect(screen, 'white', quit_button)
        title_text = title_font.render('Escape the House',True,'white')
        start = button_font.render("Start", True,'black')
        start_rect = start.get_rect(center = start_button.center)
        quit = button_font.render("Quit",True,'black')
        quit_rect = quit.get_rect(center = quit_button.center)
        screen.blit(start,start_rect) 
        screen.blit(quit,quit_rect)
        screen.blit(title_text,(340, 150)) #(x,y)

    elif current_state == 'story':
        pygame.draw.rect(screen, 'white', text_box)
        dialogue = dialogue_font.render(story[story_index],True,'black')
        dialogue_rect = dialogue.get_rect(center = text_box.center)
        screen.blit(dialogue,dialogue_rect)
        
    elif current_state == 'game':
        screen.blit(centre,(275,160))
        screen.blit(exit_floor,(279.8,160))
        screen.blit(wall_background,(275,80))
        screen.blit(exit_wall,(275,80))
        screen.blit(door,(400,108))
        screen.blit(door,(800,108))
        
        girl.movement()
        girl.graphic(screen)
     
        if girl.player.colliderect(room_A):
            current_state = 'A'
        #'A' room has a stopped clock and there is a message on the clock that 
        # 'the passage of years is important.' so there are four bookcases and when 
        # the character collide with bookcases, the book 
        # and the year of the book are shown on the screen.
        #  Through this, we can know that the password of safe is the 
        # last digit of each book's year, arranged in chronological order. And then 
        # when we open the safe, we gain the key of the next room ('C' room).
        
    elif current_state == 'A':
        screen.blit(A_floor,(350,160))
        screen.blit(A_wall,(350,80))
        screen.blit(bookshelf_scale,(320,200))
        screen.blit(bookshelf_scale,(630,200))
        screen.blit(diary_scale,(600,350))
        girl_A.movement()
        girl_A.graphic(screen)
        if girl.player.colliderect(backroom_A):
            current_state = 'game'
            girl.x = 580
            girl.y = 140

    pygame.display.flip()
pygame.quit()