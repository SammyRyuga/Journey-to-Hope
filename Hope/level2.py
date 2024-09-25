import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level 1: Wise Man's Conversation")

# Load background and music
background_image = pygame.image.load("forest_background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Music
background_music = pygame.mixer.Sound("level2_music.mp3")
background_music.play(-1)

font = pygame.font.Font(None, 28)

# Player avatar
player_avatar = pygame.image.load("male_avatar.png")
player_avatar = pygame.transform.scale(player_avatar, (50, 50))
player_x, player_y = 100, 100
player_speed = 1

# NPC Wise Man
npc_sage = pygame.image.load("npc.png")
npc_sage = pygame.transform.scale(npc_sage, (80, 80))
npc_x, npc_y = 600, 400

# Maze walls (rectangles for simplicity)
walls = [
    pygame.Rect(200, 100, 400, 30),  # Horizontal wall
    pygame.Rect(200, 200, 30, 300),  # Vertical wall
    pygame.Rect(400, 300, 30, 300),
    pygame.Rect(0, 450, 300, 30),
    pygame.Rect(500, 0, 30, 250)
]

# Dialogue flags
show_dialogue = False
show_choices = False
dialogue_text = ""
active_choice = 1
dialogue_step = 0  # Track conversation progression

def draw_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

def proceed_to_level_3():
    # Placeholder for Level 3 logic. You can replace this with your actual Level 3 code.
    print("Proceed to Level 3")  # Placeholder action
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if show_choices:
                if event.key == pygame.K_1:
                    if dialogue_step == 0:
                        dialogue_text = "It’s okay to feel that way. Sometimes, it’s hard to remember that tunnels have exits."
                    elif dialogue_step == 1:
                        dialogue_text = "I'm really sorry to hear that. It must be exhausting to lie awake like that. Sometimes, when our minds are racing, it can help to write down those thoughts before bed. Have you ever tried that, or maybe some calming activities to help settle your mind? Try that it might be helpful."
                    elif dialogue_step == 2:
                        dialogue_text = "I’m really glad you mentioned that. It’s important to acknowledge when you need help, and it shows strength. It would really help if you connect and share more about it with your friends, a therapist or even just someone who would listen. Remember, the journey of life is about exploration and discovery. Trust the process, and be kind to yourself along the way."
                    dialogue_step += 1
                elif event.key == pygame.K_2:
                    if dialogue_step == 0:
                        dialogue_text = "I’m happy to hear that."
                    elif dialogue_step == 1:
                        dialogue_text = "It’s great that you’ve been able to improve your sleep."
                    elif dialogue_step == 2:
                        dialogue_text = proceed_to_level_3()  # Move to Level 3 after conversation ends

            if dialogue_step == 3:
                proceed_to_level_3()

    # Player movement
    keys = pygame.key.get_pressed()
    if not show_dialogue:
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Ensure player stays on screen
        if player_x < 0: player_x = 0
        if player_x > screen_width - 50: player_x = screen_width - 50
        if player_y < 0: player_y = 0
        if player_y > screen_height - 50: player_y = screen_height - 50

        # Prevent player from passing through walls
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        for wall in walls:
            if player_rect.colliderect(wall):
                if keys[pygame.K_LEFT]: player_x += player_speed
                if keys[pygame.K_RIGHT]: player_x -= player_speed
                if keys[pygame.K_UP]: player_y += player_speed
                if keys[pygame.K_DOWN]: player_y -= player_speed

    # Detect collision with NPC
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    npc_rect = pygame.Rect(npc_x, npc_y, 80, 80)
    if player_rect.colliderect(npc_rect) and not show_dialogue:
        dialogue_text = "Are you lost? Do you feel like you are not worth anything?"
        show_dialogue = True
        show_choices = True

    # Rendering
    screen.blit(background_image, (0, 0))
    screen.blit(player_avatar, (player_x, player_y))
    screen.blit(npc_sage, (npc_x, npc_y))

    # Draw maze walls
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    # Display dialogue
    if show_dialogue:
        draw_text(dialogue_text, 20, 500)
        if show_choices:
            choice1 = "1. Yes, I do feel lost. Everything feels like a struggle. I don’t see any light at the end of the tunnel."
            choice2 = "2. No, I don’t feel that way. I feel everything is going just fine."
            draw_text(choice1, 20, 550)
            draw_text(choice2, 20, 580)

    pygame.display.update()
