# I imported the libraries I was going to  use.
import pygame
import time
import random

# Always have to initialise pygame.
pygame.init()

# Here I stored the scientific "RGB" format of a number of colours so that if needed I can easily call them as their
# colours instead of having to type out the "RGB" format.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 200, 200)

# Display width and height of the window.
dis_width = 600
dis_height = 400

# This sets the display dimensions mentiooned above and also gives the window a caption.
# I'm a huge batman fan, hence the caption.
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Wayne Enterprises (c)')

# We need a clock because of the speed of the moving snake.
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("aguda", 25)
score_font = pygame.font.SysFont("moonhouse", 35)


# To display your score.
def Your_score(score):
    value = score_font.render("Moyo's Snake Game! Score: " + str(score), True, pink)
    dis.blit(value, [0, 0])


# This is to describe the food (rectangular blocks) that the snake would eat.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    # These are false so that the game keeps running
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # The x and y coordinates of each block has to e randomised... The main point of the game
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:

            # What to display whenever you lose.
            dis.fill(black)
            message("You Lost :(  Press 'C' to Play Again or 'Q' to Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # The keyboard control interpretations.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # To make the snake longer with every food block it eats.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # After eating a block, random position for the next, and updated length.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


gameLoop()
