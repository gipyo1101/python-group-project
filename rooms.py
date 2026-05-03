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
    def __init__(self,floor, wall, bookshelf, diary, desk):
        self.floor = floor
        self.wall = wall
        self.bookshelf = bookshelf
        self.diary = diary
        self.desk = desk 
        self.books = [('Economics',2001),("Astronomy", 2004),
                      ('Mathematics',2013),("Fantasy", 1995), ('Computer Science',2006),
                      ("History", 1978),('Biography',1997),("Romance", 1982)]
        self.bookshelves_rect = [pygame.Rect(360, 320, 90, 30), pygame.Rect(480, 320, 90, 30), 
                                 pygame.Rect(660, 320, 90, 30), pygame.Rect(780, 320, 90, 30),  
                                 pygame.Rect(360, 450, 90, 30), pygame.Rect(480, 450, 90, 30),  
                                 pygame.Rect(660, 450, 90, 30), pygame.Rect(780, 450, 90, 30)]
        
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
        self.diary_check = False
        self.books_check = False
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
        self.before_diary_story = True
        self.before_diary_storylines = ["There is a book on the floor.",
                           "Press F near that book and press Q or E to turn the pages.",
                           'Press ESC to close the diary after reading it.']
        self.before_diary_index = 0
        self.after_diary_story = False
        self.after_diary_storylines = ["Hmm...","It looks like a diary.",
                           "This can be the clue for finding the key.",
                           "The first book was related to history.",
                           "The second book was about magic and fantasy.",
                           "The third book was about the space.",
                           "The last book was about romance.",
                           "Hmm... there are 8 bookshelves in this room.",
                           "Oh! This must be the clue!",
                           "Press F near the bookshelves.",
                           "Press I to open and close the inventory."]
        self.after_diary_index = 0
        self.after_bookshelves_story = False
        self.after_bookshelves_storylines = ['Oh! These books match what the diary said.',
                                             'I found all the books mentioned in the diary.',
                                             'The diary said, "The order of the years hides the truth."',
                                             'Maybe I should arrange these books in chronological order.']
        self.after_bookshelves_index = 0
        self.before_desk_story = False
        self.before_desk_storylines = ['The books in the inventory have been sorted by year.',
                                       'Oh! There is a desk behind the bookshelves.',
                                       'Maybe there is a clue of password with these books.',
                                       "Let's go there."]
        self.before_desk_index = 0
        self.desk_rect = pygame.Rect(560, 150, 110, 60)
        
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
                            if len(self.inventory) == 8 and self.after_bookshelves_story == False:
                                self.after_bookshelves_story = True
                                self.books_check = True
            
            if event.key == pygame.K_SPACE:
                if self.before_diary_story == True:
                    self.before_diary_index += 1 
                    if self.before_diary_index >= len(self.before_diary_storylines):
                        self.before_diary_story = False 

                elif self.after_diary_story == True:
                    self.after_diary_index += 1    
                    if self.after_diary_index >= len(self.after_diary_storylines):
                        self.after_diary_story = False   

                elif self.after_bookshelves_story == True:
                    self.after_bookshelves_index += 1
                    if self.after_bookshelves_index >= len(self.after_bookshelves_storylines):
                        self.after_bookshelves_story = False 
                        self.inventory= self.bubble_sort_years(self.inventory)
                        self.before_desk_story = True

                elif self.before_desk_story == True:
                    self.before_desk_index += 1
                    if self.before_desk_index >= len(self.before_desk_storylines):
                        self.before_desk_story = False
            
            if event.key == pygame.K_i:
                if self.inventory_open == False:
                    self.inventory_open = True
                else:
                    self.inventory_open = False

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
                    if self.diary_check == False:
                        self.diary_check = True
                        self.after_diary_story = True

    def A_room_screen(self,screen,character,diary_font,dialogue_font):
        screen.blit(self.floor,(350,160))
        screen.blit(self.wall,(350,80))
        screen.blit(self.bookshelf,(330,200))
        screen.blit(self.bookshelf,(630,200))
        screen.blit(self.diary,(600,350))
        screen.blit(self.desk,(553,110))
        

        if self.before_diary_story == True:
            story_box_1 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            story_text_1 = dialogue_font.render(self.before_diary_storylines[self.before_diary_index],True,'black')
            story_rect_1 = story_text_1.get_rect(center= story_box_1.center)
            screen.blit(story_text_1, story_rect_1)

        if self.after_diary_story == True:
            story_box_2 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            story_text_2 = dialogue_font.render(self.after_diary_storylines[self.after_diary_index],True,'black')
            story_rect_2 = story_text_2.get_rect(center= story_box_2.center)
            screen.blit(story_text_2, story_rect_2)
            

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

        if self.inventory and self.books_check == False:
            found_books = self.inventory[-1]
            books_genre = found_books[0]
            finding_books_rect = pygame.draw.rect(screen, 'white', (280,620,700,80))
            finding_texts = dialogue_font.render("You found a " + books_genre + " book.", True, 'black')
            finding_rect = finding_texts.get_rect(center = finding_books_rect.center)
            screen.blit(finding_texts,finding_rect)


        if self.after_bookshelves_story == True:
            story_box_3 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            story_text_3 = dialogue_font.render(self.after_bookshelves_storylines[self.after_bookshelves_index],True,'black')
            story_rect_3 = story_text_3.get_rect(center= story_box_3.center)
            screen.blit(story_text_3, story_rect_3)

        if self.before_desk_story == True:
            story_box_4 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            story_text_4 = dialogue_font.render(self.before_desk_storylines[self.before_desk_index],True,'black')
            story_rect_4 = story_text_4.get_rect(center= story_box_4.center)
            screen.blit(story_text_4, story_rect_4)
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
