import pygame
from character import Character
from assets import get_doors, get_diary, get_bookshelf, get_fireplace, get_walls, get_floors
from rooms import get_centre_floor, get_A_room_floor, get_C_room_floor, get_exit_floor, get_centre_wall, get_A_room_wall, get_B_room_wall, get_exit_wall
from rooms import get_B_room_floor, get_C_room_floor

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
B_room_floor = get_B_room_floor(floor) # fajr
C_room_floor = get_C_room_floor(floor)# fajr
exit_floor = get_exit_floor(floor)
centre_wall = get_centre_wall(wall)
A_room_wall = get_A_room_wall(wall)
B_room_wall = get_A_room_wall(wall) # fajr 
C_room_wall = get_centre_wall(wall)
exit_wall = get_exit_wall(wall)
B_room_floor = get_B_room_floor(floor,wall)
C_room_floor = get_C_room_floor(floor,wall)


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
backroom_A = pygame.Rect((605, 620, 55, 60))
backroom_B = pygame.Rect(520, 650, 60, 40)# fajr
map_place = pygame.Rect(560, 340, 120, 80)# fajr
room_B = pygame.Rect(405,535,20,64)
room_C = pygame.Rect(800,70, 52,63)
room_D = pygame.Rect(415, 155, 22, 10)
centre_up = pygame.Rect(300,50,700,50)

diary_rect = pygame.Rect((327,115,17,11))

girl = Character(580,320,0.7)
girl_A = Character(600,530,0.5)




story = ['I need to escape this house!','The exit is locked.', 'I should find the key to get out of here.']
story_index = 0
map_puzzle_open = False # fajr
map_puzzle_done = False
piece_count = 0
map_message = ''
text_box = pygame.Rect((140,500,1000,120))
current_state = 'menu'
running = True

while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
              if current_state == 'B':

               if event.key == pygame.K_e:
                if girl_A.player.colliderect(map_place):
                 map_open = True
                 count = 0
                 text = 'NEW TEXT TEST'

              if event.key == pygame.K_SPACE and map_open:
               count += 1

            if count == 1:
                text = 'First piece placed.'
            elif count == 2:
                text = 'The picture looks clearer.'
            elif count == 3:
                text = 'It looks like a map.'
            elif count >= 4:
                text = 'X mark found. The number is 4.'
              
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
      if current_room == 'centre' and 'centre' in rooms:
        screen.blit(centre_floor,(275,160))
        screen.blit(exit_floor,(279.8,160))
        screen.blit(centre_wall,(275,80))
        screen.blit(exit_wall,(275,80))
        screen.blit(door,(400,108))
        screen.blit(door,(800,108))
        
        girl.movement()
        girl.graphic(screen)
     
        if girl.player.colliderect(room_A):
          current_state = 'A'
          girl_A.x = 600
          girl_A.y = 530
          
        
        if girl.player.colliderect(room_B):
          current_state = 'B'
        
        if girl.player.colliderect(room_C):
          current_state = 'C'

    elif current_state == 'A'and 'A' in rooms['centre']:
        screen.blit(A_room_floor,(350,160))
        screen.blit(A_room_wall,(350,80))
        screen.blit(bookshelf,(330,200))
        screen.blit(bookshelf,(620,200))
        screen.blit(diary,(600,350))
        screen.blit(fireplace,(565,110))
        girl_A.movement()
        girl_A.graphic(screen)
        if girl.player.colliderect(backroom_A) and 'centre' in rooms['A']:
            current_state = 'game'
            girl.x = 410
            girl.y = 160
      

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

    elif current_state == 'B':
        screen.blit(B_room_floor,(0,0))

    elif current_state == 'C':
        screen.blit(C_room_floor,(0,0))

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
        map_open = True
        text = 'You found a torn picture. Press SPACE to put the pieces together.'

    if map_open:
        pygame.draw.rect(screen, 'white', (200, 500, 800, 80))
        msg = dialogue_font.render(text, True, 'black')
        screen.blit(msg, (220, 520))

    if girl_A.player.colliderect(backroom_B):
        current_state = 'game'
        girl.x = 580
        girl.y = 140

    girl_A.graphic(screen)

        
    pygame.display.flip()
pygame.quit()
