from .particle import Particle
import pygame

class ParticleSystem:
    def __init__(self) -> None:
        self.particles = []

    def add_particle(self, x: float, y: float, vx: float, vy: float, dvx: float, dvy: float, angle: float, dangle: float, speed: float, lifespan: int, size: int, red: int, green: int, blue: int, alpha: int, shape: str, gradient: bool = False) -> None:
        self.particles.append(Particle(x, y, vx, vy, dvx, dvy, angle, dangle, speed, lifespan, size, red, green, blue, alpha, shape, gradient))

    def apply_force_to_all(self, fx: float, fy: float) -> None:
        for particle in self.particles:
            particle.apply_force(fx, fy)

    def update(self) -> None:
        particle_x, particle_y = 0, 0
        for particle in self.particles:
            particle.update(particle_x, particle_y)
        self.particles = [particle for particle in self.particles if particle.lifespan > 0]

    def draw(self, screen: pygame.Surface) -> None:
        for particle in self.particles:
            particle.draw(screen)