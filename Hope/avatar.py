import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Choose Your Avatar")

# Load and scale images
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
male_avatar_image = pygame.image.load("male_avatar.png")
female_avatar_image = pygame.image.load("female_avatar.png")

male_avatar_image = pygame.transform.scale(male_avatar_image, (150, 150))
female_avatar_image = pygame.transform.scale(female_avatar_image, (150, 150))

background_music = pygame.mixer.Sound("background.mp3")
background_music.play(-1)

male_avatar_rect = male_avatar_image.get_rect(center=(screen_width // 3, screen_height // 2))
female_avatar_rect = female_avatar_image.get_rect(center=(2 * screen_width // 3, screen_height // 2))

selected_avatar = None
font = pygame.font.Font(None, 50)

def draw_avatar_screen():
    screen.blit(background_image, (0, 0))
    screen.blit(male_avatar_image, male_avatar_rect.topleft)
    screen.blit(female_avatar_image, female_avatar_rect.topleft)
    if selected_avatar:
        selected_text = font.render(f"Selected Avatar: {selected_avatar}", True, (255, 255, 255))
        screen.blit(selected_text, (screen_width // 2 - selected_text.get_width() // 2, 50))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if male_avatar_rect.collidepoint(event.pos):
                selected_avatar = "Male Avatar"
            elif female_avatar_rect.collidepoint(event.pos):
                selected_avatar = "Female Avatar"
            print(f"Selected Avatar: {selected_avatar}")

    draw_avatar_screen()
