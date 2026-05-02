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