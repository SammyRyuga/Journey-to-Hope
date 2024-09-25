import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Transition to Level 1")

background_image = pygame.image.load("transition_background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
avatar_image = pygame.image.load("male_avatar.png") 
npc_image = pygame.image.load("npc.png")  

avatar_image = pygame.transform.scale(avatar_image, (100, 100))  
npc_image = pygame.transform.scale(npc_image, (100, 100))  

background_music = pygame.mixer.Sound("background.mp3")
background_music.play(-1)

avatar_rect = avatar_image.get_rect(center=(100, screen_height // 2))
npc_rect = npc_image.get_rect(center=(screen_width // 2, screen_height // 2))
dragging = False
conversation_active = False
font = pygame.font.Font(None, 35)  

dialogues = [
    "Hello! Welcome to your adventure!",
    "I, Eldiren, will be your guide through the Valley of Shadows.", 
    "Many challenges lie ahead, but I believe you can overcome them!",
    "You will face your fears and doubts.", 
    "It won't be easy, but remember,", 
    "facing your fears is the first step to overcoming them.",
    "Stay true to yourself and trust your instincts.",
    "You have the strength within you to navigate through darkness.",
    "Good luck on your journey! I’ll be here if you need guidance!"
]
current_dialogue = 0
dialogue_timer = 0
dialogue_duration = 2000  

def draw_transition_screen():
    screen.blit(background_image, (0, 0))
    screen.blit(avatar_image, avatar_rect.topleft)
    screen.blit(npc_image, npc_rect.topleft)
    if conversation_active:
        dialogue_text = font.render(dialogues[current_dialogue], True, (255, 255, 255))
        screen.blit(dialogue_text, (screen_width // 2 - dialogue_text.get_width() // 2, 50))
    pygame.display.flip()

while True:
    delta_time = pygame.time.Clock().tick(60)  # Get elapsed time in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if avatar_rect.collidepoint(event.pos):
                dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging:
                avatar_rect.center = event.pos
                avatar_rect.x = max(0, min(avatar_rect.x, screen_width - avatar_rect.width))
                avatar_rect.y = max(0, min(avatar_rect.y, screen_height - avatar_rect.height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        avatar_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        avatar_rect.x += 5
    if keys[pygame.K_UP]:
        avatar_rect.y -= 5
    if keys[pygame.K_DOWN]:
        avatar_rect.y += 5

    avatar_rect.x = max(0, min(avatar_rect.x, screen_width - avatar_rect.width))
    avatar_rect.y = max(0, min(avatar_rect.y, screen_height - avatar_rect.height))

    if avatar_rect.colliderect(npc_rect):
        conversation_active = True
        dialogue_timer += delta_time  

        if dialogue_timer >= dialogue_duration:
            current_dialogue += 1
            dialogue_timer = 0
            if current_dialogue >= len(dialogues):
                conversation_active = False
                current_dialogue = 0

    draw_transition_screen()
