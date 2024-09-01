from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        else:
            rand_angle = random.uniform(20, 50)
            pos_rand_angle = self.velocity.rotate(rand_angle)
            neg_rand_angle = self.velocity.rotate(-1 * rand_angle)

            pos_asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            neg_asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))

            pos_asteroid.velocity = pos_rand_angle * 1.2
            neg_asteroid.velocity = neg_rand_angle * 1.2