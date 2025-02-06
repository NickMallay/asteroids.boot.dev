import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *

def game_over_screen(screen, font):
    screen.fill("black")
    game_over_text = font.render("You Died", True, (255, 0, 0))
    restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 20))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 20))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize font for the score
    pygame.font.init()
    font = pygame.font.Font(None, 36)  # Default font with size 36

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot_group, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for roid in asteroids:
            if roid.check_collisions(player):
                print("Game over!")
                if game_over_screen(screen, font):  # Restart or Quit
                        break
                return
        for roid in asteroids:
            for shot in shot_group:
                if shot.check_collisions(roid):
                    roid.split(player)
                    shot.kill()
                # Render score
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Display score at the top-left corner        

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

        

if __name__ == "__main__":  # No spaces, and double underscores
    main()