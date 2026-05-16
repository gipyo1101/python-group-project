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


#gipyo
class A_room():
    def __init__(self,floor, wall, bookshelf, diary, desk):
        self.floor = floor
        self.wall = wall
        self.bookshelf = bookshelf
        self.diary = diary
        self.desk = desk 
        self.books = [('Economics',2001),("Astronomy", 2004),
                      ('Mathematics',2013),("Fantasy", 1995), 
                      ('Computer Science',2006),("History", 1978),
                      ('Biography',1997),("Romance", 1982)]
        self.bookshelves_rect = [pygame.Rect(360, 320, 90, 30), pygame.Rect(480, 320, 90, 30), 
                                 pygame.Rect(660, 320, 90, 30), pygame.Rect(780, 320, 90, 30),  
                                 pygame.Rect(360, 450, 90, 30), pygame.Rect(480, 450, 90, 30),  
                                 pygame.Rect(660, 450, 90, 30), pygame.Rect(780, 450, 90, 30)]
        
        self.genres = ['Economics', 'Astronomy',
                       'Mathematics','Fantasy',
                       'Computer Science','History',
                       'Biography','Romance']       
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
                                       "Let's go there.",
                                       "Press F near the desk.",
                                       "Press Enter to enter the password."]
        self.before_desk_index = 0
        self.desk_rect = pygame.Rect(560, 150, 110, 60)
        self.desk_check = False
        self.desk_input = ""
        self.after_desk_check = False
        self.password = '7'
        
    def event(self,event,character):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  
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

                if character.feet_hitbox().colliderect(self.diary_rect):
                    self.diary_open = True
                
                if character.feet_hitbox().colliderect(self.desk_rect):
                    self.desk_check = True
                                
            
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
            
            if self.desk_check == True:
                if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    if len(self.desk_input) < 4:
                        self.desk_input += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    self.desk_input = self.desk_input[:-1]
                
                if event.key == pygame.K_RETURN: # enter key
                    if self.desk_input == self.get_password(self.inventory):
                        self.desk_check = False
                        self.after_desk_check = True
                    else:
                        self.desk_input = ""



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

        if self.desk_check == True:
            story_box_5 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            story_text_5 = dialogue_font.render('Take the last digit:',True,'black')
            screen.blit(story_text_5, (240,645))
            desk_input_screen = self.desk_input.ljust(4,'_')
            desk_input_screen = ' '.join(desk_input_screen)
            desk_input_text = dialogue_font.render(desk_input_screen,True,'black')
            screen.blit(desk_input_text, (550, 650))

        if self.after_desk_check == True:
            story_box_6 = pygame.draw.rect(screen, 'white', (130,620,1000,80))
            finding_password_1 = dialogue_font.render('You found a first digit of the exit password: 7',True,'black')
            story_rect_6 = finding_password_1.get_rect(center= story_box_6.center)
            screen.blit(finding_password_1,story_rect_6)
            

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
        clue_genre = ('History','Fantasy','Astronomy','Romance')
        books_for_password = []
        for book in books:
            if book[0] in clue_genre:
                books_for_password.append(book)
        books_list = self.bubble_sort_years(books_for_password)
        password = ''.join(str(year)[-1] for pw, year in books_list)
        return password
#gipyo

# Fajr
class B_room():
    def __init__(self, floor, wall, bed, map_img):
        self.floor = floor
        self.wall = wall
        self.bed = bed
        self.map = map_img
        self.map_rect = pygame.Rect(400, 390, 140, 120)
        self.message_open = False
        self.message ="What is this? Press SPACE?"
    
    def event(self, event, character):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if character.feet_hitbox().colliderect(self.map_rect):
                    self.message_open = True 
    
    def B_room_screen(self, screen, font):
        B_floor_background = pygame.Surface((1280,720), pygame.SRCALPHA)
        B_wall_background = pygame.Surface((1000,80), pygame.SRCALPHA)
        for x in range(0,500,44):
           for y in range(0,400,20):
                B_floor_background.blit(self.floor,(x,y))

           for x in range(245,275,44):
                for y in range(80,140,20):
                    B_floor_background.blit(self.floor,(x,y))
          
           for x in range(0,500,44):
                B_wall_background.blit(self.wall,(x,0))


        screen.blit(B_floor_background,(350,160))
        screen.blit(B_wall_background,(350,80))
        pygame.draw.rect(screen, (193, 140, 92), (595, 80, 44, 80))
        screen.blit(self.map,(430,430))
        screen.blit(self.bed,(360,300))
    
        if self.message_open:
           pygame.draw.rect(screen,'white',(200,500,800,80))
           text = font.render(self.message,True,'black')
           screen.blit(text,(220,520))
#Fajr

#Hashim
class C_room():
    def __init__(self, loop_room, final_room, screen_images, button_images, large_screen_images):
        self.loop_room = loop_room
        self.final_room = final_room

        # Kept so main.py does not need major changes.
        self.screen_images = screen_images
        self.button_images = button_images
        self.large_screen_images = large_screen_images

        self.current_c_room = "C_start"
        self.solved = False
        self.exit_ready = False

        # Room C is now drawn at the same kind of scale as the rest of the game.
        self.room_x = 270
        self.room_y = 75
        self.room_w = 705
        self.room_h = 530

        # Safe spawn point inside Room C
        self.spawn_x = self.room_x + 350
        self.spawn_y = self.room_y + 360

        # Directed graph for the looping-door puzzle
        self.c_graph = {
            "C_start": {
                "left": "C_start",
                "middle": "C_start",
                "right": "C_one"
            },
            "C_one": {
                "left": "C_two",
                "middle": "C_start",
                "right": "C_start"
            },
            "C_two": {
                "left": "C_start",
                "middle": "C_final",
                "right": "C_start"
            },
            "C_final": {}
        }

        # DFS finds the correct route through the graph
        self.correct_path = self.find_path_to_final_room(self.c_graph, "C_start", "C_final")

        self.player_sequence = []
        self.message = "The first echo moves away. Press F near a door."

        # Door rectangles in the looping room
        self.left_door_rect = pygame.Rect(self.room_x + 100, self.room_y + 110, 100, 85)
        self.middle_door_rect = pygame.Rect(self.room_x + 305, self.room_y + 110, 100, 85)
        self.right_door_rect = pygame.Rect(self.room_x + 505, self.room_y + 110, 100, 85)

        # Bottom door back to centre room
        self.backroom_rect = pygame.Rect(self.room_x + 310, self.room_y + 480, 85, 35)

        # Final chamber button rectangles.
        # These are larger than the visual buttons so the player can stand near them and press E.
        self.button_rects = {
            "left": pygame.Rect(self.room_x + 190, self.room_y + 245, 105, 110),
            "middle": pygame.Rect(self.room_x + 300, self.room_y + 245, 105, 110),
            "right": pygame.Rect(self.room_x + 410, self.room_y + 245, 105, 110)
        }

        # Where the top-screen arrow overlays should appear.
        # These are aligned to the black screens in the top monitor row.
        self.screen_overlay_rects = {
            "left": pygame.Rect(self.room_x + 330, self.room_y + 165, 42, 24),
            "middle": pygame.Rect(self.room_x + 437, self.room_y + 165, 42, 24),
            "right": pygame.Rect(self.room_x + 225, self.room_y + 165, 42, 24)

        }

        # Where the button arrow overlays should appear.
        # These are aligned to the cream button faces.
        self.button_overlay_rects = {
            "left": pygame.Rect(self.room_x + 223, self.room_y + 243, 44, 28),
            "middle": pygame.Rect(self.room_x + 330, self.room_y + 247, 44, 28),
            "right": pygame.Rect(self.room_x + 437, self.room_y + 243, 44, 28)
        }

        # Where the final digit overlay should appear.
        # This is centred on the large screen.
        self.large_screen_digit_rect = pygame.Rect(self.room_x + 312, self.room_y + 304, 82, 82)

        # Room C movement area
        self.walkable = [
            pygame.Rect(self.room_x + 40, self.room_y + 185, self.room_w - 80, 300),
            pygame.Rect(self.room_x + 310, self.room_y + 455, 85, 60)
        ]

        # Set this to False after testing.
        self.debug_interactions = False

    def enter_room(self):
        self.exit_ready = False

        if self.solved == False:
            self.current_c_room = "C_start"
            self.player_sequence = []
            self.message = "The first echo moves away. Press F near a door."
    def find_path_to_final_room(self, graph, start, goal):
        visited = set()
        stack = [(start, [])]

        while stack:
            room, path = stack.pop()

            if room == goal:
                return path

            if room not in visited:
                visited.add(room)

                # Reversed order so DFS checks left first, then middle, then right
                for door in ["right", "middle", "left"]:
                    if door in graph[room]:
                        next_room = graph[room][door]
                        stack.append((next_room, path + [door]))

        return []

    def selected_door(self, character):
        feet = character.feet_hitbox()

        if feet.colliderect(self.left_door_rect):
            return "left"

        if feet.colliderect(self.middle_door_rect):
            return "middle"

        if feet.colliderect(self.right_door_rect):
            return "right"

        return None

    def selected_button(self, character):
        feet = character.feet_hitbox()

        for button_name in self.button_rects:
            if feet.colliderect(self.button_rects[button_name]):
                return button_name

        return None

    def choose_door(self, door, character):
        self.current_c_room = self.c_graph[self.current_c_room][door]
        character.set_position(self.spawn_x, self.spawn_y)

        if self.current_c_room == "C_start":
            self.message = "The doors repeat, but that path feels wrong."

        elif self.current_c_room == "C_one":
            self.message = "The next echo turns back."

        elif self.current_c_room == "C_two":
            self.message = "The last echo settles in the centre."

        elif self.current_c_room == "C_final":
            self.message = "The chamber asks you to repeat what the loop remembers. Press F on the buttons."

    def press_final_button(self, button):
        self.player_sequence.append(button)

        if self.player_sequence == self.correct_path[:len(self.player_sequence)]:
            if self.player_sequence == self.correct_path:
                self.solved = True
                self.message = "The loop accepts the sequence. The large screen reveals digit 3."
            else:
                self.message = "The machine accepts the echo. Continue the remembered path."
        else:
            self.player_sequence = []
            self.message = "The machine rejects the order. Try the remembered path again."

    def event(self, event, character):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:

                if self.current_c_room != "C_final":
                    chosen_door = self.selected_door(character)

                    if chosen_door is not None:
                        self.choose_door(chosen_door, character)

                else:
                    chosen_button = self.selected_button(character)

                    if chosen_button is not None and self.solved == False:
                        self.press_final_button(chosen_button)

    def draw_wrapped_text(self, screen, font, text, colour, box_rect, line_spacing=6):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = word if current_line == "" else current_line + " " + word
            test_surface = font.render(test_line, True, colour)

            if test_surface.get_width() <= box_rect.width - 30:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        total_height = len(lines) * font.get_height() + (len(lines) - 1) * line_spacing
        start_y = box_rect.y + (box_rect.height - total_height) // 2

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, colour)
            text_rect = text_surface.get_rect(centerx=box_rect.centerx)
            text_rect.y = start_y + i * (font.get_height() + line_spacing)
            screen.blit(text_surface, text_rect)

    def draw_arrow_overlay(self, screen, direction, rect, colour):
        x = rect.x
        y = rect.y
        w = rect.width
        h = rect.height

        if direction == "left":
            shaft = pygame.Rect(
                int(x + w * 0.35),
                int(y + h * 0.40),
                int(w * 0.40),
                int(h * 0.20)
            )
            head = [
                (int(x + w * 0.20), int(y + h * 0.50)),
                (int(x + w * 0.42), int(y + h * 0.22)),
                (int(x + w * 0.42), int(y + h * 0.78))
            ]

        elif direction == "right":
            shaft = pygame.Rect(
                int(x + w * 0.25),
                int(y + h * 0.40),
                int(w * 0.40),
                int(h * 0.20)
            )
            head = [
                (int(x + w * 0.80), int(y + h * 0.50)),
                (int(x + w * 0.58), int(y + h * 0.22)),
                (int(x + w * 0.58), int(y + h * 0.78))
            ]

        else:
            # middle is shown visually as an up arrow
            shaft = pygame.Rect(
                int(x + w * 0.40),
                int(y + h * 0.35),
                int(w * 0.20),
                int(h * 0.40)
            )
            head = [
                (int(x + w * 0.50), int(y + h * 0.15)),
                (int(x + w * 0.22), int(y + h * 0.42)),
                (int(x + w * 0.78), int(y + h * 0.42))
            ]

        pygame.draw.rect(screen, colour, shaft)
        pygame.draw.polygon(screen, colour, head)

    def draw_screen_arrow(self, screen, direction, rect):
        glow_colour = (60, 120, 20)
        bright_colour = (140, 255, 60)

        bigger_rect = pygame.Rect(
            rect.x - 2,
            rect.y - 2,
            rect.width + 4,
            rect.height + 4
        )

        self.draw_arrow_overlay(screen, direction, bigger_rect, glow_colour)
        self.draw_arrow_overlay(screen, direction, rect, bright_colour)

    def draw_button_arrow(self, screen, direction, rect):
        shadow_colour = (120, 95, 65)
        main_colour = (210, 190, 150)

        shadow_rect = pygame.Rect(
            rect.x + 2,
            rect.y + 2,
            rect.width,
            rect.height
        )

        self.draw_arrow_overlay(screen, direction, shadow_rect, shadow_colour)
        self.draw_arrow_overlay(screen, direction, rect, main_colour)

    def draw_digit_3(self, screen):
        font = pygame.font.SysFont("arial", 52, bold=True)
        digit_colour = (140, 255, 60)
        glow_colour = (60, 120, 20)

        glow_surface = font.render("3", True, glow_colour)
        glow_rect = glow_surface.get_rect(center=self.large_screen_digit_rect.center)
        screen.blit(glow_surface, (glow_rect.x + 2, glow_rect.y + 2))

        digit_surface = font.render("3", True, digit_colour)
        digit_rect = digit_surface.get_rect(center=self.large_screen_digit_rect.center)
        screen.blit(digit_surface, digit_rect)

    def draw_debug_rects(self, screen):
        # Red = loop-room doors
        pygame.draw.rect(screen, "red", self.left_door_rect, 2)
        pygame.draw.rect(screen, "red", self.middle_door_rect, 2)
        pygame.draw.rect(screen, "red", self.right_door_rect, 2)

        # Blue = final-room buttons
        for rect in self.button_rects.values():
            pygame.draw.rect(screen, "blue", rect, 2)

        # Green = exit/back door
        pygame.draw.rect(screen, "green", self.backroom_rect, 2)

    def C_room_screen(self, screen, font):
        if self.current_c_room == "C_final":
            screen.blit(self.final_room, (self.room_x, self.room_y))

            # Buttons always show what direction they represent
            self.draw_button_arrow(screen, "left", self.button_overlay_rects["left"])
            self.draw_button_arrow(screen, "middle", self.button_overlay_rects["middle"])
            self.draw_button_arrow(screen, "right", self.button_overlay_rects["right"])

            # Top screens reveal arrows based on correct button presses
            screen_order = ["right", "left", "middle"]

            for i in range(len(self.player_sequence)):
                if i < len(screen_order):
                    screen_position = screen_order[i]
                    chosen_direction = self.player_sequence[i]

                    self.draw_screen_arrow(
                        screen,
                        chosen_direction,
                        self.screen_overlay_rects[screen_position]
                    )

            # Large screen only shows 3 after solving
            if self.solved:
                self.draw_digit_3(screen)

        else:
            screen.blit(self.loop_room, (self.room_x, self.room_y))

        # Message box
        message_box = pygame.Rect(130, 620, 1000, 80)
        pygame.draw.rect(screen, "white", message_box)
        pygame.draw.rect(screen, "black", message_box, 2)
        self.draw_wrapped_text(screen, font, self.message, "black", message_box)

        if self.debug_interactions:
            self.draw_debug_rects(screen)

    def should_leave(self, character):
        touching_exit = character.feet_hitbox().colliderect(self.backroom_rect)

        if touching_exit == False:
            self.exit_ready = True
            return False
        if self.exit_ready == True and touching_exit == True:
            self.exit_ready = False
            return True

        return False
#Hashim