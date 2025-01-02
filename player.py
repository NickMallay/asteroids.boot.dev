import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x , y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.p_pressed = False
        self.o_pressed = False
        self.score = 0



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        if keys[pygame.K_p]:
            if not self.p_pressed:
                self.shot_cooldown += 0.1
                print(f"Cooldown is {self.shot_cooldown}")
                self.p_pressed = True
                if self.shot_cooldown < 0:
                    self.shot_cooldown = 0
                elif self.shot_cooldown > 10:
                    self.shot_cooldown = 10
        else:
                self.p_pressed = False

        
        if keys[pygame.K_o]:
            if not self.o_pressed:
                self.shot_cooldown -= 0.1
                print(f"Cooldown is {self.shot_cooldown}")
                self.o_pressed = True
                if self.shot_cooldown < 0:
                    self.shot_cooldown = 0
                elif self.shot_cooldown > 10:
                    self.shot_cooldown = 10
        else:
                self.o_pressed = False

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer <= 0:
            self.timer += self.shot_cooldown
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) 
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.timer -= dt
        if self.timer < 0:
            self.timer = 0
    
    def add_score(self):
        self.score += 100
    
