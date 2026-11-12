import pygame
pygame.init()

#constants & variables settings
main_width = 800
main_height = 600
phase = 0
intro_phase = 0

#lists (?)
schedule = []

main_screen = pygame.display.set_mode((main_width, main_height))
pygame.display.set_caption("WHFT 1.0 Testing")

#pics loadingggg
starting_bg = pygame.image.load("starting_bg.png")
starting_btn = pygame.image.load("starting_btn.png")

intro_bg_1 = pygame.image.load("intro1.png")
intro_bg_2 = pygame.image.load("intro2.png")
intro_bg_3 = pygame.image.load("intro3.png") #kiera's note: lets say we have 3 pics for intro for now

#selection stuff
selection_bg = pygame.image.load("selection_bg.png")
option_1 = pygame.image.load("option_1.png")
option_2 = pygame.image.load("option_2.png")
#I am putting in only work session and hang out session for 1 character for now, but adding more is mostly manual labor so

#tbc...

#rect loading
starting_btn_rect = starting_btn.get_rect()
starting_btn_rect.center = (main_width // 2, main_height // 2)
option_1_rect = option_1.get_rect()
option_1_rect.center = (main_width // 4, main_height // 2)
option_2_rect = option_2.get_rect()
option_2_rect.center = (3*main_width // 4, main_height // 2)

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
                     
        if phase == 0:
            main_screen.blit(starting_bg, (0, 0))
            main_screen.blit(starting_btn, starting_btn_rect)
            if event.event.type == pygame.MOUSEBUTTONDOWN:
                if starting_btn_rect.collidepoint(event.pos):
                    print("game_starteddddddddd^^")
                    phase = 1 #lets gooooo

        if phase == 1:
            main_screen.blit(intro_bg_1, (0, 0))
            if event.type == pygame.KEYDOWN: and event.key == pygame.K_SPACE: or event.type == pygame.MOUSEBUTTONDOWN:
               main_screen.blit(intro_bg_2, (0, 0))
               intro_phase += 1
            if intro_phase == 1:
                main_screen.blit(intro_bg_2, (0, 0))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                    main_screen.blit(intro_bg_3, (0, 0))
                    phase = 2 #enter main gane -- or lets say pick your poison!
        if phase == 2:
            main_screen.blit(selection_bg, (0, 0))
            main_screen.blit(option_1, option_1_rect)
            main_screen.blit(option_2, option_2_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_1_rect.collidepoint(event.pos):
                    print("option 1 selected")
                    schedule.append("work session")
                    
                elif option_2_rect.collidepoint(event.pos):
                    print("option 2 selected")
                    schedule.append("hang out")
                    
            if len(schedule) == 7:
                print("schedule is now: ", schedule)
                phase = 3

    
    pygame.display.flip()