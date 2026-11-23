import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cookie Clicker")


cookies = 0
clicked = False

clock = pygame.time.Clock()
running = True
wait = 0
rate_wait = 0

num_of_clickers = 0
clicker_boosts = 0
rate_wait = time.time()
num_of_grandmas = 0
num_of_ovens = 0
past_x = 0
past_y = 0
font = pygame.font.SysFont(None, 50)
def create_rects():
    global cookies, wait,clicked, num_of_clickers, clicker_boosts, num_of_grandmas, num_of_ovens, past_x, past_y,  font
    
    helper_font = pygame.font.SysFont(None, 35)
    descriptive_font = pygame.font.SysFont(None, 20)
    screen.fill((65, 105, 225))

    cookie = pygame.image.load("cookie_clicker/icons/Cookie.png").convert_alpha()
    cookie = pygame.transform.scale(cookie, (500, 500))
    cookie_rect = cookie.get_rect(center =(200, 200))
    

    cookie_count = font.render(f"Cookies: {cookies}", True, (0, 0, 0))
    cookie_text = screen.blit(cookie_count, cookie_count.get_rect(center = (175, 50)))

    pygame.draw.line(screen, (150, 150, 150), (450, 600), (450, 0), width = 4)

    first_block = pygame.draw.rect(screen, (150, 75, 0), (450, 0, 400, 100))

    
    if time.time() - rate_wait > 1: change_cookies_with_rates()

    if num_of_clickers < 25 and cookies >= 2: 
        first_block = pygame.draw.rect(screen, (150, 90, 0), (450, 0, 400, 100))
        
        if first_block.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not clicked and time.time() - wait > 0.3:
            cookies -= 2
            
            screen.blit(font.render("-2$", True, (200, 0, 0)), (200, 200))
            num_of_clickers += 1 
            clicked = True
            wait = time.time()
        elif event.type == pygame.MOUSEBUTTONUP and time.time() - wait > 0.3: clicked = False
    else: first_block = pygame.draw.rect(screen, (150, 50, 0), (450, 0, 400, 100))



    clickers_text = helper_font.render(f"Cookie clickers - {num_of_clickers}", True, (200, 200, 200))
    clickers_text = screen.blit(clickers_text, (495, 0))

    clickers_descriptive_text = descriptive_font.render("These helpful friends increase your", True, (200, 200, 200))
    clickers_descriptive_text = screen.blit(clickers_descriptive_text, (495, 40))

    clickers_descriptive_text2 = descriptive_font.render("automated return rate on cookies by", True, (200, 200, 200))
    clickers_descriptive_text2 = screen.blit(clickers_descriptive_text2, (495, 60))

    clickers_descriptive_text3 = descriptive_font.render("1 cookie per second. Cost 2 cookies.", True, (200, 200, 200))
    clickers_descriptive_text3 = screen.blit(clickers_descriptive_text3, (495, 80))

    if clicker_boosts < 4 and cookies >= 500: 
        second_block = pygame.draw.rect(screen, (150, 90, 0), (450, 110, 400, 100))
        
        if second_block.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not clicked and time.time() - wait > 0.3:
            cookies -= 500
            
            screen.blit(font.render("-500$", True, (200, 0, 0)), (200, 200))
            clicker_boosts += 1 
            clicked = True
            wait = time.time()
        elif event.type == pygame.MOUSEBUTTONUP and time.time() - wait > 0.3: clicked = False
    else: second_block = pygame.draw.rect(screen, (150, 50, 0), (450, 110, 400, 100))

    two_x = pygame.image.load("cookie_clicker/icons/2x.png").convert_alpha()
    two_x = pygame.transform.scale(two_x, (50, 50))
    two_x_rect = two_x.get_rect(center =(470, 160))
    screen.blit(two_x, two_x_rect)
    
    clicker_boost_title = helper_font.render(f"Clicker boosts - {clicker_boosts}", True, (200, 200, 200))
    clicker_boost_title = screen.blit(clicker_boost_title, (495, 110))

    clickers_boost_text = descriptive_font.render("These boosts help your little guys", True, (200, 200, 200))
    clickers_boost_text = screen.blit(clickers_boost_text, (495, 150))

    clickers_boost_text2 = descriptive_font.render("by 2 TIMES. Max 4 boosts for ", True, (200, 200, 200))
    clickers_boost_text2 = screen.blit(clickers_boost_text2, (495, 170))

    clickers_boost_text3 = descriptive_font.render("clickers. Cost 500 cookies each.", True, (200, 200, 200))
    clickers_boost_text3 = screen.blit(clickers_boost_text3, (495, 190))

    if num_of_grandmas < 5 and cookies >= 2500: 
        third_block = pygame.draw.rect(screen, (150, 90, 0), (450, 220, 400, 100))
        
        if third_block.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not clicked and time.time() - wait > 0.3:
            cookies -= 2500
            
            screen.blit(font.render("-2500$", True, (200, 0, 0)), (200, 200))
            num_of_grandmas += 1 
            clicked = True
            wait = time.time()
        elif event.type == pygame.MOUSEBUTTONUP and time.time() - wait > 0.3: clicked = False
    else: third_block = pygame.draw.rect(screen, (150, 50, 0), (450, 220, 400, 100))

    grandma = pygame.image.load("cookie_clicker/icons/Pixelated Grandma Baker (1).png").convert_alpha()
    grandma = pygame.transform.scale(grandma, (75, 75))
    grandma_rect = grandma.get_rect(center = (470, 270))
    screen.blit(grandma, grandma_rect)

    grandma_title = helper_font.render(f"Grandma Bakers - {num_of_grandmas}", True, (200, 200, 200))
    grandma_title = screen.blit(grandma_title, (495, 220))

    grandma_text = descriptive_font.render("These bakers produce 25 ", True, (200, 200, 200))
    grandma_text = screen.blit(grandma_text, (495, 260))

    grandma_text2 = descriptive_font.render("cookies per second. Max 5 grandmas ", True, (200, 200, 200))
    grandma_text2 = screen.blit(grandma_text2, (495, 280))

    grandma_text3 = descriptive_font.render("for baking. Cost 2500 cookies each.", True, (200, 200, 200))
    grandma_text3 = screen.blit(grandma_text3, (495, 300))

    if num_of_ovens <= 9 and cookies >= 10000: 
        fourth_block = pygame.draw.rect(screen, (150, 90, 0), (450, 330, 400, 100))
        
        if fourth_block.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not clicked and time.time() - wait > 0.3:
            cookies -= 10000
            
            screen.blit(font.render("-100000$", True, (200, 0, 0)), (200, 200))
            num_of_ovens += 1 
            clicked = True
            wait = time.time()
        elif event.type == pygame.MOUSEBUTTONUP and time.time() - wait > 0.3: clicked = False
    else: fourth_block = pygame.draw.rect(screen, (150, 50, 0), (450, 330, 400, 100))

    ovens_title = helper_font.render(f"Powerful Ovens - {num_of_ovens}", True, (200, 200, 200))
    ovens_title = screen.blit(ovens_title, (495, 330))

    ovens_text = descriptive_font.render("These efficient ovens produce 100 ", True, (200, 200, 200))
    ovens_text = screen.blit(ovens_text, (495, 370))

    ovens_text2 = descriptive_font.render("cookies per second. Max 10 ovens ", True, (200, 200, 200))
    ovens_text2 = screen.blit(ovens_text2, (495, 390))

    ovens_text3 = descriptive_font.render("for baking. Cost 10,000 cookies each.", True, (200, 200, 200))
    ovens_text3 = screen.blit(ovens_text3, (495, 410))
    
    oven = pygame.image.load("cookie_clicker/icons/Pixelated Oven Image.png").convert_alpha()
    oven = pygame.transform.scale(oven, (80, 80))
    oven_rect = oven.get_rect(center = (470, 380))
    screen.blit(oven, oven_rect)

    clicker = pygame.image.load("cookie_clicker/icons/cookie_clicker.png").convert_alpha()
    clicker = pygame.transform.scale(clicker, (100, 100))
    clicker_rect = clicker.get_rect(center = (470, 50))
    screen.blit(clicker, clicker_rect)

    if cookie_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(cookie, cookie_rect)
        if (time.time() - wait) < 0.5:
            if not clicked: 
                money_increase = font.render(f"+{num_of_clickers * (2 ** clicker_boosts) + num_of_grandmas * 25 if num_of_clickers > 0 else 1}$", True, (0, 225, 0))
                
                money = screen.blit(money_increase, (past_x, past_y - (time.time() - wait) * 250))
        elif event.type == pygame.MOUSEBUTTONUP and time.time() - wait > 0.3:
            clicked = False
        elif event.type == pygame.MOUSEBUTTONDOWN and time.time() - wait > 0.3 and not clicked:
            if num_of_clickers == 0: 
                cookies += 1
                money_increase = font.render(f"+1$", True, (0, 225, 0))
                money = screen.blit(money_increase, (pygame.mouse.get_pos()))
                past_x = pygame.mouse.get_pos()[0]
                past_y = pygame.mouse.get_pos()[1]
            else: 
                money_increase = font.render(f"+{num_of_clickers * (2 ** clicker_boosts) + num_of_grandmas * 25 if clicker_boosts > 0 else num_of_clickers + num_of_grandmas * 25}$", True, (0, 200, 0))
                cookies += num_of_clickers * (2 ** clicker_boosts) + num_of_grandmas * 25 if clicker_boosts > 0 else num_of_clickers + num_of_grandmas * 25
            clicked = True
            
            money = screen.blit(money_increase, (pygame.mouse.get_pos()[0], 200))
            wait = time.time()
    else: 
        cookie = pygame.transform.scale(cookie, (400, 400))
        screen.blit(cookie, cookie_rect)
def change_cookies_with_rates():
    global cookies, rate_wait, clicker_boosts
    cookies += num_of_clickers * (2 ** clicker_boosts) if clicker_boosts > 0 else num_of_clickers
    cookies += num_of_grandmas * 25 + num_of_ovens * 100
    rate_wait = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if cookies < 100000:
        create_rects()
    else: 
        screen.fill((255, 255, 255))
        congrats = pygame.image.load("cookie_clicker/icons/Congratulations.png").convert_alpha()
        congrats = pygame.transform.scale(congrats, (300, 300))
        congrats_rect = congrats.get_rect(center = (400, 300))
        screen.blit(congrats, congrats_rect)
        final_text = font.render(f"You have successfully reached 100k!", True, (0, 225, 0))
        screen.blit(final_text, (100, 450))
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
