from .particle import Particle

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y, vx, vy, dvx, dvy, angle, dangle, speed, lifespan, size, red, green, blue, alpha, shape, gradient=False):
        self.particles.append(
            Particle(x, y, vx, vy, dvx, dvy, angle, dangle, speed, lifespan, size, red, green, blue, alpha, shape, gradient))

    def apply_force_to_all(self, fx, fy):
        for particle in self.particles:
            particle.apply_force(fx, fy)

    def update(self):
        particle_x, particle_y = 0, 0
        for particle in self.particles:
            particle.update(particle_x, particle_y)
            if particle.lifespan <= 0:
                self.particles.remove(particle)
                del particle

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)