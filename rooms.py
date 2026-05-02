#gipyo
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
#gipyo

# Fajr
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
#Fajr

#gipyo
class A_room():
    def __init__(self,floor, wall, bookshelf, diary, fireplace):
        self.floor = floor
        self.wall = wall
        self.bookshelf = bookshelf
        self.diary = diary
        self.fireplace = fireplace
        
        self.books = [('Economics',2001),("Astronomy", 2004),
                      ('Mathematics',2013),("Fantasy", 1995), ('Computer Science',2006),
                      ("History", 1978),('Biography',1997),("Romance", 1982)]
        self.bookshelves_rect = [pygame.Rect(360, 320, 90, 30), pygame.Rect(480, 320, 90, 30), 
                                 pygame.Rect(660, 320, 90, 30), pygame.Rect(780, 320, 90, 30),  
                                 pygame.Rect(360, 440, 90, 30), pygame.Rect(480, 440, 90, 30),  
                                 pygame.Rect(660, 440, 90, 30), pygame.Rect(780, 440, 90, 30)]
        
        self.genres = ['Economics', 'Astronomy','Mathematics','Fantasy',
                       'Computer Science','History','Biography','Romance']
        
        self.diary_rect = pygame.Rect((590,340,50,50))
        self.diary_open = False
        self.diary_page = 0
        self.diary_texts = ['I loved reading books\nin the library.',
               'Reading about the\nSecond World War\nwas helpful for\nmy history class\nat school.',
               'I wished I could use\nspells and magic\nlike the wizards\nin Harry Potter.', 
               'I often imagined\ntravelling through\nspace and discovering\nnew planets.',
               'I cried after reading\ntragic romance stories\nlike Romeo and Juliet.\nIt broke my heart.',
               'My grandfather always\ntold me,\n"The order of the\nyears hides the truth."']
        
        self.books_finding = {'History': "You found a History book.",
                          'Romance': "You found a Romance book.",
                          'Fantasy': "You found a Fantasy book.",
                          'Astronomy': "You found an Astronomy book.",
                          'Biography': "You found a Biography book.",
                          'Mathematics': "You found a Mathematics book.",
                          'Computer Science': "You found a Computer Science book.",
                          'Economics': "You found an Economics book."}
        self.inventory_open = False
        self.inventory = []

        self.A_room_story = True
        self.storylines = ["There is a book on the floor.",
                           "Press F near that book and press Q or E to turn the pages.",
                           "Hmm...","It looks like a diary.",
                           "This can be the clue for finding the key.",
                           "The first book was related to history.",
                           "The second book was about magic and fantasy.",
                           "The third book was about the space.",
                           "The last book was about romance.",
                           "I need to find those books in the bookshelves."]
        self.A_room_story_index = 0
        
    def event(self,event,character):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if character.feet_hitbox().colliderect(self.diary_rect):
                    self.diary_open = True
                
                for order in range (len(self.bookshelves_rect)):
                    if character.feet_hitbox().colliderect(self.bookshelves_rect[order]):
                        genre = self.genres[order]
                        stored_books = self.linear_search_books(genre)
                        if stored_books not in self.inventory:
                            self.inventory.append(stored_books)
                            self.find_books = self.books_finding[genre]
            
            if event.key == pygame.K_SPACE:
                if self.A_room_story == True:
                    self.A_room_story_index += 1
                    if self.A_room_story_index >= 2:
                        self.A_room_story = False


            
            if event.key == pygame.K_i:
                self.inventory_open = True


            if self.diary_open == True:
                if event.key == pygame.K_e:
                    self.diary_page += 1
                    if self.diary_page >= len(self.diary_texts):
                        self.diary_page = len(self.diary_texts) - 1
                if event.key == pygame.K_q:
                    self.diary_page -= 1
                    if self.diary_page < 0:
                        self.diary_page = 0

            if event.key == pygame.K_ESCAPE:
                self.diary_open = False
                self.diary_page = 0
                self.inventory_open = False
            
            

    def A_room_screen(self,screen,character,diary_font,dialogue_font):
        screen.blit(self.floor,(350,160))
        screen.blit(self.wall,(350,80))
        screen.blit(self.bookshelf,(330,200))
        screen.blit(self.bookshelf,(630,200))
        screen.blit(self.diary,(600,350))
        screen.blit(self.fireplace,(565,110))
        

        if self.A_room_story == True:
            A_room_story_box = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            A_room_story_text = dialogue_font.render(self.storylines[self.A_room_story_index],True,'black')
            A_room_story_rect = A_room_story_text.get_rect(center= A_room_story_box.center)
            screen.blit(A_room_story_text, A_room_story_rect)
            

        if self.diary_open == True:
            pygame.draw.rect(screen, 'white', (410, 120, 400, 400))
            newline = self.diary_texts[self.diary_page].split('\n')
            for i in range(len(newline)):
                self.diary_inside = dialogue_font.render(newline[i], True, 'black')
                screen.blit(self.diary_inside, (420,170 + i * 50))

        if self.inventory_open == True:
            pygame.draw.rect(screen,'white',(30,200,300,300))
            for i in range(len(self.inventory)):
                title_year = str(self.inventory[i])
                inventory_text = diary_font.render(title_year,True,'black')
                screen.blit(inventory_text,(50,220+ i * 30))

        if self.inventory:
            found_books = self.inventory[-1]
            books_genre = found_books[0]
            finding_books_rect = pygame.draw.rect(screen, 'white', (280,620,700,80))
            finding_texts = dialogue_font.render("You found a " + books_genre + " book.", True, 'black')
            finding_rect = finding_texts.get_rect(center = finding_books_rect.center)
            screen.blit(finding_texts,finding_rect)




    def linear_search_books(self,genre):
        for i in range(len(self.books)):
            if genre == self.books[i][0]:
                return self.books[i]
        return None


    def bubble_sort_years(self,books):
        repeated_nums = len(books) - 1
        for i in range(repeated_nums, 0, -1):
            for j in range(i):
                if books[j][1] > books[j+1][1]:
                    temp = books[j]
                    books[j] = books[j+1]
                    books[j+1] = temp
    
        return books
        
    def get_password(self,books):
        books_list = self.bubble_sort_years(books)
        password = ''.join(str(year)[-1] for pw, year in books_list)
        return password
    
    

        
    
        
#gipyo