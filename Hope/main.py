import pygame
import sys
import intro
import avatar
import transition
import level1
import level2

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def intro():
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
    background_image = pygame.transform.scale(
        background_image, (screen_width, screen_height))
    background_music = pygame.mixer.Sound("background.mp3")
    background_music.play(-1)

    username = ""
    input_active = False
    input_box = pygame.Rect(screen_width // 2 - 100, 300, 200, 50)

    def draw_intro_screen():
        screen.blit(background_image, (0, 0))
        title_text = font.render("Journey to Hope", True, (255, 255, 255))
        screen.blit(title_text, (screen_width // 2 -
                    title_text.get_width() // 2, 100))
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
    pass


def avatar_screen():
    import pygame
    import sys

    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Choose Your Avatar")

    # Load and scale images
    background_image = pygame.image.load("background.jpg")
    background_image = pygame.transform.scale(
        background_image, (screen_width, screen_height))
    male_avatar_image = pygame.image.load("male_avatar.png")
    female_avatar_image = pygame.image.load("female_avatar.png")

    male_avatar_image = pygame.transform.scale(male_avatar_image, (150, 150))
    female_avatar_image = pygame.transform.scale(
        female_avatar_image, (150, 150))

    background_music = pygame.mixer.Sound("background.mp3")
    background_music.play(-1)

    male_avatar_rect = male_avatar_image.get_rect(
        center=(screen_width // 3, screen_height // 2))
    female_avatar_rect = female_avatar_image.get_rect(
        center=(2 * screen_width // 3, screen_height // 2))

    selected_avatar = None
    font = pygame.font.Font(None, 50)

    def draw_avatar_screen():
        screen.blit(background_image, (0, 0))
        screen.blit(male_avatar_image, male_avatar_rect.topleft)
        screen.blit(female_avatar_image, female_avatar_rect.topleft)
        if selected_avatar:
            selected_text = font.render(
                f"Selected Avatar: {selected_avatar}", True, (255, 255, 255))
            screen.blit(selected_text, (screen_width // 2 -
                        selected_text.get_width() // 2, 50))
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
    pass


def transition():
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
    pass


def level_1():
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
    pass


def level_2():
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
    pass


def main():
    pygame.mixer.music.play(-1)  # Loop background music
    intro()
    avatar_screen()
    transition()
    level_1()
    level_2()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
