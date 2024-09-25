import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Journey to Hope")

font = pygame.font.Font(None, 74)
input_font = pygame.font.Font(None, 50)

background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
background_music = pygame.mixer.Sound("background.mp3")
background_music.play(-1)

username = ""
input_active = False
input_box = pygame.Rect(screen_width // 2 - 100, 300, 200, 50)

def draw_intro_screen():
    screen.blit(background_image, (0, 0))
    title_text = font.render("Journey to Hope", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
    pygame.draw.rect(screen, (0, 0, 0), input_box)
    input_text = input_font.render(username, True, (255, 255, 255))
    screen.blit(input_text, (input_box.x + 10, input_box.y + 10))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    print(f"Username: {username}")
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

    draw_intro_screen()
