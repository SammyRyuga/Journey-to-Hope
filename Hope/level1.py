import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level 1: The Valley of Shadows")

# Load images and sound
background_image = pygame.image.load("level1_background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Music
background_music = pygame.mixer.Sound("level1_music.mp3")
background_music.play(-1)

font = pygame.font.Font(None, 28)
user_input = ""
show_input_box = False
consolation_message = ""
active_choice = 1
message_timer = 0

def draw_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

def level_2():
    print("Welcome to Level 2!")  # Placeholder for Level 2 logic
    # Implement Level 2 code here
    sys.exit()  # Remove this and replace with Level 2 code

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if show_input_box:
                if event.key == pygame.K_RETURN:
                    consolation_message = "Thank you for sharing. It's okay to feel this way."
                    show_input_box = False
                    message_timer = pygame.time.get_ticks()  # Start timer for message display
                    level_2()  # Immediately transition to Level 2
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
            else:
                if event.key == pygame.K_UP:
                    active_choice = 1
                elif event.key == pygame.K_DOWN:
                    active_choice = 2
                elif event.key == pygame.K_RETURN:
                    if active_choice == 1:
                        show_input_box = True
                    elif active_choice == 2:
                        consolation_message = "It's perfectly okay to just sit with your feelings."
                        message_timer = pygame.time.get_ticks()  # Start timer for message display
                        level_2()  # Immediately transition to Level 2

    screen.blit(background_image, (0, 0))
    
    npc_question = "Hello! I sense you’re feeling a bit down. Can you share what’s on your mind?"
    instructions = "Use UP/DOWN to select, ENTER to choose."
    choice1 = "1. If you want to talk about what’s on your mind, I’m here to listen."
    choice2 = "2. Or if you prefer, we can just sit in this together for a moment."

    draw_text(npc_question, 20, 20)
    draw_text(instructions, 20, 80)
    draw_text(choice1 if active_choice == 1 else "> " + choice1, 20, 120)
    draw_text(choice2 if active_choice == 2 else "> " + choice2, 20, 160)

    if show_input_box:
        input_box = pygame.Rect(20, 220, 400, 40)
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
        draw_text(user_input, 25, 225)

    if consolation_message:
        draw_text(consolation_message, 20, 280)

    if message_timer:
        current_time = pygame.time.get_ticks()
        if current_time - message_timer >= 3000:  # 3 seconds
            consolation_message = ""  # Clear message after 3 seconds
            message_timer = 0  # Reset timer

    pygame.display.flip()
