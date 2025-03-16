import pygame
import sys


pygame.init()


width = 1000
height = 600


screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Arial", 36)


pygame.display.set_caption("Timer for study")

class Timer:
    def __init__(self):
        self.running = False
        self.started_time = 0
        self.pause = False
    def start(self):
        self.started_time = pygame.time.get_ticks()
        self.running = True

    def get_time(self):
        if self.running:
            # difference between the current time and started time
            elapsed_time = pygame.time.get_ticks() - self.started_time
            remaining_time =  5400000 - elapsed_time  # 2 h in ms

            if remaining_time <= 0:
                self.running = False
                remaining_time = 0

            hours = remaining_time // 3600000  # 1 h = 3600000 ms
            remaining_time -= hours * 3600000
            minutes = remaining_time // 60000  # 1 m = 60000 ms
            return hours, minutes

        elif self.pause == True:
            remaining_time = 5400000 - self.paused_time  # 2 h in ms

            if remaining_time <= 0:
                self.running = False
                remaining_time = 0

            hours = remaining_time // 3600000  # 1 h = 3600000 ms
            remaining_time -= hours * 3600000
            minutes = remaining_time // 60000  # 1 m = 60000 ms
            return hours, minutes

        else:
            return 0, 0  # if timer is stoped programm outputs 0

    def reset_timer(self):
        self.running = False
        self.started_time = pygame.time.get_ticks()
        self.paused_time = 0

    def pause_timer(self):
        if self.running:
            self.pause = True
            self.running = False
            self.paused_time = pygame.time.get_ticks() - self.started_time

# Creating object of Timer
time = Timer()
waiting_for_start = True
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and waiting_for_start:
            if event.key == pygame.K_SPACE:
                time.start()
                waiting_for_start = False
        elif event.type == pygame.KEYDOWN and waiting_for_start == False:
            if event.key == pygame.K_p:
                time.pause_timer()
            elif event.key == pygame.K_r:
                time.reset_timer()
                waiting_for_start = True

    # Getting the time from timer
    hours, minutes = time.get_time()

    if hours == 0 and minutes == 0 and waiting_for_start == False:
        end_text = font.render("Salamaleihum CHAT, you are awesome!!!!", True, (0, 0, 0))
        screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 3))

    # Text rendering
    time_text = font.render(f"{hours}:{minutes:02} ", True, (0, 0, 0))
    helping_text = font.render("You can pause with P and reset with R", True, (0, 0, 0))

    # Filling the screen with white
    screen.fill((255, 255, 255))

    # Message if waiting
    if waiting_for_start:
        prompt_text = font.render("Khakim please press space to begin your session.", True, (0, 0, 0))
        screen.blit(prompt_text, (width // 2 - prompt_text.get_width() // 2, height // 3))

    screen.blit(time_text, (width // 2 - time_text.get_width() // 2, height // 2))
    screen.blit(helping_text, (width // 2 - helping_text.get_width() // 2, height // 2 - 40))
    # screen update
    pygame.display.flip()

# quiting pygame
pygame.quit()
sys.exit()
