import pygame
import json
import math
import os
from network import *
import random
from code_injector import main
import webbrowser
pygame.init()
global current_user
global current_username
global attack_counter
global damage_applied_dos
global damage_applied_dnf
global damage_applied_code
damage_applied_dnf = False
damage_applied_dos = False
damage_applied_code = False
global data
data = ""
global data2
data2 = ""
damage_applied = False
global done_hack
done_hack = False
global done_data
done_data = False
attack_counter = 0
global system_life
global timer_done_sent
timer_done_sent = False
system_life = 100
pygame.mixer.init()
global sound_effect
sound_effect = pygame.mixer.Sound("error.mp3")
sound_effect2 = pygame.mixer.Sound("Binary Code - Interface Sound Effects  Sci-Fi Computer Beeps & Data Processing Sounds.mp3")
sound_effect3 = pygame.mixer.Sound("Welcome to the Game - Hacking Alert.mp3")
sound_effect4 = pygame.mixer.Sound("Futuristic interface  HUD sound effects.mp3")
sound_effect5 = pygame.mixer.Sound("1.mp3")
SCREEN_HEIGHT = 659
SCREEN_WIDTH = 1280
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
name = 'Crest'
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption(name)
back_img = pygame.image.load("רקע.jpg")
back_img = pygame.transform.scale(back_img, screen_size)
icon_ = pygame.image.load('icon_.jpg')
pygame.display.set_icon(icon_)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont_2 = pygame.font.SysFont('Marlett', 130)
smallfont_3 = pygame.font.SysFont('ebrima', 64)
smallfont_4 = pygame.font.SysFont('Corbel', 40)
smallfont_5 = pygame.font.SysFont('Corbel', 25)
welcome_text = smallfont_2.render(f'welcome to {name}', True, (135, 206, 235))
welcome_text_2 = smallfont_3.render('to start the game please log in or sign up', True, (135, 206, 235))
screen_center_x = SCREEN_WIDTH // 2
screen_center_y = SCREEN_HEIGHT // 2
button_width = 200
button_height = 100
button_x = screen_center_x - button_width // 2
button_y = screen_center_y - button_height // 2
global running
running = True
n = Network()
global target_ip
global current_attack
global target_user
global clients_connected
global turn_name
global attack_sender
attack_sender = ""
global clients
global clients_play
clients_play = 0
class Button:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def drew_text(self, text, font, font_size, color_):
        font_ = pygame.font.SysFont('Marlett', font_size)
        text_ = font_.render(text, True, color_)
        text_rect = text_.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_, text_rect)

    def mouse_over_button(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def drew_rec(self, mouse_over_button):
        if mouse_over_button:
            icon = pygame.image.load("button.png")
            icon = pygame.transform.scale(icon, (self.width, self.height))
            icon_rect = icon.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(icon, icon_rect)
        else:
            icon = pygame.image.load("noBackground.png")
            icon = pygame.transform.scale(icon, (self.width, self.height))
            icon_rect = icon.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(icon, icon_rect)


class Coustum_button:
    def __init__(self, width, height, x, y, icon):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.icon = icon
    def drew_icon(self):
        icon_rect = self.icon.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(self.icon, icon_rect)
    def drew_rec(self):
        screen.blit(self.icon, (self.x, self.y))


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.level = "1"
        self.points = 14
        self.connected = False
        self.ip = n.get_target_ip()

    def get_user_name(self):
        return self.user_name
    def get_password(self):
        return self.password
    def set_user_name(self, user_name):
        self.user_name = user_name
    def set_password(self, password):
        self.password = password
    def get_connected(self):
        return self.connected
    def set_connected(self, connect):
        self.connected = connect
    def get_points(self):
        return self.points
    def get_ip(self):
        return self.ip
    def save_data(self):
        data = []
        user_exists = False
        if os.path.isfile('users_data.json') and os.path.getsize('users_data.json') > 0:
            with open('users_data.json', "r") as f:
                existing_data = json.load(f)
                for user in existing_data:
                    if user["username"] == self.user_name:
                        user["gameLevel"] = self.level
                        user["gamePoints"] = self.points
                        user_exists = True
                    else:
                        data.append(user)
        if not user_exists:
            new_user_data = {
                "username": self.user_name,
                "password": self.password,
                "gameLevel": self.level,
                "gamePoints": self.points,
                "ip": self.ip
            }
            data.append(new_user_data)
        with open('users_data.json', "w") as f:
            json.dump(data, f, indent=4)

    def load_data_to_user_variables(self):
        with open("users_data.json", "r") as f:
            data = json.load(f)
            for user in data:
                if user["username"] == self.user_name:
                    self.user_name = user["username"]
                    self.password = user["password"]
                    self.level = user["gameLevel"]
                    self.points = user["gamePoints"]
                    self.ip = user["ip"]

    def connect(self):
        self.connected = True

    def add_point(self):
        self.points += 1

    def print_details(self):
        print(f"{self.user_name}, {self.password}, {self.level}, {self.points}, {self.ip}")

class TextBox:
    def __init__(self, x, y, width, height, font, user_text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)
        self.user_text = user_text
        self.font = font
        self.active = True

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, 2)
"""
start_button = Button(button_width, button_height, button_x, button_y + 100)
start_button.drew_rec(start_button.mouse_over_button(mouse_pos))
start_button.drew_text('START', 'Corbel', 35, color)
"""
def is_mouse_on_circle(mouse_pos, circle_pos, circle_radius):
    distance = math.sqrt((mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2)
    return distance <= circle_radius


def load_data():
    if os.path.isfile('users_data.json') and os.path.getsize('users_data.json') > 0:
        with open("users_data.json", "r") as f:
            data = json.load(f)
            for user_data in data:
                user = User(user_data["username"], user_data["password"])
                users.append(user)


global users
users = []
global username_text_log_in
username_text_log_in = ''
global password_text_log_in
password_text_log_in = ''
global confirm_username_log_in
confirm_username_log_in = False
global confirm_password_log_in
confirm_password_log_in = False
global new_text_log_in
new_text_log_in = ''
global new_text_log_in_
new_text_log_in_ = ''
global username_text_sign_up
username_text_sign_up = ''
global password_text_sign_up
password_text_sign_up = ''
global confirm_username_sign_up
confirm_username_sign_up = False
global confirm_password_sign_up
confirm_password_sign_up = False
global new_text_sign_up
new_text_sign_up = ''
global new_text_sign_up_
new_text_sign_up_ = ''
global username_text_war
username_text_war = ''
global password_text_war
password_text_war = ''
global confirm_username_war
confirm_username_war = False
global confirm_password_war
confirm_password_war = False
global new_text_war
new_text_war = ''
global new_text_war_
new_text_war_ = ''
global c
c = False


def firewall_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
        "Firewalls are security systems designed to monitor and",
        "control incoming and outgoing network traffic based on",
        "predetermined security rules. They can be hardware-based or",
        "software-based and act as a barrier between a trusted",
        "internal network and untrusted external networks, such as",
        "the internet. Firewalls can prevent unauthorized access",
        "or from a private network and are essential for network security."
    ]

    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "firewall_data"


def antivirus_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
        "Antivirus software, also known as anti-malware software, is",
        "designed to detect, prevent, and remove malicious software",
        "(malware) from computers and networks. This includes viruses,",
        "worms, Trojans, spyware, adware, and more. Antivirus programs",
        "typically scan files or activities on a computer or network",
        "for patterns indicative of malicious code and then quarantine",
        "or remove the detected threats. They often include real-time",
        "protection to prevent malware infections in real-time."
    ]

    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "antivirus_data"


def network_scanning_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
        "Network scanning involves the use of specialized tools or",
        "software to identify and assess vulnerabilities and security",
        "weaknesses within a network. This can include scanning for",
        "open ports, misconfigured devices, outdated software, weak",
        "passwords, and other potential entry points for hackers.",
        "Network scanning is an essential part of network security",
        "practices and helps organizations identify and mitigate",
        "potential risks before they can be exploited by malicious actors."
    ]

    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "network_scanning_data"


def Intrusion_Detection_System_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: An intrusion detection system is a security tool",
    "that monitors network or system activities for malicious activities",
    "or policy violations.",
    "Uses: IDS detects and alerts administrators about potential",
    "security threats, such as suspicious traffic patterns, known",
    "attack signatures, or abnormal user behavior.",
    "Additional Information: IDS can be network-based or host-based",
    "and can operate in real-time or analyze log data retrospectively."
    ]

    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Intrusion_Detection_System_data"


def Data_Loss_Prevention_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: A Data Loss Prevention system is a security tool",
    "designed to prevent unauthorized access, use, or transmission",
    "of sensitive data.",
    "Uses: DLP systems monitor and control data in motion, data",
    "at rest, and data in use to prevent data breaches, leakage,",
    "or exfiltration.",
    "Additional Information: DLP solutions employ content inspection,",
    "contextual analysis, and policy enforcement to classify, protect,",
    "and remediate sensitive data across the organization's network",
    "and endpoints."
    ]
    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Data_Loss_Prevention_data"


def Security_Information_and_Event_Management_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: A Security Information and Event Management (SIEM)",
    "system is a technology that provides real-time analysis of security",
    "alerts generated by network hardware and applications.",
    "Uses: SIEM aggregates security data from various sources,",
    "correlates events, and provides centralized monitoring and reporting",
    "capabilities for cybersecurity professionals.",
    "Additional Information: SIEM solutions help organizations detect,",
    "investigate, and respond to security incidents more effectively",
    "by providing insights into potential threats and anomalies."
    ]
    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Security_Information_and_Event_Management_data"


def Blockchain_based_Security_Solutions_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: Blockchain-based security solutions leverage",
    "blockchain technology to secure critical systems, applications,",
    "and data against cyber threats.",
    "Uses: Blockchain offers immutable and decentralized security",
    "features that can enhance data integrity, authentication,",
    "and confidentiality, making it suitable for protecting against",
    "various cyber threats, including data tampering and identity theft.",
    "Additional Information: Blockchain-based security solutions are",
    "gaining traction in industries such as finance, healthcare, and",
    "supply chain management, where trust, transparency, and data",
    "integrity are paramount."
    ]
    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Blockchain_based_Security_Solutions_data"


def Endpoint_Detection_and_Response_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: EDR is a security solution that continuously",
    "monitors and responds to suspicious activities and threats",
    "on endpoint devices.",
    "Uses: EDR solutions provide real-time visibility into endpoint",
    "activities, allowing security teams to detect, investigate,",
    "and respond to security incidents more effectively.",
    "Additional Information: EDR solutions combine endpoint security",
    "with advanced threat detection capabilities, such as behavioral",
    "analysis, machine learning, and threat intelligence integration."
    ]
    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Endpoint_Detection_and_Response_data"


def Behavioral_Analytics_data_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("data.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    font = pygame.font.Font(None, 40)
    text_lines = [
    "Definition: Behavioral analytics uses machine learning algorithms",
    "to analyze patterns of user and entity behavior within an",
    "organization's network.",
    "Uses: Behavioral analytics can identify anomalous behavior indicative",
    "of potential security threats, such as insider threats, compromised",
    "accounts, or unusual network activity.",
    "Additional Information: By baselining normal behavior and detecting",
    "deviations, behavioral analytics solutions can help organizations",
    "detect and mitigate advanced attacks that traditional security",
    "measures may miss."
    ]
    y = 165
    for line in text_lines:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (200, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
        if event.type == pygame.QUIT:
            return 'quit'
    return "Behavioral_Analytics_data"


global sound_effect5_time
sound_effect5_time = sound_effect5.get_length()

global ti
ti = None


def run_timer(timer_duration, timer_start_time_):
    global sound_effect2
    WHITE = (255, 255, 255)
    if timer_start_time_ is None:
        timer_start_time_ = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - timer_start_time_) // 1000
    remaining_time = max(0, timer_duration - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {minutes:02d}:{seconds:02d}", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH // 2, 20))
    if remaining_time == 0:
        return "done"


def run_timer_1(timer_duration):
    global sound_effect5
    global ti
    WHITE = (255, 255, 255)
    if ti is None:
        ti = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - ti) // 1000
    remaining_time = max(0, timer_duration - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    if remaining_time == 0:
        return "done"


def intro_screen():
    global ti
    global sound_effect5_time
    screen.fill(BLACK)
    im = pygame.image.load("icon_.jpg")
    im = pygame.transform.scale(im, (200, 200))
    screen.blit(im, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))
    z = run_timer_1(2)
    if not pygame.mixer.Channel(0).get_busy():
        pygame.mixer.Channel(0).play(sound_effect5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
    if z == "done":
        return "start"
    return "intro_screen"


def start_screen():
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(back_img, (0, 0))
    log_in_button = Button(150, 50, 950, 10)
    log_in_button.drew_rec(log_in_button.mouse_over_button(mouse_pos))
    log_in_button.drew_text("log in", 'Corbel', 30, color)
    sign_up_button = Button(150, 50, 1110, 10)
    sign_up_button.drew_rec(sign_up_button.mouse_over_button(mouse_pos))
    sign_up_button.drew_text("sign up", 'Corbel', 30, color)
    screen.blit(welcome_text, (270, SCREEN_HEIGHT / 2 - 70))
    # screen.blit(welcome_text_2, (50, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if log_in_button.mouse_over_button(mouse_pos):
                return "log in"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sign_up_button.mouse_over_button(mouse_pos):
                return "sign up"
    return 'start'


def sign_up_screen():
    global sound_effect
    global users
    global username_text_sign_up
    global password_text_sign_up
    global confirm_username_sign_up
    global confirm_password_sign_up
    global new_text_sign_up
    global new_text_sign_up_
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(back_img, (0, 0))
    back_to_start_button = Button(150, 50, 1117, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to home", 'Corbel', 30, color)
    username_box = TextBox(200, 250, 1000, 50, smallfont_3, username_text_sign_up)
    password_box = TextBox(200, 450, 1000, 50, smallfont_3, password_text_sign_up)
    password_box.draw()
    password_text = smallfont_4.render(f'enter password:', True, color)
    screen.blit(password_text, (200, 380))
    username_box.draw()
    username_text_ = smallfont_4.render(f'enter username:', True, color)
    screen.blit(username_text_, (200, 180))
    load_data()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                username_text_sign_up = ''
                password_text_sign_up = ''
                new_text_sign_up = ''
                new_text_sign_up_ = ''
                confirm_username_sign_up = False
                confirm_password_sign_up = False
                return "start"
        if event.type == pygame.TEXTINPUT:
            if confirm_username_sign_up is False:
                new_text_sign_up += event.text
            elif confirm_password_sign_up is False:
                new_text_sign_up_ += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if confirm_username_sign_up is False:
                    try:
                        new_text_sign_up = new_text_sign_up[:-1]
                    except IndexError:
                        pass
                elif confirm_password_sign_up is False:
                    try:
                        new_text_sign_up_ = new_text_sign_up_[:-1]
                    except IndexError:
                        pass
            if event.key == pygame.K_RETURN:
                if confirm_username_sign_up is False and len(new_text_sign_up) > 0:
                    for user in users:
                        if new_text_sign_up == user.get_user_name():
                            sound_effect.play()
                            new_text_sign_up = ''
                            return 'sign up'
                    confirm_username_sign_up = True
                elif confirm_password_sign_up is False and len(new_text_sign_up_) > 0 and len(new_text_sign_up) > 0:
                    confirm_password_sign_up = True
                    user = User(username_text_sign_up, password_text_sign_up)
                    users.append(user)
                    user.save_data()
                    username_text_sign_up = ''
                    password_text_sign_up = ''
                    new_text_sign_up = ''
                    new_text_sign_up_ = ''
                    confirm_username_sign_up = False
                    confirm_password_sign_up = False
    text_width_ = smallfont_4.size(new_text_sign_up_)[0]
    if text_width_ <= 990 and confirm_password_sign_up is False:
        password_text_sign_up = new_text_sign_up_
    text_width_2 = smallfont_4.size(new_text_sign_up)[0]
    if text_width_2 <= 990 and confirm_username_sign_up is False:
        username_text_sign_up = new_text_sign_up

    text_3 = smallfont_4.render(password_text_sign_up, True, color)
    text_rect_ = text_3.get_rect(topleft=(password_box.rect.x + 5, password_box.rect.y + 5))
    if text_rect_.w <= 990:
        screen.blit(text_3, (password_box.rect.x + 5, password_box.rect.y + 8))
    text_2 = smallfont_4.render(username_text_sign_up, True, color)
    text_rect = text_2.get_rect(topleft=(username_box.rect.x + 5, username_box.rect.y + 5))
    if text_rect.w <= 990:
        screen.blit(text_2, (username_box.rect.x + 5, username_box.rect.y + 8))
    return 'sign up'


def log_in_screen():
    global c
    global sound_effect
    global users
    global username_text_log_in
    global password_text_log_in
    global confirm_username_log_in
    global confirm_password_log_in
    global new_text_log_in
    global new_text_log_in_
    global clients_connected
    clients_connected = n.get_clients_connected()
    global current_user
    global current_username
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(back_img, (0, 0))
    back_to_start_button = Button(150, 50, 1117, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to home", 'Corbel', 30, color)
    username_box_2 = TextBox(200, 250, 1000, 50, smallfont_3, username_text_log_in)
    password_box_2 = TextBox(200, 450, 1000, 50, smallfont_3, password_text_log_in)
    password_box_2.draw()
    password_text_2 = smallfont_4.render(f'enter password:', True, color)
    screen.blit(password_text_2, (200, 380))
    username_box_2.draw()
    username_text_2 = smallfont_4.render(f'enter username:', True, color)
    screen.blit(username_text_2, (200, 180))
    load_data()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            n.send("disconnect")
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                username_text_log_in = ''
                password_text_log_in = ''
                new_text_log_in = ''
                new_text_log_in_ = ''
                confirm_username_log_in = False
                confirm_password_log_in = False
                return "start"
        if event.type == pygame.TEXTINPUT:
            if confirm_username_log_in is False:
                new_text_log_in += event.text
            elif confirm_password_log_in is False:
                new_text_log_in_ += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if confirm_username_log_in is False:
                    try:
                        new_text_log_in = new_text_log_in[:-1]
                    except IndexError:
                        pass
                elif confirm_password_log_in is False:
                    try:
                        new_text_log_in_ = new_text_log_in_[:-1]
                    except IndexError:
                        pass
            if event.key == pygame.K_RETURN:
                if confirm_username_log_in is False and len(new_text_log_in) > 0:
                    confirm_username_log_in = True
                    confirm_password_log_in = False
                elif confirm_password_log_in is False and len(new_text_log_in_) > 0:
                    confirm_password_log_in = True
                    login_successful = False
                    for user in users:
                        if new_text_log_in == user.get_user_name() and new_text_log_in_ == user.get_password() and len(new_text_log_in_) > 0 and len(new_text_log_in) > 0:
                            if n.is_username_connected(user.get_user_name()):
                                sound_effect.play()
                                username_text_log_in = ''
                                password_text_log_in = ''
                                new_text_log_in = ''
                                new_text_log_in_ = ''
                                confirm_username_log_in = False
                                confirm_password_log_in = False
                                return 'log in'
                            else:
                                n.send(new_text_log_in)
                                user.connect()
                                current_username = user.get_user_name()
                                current_user = user
                                username_text_log_in = ''
                                password_text_log_in = ''
                                new_text_log_in = ''
                                new_text_log_in_ = ''
                                confirm_username_log_in = False
                                confirm_password_log_in = False
                                c = True
                                login_successful = True
                                return "start2"
                    if not login_successful:
                        sound_effect.play()
                        username_text_log_in = ''
                        password_text_log_in = ''
                        new_text_log_in = ''
                        new_text_log_in_ = ''
                        confirm_username_log_in = False
                        confirm_password_log_in = False
    text_width_2 = smallfont_4.size(new_text_log_in_)[0]
    if text_width_2 <= 990 and confirm_password_log_in is False:
        password_text_log_in = new_text_log_in_
    text_width2 = smallfont_4.size(new_text_log_in)[0]
    if text_width2 <= 990 and confirm_username_log_in is False:
        username_text_log_in = new_text_log_in

    text_5 = smallfont_4.render(password_text_log_in, True, color)
    text_rect_ = text_5.get_rect(topleft=(password_box_2.rect.x + 5, password_box_2.rect.y + 5))
    if text_rect_.w <= 990:
        screen.blit(text_5, (password_box_2.rect.x + 5, password_box_2.rect.y + 8))
    text_1 = smallfont_4.render(username_text_log_in, True, color)
    text_rect = text_1.get_rect(topleft=(username_box_2.rect.x + 5, username_box_2.rect.y + 5))
    if text_rect.w <= 990:
        screen.blit(text_1, (username_box_2.rect.x + 5, username_box_2.rect.y + 8))
    return 'log in'




def start_screen_2():
    global current_user
    global current_username
    global users
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(back_img, (0, 0))
    log_in_button = Button(button_width, button_height, 112, 292 - button_height)
    log_in_button.drew_rec(log_in_button.mouse_over_button(mouse_pos))
    log_in_button.drew_text("TRAINING", 'Corbel', 50, color)
    back_to_start_button = Button(button_width, button_height, 110, 322)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("LOG OUT", 'Corbel', 50, color)
    lobby_button = Button(button_width, button_height, 100, 452)
    lobby_button.drew_rec(lobby_button.mouse_over_button(mouse_pos))
    lobby_button.drew_text("LOBBY", 'Corbel', 50, color)
    load_data()
    if current_user.get_connected():
        text_width = smallfont_4.size(current_username)[0]
        user_name_text = smallfont_4.render(f'welcome! {current_username}', True, (135, 206, 235))
        screen.blit(user_name_text, (1130 - text_width - 150, 58))
    image = pygame.image.load("user.png")
    image = pygame.transform.scale(image, (100, 80))
    user_button = Coustum_button(150, 150, 1130, 5, image)
    user_button.drew_icon()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            n.send("disconnect")
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if log_in_button.mouse_over_button(mouse_pos):
                return "roadmap"
            if back_to_start_button.mouse_over_button(mouse_pos):
                current_user.set_connected(False)
                n.send("disconnect")  # Send a disconnect message to the server
                current_username = ""
                return "start"
            if lobby_button.mouse_over_button(mouse_pos):
                return "lobby"
    return 'start2'


def lobby():
    global clients
    global clients_play
    clients_play = n.get_clients_play()
    clients = n.get_connections()
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("רקע_2.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 10, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to home", 'Corbel', 30, color)
    font = pygame.font.Font(None, 35)
    text = font.render(f"number of players connected: {clients}", True, (255, 255, 255))
    screen.blit(text, (500, 130))
    log_in_button = Button(button_width, button_height, button_x, button_y + 100)
    log_in_button.drew_rec(log_in_button.mouse_over_button(mouse_pos))
    log_in_button.drew_text("play", 'Corbel', 50, color)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "start2"
            if log_in_button.mouse_over_button(mouse_pos):
                n.send("play")
                return "connect_screen"
        if event.type == pygame.QUIT:
            n.send("disconnect")
            return 'quit'
    return "lobby"


def connect_screen():
    global clients_play
    clients_play = n.get_clients_play()
    if clients_play < 2:
        mouse_pos = pygame.mouse.get_pos()
        im = pygame.image.load("רקע_2.jpg")
        im = pygame.transform.scale(im, screen_size)
        screen.blit(im, (0, 0))
        back_to_start_button = Button(150, 50, 25, 12)
        back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
        back_to_start_button.drew_text("Back to lobby", 'Corbel', 30, color)
        font = pygame.font.Font(None, 35)
        text_ = font.render(f"waiting for other player to connect.....", True, (255, 255, 255))
        screen.blit(text_, (450, 300))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_start_button.mouse_over_button(mouse_pos):
                    n.send("back")
                    return "lobby"
            if event.type == pygame.QUIT:
                n.send("back")
                n.send("disconnect")
                return 'quit'
        return "connect_screen"
    else:
        return "war_online_screen"


def draw_life_bar(x, y, life):
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GRAY = (128, 128, 128)
    BAR_WIDTH = 200
    BAR_HEIGHT = 20
    if life >= 75:
        color = GREEN
        width = life / 100 * BAR_WIDTH
    elif life >= 25:
        color = YELLOW
        width = life / 100 * BAR_WIDTH
    elif life > 0:
        color = RED
        width = life / 100 * BAR_WIDTH
    else:
        color = RED
        width = BAR_WIDTH
    pygame.draw.rect(screen, WHITE, (x, y, BAR_WIDTH, BAR_HEIGHT), 2)
    pygame.draw.rect(screen, color, (x, y, int(width), BAR_HEIGHT))


global timer_start_time
timer_start_time = None
global timer_start_time2
timer_start_time2 = None
global com
com = False
global com2
com2 = False
global comDOS
comDOS = False
global comDNF
comDNF = False
global comCODE
comCODE = False


def run_timer_(timer_duration):
    global sound_effect2
    global timer_start_time
    WHITE = (255, 255, 255)
    if timer_start_time is None:
        timer_start_time = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - timer_start_time) // 1000
    remaining_time = max(0, timer_duration - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {minutes:02d}:{seconds:02d}", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH // 2, 20))
    if remaining_time == 0:
        timer_start_time = None
        return "done"



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 36)


def generate_numbers_and_task():
    numbers = random.sample(range(1, 1001), 4)
    task = random.choice(["smallest to largest", "largest to smallest"])
    return numbers, task


def draw_task(task):
    task_text = font.render("Task: Sort numbers from " + task, True, BLACK)
    task_rect = task_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(task_text, task_rect)


def draw_numbers(numbers, number_positions, number_rects):
    for i, number in enumerate(numbers):
        if number is not None:
            number_text = font.render(str(number), True, BLACK)
            number_rect = number_text.get_rect(center=number_positions[i])
            x = number_rect.x
            y = number_rect.y
            pygame.draw.rect(screen, GRAY, number_rects[i])
            screen.blit(number_text, (x + 10 + 15 + 10, y + 5 + 10 + 3))


def draw_sorted_numbers(sorted_numbers):
    sorted_text = font.render("Sorted: " + str(sorted_numbers), True, BLACK)
    sorted_rect = sorted_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
    screen.blit(sorted_text, sorted_rect)


def check_sorted_numbers(sorted_numbers, original_numbers, task):
    global com
    global com2
    if len(sorted_numbers) == 4:
        if task == "smallest to largest" and sorted_numbers == sorted(original_numbers):
            result_text = font.render("Congratulations! You sorted the numbers correctly.", True, BLACK)
            com2 = True
        elif task == "largest to smallest" and sorted_numbers == sorted(original_numbers, reverse=True):
            result_text = font.render("Congratulations! You sorted the numbers correctly.", True, BLACK)
            com2 = True
        else:
            result_text = font.render("Oops! The numbers are not sorted correctly.", True, BLACK)
            com = False
            com2 = False
        result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, 550))
        screen.blit(result_text, result_rect)


def task_screen(ability):
    global com2, comDOS, comDNF, comCODE, timer_start_time2
    timer_start_time2 = pygame.time.get_ticks()
    numbers, task = generate_numbers_and_task()
    original_numbers = numbers.copy()
    sorted_numbers = []
    number_positions = [(200, 300), (300, 300), (400, 300), (500, 300)]
    number_rects = [pygame.Rect(pos[0], pos[1], 80, 40) for pos in number_positions]
    running = True
    while running:
        im = pygame.image.load("רקע_2.jpg")
        im = pygame.transform.scale(im, screen_size)
        screen.blit(im, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        draw_task(task)
        draw_numbers(numbers, number_positions, number_rects)
        draw_sorted_numbers(sorted_numbers)
        check_sorted_numbers(sorted_numbers, original_numbers, task)
        b = run_timer(10, timer_start_time2)
        timer = pygame.image.load("timer.png")
        timer = pygame.transform.scale(timer, (40, 40))
        screen.blit(timer, (SCREEN_WIDTH // 2 - 40, 12))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                com2 = False
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, rect in enumerate(number_rects):
                        if rect.collidepoint(event.pos):
                            selected_number = numbers[i]
                            sorted_numbers.append(selected_number)
                            numbers[i] = None
                            break
        if com2:
            if ability == "DOS":
                comDOS = True
            if ability == "DNF":
                comDNF = True
            if ability == "CODE":
                comCODE = True
            com2 = False
            return "war_online_screen"
        if b == "done":
            com2 = False
            return "war_online_screen"
        pygame.display.update()
    return "task_screen"


global ti2
ti2 = None
global sound_effect3_time
sound_effect3_time = sound_effect3.get_length()


def run_timer_2(timer_duration):
    global sound_effect3
    global ti2
    if ti2 is None:
        ti2 = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - ti2) // 1000
    remaining_time = max(0, timer_duration - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    if remaining_time == 0:
        return "done"


def hacked_screen(attack):
    global sound_effect3
    global sound_effect3_time
    global ti2
    global done_hack
    z = run_timer_2(13)
    if not pygame.mixer.Channel(0).get_busy():
        pygame.mixer.Channel(0).play(sound_effect3)
    font_large = pygame.font.Font(None, 48)
    font_medium = pygame.font.Font(None, 36)
    glitch_offset = 2
    glitch_probability = 0.1
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    screen.fill(BLACK)
    if random.random() < glitch_probability:
        glitch_x = random.randint(-glitch_offset, glitch_offset)
        glitch_y = random.randint(-glitch_offset, glitch_offset)
    else:
        glitch_x = 0
        glitch_y = 0
    title_text = font_large.render("You Hacked!", True, GREEN)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2 + glitch_x, 100 + glitch_y))
    screen.blit(title_text, title_rect)
    if attack == "dos":
        subtitle_text = font_medium.render("You Got Freeze.", True, GREEN)
    if attack == "dnf":
        subtitle_text = font_medium.render("Your data has been compromised.", True, GREEN)
    subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2 + glitch_x, 150 + glitch_y))
    screen.blit(subtitle_text, subtitle_rect)
    warning_text = font_medium.render("WARNING: Do not attempt to close this screen or shutdown your device!", True, RED)
    warning_rect = warning_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
    screen.blit(warning_text, warning_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ti2 = None
            sound_effect3.stop()
            return 'quit'
    if z == "done":
        ti2 = None
        sound_effect3.stop()
        done_hack = True
        return "war_online_screen"
    return attack


def war_online_screen():
    global com
    global clients_play
    global timer_start_time
    global timer_start_time2
    global comDOS
    global comDNF
    global comCODE
    global current_attack
    global attack_counter
    global attack_sender
    global system_life
    global current_user
    global target_user
    global turn_name
    global current_username
    global damage_applied_code
    global ti2
    global done_hack
    global data
    global done_data
    global target_ip
    global data2
    global damage_applied_dos
    global damage_applied_dnf
    turn_name = n.get_turn_name()
    target_user = n.get_target_user()
    attack_sender = n.get_attack_sender()
    current_attack = n.get_current_attack()
    print(current_attack)
    GREEN = (0, 128, 0)
    clients_play = n.get_clients_play()
    if clients_play > 2 or clients_play == 2:
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(sound_effect2)
        mouse_pos = pygame.mouse.get_pos()
        im = pygame.image.load("רקע_2.jpg")
        im = pygame.transform.scale(im, screen_size)
        screen.blit(im, (0, 0))
        box = TextBox(1000, 150, 200, 190, smallfont_4, 't')
        box.draw()
        font = pygame.font.Font(None, 24)
        text = font.render("your abilities:", True, (255, 255, 255))
        screen.blit(text, (1000, 130))
        back_to_start_button = Button(150, 50, 25, 12)
        back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
        back_to_start_button.drew_text("Back to lobby", 'Corbel', 30, color)
        text_box_width = 600
        text_box_height = 530
        text_box_x = 10
        text_box_y = 20
        font1 = pygame.font.Font(None, 30)
        te = font1.render("Data From Attack:", True, (255, 255, 255))
        screen.blit(te, (text_box_x, text_box_y + 50))
        if current_username != target_user:
            for user in users:
                if user.get_user_name() == target_user:
                    target_ip = user.get_ip()
                    data = f"username: {user.get_user_name()} password: {user.get_password()}"
                    data2 = f"target ip: {target_ip}"
                    break
        if done_data:
            te1 = font1.render(f"[+] new data from target: {data}", True, WHITE)
            screen.blit(te1, (text_box_x + 5, text_box_y + 120))
            te2 = font1.render(f"[+] new data from target: {data2}", True, WHITE)
            screen.blit(te2, (text_box_x + 5, text_box_y + 160))
        text_box = TextBox(text_box_x, text_box_y + 80, text_box_width + 20, text_box_height, smallfont_4, '')
        text_box.draw()
        font = pygame.font.Font(None, 26)
        text_ = font.render("System Life:", True, (255, 255, 255))
        screen.blit(text_, (890, 20))
        text_1 = font.render(f"the turn is:{turn_name}", True, (255, 255, 255))
        screen.blit(text_1, (300, 20))
        text_3 = font.render(f"{system_life}%", True, (255, 255, 255))
        screen.blit(text_3, (1210, 20))
        q = run_timer_(35)
        timer = pygame.image.load("timer.png")
        timer = pygame.transform.scale(timer, (40, 40))
        screen.blit(timer, (SCREEN_WIDTH // 2 - 40, 12))
        global timer_done_sent
        timer = pygame.image.load("timer.png")
        timer = pygame.transform.scale(timer, (40, 40))
        screen.blit(timer, (SCREEN_WIDTH // 2 - 40, 12))
        if q == "done" and not timer_done_sent and current_username == turn_name:
            n.send("done")
            timer_done_sent = True
        if current_username == turn_name:
            timer_done_sent = False
        else:
            timer_done_sent = True
        if comDNF:
            ability_button4 = Button(160, 50, 1020, 440 - 180 - 100)
            ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
            ability_button4.drew_text("data sniffing", 'Corbel', 30, GREEN)
        else:
            ability_button4 = Button(160, 50, 1020, 440 - 180 - 100)
            ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
            ability_button4.drew_text("data sniffing", 'Corbel', 30, (255, 255, 255))
        if comDOS:
            ability_button5 = Button(160, 50, 1020, 500 - 100 - 180)
            ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
            ability_button5.drew_text("Dos attack", 'Corbel', 30, GREEN)
        else:
            ability_button5 = Button(160, 50, 1020, 500 - 100 - 180)
            ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
            ability_button5.drew_text("Dos attack", 'Corbel', 30, (255, 255, 255))
        if comCODE:
            ability_button6 = Button(160, 50, 1020, 560 - 100 - 180)
            ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
            ability_button6.drew_text("code injector", 'Corbel', 30, GREEN)
        else:
            ability_button6 = Button(160, 50, 1020, 560 - 100 - 180)
            ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
            ability_button6.drew_text("code injector", 'Corbel', 30, (255, 255, 255))
        load_data()
        if current_username == target_user:
            if current_attack == 1 and not damage_applied_dos:
                system_life -= 30
                damage_applied_dos = True
                draw_life_bar(990, 20, system_life)
                sound_effect2.stop()
                ti2 = None
                if done_hack is False:
                    return "dos"
            elif current_attack == 2 and not damage_applied_dnf:
                system_life -= 40
                damage_applied_dnf = True
                draw_life_bar(990, 20, system_life)
                sound_effect2.stop()
                ti2 = None
                if done_hack is False:
                    return "dnf"
            elif current_attack == 3 and not damage_applied_code:
                system_life -= 30
                damage_applied_code = True
                draw_life_bar(990, 20, system_life)
                sound_effect2.stop()
                ti2 = None
                if done_hack is False:
                    return "main"
        else:
            damage_applied_dnf = False
            damage_applied_dos = False
            damage_applied_code = False
        if current_attack == 0:
            damage_applied_dnf = False
            damage_applied_dos = False
            damage_applied_code = False
        draw_life_bar(990, 20, system_life)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_start_button.mouse_over_button(mouse_pos):
                    timer_start_time2 = None
                    timer_start_time = None
                    n.send("back")
                    com = False
                    comDOS = False
                    comDNF = False
                    comCODE = False
                    done_data = False
                    attack_counter = 0
                    system_life = 100
                    sound_effect2.stop()
                    return "lobby"
                if current_username == turn_name:
                    if ability_button5.mouse_over_button(mouse_pos) and comDOS:
                        n.send("dos")
                    elif ability_button5.mouse_over_button(mouse_pos):
                        timer_start_time2 = None
                        return "DOS"
                    if ability_button4.mouse_over_button(mouse_pos) and comDNF:
                        done_data = True
                        n.send("dnf")
                    elif ability_button4.mouse_over_button(mouse_pos):
                        timer_start_time2 = None
                        return "DNF"
                    if ability_button6.mouse_over_button(mouse_pos) and comCODE:
                        n.send("code")
                    elif ability_button6.mouse_over_button(mouse_pos):
                        timer_start_time2 = None
                        return "CODE"
            if event.type == pygame.QUIT:
                n.send("back")
                com = False
                comDOS = False
                comDNF = False
                comCODE = False
                done_data = False
                attack_counter = 0
                system_life = 100
                sound_effect2.stop()
                n.send("disconnect")
                return 'quit'
        return "war_online_screen"
    else:
        sound_effect2.stop()
        return "connect_screen"


def roadmap_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("RoadMAP.png")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to home", 'Corbel', 30, color)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    load_data()
    stages = [
        {"x": 200, "y": 430, "radius": 100, "color": BLUE, "text": "Level 1: Script Kiddie"},
        {"x": 550, "y": 330, "radius": 105, "color": BLUE, "text": "Level 2: Rookie Hacker"},
        {"x": 900, "y": 130, "radius": 110, "color": BLUE, "text": "Level 3: Elite Hacker"}
    ]
    lines = [
        ((260, 430), (510, 330)),
        ((510, 330), (910, 130))
    ]
    for line in lines:
        pygame.draw.aaline(screen, (255, 255, 255), line[0], line[1], 200)
    for stage in stages:
        pygame.draw.circle(screen, stage["color"], (stage["x"], stage["y"]), stage["radius"])
        if is_mouse_on_circle(mouse_pos, (stage["x"], stage["y"]), stage["radius"]):
            pygame.draw.circle(screen, (135, 206, 235), (stage["x"], stage["y"]), stage["radius"])
        font = pygame.font.Font(None, 24)
        text = font.render(stage["text"], True, BLACK)
        text_rect = text.get_rect(center=(stage["x"], stage["y"]))
        screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "start2"
            for user in users:
                if user.get_points() < 4 or user.get_points() == 4 and user.get_points() < 9 or user.get_points() == 9:
                    if is_mouse_on_circle(mouse_pos,  (200, 430), 100):
                        return "main1"
                elif user.get_points() == 4 and user.get_points() <= 9:
                    if is_mouse_on_circle(mouse_pos,  (200, 430), 100):
                        return "main1"
                    if is_mouse_on_circle(mouse_pos,  (550, 330), 105):
                        return "main2"
                elif user.get_points() < 9 or user.get_points() == 9 and user.get_points() < 14 or user.get_points() == 14:
                    if is_mouse_on_circle(mouse_pos,  (200, 430), 100):
                        return "main1"
                    if is_mouse_on_circle(mouse_pos,  (550, 330), 105):
                        return "main2"
                    if is_mouse_on_circle(mouse_pos,  (900, 130), 110):
                        return "main3"
        if event.type == pygame.QUIT:
            return 'quit'
    return "roadmap"


def quests(mouse_pos, quests):
    global current_user
    font = pygame.font.Font(None, 24)
    box2 = TextBox(150, 100, 200, 312, smallfont_4, 't')
    box2.draw()
    quest_button1 = Button(160, 50, 170, 260 - 150)
    quest_button1.drew_rec(quest_button1.mouse_over_button(mouse_pos))
    quest_button1.drew_text("quest 1", 'Corbel', 30, (255, 255, 255))
    quest_button2 = Button(160, 50, 170, 320 - 150)
    quest_button2.drew_rec(quest_button2.mouse_over_button(mouse_pos))
    quest_button2.drew_text("quest 2", 'Corbel', 30, (255, 255, 255))
    quest_button3 = Button(160, 50, 170, 380 - 150)
    quest_button3.drew_rec(quest_button3.mouse_over_button(mouse_pos))
    quest_button3.drew_text("quest 3", 'Corbel', 30, (255, 255, 255))
    quest_button4 = Button(160, 50, 170, 440 - 150)
    quest_button4.drew_rec(quest_button4.mouse_over_button(mouse_pos))
    quest_button4.drew_text("quest 4", 'Corbel', 30, (255, 255, 255))
    quest_button5 = Button(160, 50, 170, 500 - 150)
    quest_button5.drew_rec(quest_button5.mouse_over_button(mouse_pos))
    quest_button5.drew_text("quest 5", 'Corbel', 30, (255, 255, 255))
    text = font.render("your quests:", True, (255, 255, 255))
    screen.blit(text, (150, 80))
    if quest_button1.mouse_over_button(mouse_pos):
        return quests[0]
    if quest_button2.mouse_over_button(mouse_pos):
        return quests[1]
    if quest_button3.mouse_over_button(mouse_pos):
        return quests[2]
    if quest_button4.mouse_over_button(mouse_pos):
        return quests[3]
    if quest_button5.mouse_over_button(mouse_pos):
        return quests[4]


def main1_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("רקע_2.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    box = TextBox(1000, 150, 200, 190, smallfont_4, 't')
    box.draw()
    font = pygame.font.Font(None, 24)
    text = font.render("your abilities:", True, (255, 255, 255))
    screen.blit(text, (1000, 130))
    ability_button4 = Button(160, 50, 1020, 440 - 180 - 100)
    ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
    ability_button4.drew_text("firewall", 'Corbel', 30, (255, 255, 255))
    ability_button5 = Button(160, 50, 1020, 500 - 100 - 180)
    ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
    ability_button5.drew_text("antivirus", 'Corbel', 30, (255, 255, 255))
    ability_button6 = Button(160, 50, 1020, 560 - 100 - 180)
    ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
    ability_button6.drew_text("network_scanning", 'Corbel', 30, (255, 255, 255))
    quests(mouse_pos, ["quest1", "quest2", "quest3", "quest4", "quest5"])
    map = pygame.image.load("רקע_2.png")
    map = pygame.transform.scale(map, (500, 350))
    screen.blit(map, (420, 200))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
            if ability_button4.mouse_over_button(mouse_pos):
                return "firewall_data"
            if ability_button5.mouse_over_button(mouse_pos):
                return "antivirus_data"
            if ability_button6.mouse_over_button(mouse_pos):
                return "network_scanning_data"
            return quests(mouse_pos, ["quest1", "quest2", "quest3", "quest4", "quest5"])
        if event.type == pygame.QUIT:
            return 'quit'
    return "main1"


def main2_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("רקע_2.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    box = TextBox(980, 50, 250, 560 - 120 - 60, smallfont_4, 't')
    box.draw()
    font = pygame.font.Font(None, 24)
    text = font.render("your abilities:", True, (255, 255, 255))
    screen.blit(text, (1000, 30))
    ability_button1 = Button(160, 50, 1020, 440 - 180 - 100 - 100)
    ability_button1.drew_rec(ability_button1.mouse_over_button(mouse_pos))
    ability_button1.drew_text("firewall", 'Corbel', 30, (255, 255, 255))
    ability_button2 = Button(160, 50, 1020, 500 - 100 - 180 - 100)
    ability_button2.drew_rec(ability_button2.mouse_over_button(mouse_pos))
    ability_button2.drew_text("antivirus", 'Corbel', 30, (255, 255, 255))
    ability_button3 = Button(160, 50, 1020, 560 - 100 - 180 - 100)
    ability_button3.drew_rec(ability_button3.mouse_over_button(mouse_pos))
    ability_button3.drew_text("network_scanning", 'Corbel', 30, (255, 255, 255))
    ability_button4 = Button(160, 50, 1020, 620 - 280 - 100)
    ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
    ability_button4.drew_text("Intrusion Detection System (IDS)", 'corbel', 20, (255, 255, 255))
    ability_button5 = Button(160, 50, 1020, 680 - 280 - 100)
    ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
    ability_button5.drew_text("Data Loss Prevention (DLP)", 'corbel', 20, (255, 255, 255))
    ability_button6 = Button(160, 50, 1020, 740 - 280 - 100)
    ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
    ability_button6.drew_text("Security Information and Event Management", 'corbel', 15, (255, 255, 255))
    quests(mouse_pos, ["quest1_2", "quest2_2", "quest3_2", "quest4_2", "quest5_2"])
    map = pygame.image.load("רקע_2.png")
    map = pygame.transform.scale(map, (500, 350))
    screen.blit(map, (420, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
            if ability_button1.mouse_over_button(mouse_pos):
                return "firewall_data"
            if ability_button2.mouse_over_button(mouse_pos):
                return "antivirus_data"
            if ability_button3.mouse_over_button(mouse_pos):
                return "network_scanning_data"
            if ability_button4.mouse_over_button(mouse_pos):
                return "Intrusion_Detection_System_data"
            if ability_button5.mouse_over_button(mouse_pos):
                return "Data_Loss_Prevention_data"
            if ability_button6.mouse_over_button(mouse_pos):
                return "Security Information and Event Management"
            return quests(mouse_pos, ["quest1_2", "quest2_2", "quest3_2", "quest4_2", "quest5_2"])
    return "main2"


def main3_screen():
    mouse_pos = pygame.mouse.get_pos()
    im = pygame.image.load("רקע_2.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to roadmap", 'Corbel', 30, color)
    box = TextBox(980, 50, 250, 560, smallfont_4, 't')
    box.draw()
    font = pygame.font.Font(None, 24)
    text = font.render("your abilities:", True, (255, 255, 255))
    screen.blit(text, (1000, 30))
    ability_button1 = Button(160, 50, 1020, 440 - 180 - 100 - 100)
    ability_button1.drew_rec(ability_button1.mouse_over_button(mouse_pos))
    ability_button1.drew_text("firewall", 'Corbel', 30, (255, 255, 255))
    ability_button2 = Button(160, 50, 1020, 500 - 100 - 180 - 100)
    ability_button2.drew_rec(ability_button2.mouse_over_button(mouse_pos))
    ability_button2.drew_text("antivirus", 'Corbel', 30, (255, 255, 255))
    ability_button3 = Button(160, 50, 1020, 560 - 100 - 180 - 100)
    ability_button3.drew_rec(ability_button3.mouse_over_button(mouse_pos))
    ability_button3.drew_text("network_scanning", 'Corbel', 30, (255, 255, 255))
    ability_button4 = Button(160, 50, 1020, 620 - 280 - 100)
    ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
    ability_button4.drew_text("Intrusion Detection System (IDS)", 'corbel', 20, (255, 255, 255))
    ability_button5 = Button(160, 50, 1020, 680 - 280 - 100)
    ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
    ability_button5.drew_text("Data Loss Prevention (DLP)", 'corbel', 20, (255, 255, 255))
    ability_button6 = Button(160, 50, 1020, 740 - 280 - 100)
    ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
    ability_button6.drew_text("Security Information and Event Management", 'corbel', 15, (255, 255, 255))
    ability_button7 = Button(160, 50, 1020, 800 - 280 - 100)
    ability_button7.drew_rec(ability_button7.mouse_over_button(mouse_pos))
    ability_button7.drew_text("Behavioral Analytics", 'corbel', 30, (255, 255, 255))
    ability_button8 = Button(160, 50, 1020, 860 - 280 - 100)
    ability_button8.drew_rec(ability_button8.mouse_over_button(mouse_pos))
    ability_button8.drew_text("Endpoint Detection and Response", 'corbel', 20, (255, 255, 255))
    ability_button9 = Button(160, 50, 1020, 920 - 280 - 100)
    ability_button9.drew_rec(ability_button9.mouse_over_button(mouse_pos))
    ability_button9.drew_text("Blockchain based Security Solutions", 'corbel', 18, (255, 255, 255))
    quests(mouse_pos, ["quest1_3", "quest2_3", "quest3_3", "quest4_3", "quest5_3"])
    map = pygame.image.load("רקע_2.png")
    map = pygame.transform.scale(map, (500, 350))
    screen.blit(map, (420, 200))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "roadmap"
            if ability_button1.mouse_over_button(mouse_pos):
                return "firewall_data"
            if ability_button2.mouse_over_button(mouse_pos):
                return "antivirus_data"
            if ability_button3.mouse_over_button(mouse_pos):
                return "network_scanning_data"
            if ability_button4.mouse_over_button(mouse_pos):
                return "Intrusion_Detection_System_data"
            if ability_button5.mouse_over_button(mouse_pos):
                return "Data_Loss_Prevention_data"
            if ability_button6.mouse_over_button(mouse_pos):
                return "Security Information and Event Management"
            if ability_button7.mouse_over_button(mouse_pos):
                return "Behavioral_Analytics_data"
            if ability_button8.mouse_over_button(mouse_pos):
                return "Endpoint_Detection_and_Response_data"
            if ability_button9.mouse_over_button(mouse_pos):
                return "Blockchain_based_Security_Solutions_data"
            return quests(mouse_pos, ["quest1_3", "quest2_3", "quest3_3", "quest4_3", "quest5_3"])
    return "main3"


def war_screen(quest_num, text_line, defence_tool, num_of_tools, complete, main):
    global current_user
    global username_text_war
    global confirm_username_war
    global new_text_war
    im = pygame.image.load("רקע_2.jpg")
    im = pygame.transform.scale(im, screen_size)
    screen.blit(im, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    back_to_start_button = Button(150, 50, 25, 12)
    back_to_start_button.drew_rec(back_to_start_button.mouse_over_button(mouse_pos))
    back_to_start_button.drew_text("Back to main hub", 'Corbel', 30, color)
    username_box_2 = TextBox(570, 320, 350, 50, smallfont_3, username_text_war)
    username_box_2.draw()
    username_text_2 = smallfont_4.render(f'enter chosen ability:', True, color)
    screen.blit(username_text_2, (570, 210))
    if num_of_tools == 1:
        username_text_2 = smallfont_4.render(f'there are {num_of_tools} tool:', True, color)
    else:
        username_text_2 = smallfont_4.render(f'there are {num_of_tools} tools:', True, color)
    screen.blit(username_text_2, (570, 250))
    box = TextBox(1000, 320, 200, 370 - 150, smallfont_4, 't')
    box.draw()
    font = pygame.font.Font(None, 24)
    text = font.render("your abilities:", True, (255, 255, 255))
    screen.blit(text, (1000, 295))
    ability_button4 = Button(160, 50, 1020, 440 - 100)
    ability_button4.drew_rec(ability_button4.mouse_over_button(mouse_pos))
    ability_button4.drew_text("firewall", 'Corbel', 20, (255, 255, 255))
    ability_button5 = Button(160, 50, 1020, 500 - 100)
    ability_button5.drew_rec(ability_button5.mouse_over_button(mouse_pos))
    ability_button5.drew_text("antivirus", 'Corbel', 20, (255, 255, 255))
    ability_button6 = Button(160, 50, 1020, 560 - 100)
    ability_button6.drew_rec(ability_button6.mouse_over_button(mouse_pos))
    ability_button6.drew_text("network_scanning", 'Corbel', 13, (255, 255, 255))
    load_data()
    text_box_width = 500
    text_box_height = 400
    text_box_x = 10
    text_box_y = 30
    text_box = TextBox(text_box_x, text_box_y + 90, text_box_width + 20, text_box_height, smallfont_4, '')
    text_box.draw()
    font = pygame.font.Font(None, 22)
    line_spacing = 30
    y = text_box_y + 20 + 90
    for line in text_line:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (text_box_x + 20, y))
        y += line_spacing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_start_button.mouse_over_button(mouse_pos):
                return main
            if back_to_start_button.mouse_over_button(mouse_pos):
                return "start"
        if event.type == pygame.TEXTINPUT:
            if confirm_username_war is False:
                new_text_war += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if confirm_username_war is False:
                    try:
                        new_text_war = new_text_war[:-1]
                    except IndexError:
                        pass
            if event.key == pygame.K_RETURN:
                if confirm_username_war is False:
                    confirm_username_war = True
                for defence_tool_ in defence_tool:
                    if username_text_war.strip().lower() == defence_tool_:
                        new_text_war = ''
                        confirm_username_war = False
                        if complete == False:
                            current_user.add_point()
                            current_user.save_data()
                        return "roadmap"
                else:
                    confirm_username_war = False
                    username_text_war = ''
                    new_text_war = ''
    text_width_ = smallfont_5.size(new_text_war)[0]
    if text_width_ <= 350 and confirm_username_war is False:
        username_text_war = new_text_war
    text_2 = smallfont_5.render(username_text_war, True, color)
    text_rect = text_2.get_rect(topleft=(username_box_2.rect.x + 5, username_box_2.rect.y + 5))
    if text_rect.w <= 350:
        screen.blit(text_2, (username_box_2.rect.x + 5, username_box_2.rect.y + 12))
    return quest_num


def quest1():
    global current_user
    if current_user.get_points() == 0:
        complete = False
    else:
        complete = True
    t = [
        "Distributed Denial of Service (DDoS) Attack A DDoS attack",
        "aims to make a service unavailable",
        "to legitimate users by overwhelming it with a flood of",
        "malicious traffic from multiple sources.",
        "Attackers typically leverage a botnet - a network of",
        " compromised devices they control remotely.",
        "The massive volumes of junk traffic exhaust the target's",
        "resources, causing it to become unresponsive.",
        "Attacker: Clop Ransomware Gang - A financially",
        "motivated cybercrime syndicate known for deploying",
        "botnets to conduct large-scale DDoS attacks as a service",
        "often targeting financial institutions."
    ]
    a = war_screen("quest1", t, ["firewall"], 1, complete, "main1")
    if a == "roadmap":
        complete = True
        return "main1"
    return a

def quest2():
    global current_user
    if current_user.get_points() == 1:
        complete = False
    else:
        complete = True
    t = [
        "SQL Injection Attack SQL injection is a technique where an attacker",
        "inserts malicious SQL code via application input fields to gain",
        "unauthorized access to the backend database. If user input is not",
        "properly sanitized, an attacker can leverage injection flaws to",
        "steal, modify or delete data.",
        "These attacks often target web applications.",
        "Fictional Attacker: Naikon - A suspected Chinese state-sponsored",
        "APT group that has conducted cyber espionage operations by",
        "exploiting SQL injection and other vulnerabilities in popular",
        "content management systems.",
        "Distributed Denial of Service (DDoS) Attack A DDoS attack aims",
        "to make a service unavailable"
    ]
    a = war_screen("quest2", t, ["firewall and network_scanning", "network_scanning and firewall"], 2, complete, "main1")
    if a == "roadmap":
        complete = True
        return "main1"
    return a

def quest3():
    global current_user
    if current_user.get_points() == 2:
        complete = False
    else:
        complete = True
    t = [
        "Malware Attack Malware refers to any malicious software like",
        "viruses, worms, trojans and rootkits designed to cause damage,",
        "disrupt operations or gain unauthorized access to systems.",
        "Malware may be delivered via email attachments, drive-by",
        "downloads or network vulnerabilities. It poses serious risks",
        "of data theft, system disruption and loss of control.",
        "Fictional Attacker: Conti Cybercrime Group - A prolific,",
        "ruthless Russia-based syndicate responsible for distributing",
        "damaging malware strains in high-impact 'big game' attacks",
        "against corporations and critical infrastructure."
    ]
    a = war_screen("quest3", t, ["antivirus"], 1, complete, "main1")
    if a == "roadmap":
        complete = True
        return "main1"
    return a


def quest4():
    global current_user
    if current_user.get_points() == 3:
        complete = False
    else:
        complete = True
    t = [
    "Ransomware Attack Ransomware is a type of malware",
    "that encrypts the victim's files and systems, after which",
    "the attackers demand payment (usually cryptocurrency) for",
    "a decryption key. It often spreads via phishing emails",
    "with malicious attachments. Upon infecting the system,",
    "ransomware lays dormant before encrypting data",
    "and displaying the ransom note.",
    "Fictional Attacker: SamSam Ransomware Group - An Iranian",
    "cybercriminal outfit that carried out targeted ransomware",
    "attacks exploiting vulnerabilities in servers and network",
    "devices to infiltrate and encrypt data."
    ]
    a = war_screen("quest4", t, ["antivirus and network_scanning", "network_scanning and antivirus"], 2, complete, "main1")
    if a == "roadmap":
        complete = True
        return "main1"
    return a


def quest5():
    global current_user
    if current_user.get_points() == 4:
        complete = False
    else:
        complete = True
    t = [
    "Man-in-the-Middle Attack In this attack, the adversary",
    "positions themselves between two legitimately communicating",
    "parties to eavesdrop on and potentially alter network traffic.",
    "The attacker may impersonate one party to the other, allowing",
    "interception, data theft, and traffic manipulation while",
    "going undetected.",
    "Fictional Attacker: Turla - A sophisticated Russian state-backed",
    "threat group known for using man-in-the-middle techniques",
    "among an array of stealthy tactics to compromise government",
    "and diplomatic networks worldwide."
    ]
    a = war_screen("quest5", t, ["network_scanning"], 1, complete, "main1")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main1"
    return a


def quest6():
    t = [
    "Cross-Site Scripting (XSS) XSS enables an attacker",
    "to inject malicious scripts into web applications,",
    "which then execute in the victim's browser. By exploiting",
    "poor input validation, the attacker can deploy scripts",
    "that hijack user sessions, deface websites, or redirect",
    "users to malicious sites and compromise their systems.",
    "Fictional Attacker: Lapsus$ - A brash cybercriminal",
    "group that gained notoriety for audacious data breaches",
    "and extortion schemes involving XSS attacks against",
    "major corporations' websites and cloud services."
    ]
    global current_user
    if current_user.get_points() == 5:
        complete = False
    else:
        complete = True

    a = war_screen("quest1_2", t, ["firewall and network_scanning", "network_scanning and firewall"], 2, complete, "main2")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main2"
    return a


def quest7():
    t = [
    "Brute Force Attack Brute force is an attack method",
    "of trying numerous password/encryption key combinations",
    "systematically until guessing correctly. Attackers deploy",
    "automated tools to rapidly attempt every possible permutation.",
    "Brute forcing weak credentials allows unauthorized system access.",
    "Fictional Attacker: SpyEye Botnet - A prolific crimeware",
    "operation that rented out its network of infected computers",
    "to countless cybercriminals specifically for brute-forcing",
    "attacks on banking systems."
    ]
    global current_user
    if current_user.get_points() == 6:
        complete = False
    else:
        complete = True
    a = war_screen("quest2_2", t, ["firewall"], 1, complete, "main2")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main2"
    return a


def quest8():
    global current_user
    t = [
    "Data Exfiltration Attack Attack Method: This attack involves",
    "gaining unauthorized access to target systems through various",
    "entry vectors like phishing emails or exploiting software",
    "vulnerabilities. Once inside, the attacker stealthily extracts",
    "and transmits sensitive data outside the network using covert",
    "channels.",
    "Fictional Attacker: APT10 - An advanced persistent threat (APT)",
    "group linked to Chinese military intelligence, specializing",
    "in data theft from government, military, and industrial systems",
    "for espionage purposes."
    ]
    if current_user.get_points() == 7:
        complete = False
    else:
        complete = True
    a = war_screen("quest3_2", t, ["Data Loss Prevention (DLP)"], 1, complete, "main2")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main2"
    return a


def quest9():
    global current_user
    t = [
    "Advanced Persistent Threat (APT) Attack",
    "Attack Method: An APT attack is a prolonged, multi-stage attack",
    "that aims to establish a long-term, undetected presence within",
    "the target network. Attackers use advanced techniques and malicious",
    "tools to deeply infiltrate systems, move laterally, and maintain",
    "persistent access for espionage or disruptive purposes.",
    "Fictional Attacker: Equation Group - A sophisticated threat group",
    "associated with the U.S. NSA, known for using advanced and stealthy",
    "attack tools and techniques for intelligence gathering against",
    "government and military systems."
    ]
    if current_user.get_points() == 8:
        complete = False
    else:
        complete = True
    a = war_screen("quest4_2", t, ["Intrusion Detection System data and Data Loss Prevention_data (DLP)", "Data_Loss Prevention_data (DLP) and Intrusion Detection System data"], 2, complete, "main2")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main2"
    return a


def quest10():
    global current_user
    t = [
    "Insider Threat Attack Attack Method: In this attack, a malicious",
    "insider with legitimate access to organizational systems and data",
    "abuses their privileges to steal, sabotage, or destroy sensitive",
    "information or infrastructure.",
    "Fictional Attacker: Edward Snowden - A former NSA intelligence",
    "contractor who leaked massive amounts of classified information,",
    "exposing himself as a malicious insider."
    ]
    if current_user.get_points() == 9:
        complete = False
    else:
        complete = True
    a = war_screen("quest5_2", t, ["Security Information and Event Management and Data Loss Prevention data (DLP)", "Data Loss_Prevention data (DLP) and Security Information and Event Management"], 2, complete, "main2")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main2"
    return a


def quest11():
    global current_user
    t = [
    "Cyber Warfare Attack Attacker: Stuxnet - The sophisticated cyber",
    "worm attributed to U.S. and North Korean intelligence agencies,",
    "designed to sabotage nuclear facilities of an adversary nation.",
    "Attack Method: Infiltrating industrial control systems (ICS/SCADA)",
    "networks using advanced attack vectors to disrupt or destroy",
    "critical systems and infrastructure."
    ]
    if current_user.get_points() == 10:
        complete = False
    else:
        complete = True
    a = war_screen("quest1_3", t, ["Data Loss_Prevention data (DLP)"], 1, complete, "main3")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main3"
    return a


def quest12():
    global current_user
    t = [
    "Supply Chain Attack Attacker: CCLeaner - A legitimate computer",
    "cleaning utility distributed by Avast, embedded with a malicious",
    "module to gather intelligence from organizational systems by",
    "a Russian state-sponsored group.",
    "Attack Method: Implanting malicious code in software or hardware",
    "distributed by suppliers or third parties, enabling hostile access",
    "to the organization's networks."
    ]
    if current_user.get_points() == 11:
        complete = False
    else:
        complete = True
    a = war_screen("quest2_3", t, ["network_scanning and Security Information and Event Management ", "Security Information and Event Management and network_scanning"], 2, complete, "main3")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main3"
    return a


def quest13():
    global current_user
    t = [
    "Watering Hole Attack Attacker: Athens Unc0ver - A Chinese APT",
    "group that attacked using carefully crafted fake websites",
    "impersonating legitimate, attractive targets.",
    "Attack Method: Popular legitimate websites compromised by",
    "attackers to deliver malicious code to victims visiting",
    "those sites."
    ]
    if current_user.get_points() == 12:
        complete = False
    else:
        complete = True
    a = war_screen("quest3_3", t, ["Data Loss_Prevention data (DLP)"], 1, complete, "main3")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main3"
    return a


def quest14():
    global current_user
    t = [
    "Fileless Malware Attack Attacker: SNOWBLOW - An advanced,",
    "targeted fileless malware allegedly developed by a North Korean",
    "cybercriminal group for industrial espionage.",
    "Attack Method: Infiltrating systems by exploiting vulnerabilities",
    "while operating solely in memory and leveraging operating system",
    "resources to avoid files."
    ]
    if current_user.get_points() == 13:
        complete = False
    else:
        complete = True
    a = war_screen("quest4_3", t, ["Behavioral Analytics and Endpoint Detection and Response", "Endpoint Detection and Behavioral Analytics"], 2, complete, "main3")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main3"
    return a


def quest15():
    global current_user
    t = [
    "Cyber Espionage Attack Attacker: APT41 - A sophisticated Russian",
    "APT group targeting diverse government and industry sectors of",
    "adversary nations for espionage and economic crime.",
    "Attack Method: Employing advanced techniques to infiltrate systems,",
    "collect sensitive intelligence, steal intellectual property and",
    "trade secrets for national and economic interests."
    ]
    if current_user.get_points() == 14:
        complete = False
    else:
        complete = True
    a = war_screen("quest5_3", t, ["network_scanning and Security Information and Event Management ", "Security Information and Event Management and network_scanning"], 2, complete, "main3")
    if a == "roadmap":
        complete = True
    else:
        complete = True
        return "main3"
    return a


current_screen = "intro_screen"
while running:
    global current_user
    if current_screen != "intro_screen":
        sound_effect5.stop()
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(sound_effect4)
    if current_screen == "intro_screen":
        current_screen = intro_screen()
    if current_screen == "start":
        current_screen = start_screen()
    elif current_screen == "log in":
        current_screen = log_in_screen()
    elif current_screen == "sign up":
        current_screen = sign_up_screen()
    elif current_screen == "quit":
        running = False
    elif current_screen == "start2":
        current_screen = start_screen_2()
    elif current_screen == "roadmap":
        current_screen = roadmap_screen()
    elif current_screen == "main1":
        current_screen = main1_screen()
    elif current_screen == "main2":
        current_screen = main2_screen()
    elif current_screen == "main3":
        current_screen = main3_screen()
    elif current_screen == "firewall_data":
        current_screen = firewall_data_screen()
    elif current_screen == "antivirus_data":
        current_screen = antivirus_data_screen()
    elif current_screen == "network_scanning_data":
        current_screen = network_scanning_data_screen()
    elif current_screen == "quest1":
        current_screen = quest1()
    elif current_screen == "quest2":
        current_screen = quest2()
    elif current_screen == "quest3":
        current_screen = quest3()
    elif current_screen == "quest4":
        current_screen = quest4()
    elif current_screen == "quest5":
        current_screen = quest5()
    elif current_screen == "quest1_2":
        current_screen = quest6()
    elif current_screen == "quest2_2":
        current_screen = quest7()
    elif current_screen == "quest3_2":
        current_screen = quest8()
    elif current_screen == "quest4_2":
        current_screen = quest9()
    elif current_screen == "quest5_2":
        current_screen = quest10()
    elif current_screen == "quest1_3":
        current_screen = quest11()
    elif current_screen == "quest2_3":
        current_screen = quest12()
    elif current_screen == "quest3_3":
        current_screen = quest13()
    elif current_screen == "quest4_3":
        current_screen = quest14()
    elif current_screen == "quest5_3":
        current_screen = quest15()
    elif current_screen == "Intrusion_Detection_System_data":
        current_screen = Intrusion_Detection_System_data_screen()
    elif current_screen == "Data_Loss_Prevention_data":
        current_screen = Data_Loss_Prevention_data_screen()
    elif current_screen == "Security Information and Event Management":
        current_screen = Security_Information_and_Event_Management_data_screen()
    elif current_screen == "Blockchain_based_Security_Solutions_data":
        current_screen = Blockchain_based_Security_Solutions_data_screen()
    elif current_screen == "Endpoint_Detection_and_Response_data":
        current_screen = Endpoint_Detection_and_Response_data_screen()
    elif current_screen == "Behavioral_Analytics_data":
        current_screen = Behavioral_Analytics_data_screen()
    elif current_screen == "lobby":
        current_screen = lobby()
    elif current_screen == "connect_screen":
        current_screen = connect_screen()
    elif current_screen == "war_online_screen":
        sound_effect4.stop()
        current_screen = war_online_screen()
    elif current_screen == "DOS":
        current_screen = task_screen("DOS")
    elif current_screen == "DNF":
        current_screen = task_screen("DNF")
    elif current_screen == "CODE":
        current_screen = task_screen("CODE")
    elif current_screen == "dos":
        current_screen = hacked_screen("dos")
    elif current_screen == "dnf":
        current_screen = hacked_screen("dnf")
    elif current_screen == "main":
        current_screen = main()
    pygame.display.update()
pygame.quit()
