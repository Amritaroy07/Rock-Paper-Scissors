import pygame
import random

x = pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
violet = (127, 0, 255)

font = pygame.font.SysFont(None, 55)

screen_height = 700
screen_width = 1200

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissor")
pygame.display.update()

mainimg = pygame.image.load("Untitled.png")
mainimg = pygame.transform.scale(mainimg, (screen_width, screen_height)).convert_alpha()


exit_game = False
loss_game = False

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def game_title(exit_game):
    while not exit_game:
        gameWindow.blit(mainimg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameWindow.fill(violet)
                        pygame.display.update()
                        game_loop(exit_game)

def pc_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choices(choices)
    text_screen(f"PC chooses {computer_choice}", black, 10, 100)
    pygame.display.update()
    return computer_choice

def win_game(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == ['Rock']:
        text_screen("Draw", black, 10, 150)
    if user_choice == "rock" and computer_choice == ['Scissors']:
        text_screen("You win", black, 10, 150)
    if user_choice == "rock" and computer_choice == ['Paper']:
        text_screen("Computer wins", black, 10, 150)
    if user_choice == "paper" and computer_choice == ['Rock']:
        text_screen("You win", black, 10, 150)
    if user_choice == "paper" and computer_choice == ['Scissors']:
        text_screen("Computer wins", black, 10, 150)
    if user_choice == "paper" and computer_choice == ['Paper']:
        text_screen("Draw", black, 10, 150)
    if user_choice == "Scissor" and computer_choice == ['Rock']:
        text_screen("Computer wins", black, 10, 150)
    if user_choice == "Scissor" and computer_choice == ['Scissors']:
        text_screen("Draw", black, 10, 150)
    if user_choice == "Scissor" and computer_choice == ['Paper']:
        text_screen("You win", black, 10, 150)

def game_loop(exit_game):
    while not exit_game:
        for event in pygame.event.get():
            text_screen("Choose R for Rock, P for Paper, S for Scissors.", black, 10, 10)
            pygame.display.update()
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    user_choice = "rock"
                    text_screen("Your choice is Rock", black, 10, 60)
                    pc = pc_choice()
                    pygame.display.update()
                elif event.key == pygame.K_p:
                    user_choice = "paper"
                    text_screen("Your choice is Paper", black, 10, 60)
                    pc = pc_choice()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    user_choice = "scissor"
                    text_screen("Your choice is Scissor", black, 10, 60)
                    pc = pc_choice()
                    pygame.display.update()
                if user_choice:
                    win_game(user_choice, pc)
                    pygame.display.update()
                text_screen("To play again press Space button.", black, 10, 200)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameWindow.fill(violet)
                        pygame.display.update()
                        game_loop(exit_game)
    pygame.quit()

game_title(exit_game)
