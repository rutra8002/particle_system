import pygame
import random
from src.particle_system.particle_system import ParticleSystem

def test_particle_system_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Particle System Test")
    clock = pygame.time.Clock()
    particle_system = ParticleSystem()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        particle_system.add_particle(400, 300, random.uniform(-1, 1), 0, 0, 0.1, 0, 2, 1, 100, 10, 255, 0, 0, 255, 'circle')
        particle_system.add_particle(2, 300, 0, random.uniform(-1, 1), 0.1, 0, 0, 2, 1, 100, 10, 0, 255, 0, 255, 'square')
        particle_system.add_particle(500, 10, random.uniform(-1, 1), random.uniform(-1, 1), 0, 0.1, 0, 2, 1, 100, 10, 0, 0, 255, 255, 'triangle')
        particle_system.add_particle(400, 300, 0, 0, 0.1, 0, 0, 2, 1, 100, 10, 255, 255, 0, 255, 'star')

        screen.fill((0, 0, 0))
        particle_system.update()
        particle_system.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    test_particle_system_window()