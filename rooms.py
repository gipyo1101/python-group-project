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
        
        self.books = [('Economics',2001),("Fantasy", 1995), ("History", 1978),
                      ("Astronomy", 2004),("Romance", 1982),
                      ('Biography',1997),('Mathematics',2013),('Computer Science',2006)]
        self.bookshelves_rect = [pygame.Rect(330, 200, 120, 130), pygame.Rect(500, 200, 120, 130), 
                                 pygame.Rect(760, 200, 120, 130), pygame.Rect(930, 200, 120, 130),  
                                 pygame.Rect(330, 430, 120, 130), pygame.Rect(500, 430, 120, 130),  
                                 pygame.Rect(760, 430, 120, 130), pygame.Rect(930, 430, 120, 130)]
        
        self.genres = ['History', 'Romance','Fantasy','Astronomy',
                       'Biography','Mathematics','Computer Science','Economics']
        
        self.diary_rect = pygame.Rect((600,360,40,30))
        self.diary_open = False
        self.diary_page = 0
        self.diary_texts = ['I loved reading books in the library.',
               'Reading about the Second World War\nwas helpful for my history class at school.',
               'I wished I could use spells and magic\nlike the wizards in Harry Potter.', 
               'I often wondered what it would be like to\ntravel through space and discover new planets.',
               'I cried after reading tragic romance stories\nlike Romeo and Juliet. It broke my heart.',
               'My grandfather always told me,\n"The order of the years hides the truth."']
        
        self.books_finding = {'History': "You found a History book.",
                          'Romance': "You found a Romance book.",
                          'Fantasy': "You found a Fantasy book.",
                          'Astronomy': "You found an Astronomy book.",
                          'Biography': "You found a Biography book.",
                          'Mathematics': "You found a Mathematics book.",
                          'Computer Science': "You found a Computer Science book.",
                          'Economics': "You found an Economics book."}
        self.finding_index = 0
        self.inventory_open = False
        self.inventory = []

        self.storylines = ["There is a book on the floor. Let's check it out!",
                           "Press F near that book and press Q or E to turn the pages.",
                           "Hmm...","It looks like a diary.",
                           "This can be the clue for finding the key.",
                           "The first book was related to history.",
                           "The second book was about magic and fantasy.",
                           "The third book was about the space.",
                           "The last book was about romance.",
                           "I need to find those books in the bookshelves."]
        
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
            if self.diary_open == True:
                if event.key == pygame.K_e:
                    self.diary_page += 1
                    if self.diary_page >= len(self.diary_texts):
                        self.diary_page = len(self.diary_texts) - 1
                if event.key == pygame.K_q:
                    self.diary_page -= 1
                    if self.diary_page < 0:
                        self.diary_page = 0
            if event.key == pygame.K_SPACE:
                self.finding_index += 1
                if self.finding_index >= len(self.books_finding):
                    current_state = 'game'
                    current_room = 'centre'
               
            if event.key == pygame.K_i:
                self.inventory_open = True


            if event.key == pygame.K_ESCAPE:
                self.diary_open = False
                self.diary_page = 0
                self.inventory_open = False
            

    def A_room_screen(self,screen,character,diary_font):
        screen.blit(self.floor,(350,160))
        screen.blit(self.wall,(350,80))
        screen.blit(self.bookshelf,(330,200))
        screen.blit(self.bookshelf,(630,200))
        screen.blit(self.diary,(600,350))
        screen.blit(self.fireplace,(565,110))
        if self.diary_open == True:
            pygame.draw.rect(screen, 'white', (420, 120, 400, 400))
            self.diary_inside = diary_font.render(self.diary_texts[self.diary_page], True, 'black')
            screen.blit(self.diary_inside, (440,160))

        if self.inventory_open == True:
            pygame.draw.rect(screen,'white',(100,300,1000,200))
            for i in range(len(self.inventory)):
                title_year = str(self.inventory[i])
                inventory_text = diary_font.render(title_year,True,'black')
                screen.blit(inventory_text,(150,300+ i * 20))

        if self.inventory:
            found_books = self.inventory[-1]
            books_genre = found_books[0]
            pygame.draw.rect(screen, 'white', (290, 600, 650, 60))
            finding_texts = diary_font.render("You found a " + books_genre + " book.", True, 'black')
            screen.blit(finding_texts, (470, 620))

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