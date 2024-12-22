import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fact or Fake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 48)

TIMER_LIMIT = 10
score = 0
penalty = 5

real_facts = [
    "The Earth revolves around the Sun.",
    "Water boils at 100 degrees Celsius at sea level.",
    "Humans have 206 bones in their adult bodies.",
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts.",
    "Honey never spoils.",
    "Sharks predate dinosaurs.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Mount Everest is not the closest point to space.",
    "Venus is the hottest planet in the solar system.",
    "The Amazon Rainforest produces 20% of the world’s oxygen.",
    "An octopus can regrow its arms.",
    "A day on Venus is longer than a year on Venus.",
    "Antarctica is the driest continent on Earth.",
    "The human body contains enough DNA to stretch to the sun and back.",
    "Whales are mammals, not fish.",
    "A snail can sleep for three years.",
    "The Sahara Desert can go years without rain.",
    "Sound travels faster in water than in air.",
    "Cats have fewer toes on their back paws than their front paws.",
    "Water is made up of two hydrogen atoms and one oxygen atom.",
    "The speed of light is approximately 299,792 kilometers per second.",
    "Lightning is hotter than the surface of the sun.",
    "Polar bears have black skin under their white fur.",
    "An ostrich's eye is bigger than its brain.",
    "Some turtles can breathe through their butts.",
    "The Eiffel Tower can grow taller in summer.",
    "Octopuses have blue blood.",
    "Butterflies can taste with their feet.",
    "Sloths can hold their breath longer than dolphins.",
    "Sea otters hold hands while they sleep to keep from drifting apart.",
    "A group of flamingos is called a flamboyance.",
    "Pineapples take about two years to grow.",
    "Humans share 98% of their DNA with chimpanzees.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "The average human body contains enough sulfur to kill all fleas on a dog.",
    "The longest recorded flight of a chicken is 13 seconds.",
    "The fingerprints of a koala are almost indistinguishable from humans.",
    "The world's oldest piece of chewing gum is over 9,000 years old.",
    "Wombat poop is cube-shaped."
]

false_facts = [
    "The Great Wall of China is visible from the Moon.",
    "Goldfish have a memory span of three seconds.",
    "Bulls are enraged by the color red.",
    "Humans use only 10% of their brains.",
    "Camels store water in their humps.",
    "Eating carrots improves night vision.",
    "Lightning never strikes the same place twice.",
    "Cracking knuckles causes arthritis.",
    "Earth is the only planet with water.",
    "Penguins can fly.",
    "Owls can turn their heads 360 degrees.",
    "The human heart stops beating during a sneeze.",
    "Dogs can see in complete darkness.",
    "Humans have more teeth than sharks.",
    "A goldfish turns black when it gets old.",
    "The moon is made of cheese.",
    "Tomatoes grow on trees.",
    "Bees can live for years.",
    "Rats are bigger than cats.",
    "A day on Mars is shorter than a day on Earth.",
    "Humans can breathe underwater naturally.",
    "The Earth is flat.",
    "Vaccines cause autism.",
    "Bats are blind.",
    "Dinosaurs and humans coexisted.",
    "Milk is naturally pink.",
    "Gold is the heaviest material on Earth.",
    "The internet is stored in the ocean.",
    "The sun revolves around the Earth.",
    "Eating bread crusts will make your hair curly.",
    "You can see the Great Wall of China from space.",
    "Humans can digest rocks.",
    "Drinking coffee stunts your growth.",
    "Hair grows faster when it's trimmed.",
    "Humans have more than five senses.",
    "The moon has its own atmosphere.",
    "Whales are fish.",
    "Humans can regrow limbs.",
    "Birds don't have bones.",
    "Chewing gum stays in your stomach for seven years."
]

presented_facts = []
def get_random_fact():
    available_facts = [fact for fact in real_facts + false_facts if fact not in presented_facts]
    if not available_facts:
        return "No more facts!", None
    is_real = random.choice([True, False])
    statement = random.choice(real_facts if is_real else false_facts)
    presented_facts.append(statement)
    return statement, is_real

running = True
clock = pygame.time.Clock()
game_started = False
current_statement, is_real = get_random_fact()
start_time = 0
animation_color = None
animation_start_time = None
verification_message = ""

button_width, button_height = 200, 50
button_x = WIDTH // 2 - button_width // 2
button_y = HEIGHT // 2 + 100

while running:
    screen.fill(WHITE)

    if not game_started:
        title_surface = LARGE_FONT.render("Welcome to Fact or Fake!", True, BLACK)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 4))

        instructions = [
            "Instructions:",
            "- Press 'T' if you think the statement is True.",
            "- Press 'F' if you think the statement is False.",
            "- Press 'V' to verify for a penalty.",
            "- Be quick! Answer Fast.",
            " 212125 (Damjan Kaloshev)™ && 214004 (Darko Vanevski)™",
        ]

        for i, line in enumerate(instructions):
            line_surface = FONT.render(line, True, BLACK)
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, HEIGHT // 3 + i * 40))

        pygame.draw.rect(screen, BLUE, (button_x, button_y, button_width, button_height))
        start_text = FONT.render("Start Game", True, WHITE)
        screen.blit(start_text, (button_x + button_width // 2 - start_text.get_width() // 2, button_y + button_height // 2 - start_text.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    game_started = True
                    start_time = time.time()
    else:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, TIMER_LIMIT - elapsed_time)

        statement_surface = FONT.render(current_statement, True, BLACK)
        screen.blit(statement_surface, (WIDTH // 2 - statement_surface.get_width() // 2, HEIGHT // 3))

        timer_surface = FONT.render(f"Time left: {int(remaining_time)}s", True, BLACK)
        screen.blit(timer_surface, (10, 10))

        score_color = GREEN if animation_color == 'green' else RED if animation_color == 'red' else BLACK
        score_surface = FONT.render(f"Score: {score}", True, score_color)
        screen.blit(score_surface, (WIDTH - 200, 10))

        if animation_start_time and time.time() - animation_start_time > 1:
            animation_color = None

        if verification_message:
            verification_surface = FONT.render(verification_message, True, GREEN if is_real else RED)
            screen.blit(verification_surface, (WIDTH // 2 - verification_surface.get_width() // 2, HEIGHT - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    if is_real:
                        score += 10
                        animation_color = 'green'
                    else:
                        score -= 10
                        animation_color = 'red'
                    animation_start_time = time.time()
                    current_statement, is_real = get_random_fact()
                    start_time = time.time()
                    verification_message = ""
                elif event.key == pygame.K_f:
                    if not is_real:
                        score += 10
                        animation_color = 'green'
                    else:
                        score -= 10
                        animation_color = 'red'
                    animation_start_time = time.time()
                    current_statement, is_real = get_random_fact()
                    start_time = time.time()
                    verification_message = ""
                elif event.key == pygame.K_v:
                    score -= penalty
                    verification_message = "The fact was correct" if is_real else "The fact was false"
                    animation_color = 'red'
                    animation_start_time = time.time()

        if score >= 200:
            game_started = False
            title_surface = LARGE_FONT.render("You Win! You are a well-informed person!", True, GREEN)
            screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
        elif score <= -200:
            game_started = False
            title_surface = LARGE_FONT.render("Game Over! You are not a well-informed person!", True, RED)
            screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        if remaining_time <= 0:
            score -= penalty
            animation_color = 'red'
            animation_start_time = time.time()
            current_statement, is_real = get_random_fact()
            start_time = time.time()
            verification_message = ""

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
