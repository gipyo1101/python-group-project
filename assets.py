#gipyo
import pygame
def get_floors():
    floors = pygame.image.load('images/floorswalls_LRK.png').convert_alpha()
    floor = pygame.Surface((44,20), pygame.SRCALPHA)
    floor.blit(floors, (0,0), ((22,82,44,20)))
    return floor

def get_walls():
    walls = pygame.image.load('images/floorswalls_LRK.png').convert_alpha()
    wall = pygame.Surface((44,80),pygame.SRCALPHA)
    wall.blit(walls,(0,0),(22,20,44,80))
    wall = pygame.transform.scale(wall,(44,150))
    return wall


def get_doors():
    doors = pygame.image.load('images/doors_LRK.png').convert_alpha()
    door = pygame.Surface((40,56),pygame.SRCALPHA)
    door.blit(doors,(0,0),(102,16,40,56))
    door_scale = pygame.transform.scale(door,(52,64))
    return door_scale


def get_diary():
    furniture_set = pygame.image.load('images/furniture set.png').convert_alpha()
    diary = pygame.Surface((17,11),pygame.SRCALPHA)
    diary.blit(furniture_set,(0,0),(327,115,17,11))
    diary_scale = pygame.transform.scale(diary,(30,20))
    return diary_scale

def get_desk():
    furniture_set = pygame.image.load('images/furniture set.png').convert_alpha()
    desk = pygame.Surface((65,65),pygame.SRCALPHA)
    desk.blit(furniture_set,(0,0),(252,0,65,65))
    desk_scale = pygame.transform.scale(desk,(110,90))
    return desk_scale

def get_bookshelf():
    bookshelf_set = pygame.image.load('images/bookshelf_LRK.png').convert_alpha()
    bookshelf = pygame.Surface((134,126),pygame.SRCALPHA)
    bookshelf.blit(bookshelf_set, (0, 0), (0, 0, 134, 126))
    bookshelf_scale = pygame.transform.scale(bookshelf,(250,250))
    return bookshelf_scale
#gipyo

# Hashim (Room C assets)

ROOM_C_SIZE = (705, 530)

def get_c_image(filename, size=None, remove_white=True):
    image = pygame.image.load("images/" + filename).convert_alpha()

    if remove_white:
        image.set_colorkey((255, 255, 255))

    if size is not None:
        image = pygame.transform.scale(image, size)

        if remove_white:
            image.set_colorkey((255, 255, 255))

    return image


def get_c_loop_room():
    image = pygame.image.load("images/c_loop_room.png").convert_alpha()
    image = pygame.transform.scale(image, ROOM_C_SIZE)
    return image


def get_c_final_room():
    image = pygame.image.load("images/c_final_room.png").convert_alpha()
    image = pygame.transform.scale(image, ROOM_C_SIZE)
    return image


def get_c_screen_blank():
    return get_c_image("c_screen_blank.png", (80, 48))


def get_c_screen_left():
    return get_c_image("c_screen_left.png", (80, 48))


def get_c_screen_up():
    return get_c_image("c_screen_up.png", (80, 48))


def get_c_screen_right():
    return get_c_image("c_screen_right.png", (80, 48))


def get_c_button_blank():
    return get_c_image("c_button_blank.png", (75, 52))


def get_c_button_left():
    return get_c_image("c_button_left.png", (75, 52))


def get_c_button_up():
    return get_c_image("c_button_up.png", (75, 52))


def get_c_button_right():
    return get_c_image("c_button_right.png", (75, 52))


def get_c_large_screen_blank():
    return get_c_image("c_large_screen_blank.png", (215, 95))


def get_c_large_screen_3():
    return get_c_image("c_large_screen_3.png", (215, 95))

# Hashim