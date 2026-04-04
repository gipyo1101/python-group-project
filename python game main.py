import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
running = True
font = pygame.font.SysFont(None,40)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    pygame.draw.rect(screen, 'white', (250,525,800,150))  #(x, y, width, height)
    text_in_rect = font.render("You wake up in a strange room.", True, (255, 255, 255),'black')
    screen.blit(text_in_rect, (450,585))

    pygame.display.flip()



pygame.quit()
