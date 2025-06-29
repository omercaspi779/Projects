import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((1280, 659))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (1280, 659))
font = pygame.font.SysFont("Courier", 24)
large_font = pygame.font.SysFont("Courier", 48)
messages = [
    "Initializing hack...",
    "Accessing system...",
    "Bypassing security...",
    "Extracting data...",
    "Encrypting files...",
    "Planting malware...",
    "Hacking complete!",
]
running1 = True
while running1:
    screen.blit(background, (0, 0))
    subtitle_text = font.render("there are virus downloaded in your pc", True, GREEN)
    subtitle_rect = subtitle_text.get_rect(center=(1280 // 2, 659 - 400))
    screen.blit(subtitle_text, subtitle_rect)
    for i, message in enumerate(messages):
        text = font.render(message, True, GREEN)
        screen.blit(text, (50, 50 + i * 40))
        pygame.display.update()
        for _ in range(random.randint(10, 30)):
            x = random.randint(50, 1280 - 50)
            y = random.randint(50, 659 - 50)
            char = chr(random.randint(33, 126))
            text = font.render(char, True, GREEN)
            screen.blit(text, (x, y))
            pygame.display.update()
    text = large_font.render("You've been hacked!", True, RED)
    text_rect = text.get_rect(center=(1280 // 2, 659 // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(10)
    running1 = False
