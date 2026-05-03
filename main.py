import pygame
from character import Character
from assets import get_doors, get_diary, get_bookshelf, get_fireplace, get_walls, get_floors
from rooms import get_centre_floor, get_A_room_floor, get_exit_floor, get_centre_wall, get_A_room_wall, get_exit_wall
from rooms import get_B_room_floor, get_C_room_floor, get_B_room_wall

pygame.init()
screen = pygame.display.set_mode((1280,720))
floor = get_floors()
wall = get_walls()
door = get_doors()
diary = get_diary()
bookshelf = get_bookshelf()
fireplace = get_fireplace()
centre_floor = get_centre_floor(floor)
A_room_floor = get_A_room_floor(floor)
B_room_floor = get_B_room_floor(floor)
C_room_floor = get_C_room_floor(floor)
exit_floor = get_exit_floor(floor)
centre_wall = get_centre_wall(wall)
exit_wall = get_exit_wall(wall)
A_room_wall = get_A_room_wall(wall)
B_room_wall = get_B_room_wall(wall) # fajr 
C_room_wall = get_centre_wall(wall)
 

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

# Door / transition triggers
room_A = pygame.Rect(400, 150, 52, 25)
room_C = pygame.Rect(790, 145, 70, 45)

room_B = pygame.Rect(410, 560, 44, 40)
room_D = pygame.Rect(810, 560, 44, 40)

backroom_A = pygame.Rect(595, 560, 44, 40)
backroom_B = pygame.Rect(595, 150, 44, 40)
backroom_C = pygame.Rect(595, 560, 44, 40)

# Areas where the player is allowed to walk
centre_walkable = [
    pygame.Rect(275, 160, 704, 400),   # main centre room floor
    pygame.Rect(410, 560, 44, 40),     # bottom left doorway
    pygame.Rect(810, 560, 44, 40),     # bottom right doorway
    pygame.Rect(940, 280, 60, 180),    # connector to right side
    pygame.Rect(980, 260, 100, 180),   # right side corridor
]

A_walkable = [
    pygame.Rect(350, 160, 528, 400),   # main room A floor
    pygame.Rect(595, 560, 44, 40),     # bottom doorway
    pygame.Rect(878, 320, 60, 60),     # right side extension
]

B_walkable = [
    pygame.Rect(350, 160, 528, 400),   # main room B floor
    pygame.Rect(595, 150, 44, 40),     # top doorway
    pygame.Rect(878, 320, 60, 60),     # right side extension
]

C_walkable = [
    pygame.Rect(350, 160, 528, 400),   # main room C floor
    pygame.Rect(595, 560, 44, 40),     # bottom doorway
]

# Object rectangles
diary_rect = pygame.Rect(600, 340, 30, 20)
map_place = pygame.Rect(560, 340, 120, 80)

# Characters
girl = Character(580,320,0.7)
girl_A = Character(595,510,0.7)
girl_B = Character(595,510,0.7)
girl_C = Character(595,510,0.7)

# fajr
piece_count = 0
map_puzzle_open = False 
map_puzzle_done = False
map_message = ''

#gipyo
story = ['I need to escape this house!','The exit is locked.', 'I should find the key to get out of here.']
story_index = 0
diary_open = False
diary_texts = ['I loved reading books in the library.',
               'Reading about the Second World War was helpful for my history class at school.',
               'I wished I could use spells and magic like the wizards in Harry Potter.', 
               'I often wondered what it would be like to travel through space and discover new planets.',
               'I cried after reading tragic romance stories like Romeo and Juliet. It broke my heart.',
               'My grandfather always told me, "The order of the years hides the truth."']
books = [("Fantasy", 1995), ("History", 1978),("Science Fiction", 2004),("Romance", 1982)]

text_box = pygame.Rect((140,500,1000,120))
current_state = 'menu'
running = True

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
                        current_room = 'centre'
                else:
                    None

        if event.type == pygame.KEYDOWN:
            if current_state == 'A':
                if event.key == pygame.K_f:
                    if girl_A.player.colliderect(diary_rect):
                        diary_open = True
                
                if event.key == pygame.K_ESCAPE:
                        diary_open = False
                
                    

            if current_state == 'B': # Fajr

                if event.key == pygame.K_e:
                    if girl_B.feet_hitbox().colliderect(map_place):
                        map_puzzle_open = True
                        if not map_puzzle_done:
                            map_message = 'You found a torn picture. Press SPACE to put the pieces together.'

                if event.key == pygame.K_SPACE and map_puzzle_open and not map_puzzle_done:
                    piece_count += 1

                    if piece_count == 1:
                        map_message = 'First piece placed.'

                    elif piece_count == 2:
                        map_message = 'The picture looks clearer.'

                    elif piece_count == 3:
                        map_message = 'It looks like a map.'

                    elif piece_count >= 4:
                        map_puzzle_done = True
                        map_message = 'X mark found. The number is 4.'


    if current_state == 'menu': # gipyo
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

    elif current_state == 'story': # gipyo
        pygame.draw.rect(screen, 'white', text_box)
        dialogue = dialogue_font.render(story[story_index],True,'black')
        dialogue_rect = dialogue.get_rect(center = text_box.center)
        screen.blit(dialogue,dialogue_rect)
        
    elif current_state == 'game':
        if current_room == 'centre' and 'centre' in rooms: #gipyo
            screen.blit(centre_floor,(275,160))
            screen.blit(exit_floor,(279.8,160))
            screen.blit(centre_wall,(275,80))
            screen.blit(exit_wall,(275,80))
            screen.blit(door,(400,108))
            screen.blit(door,(800,108))
        
            # debug rectangles, remove later
            for area in centre_walkable:
                pygame.draw.rect(screen, 'green', area, 2)

            pygame.draw.rect(screen, 'blue', room_A, 2)
            pygame.draw.rect(screen, 'blue', room_C, 2)
            pygame.draw.rect(screen, 'blue', room_B, 2)
            pygame.draw.rect(screen, 'purple', girl.feet_hitbox(), 2)

            girl.movement(centre_walkable)
            girl.graphic(screen)

            if girl.feet_hitbox().colliderect(room_A):
                current_state = 'A'
                girl_A.set_position(595,510)

            if girl.feet_hitbox().colliderect(room_C):
                current_state = 'C'
                girl_C.set_position(595,510)

            if girl.feet_hitbox().colliderect(room_B):
                current_state = 'B'
                girl_B.set_position(595,170)

    elif current_state == 'A':
        if 'A' in rooms['centre']:  # gipyo
            screen.blit(A_room_floor,(350,160))
            screen.blit(A_room_wall,(350,80))
            screen.blit(bookshelf,(330,200))
            screen.blit(bookshelf,(630,200))
            screen.blit(diary,(600,350))
            screen.blit(fireplace,(565,110))
        # debug rectangles, remove later
        for area in A_walkable:
            pygame.draw.rect(screen, 'green', area, 2)

        pygame.draw.rect(screen, 'blue', backroom_A, 2)
        pygame.draw.rect(screen, 'purple', girl_A.feet_hitbox(), 2)

        girl_A.movement(A_walkable)
        girl_A.graphic(screen)

        if girl_A.feet_hitbox().colliderect(backroom_A):
            current_state = 'game'
            girl.set_position(405,165)

            if diary_open == True:
                pygame.draw.rect(screen, 'white', (420, 120, 400, 400))
    
                

            
               

        def bubble_sort_years(books):
            repeated_nums = len(books) - 1
            for i in range(repeated_nums, 0, -1):
                for j in range(i):
                    if books[j][1] > books[j+1][1]:
                        temp = books[j]
                        books[j] = books[j+1]
                        books[j+1] = temp
    
            return books
        
        
        def get_password(books):
            books_list = bubble_sort_years(books)
            password = ''.join(str(year)[-1] for pw, year in books_list)
            return password

    elif current_state == 'B': # Fajr
        screen.blit(B_room_floor, (350, 160))
        screen.blit(B_room_wall, (350, 80))

        # cover the little bottom protruding floor bit
        pygame.draw.rect(screen, 'black', (590, 560, 60, 80))

        # draw a door at the top
        screen.blit(door, (595, 108))

        pygame.draw.rect(screen, 'brown', map_place)

        # debug rectangles, remove later
        for area in B_walkable:
            pygame.draw.rect(screen, 'green', area, 2)

        pygame.draw.rect(screen, 'blue', backroom_B, 2)
        pygame.draw.rect(screen, 'purple', girl_B.feet_hitbox(), 2)

        girl_B.movement(B_walkable, [map_place])
        girl_B.graphic(screen)

        if map_puzzle_open:
            pygame.draw.rect(screen, 'white', (200, 500, 800, 80))
            msg = dialogue_font.render(map_message, True, 'black')
            screen.blit(msg, (220, 520))

        if girl_B.feet_hitbox().colliderect(backroom_B):
            current_state = 'game'
            girl.set_position(410, 485)

    elif current_state == 'C':
        # Placeholder room C for now
        screen.blit(A_room_floor,(350,160))
        screen.blit(A_room_wall,(350,80))

        # simple placeholder object
        pygame.draw.rect(screen, 'grey', (570,300,120,80))

        # debug rectangles, remove later
        for area in C_walkable:
            pygame.draw.rect(screen, 'green', area, 2)

        pygame.draw.rect(screen, 'blue', backroom_C, 2)
        pygame.draw.rect(screen, 'purple', girl_C.feet_hitbox(), 2)

        girl_C.movement(C_walkable)
        girl_C.graphic(screen)

        placeholder_text = dialogue_font.render('Room C placeholder', True, 'white')
        screen.blit(placeholder_text, (430,620))

        if girl_C.feet_hitbox().colliderect(backroom_C):
            current_state = 'game'
            girl.set_position(805,165)
    
        
    pygame.display.flip()
pygame.quit()
