import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 1100, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up assets
CAR_WIDTH, CAR_HEIGHT = 70, 90
car = pygame.image.load('car.png')  # Load a car image
opponent_car = pygame.image.load('opponent_car.png')  # Load an opponent car image

def draw_window(car_x, car_y, opponent_car_x, opponent_car_y, score):
    win.fill((0,0,0))  # Fill the screen with black
    win.blit(car, (car_x, car_y))  # Draw the car
    win.blit(opponent_car, (opponent_car_x, opponent_car_y))  # Draw the opponent car
    score_text = pygame.font.Font(None, 50).render("Score: " + str(score), 1, (255,255,255))
    win.blit(score_text, (10, 10))  # Draw the score
    pygame.display.update()  # Update the display

def main():
    clock = pygame.time.Clock()

    car_x, car_y = WIDTH // 2, HEIGHT - CAR_HEIGHT - 10  # Start the car at the bottom center of the screen
    opponent_car_x, opponent_car_y = random.randrange(CAR_WIDTH, WIDTH - CAR_WIDTH), 0  # Start the opponent car at a random x position at the top of the screen
    car_vel = 5
    opponent_car_vel = 2
    score = 0

    run = True
    while run:
        clock.tick(60)  # Cap the speed at 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow the game to quit
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x - car_vel > 0:  # Move left
            car_x -= car_vel
        if keys[pygame.K_RIGHT] and car_x + car_vel < WIDTH - CAR_WIDTH:  # Move right
            car_x += car_vel

        opponent_car_y += opponent_car_vel  # Move the opponent car down
        if opponent_car_y > HEIGHT:  # If the opponent car has moved off the bottom of the screen
            opponent_car_y = 0  # Move it back to the top
            opponent_car_x = random.randrange(CAR_WIDTH, WIDTH - CAR_WIDTH)  # Give it a new random x position
            score += 1  # Increase the score

        draw_window(car_x, car_y, opponent_car_x, opponent_car_y, score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
