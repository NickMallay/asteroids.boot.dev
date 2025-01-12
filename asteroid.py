from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.add_score()
            print(player.score)
            return
        
        angle_change = random.uniform(20,50)

        new_velocity_1 = self.velocity.rotate(angle_change)
        new_velocity_2 = self.velocity.rotate(-angle_change)

        child_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        child_1.velocity = new_velocity_1 * random.uniform(1 , 5)
        child_2.velocity = new_velocity_2 * random.uniform(1 , 5)
        player.add_score()
        print(player.score)