# Main game file which handles the main game running loop, screen states, room transitions, 
# story progression, password input, character movement, and timer.
import pygame
import time
from character import Character
from rooms import A_room
from rooms import B_room
from rooms import C_room
from rooms import get_centre_floor, get_A_room_floor, get_exit_floor, get_centre_wall, get_A_room_wall, get_exit_wall
from assets import get_doors, get_diary, get_bookshelf, get_desk, get_walls, get_floors
from assets import get_c_loop_room, get_c_final_room
from assets import get_c_screen_blank, get_c_screen_left, get_c_screen_up, get_c_screen_right
from assets import get_c_button_blank, get_c_button_left, get_c_button_up, get_c_button_right
from assets import get_c_large_screen_blank, get_c_large_screen_3

# 5754447 Gipyo 
pygame.init()
screen = pygame.display.set_mode((1280,720))
floor = get_floors()
wall = get_walls()
door = get_doors()
diary = get_diary()
bookshelf = get_bookshelf()
desk = get_desk()
centre_floor = get_centre_floor(floor)
A_room_floor = get_A_room_floor(floor)
exit_floor = get_exit_floor(floor)
centre_wall = get_centre_wall(wall)
exit_wall = get_exit_wall(wall)
A_room_wall = get_A_room_wall(wall)
C_room_wall = get_centre_wall(wall) # fajr
# 5754447 Gipyo

# Hashim room c assets
c_loop_room = get_c_loop_room()
c_final_room = get_c_final_room()

c_screen_images = {
    "blank": get_c_screen_blank(),
    "left": get_c_screen_left(),
    "up": get_c_screen_up(),
    "right": get_c_screen_right()
}
c_button_images = {
    "blank": get_c_button_blank(),
    "left": get_c_button_left(),
    "up": get_c_button_up(),
    "right": get_c_button_right()
}

c_large_screen_images = {
    "blank": get_c_large_screen_blank(),
    "3": get_c_large_screen_3()
}

room_c = C_room(c_loop_room, c_final_room, c_screen_images, c_button_images, c_large_screen_images)
# Hashim


# 575447 Gipyo
title_font = pygame.font.SysFont(None,100)
button_font = pygame.font.SysFont(None,60)
dialogue_font = pygame.font.SysFont(None,50)
diary_font = pygame.font.SysFont(None, 30)
start_button = pygame.Rect((410,300,400,100)) # (x,y,width,height)
quit_button = pygame.Rect((410,450,400,100))
try:
    menu_background = pygame.image.load('images/menu image1.jpeg').convert_alpha()
    menu_background = pygame.transform.scale(menu_background, (1280, 720))
except pygame.error:
    menu_background = pygame.Surface((1280,720))
    menu_background.fill('black')
# 5754447 Gipyo

# 5754447 Gipyo
# A graph structure showing which rooms are connected.
rooms = {'centre':['A','B','C','exit'], 'A':['centre','C'],
                'B':['centre'], 'C':['centre'], 'exit':['centre']}
current_room = 'centre'
room_a = A_room(A_room_floor, A_room_wall, bookshelf, diary, desk)
A_room_label = diary_font.render('A',True,'black')
B_room_label = diary_font.render('B',True,'white')
C_room_label = diary_font.render('C',True,'black')
D_room_label = diary_font.render('unavailable',True,'white')
exit_label = diary_font.render('exit',True,'white')
# Rectangles for collision detection with the player
room_A_rect = pygame.Rect(420, 130, 30, 40)
from_A_to_C_rect = pygame.Rect(878, 320, 60, 60)
backroom_A_rect = pygame.Rect(590, 600, 55, 30)
bookshelf_1_rect = pygame.Rect(360, 320, 90, 30)
bookshelf_2_rect = pygame.Rect(480, 320, 90, 30)
bookshelf_3_rect = pygame.Rect(660, 320, 90, 30)
bookshelf_4_rect = pygame.Rect(780, 320, 90, 30)
bookshelf_5_rect = pygame.Rect(360, 450, 90, 30)
bookshelf_6_rect = pygame.Rect(480, 450, 90, 30)
bookshelf_7_rect = pygame.Rect(660, 450, 90, 30)
bookshelf_8_rect = pygame.Rect(780, 450, 90, 30)
desk1_rect = pygame.Rect(553, 110, 170, 110)
# 5754447 Gipyo

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
    pygame.Rect(878, 320, 60, 60),    # right side extension
]
A_obstacle = [pygame.Rect(360, 230, 90, 90), # bookshelf 1
              pygame.Rect(480, 230, 90, 90), # bookshelf 2
              pygame.Rect(660, 230, 90, 90), # bookshelf 3
              pygame.Rect(780, 230, 90, 90), # bookshelf 4
              pygame.Rect(360, 360, 90, 90), # bookshelf 5
              pygame.Rect(480, 360, 90, 90), # bookshelf 6
              pygame.Rect(660, 360, 90, 90), # bookshelf 7
              pygame.Rect(780, 360, 90, 90), # bookshelf 8
              pygame.Rect((600,350,30,20)),   # diary
              pygame.Rect(565, 140, 100, 50)] # desk
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

# 5754447 Gipyo
girl = Character(580,320,1) # the character in the centre room
girl_A = Character(600,530,0.7) # the character in the Room A
# 5754447 Gipyo

#Hashim
girl_B = Character(595,510,0.7)
girl_C = Character(595,510,0.7)
#Hashim

# 5750766 Fajr
bed_img = pygame.image.load("images/bed.png")  #room B objects
bed_img = pygame.transform.scale(bed_img, (200, 200))
bed_img = pygame.transform.rotate(bed_img, 90)
map_img = pygame.image.load("images/map.png")
map_img = pygame.transform.scale(map_img, (60, 45))
bed_place =pygame.Rect(360, 300, 120, 120)
map_place = pygame.Rect(410, 430, 60, 45)
A_puzzle_done = False
A_transition_story = False
A_transition_index = 0
A_transition_done = False
piece_count = 0
map_puzzle_open = False 
map_puzzle_done = False
#room B variables
room_b_intro = False   
hallway_message = ""
map_message = ''
map_place = pygame.Rect(555, 255, 80, 30)
room_b = B_room(floor, wall, bed_img,map_img)
start_time = None
time_limit = 300 
# 5750766 Fajr
                
# 5754447 Gipyo
story_before_centre = ['I need to escape this house!','The exit is locked.', 
                       'I should find the password to get out of here.']
story_before_centre_index = 0
story_centre = False
# 5754447 Gipyo

# 5750766 Fajr
storylines_after_A = [ 
     "That diary...something feels wrong",
     "I think the next room is connected to this",
     "I should check room B..."
] #5750766 Fajr

# 5754447 Gipyo
storylines_centre = ['There are 3 rooms and the exit.',
                      "Hmm, it looks like I should visit the all rooms.",
                      "Let's go to the A room first."]
story_centre_index = 0
story_text_box = pygame.Rect((140,500,1000,120))
current_state = 'menu'
exit_story = False
exit_story_done = False
exit_storylines = ['I found all three digits.',"Let's go to the exit."]
exit_story_index = 0
password_input = ""
password_error = ""
exit_password = "743"
exit_rect = pygame.Rect(1050, 265, 50, 170)
running = True
# 5754447 Gipyo



# 5754447 Gipyo
# Main game loop which handles input events, updates game states, and renders game user interface.
while running:
    
    # 5750766 Fajr
    if current_state != 'menu' and current_state != 'story' and start_time != None:
        elsapsed_time = time.time() - start_time 
        remaining_time = max(0, int(time_limit - elsapsed_time)) 
    else:
        remaining_time = time_limit 
    # 5750766 Fajr

    # 5754447 Gipyo
    password_digits_found = room_a.after_desk_check and map_puzzle_done and room_c.solved # all three password digits are found
    screen.fill('black')
    # Controls keyboard and mouse input system depending on the current game state.
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
                    story_before_centre_index += 1
                    if story_before_centre_index >= len(story_before_centre):
                        current_state = 'game'
                        current_room = 'centre'
                        story_centre = True
                        start_time = time.time() # 5750766 Fajr
        
        elif current_state == 'game' and story_centre == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    story_centre_index += 1
                    if story_centre_index >= len(storylines_centre):
                        story_centre = False
        
        # 5750766 Fajr
        if A_transition_story == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    A_transition_index += 1
                    if A_transition_index >= len(storylines_after_A):
                        A_transition_story = False
                        A_transition_index = 0
        # 5750766 Fajr


        elif current_state == 'game' and exit_story == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit_story_index += 1
                    if exit_story_index >= len(exit_storylines):
                        exit_story = False
                if event.key == pygame.K_RETURN:
                    if password_input == exit_password:
                        exit_story = True
                        
        if event.type == pygame.KEYDOWN:
            if current_state == 'A':
                room_a.event(event,girl_A)
    # 5754447 Gipyo
                
            # 5750766 Fajr
            if current_state == 'B': 
                room_b.event(event, girl_B)

                if event.key == pygame.K_e:
                    map_puzzle_open = True
                    room_b.message_open = True
                    if not map_puzzle_done:
                        map_message = 'What is this? Press SPACE.'
                        room_b.message = map_message

                if event.key == pygame.K_SPACE and room_b.message_open and not map_puzzle_done:
                    piece_count += 1
                
                if piece_count == 1:
                    map_message = 'I need to take a closer look.'
                    room_b.message = map_message

                elif piece_count == 2:
                    map_message = 'The picture looks clearer.'
                    room_b.message = map_message
                
                elif piece_count == 3:
                    map_message = 'It looks like a map.'
                    room_b.message = map_message

                elif piece_count >= 4:
                    map_puzzle_done = True
                    map_message = 'The x is marked shows number 4!'
                    room_b.message = map_message
             # 5750766 fajr  

            # Hashim
            if current_state == 'C':
                room_c.event(event, girl_C)
            # Hashim

            # 5754447 Gipyo
            # Handles the password input for the exit.
            if current_state == 'exit':
                if event.key >= pygame.K_0 and event.key <= pygame.K_9: # only number key inputs
                    if len(password_input) < 3:
                        password_input += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    password_input = password_input[:-1] # removes the last number

                if event.key == pygame.K_RETURN:
                    if password_input == exit_password: # checks whether the password is correct
                            exit_story_done = True
                    else:
                        # Shows an error message and resets the input if the password is incorrect.
                        password_error = "The password is incorrect. Try again."
                        password_input = ""
            # 5754447 Gipyo

    # 5754447 Gipyo
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
    # 5754447 Gipyo

    # 5754447 Gipyo
    elif current_state == 'story': 
        screen.blit(menu_background,(0,0))
        pygame.draw.rect(screen, 'white', story_text_box)
        dialogue = dialogue_font.render(story_before_centre[story_before_centre_index],True,'black')
        dialogue_rect = dialogue.get_rect(center = story_text_box.center)
        screen.blit(dialogue,dialogue_rect)
    # 5754447 Gipyo

    # 5754447 Gipyo
    elif current_state == 'game':
        if current_room == 'centre' and 'centre' in rooms: 
            screen.blit(centre_floor,(275,160))
            screen.blit(exit_floor,(279.8,160))
            screen.blit(centre_wall,(275,80))
            screen.blit(exit_wall,(275,80))
            screen.blit(door,(400,108))
            screen.blit(door,(800,108))
            screen.blit(A_room_label,(390, 110))
            screen.blit(B_room_label,(385, 575))
            screen.blit(C_room_label,(790,110))
            screen.blit(D_room_label,(860, 575))    
            screen.blit(exit_label,(1120, 330))
            girl.graphic(screen)

            if story_centre == True:
                story_box = pygame.draw.rect(screen, 'white', (130,620,1000,80))
                story_text = dialogue_font.render(storylines_centre[story_centre_index],True,'black')
                story_rect = story_text.get_rect(center= story_box.center)
                screen.blit(story_text, story_rect)

            # After collecting all password digits
            if password_digits_found and exit_story == True:
                exit_story = True
                if exit_story == True:
                    story_box = pygame.draw.rect(screen, 'white', (130,620,1000,80))
                    story_text = dialogue_font.render(storylines_centre[story_centre_index],True,'black')
                    story_rect = story_text.get_rect(center= story_box.center)
                    screen.blit(story_text, story_rect)
            # 5754447 Gipyo
            
            # 5750766 Fajr
            if A_transition_story and A_transition_index < len(storylines_after_A):
                transition_box = pygame.draw.rect(screen, 'white', (130,620,1000,80))
                pygame.draw.rect(screen, 'black', transition_box, 3)
                transition_text = dialogue_font.render( 
                    storylines_after_A[A_transition_index],
                    True,
                    'black'
                )
                transition_rect = transition_text.get_rect(center=transition_box.center)
                screen.blit(transition_text, transition_rect)
            # 5750766 Fajr
            
            # 5754447 Gipyo
            # The player cannot move when the story dialouge is in progress.
            if story_centre == False and A_transition_story == False and exit_story == False:
                girl.movement(centre_walkable)
            # 5754447 Gipyo

            # Hashim
            # debug rectangles, remove later
            """for area in centre_walkable:
                pygame.draw.rect(screen, 'green', area, 2)
                pygame.draw.rect(screen, 'blue', room_A_rect, 2)
                pygame.draw.rect(screen, 'blue', room_C_rect, 2)
                pygame.draw.rect(screen, 'blue', room_B_rect, 2)
                pygame.draw.rect(screen,'blue',exit_rect,2)
                pygame.draw.rect(screen, 'purple', girl.feet_hitbox(), 2)"""
            if girl.feet_hitbox().colliderect(room_A_rect):
                current_state = 'A'
                girl_A.set_position(595,510)
            
            if girl.feet_hitbox().colliderect(room_B_rect):
                current_state = 'B'
                girl_B.set_position(595,170)

            if girl.feet_hitbox().colliderect(room_C_rect):
                current_state = 'C'
                room_c.enter_room()
                girl_C.set_position(595,510)

            if girl.feet_hitbox().colliderect(exit_rect):
                if password_digits_found:
                    current_state = 'exit'
                    exit_input = ""
            # Hashim
            
    # 5754447 Gipyo
    elif current_state == 'A':
        # Handles every gameplay logic and interactions in Room A.
        current_room = 'A'
        if current_room == 'A' and 'A' in rooms['centre']:
            # Draws the Room A screen and character graphics.
            room_a.A_room_screen(screen,girl_A,diary_font,dialogue_font)
            girl_A.graphic(screen)

            # The player returns to the centre room after colliding with the backroom rectangle.
            if girl_A.feet_hitbox().colliderect(backroom_A_rect) and 'centre' in rooms['A']:
                current_state = 'game'
                current_room = 'centre'
                girl.set_position(410,160)
                # Able to progress to next story after A room puzzle is completed.
                if room_a.after_desk_check == True and A_transition_done == False:
                    A_transition_story = True
                    A_transition_index = 0
                    A_transition_done = True
            # Allows access to room C only after the A room puzzle is completed.
            if girl_A.feet_hitbox().colliderect(from_A_to_C_rect):
                if room_a.after_desk_check == True:
                    current_state = 'C'
                    room_c.enter_room()
                    girl_C.set_position(595,510)

            # Character movement is temporarily disabled while story is active
            if (room_a.before_diary_story == False 
                and room_a.after_diary_story == False 
                and room_a.after_bookshelves_story == False 
                and room_a.diary_open == False
                and room_a.before_desk_story == False): 
                girl_A.movement(A_walkable,A_obstacle)    
            
            # Debug collision rectangles
            # These were used during testing and debugging.
            """for area in A_walkable:
                pygame.draw.rect(screen, 'green', area, 2)
                pygame.draw.rect(screen, 'blue', backroom_A_rect, 2)
                pygame.draw.rect(screen,'blue',room_a.desk_rect,2)
                pygame.draw.rect(screen,'blue',room_a.diary_rect,2)
                pygame.draw.rect(screen, 'purple', girl_A.feet_hitbox(), 2)
                pygame.draw.rect(screen, 'blue', bookshelf_1_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_2_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_3_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_4_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_5_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_6_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_7_rect, 2)
                pygame.draw.rect(screen, 'blue', bookshelf_8_rect, 2)
                pygame.draw.rect(screen, 'green', A_obstacle[0], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[1], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[2], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[3], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[4], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[5], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[6], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[7], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[8], 2)
                pygame.draw.rect(screen, 'green', A_obstacle[9], 2)"""
    # 5754447 Gipyo

    # 5750766 Fajr
    elif current_state == 'B':
       current_room = 'B'
       if current_room == 'B' and 'B' in rooms['centre']:
            room_b.B_room_screen(screen, dialogue_font)
            girl_B.movement(B_walkable, [bed_place])
            girl_B.graphic(screen)

            if girl_B.feet_hitbox().colliderect(backroom_B):
                current_state = 'game'
                current_room = 'centre'
                girl.set_position(410, 485)
    # 5750766 Fajr
        
    #Hashim
    elif current_state == 'C':
        current_room = 'C'
        if current_room == 'C' and 'C' in rooms['centre'] and rooms['A']:
            room_c.C_room_screen(screen, dialogue_font)
            girl_C.movement(room_c.walkable)
            girl_C.graphic(screen)
            if room_c.should_leave(girl_C):
                current_state = 'game'
                current_room = 'centre'
                girl.set_position(805, 165)
    # Hashim

    # 5754447 Gipyo
    elif current_state == 'exit':
        if 'exit' in rooms['centre']:
            screen.fill('black')
            pygame.draw.rect(screen, 'white', (130,620,1000,80))
            input_text = dialogue_font.render("Enter the exit password:", True, 'black')
            screen.blit(input_text, (220,645))
            # Displays the current password input.
            password_input_screen= password_input.ljust(3, "_")
            password_input_screen = " ".join(password_input_screen)
            password_input_text = dialogue_font.render(password_input_screen, True, 'black')
            screen.blit(password_input_text, (700,645))
            # Ends the game after the correct password is entered.
            if exit_story_done == True:
                screen.fill('black')
                escaped_text = title_font.render('YOU ESCAPED!', True, 'white')
                screen.blit(escaped_text,(380,300))
                pygame.display.flip()
                # Shows the ending screen for 5 seconds before automatically closing the game.
                pygame.time.delay(5000)
                running = False
            
            # Displays an error message if the password input is incorrect.
            if password_error != "":
                password_error_text = diary_font.render(password_error, True, 'red')
                screen.blit(password_error_text, (450, 590))
    # 5754447 Gipyo

    # 5750766 Fajr
    if current_state != 'menu' and current_state != 'story':
        timer = dialogue_font.render("time: " + str(remaining_time), True, "white")
        screen.blit(timer, ((1100, 50)))
        if remaining_time <= 0:
            game_over = title_font.render("GAME OVER", True, "red")
            screen.blit(game_over, (420, 300))
            pygame.display.update()
            pygame.time.delay(5000)
            running = False
    # 5750766 Fajr
    
    pygame.display.flip()
pygame.quit()
# 5754447 Gipyo
