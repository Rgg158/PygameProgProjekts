import pygame
import sys
import random
import button_class
import edienu_list

pygame.init()

screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("HiHiHiHa")

end_img = pygame.image.load('end_btn.png').convert_alpha()
anim1_img = pygame.image.load('anim1_img.png').convert_alpha()
anim2_img = pygame.image.load('anim2_img.png').convert_alpha()
#anim3_img = pygame.image.load('anim3_img.png').convert_alpha()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

    
end_button = button_class.button(end_img, 1 )
first_animal = button_class.button(anim1_img, 0.27)
second_animal = button_class.button(anim2_img, 1.27)
#third_animal = button_class.button(500, 100, anim3_img, 1)
pdziv, pir = random.randint(0, 1), False
odziv, oir = random.randint(0, 1), False
tdziv, tir = random.randint(0, 1), False

score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.fill((110,150,57))
    #pirmā lokācija
    if pdziv == 0:
        if first_animal.draw(100, 100, screen):
            score += 1
    elif pdziv == 1:
        if second_animal.draw(100, 100, screen):
            score += 1
    #otrā lokācija
    if odziv == 0:
        if first_animal.draw(350, 100, screen):
            score += 1
    elif odziv == 1:
        if second_animal.draw(350, 100, screen):
            score += 1
    #trešā lokācija
    if tdziv == 0:
        if first_animal.draw(600, 100, screen):
            score += 1
    elif tdziv == 1:
        if second_animal.draw(600, 100, screen):
            score += 1


    draw_text("Score: " + str(score), pygame.font.SysFont('comicsans', 30), (0, 0, 0), 50, 50)

    if end_button.draw(850, 25, screen):
        run = False
        print("Your score is: " + str(score))
    pygame.display.update()
pygame.quit()
        
