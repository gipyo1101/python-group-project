import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
title_font = pygame.font.SysFont(None,100)
button_font = pygame.font.SysFont(None,60)
dialogue_font = pygame.font.SysFont(None,50)

# menu
start_button = pygame.Rect((410,300,400,100))
quit_button = pygame.Rect((410,450,400,100))
menu_background = pygame.image.load('images/menu image1.jpeg').convert_alpha()
menu_background = pygame.transform.scale(menu_background, (1280, 720))

# character image
game_character = pygame.image.load('images/game_character.png').convert_alpha() # because of transparency
character = pygame.Surface((16,16), pygame.SRCALPHA)
character.set_colorkey((0,0,0))
character.blit(game_character,(0,0),(0,16,16,16))  #(x,y,width,height)
character = pygame.transform.scale(character, (45,45))
character_x = 580  
character_y = 320
character_movement_speed = 0.5

# floor 
floor_wall = pygame.image.load('images/floors_LRK.png').convert_alpha()
floor = pygame.Surface((44,20), pygame.SRCALPHA)
floor.blit(floor_wall, (0,0), ((22,82,44,20)))
floor_background = pygame.Surface((1280,720),pygame.SRCALPHA)
exit_floor = pygame.Surface((1280,720),pygame.SRCALPHA)
for x in range(0, 700, 44):
    for y in range(0,400,20):
        floor_background.blit(floor, (x,y))

for x in range(700,800,44):
    for y in range(100,280,20):
        exit_floor.blit(floor,(x,y))


# wall
wall = pygame.Surface((44,80),pygame.SRCALPHA)
wall.blit(floor_wall,(0,0),(22,20,44,80))
wall = pygame.transform.scale(wall,(44,150))
wall_background = pygame.Surface((1000,80),pygame.SRCALPHA)
wall_back = pygame.Surface((1000,180),pygame.SRCALPHA)
for x in range(0,700,44):
    wall_background.blit(wall,(x,0))

for x in range(704,800,44):
    wall_back.blit(wall,(x,100))
    

#door
doors = pygame.image.load('images/doors_LRK.png').convert_alpha()
door = pygame.Surface((40,56),pygame.SRCALPHA)
door.blit(doors,(0,0),(102,16,40,56))
door = pygame.transform.scale(door,(52,64))



# furniture set
furniture_set = pygame.image.load('images/furniture set.png').convert_alpha()
#wall = pygame.Surface((35,63),pygame.SRCALPHA)
#wall.blit(furniture_set, (0,0),((354, 416, 35, 63)))
#wall_background = pygame.Surface((1000, 63), pygame.SRCALPHA)
#for x in range(0,1000,35):
    #wall_background.blit(wall,(x,0))




story = ['I need to escape this house!','The exit is locked.', 'I should find the key to get out of here.']
story_index = 0
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
        screen.fill('black')
        pygame.draw.rect(screen, 'white', text_box)
        dialogue = dialogue_font.render(story[story_index],True,'black')
        dialogue_rect = dialogue.get_rect(center = text_box.center)
        screen.blit(dialogue,dialogue_rect)
        

        
    elif current_state == 'game':
        keys = pygame.key.get_pressed()
        screen.blit(floor_background,(275,160))
        screen.blit(exit_floor,(279.8,160))
        screen.blit(wall_background,(275,80))
        screen.blit(wall_back,(275,80))
        screen.blit(door,(400,108))
        screen.blit(door,(800,108))
        screen.blit(character, (character_x,character_y)) #(x,y) - start point
        
        
        if keys[pygame.K_LEFT]: character_x -= character_movement_speed # arrow keys
        if keys[pygame.K_RIGHT]: character_x += character_movement_speed
        if keys[pygame.K_DOWN]: character_y += character_movement_speed
        if keys[pygame.K_UP]: character_y -= character_movement_speed


        if character_x < 275: character_x = 275   # limits
        if character_x > 935: character_x = 935
        if character_y < 140: character_y = 140
        if character_y > 515: character_y = 515


        current_room = 'centre'

        rooms = {'centre':['A','B','C','D','exit'], 'A':['centre','C'],
                'B':['centre','D'], 'C':['centre','A'], 'D':['centre','B'], 'exit':['centre']}
        
        

    pygame.display.flip()
pygame.quit()