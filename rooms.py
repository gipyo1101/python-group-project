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
    return exit_wall_background

