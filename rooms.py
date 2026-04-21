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
    return exit_wall_background

def get_B_room_floor(floor, wall):
    # create surface for room B 
    B_floor = pygame.Surface((1280, 720), pygame.SRCALPHA)

    # main floor area
    for x in range(50, 650, 48):
        for y in range(100, 500, 24):
            B_floor.bilt(floor, (x, y))

 # left side extension 
        for x in range(0, 150, 48):
               for y in range(200, 400, 24):
                    B_floor.bilt(floor, (x, y))

  # small bottom section 
    for x in range(300, 500, 48):
        for y in range(500, 650, 24):
               B_floor.bilt(floor, (x, y))
               
# top wall
for x in range(0, 1280, 48):
     B_floor.bilt(wall, (x, 0))
    
# left wall
for y in range(0, 720, 48):
     B_floor.bilt(wall, (0, y))

# right wall
for y in range(0, 720, 48):
        B_floor.blit(wall, (1232, y))

    return B_floor
