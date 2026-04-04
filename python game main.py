import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
running = True
font = pygame.font.SysFont(None,60)

current_state = 'menu'
while running:
    screen.fill('black')
    start_button = pygame.Rect((410,300,400,100))
    quit_button = pygame.Rect((410,450,400,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse):
                current_state = 'story'
            if quit_button.collidepoint(mouse):
                pygame.quit()
                ruuning = False
    if current_state == 'menu':
        pygame.draw.rect(screen, 'white', start_button)  #(x, y, width, height)
        text_in_start = font.render("Start", True,'black')
        pygame.draw.rect(screen, 'white', quit_button)
        text_in_quit = font.render("Quit",True,'black')
        screen.blit(text_in_start, (560,330)) #(x,y)
        screen.blit(text_in_quit, (565,480))
    
    elif current_state == 'story':
        screen.fill('blue')

    pygame.display.flip()
