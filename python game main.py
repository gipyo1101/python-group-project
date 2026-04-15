import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
title_font = pygame.font.SysFont(None,100)
button_font = pygame.font.SysFont(None,60)
dialogue_font = pygame.font.SysFont(None,50)
start_button = pygame.Rect((410,300,400,100))
quit_button = pygame.Rect((410,450,400,100))
menu_background = pygame.image.load('images/menu image1.jpeg').convert()
menu_background = pygame.transform.scale(menu_background, (1280, 720))
game_character = pygame.image.load('images/game_character.png').convert_alpha() # because of transparency
character = pygame.Surface((16,16), pygame.SRCALPHA)
character.blit(game_character,(0,0),(0,16,16,16))  #(x,y,width,height)
character = pygame.transform.scale(character, (64, 64))
character_x = 100
character_y = 550
character_movement_speed = 1

story = ['I need to escape this room!','The door is locked.', 'I should find the key to get out of here.']
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
        title_text = title_font.render('Escape the Room',True,'white')
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
        screen.fill('black')
        screen.blit(character, (character_x,character_y)) #(x,y) - start point
        if keys[pygame.K_LEFT]:
            character_x -= character_movement_speed
        if keys[pygame.K_RIGHT]:
            character_x += character_movement_speed
        if keys[pygame.K_DOWN]:
            character_y += character_movement_speed
        if keys[pygame.K_UP]:
            character_y -= character_movement_speed
        if character_x < 0: character_x = 0    # screen limits
        if character_x > 1216: character_x = 1216
        if character_y < 0: character_y = 0
        if character_y > 650: character_y = 650

    pygame.display.flip()
pygame.quit()