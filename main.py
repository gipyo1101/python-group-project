import pygame
from character import Character
from rooms import A_room
from assets import get_doors, get_diary, get_bookshelf, get_fireplace, get_walls, get_floors
from rooms import get_centre_floor, get_A_room_floor, get_exit_floor, get_centre_wall, get_A_room_wall, get_exit_wall
from rooms import get_B_room_floor, get_C_room_floor, get_B_room_wall

#gipyo 
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
B_room_floor = get_B_room_floor(floor) #fajr
C_room_floor = get_C_room_floor(floor) #fajr
exit_floor = get_exit_floor(floor)
centre_wall = get_centre_wall(wall)
exit_wall = get_exit_wall(wall)
A_room_wall = get_A_room_wall(wall)
B_room_wall = get_A_room_wall(wall) # fajr 
C_room_wall = get_centre_wall(wall) # fajr
room_a = A_room(A_room_floor, A_room_wall, bookshelf, diary, fireplace)
#gipyo

#gipyo
title_font = pygame.font.SysFont(None,100)
button_font = pygame.font.SysFont(None,60)
dialogue_font = pygame.font.SysFont(None,50)
diary_font = pygame.font.SysFont(None, 30)
#gipyo

#gipyo
start_button = pygame.Rect((410,300,400,100)) # (x,y,width,height)
quit_button = pygame.Rect((410,450,400,100))
menu_background = pygame.image.load('images/menu image1.jpeg').convert_alpha()
menu_background = pygame.transform.scale(menu_background, (1280, 720))
#gipyo

#gipyo
rooms = {'centre':['A','B','C','exit'], 'A':['centre','C'],
                'B':['centre'], 'C':['centre','A'], 'exit':['centre']}
current_room = 'centre'
room_A_rect = pygame.Rect(420, 130, 30, 40)
backroom_A_rect = pygame.Rect(590, 600, 55, 30)
bookshelf_1_rect = pygame.Rect(360, 320, 90, 30)
bookshelf_2_rect = pygame.Rect(480, 320, 90, 30)
bookshelf_3_rect = pygame.Rect(660, 320, 90, 30)
bookshelf_4_rect = pygame.Rect(780, 320, 90, 30)
bookshelf_5_rect = pygame.Rect(360, 440, 90, 30)
bookshelf_6_rect = pygame.Rect(480, 440, 90, 30)
bookshelf_7_rect = pygame.Rect(660, 440, 90, 30)
bookshelf_8_rect = pygame.Rect(780, 440, 90, 30)
#gipyo

#Hashim
room_B_rect = pygame.Rect(410,560,44,40)
room_C_rect = pygame.Rect(820,130,30,40)
backroom_B = pygame.Rect(595, 150, 44, 40)
backroom_C = pygame.Rect(595, 560, 44, 40)

centre_walkable = [
    pygame.Rect(275, 160, 704, 400),   # main centre room floor
    pygame.Rect(410, 560, 44, 40),     # bottom left doorway
    pygame.Rect(810, 560, 44, 40),     # bottom right doorway
    pygame.Rect(940, 260, 60, 180),    # connector to right side
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
#Hashim

#gipyo
centre_up = pygame.Rect(300,50,700,50)
girl = Character(580,320,1)
girl_A = Character(600,530,0.7)
# gipyo

#Hashim
girl_B = Character(595,510,1)
girl_C = Character(595,510,1)
#Hashim

# fajr
piece_count = 0
map_puzzle_open = False 
map_puzzle_done = False
map_message = ''
# fajr
                
# gipyo
story = ['I need to escape this house!','The exit is locked.', 'I should find the key to get out of here.']
story_index = 0
text_box = pygame.Rect((140,500,1000,120))
current_state = 'menu'
running = True
# gipyo

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
                room_a.event(event,girl_A)
                
                
            #Fajr
            if current_state == 'B': 
                if event.key == pygame.K_e:
                    if girl_A.player.colliderect(map_place):
                        map__puzzle_open = True
                        count = 0
                        text = 'NEW TEXT TEST'
                        if event.key == pygame.K_SPACE and map__puzzle_open:
                            count += 1
                
                        if count == 1:
                            text = 'First piece placed.'
                
                        elif count == 2:
                            text = 'The picture looks clearer.'
               
                        elif count == 3:
                            text = 'It looks like a map.'
                
                        elif count >= 4:
                            text = 'X mark found. The number is 4.'

    #gipyo
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
    #gipyo

    #gipyo
    elif current_state == 'story': 
        pygame.draw.rect(screen, 'white', text_box)
        dialogue = dialogue_font.render(story[story_index],True,'black')
        dialogue_rect = dialogue.get_rect(center = text_box.center)
        screen.blit(dialogue,dialogue_rect)
    #gipyo

    #gipyo
    elif current_state == 'game': 
        if current_room == 'centre' and 'centre' in rooms: 
            screen.blit(centre_floor,(275,160))
            screen.blit(exit_floor,(279.8,160))
            screen.blit(centre_wall,(275,80))
            screen.blit(exit_wall,(275,80))
            screen.blit(door,(400,108))
            screen.blit(door,(800,108))
            #gipyo

            #Hashim
            # debug rectangles, remove later
            #for area in centre_walkable:
                #pygame.draw.rect(screen, 'green', area, 2)
                #pygame.draw.rect(screen, 'blue', room_A_rect, 2)
                #pygame.draw.rect(screen, 'blue', room_C_rect, 2)
                #pygame.draw.rect(screen, 'blue', room_B_rect, 2)
                #pygame.draw.rect(screen, 'purple', girl.feet_hitbox(), 2)

            girl.movement(centre_walkable)
            girl.graphic(screen)

            if girl.feet_hitbox().colliderect(room_A_rect):
                    current_state = 'A'
                    girl_A.set_position(595,510)

            if girl.feet_hitbox().colliderect(room_C_rect):
                current_state = 'C'
                girl_C.set_position(595,510)

            if girl.feet_hitbox().colliderect(room_B_rect):
                current_state = 'B'
                girl_B.set_position(595,170)
            #Hashim
     
                girl_A.x = 600
                girl_A.y = 530
            
    #gipyo
    elif current_state == 'A':
        if 'A' in rooms['centre']:
            room_a.A_room_screen(screen,girl_A,diary_font,dialogue_font)
            
            

            if girl_A.feet_hitbox().colliderect(backroom_A_rect) and 'centre' in rooms['A']:
                current_state = 'game'
                girl.set_position(410,160)
            if room_a.A_room_story == False and room_a.diary_open == False:
                girl_A.movement(A_walkable)
                girl_A.graphic(screen)
        
            for area in A_walkable:
                #pygame.draw.rect(screen, 'green', area, 2)
                #pygame.draw.rect(screen, 'blue', backroom_A_rect, 2)
                pygame.draw.rect(screen,'blue',room_a.diary_rect,2)
                #pygame.draw.rect(screen, 'purple', girl_A.feet_hitbox(), 2)
                pygame.draw.rect(screen, 'blue', bookshelf_1_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_2_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_3_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_4_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_5_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_6_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_7_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_8_rect, 2)
               

       

    # Fajr
    elif current_state == 'B':
        screen.blit(B_room_floor, (350, 160))
        screen.blit(B_room_wall, (350, 80))

        pygame.draw.rect(screen, 'brown', map_place) 

        old_x = girl_A.x
        old_y = girl_A.y

        girl_A.movement()

        main_room = pygame.Rect(430, 160, 430, 370)

        in_main = girl_A.player.colliderect(main_room)

        if not in_main:
            girl_A.x = old_x
            girl_A.y = old_y

        if girl_A.player.colliderect(map_place):
            girl_A.x = old_x
            girl_A.y = old_y

        if girl_A.player.colliderect(map_place):
            map_puzzle_open = True
            text = 'You found a torn picture. Press SPACE to put the pieces together.'

        if map_puzzle_open:
            pygame.draw.rect(screen, 'white', (200, 500, 800, 80))
            msg = dialogue_font.render(text, True, 'black')
            screen.blit(msg, (220, 520))

        if girl_A.player.colliderect(backroom_B):
            current_state = 'game'
            girl.x = 580
            girl.y = 140

        girl_A.graphic(screen)

    #Hashim
    elif current_state == 'C':
        screen.blit(C_room_floor,(0,0))
    
        
    pygame.display.flip()
pygame.quit()
