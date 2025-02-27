import pygame
import random

from src.particle_system.particle_system import ParticleSystem
from src.particle_system.particle_generator import ParticleGenerator

def test_particle_system_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Particle System Test")

    clock = pygame.time.Clock()

    particle_system = ParticleSystem()

    particle_generator = ParticleGenerator(particle_system, 400, 300, 0, 0, 0, 0, 0, 0, 10, 100,  100, 255, 0, 0, 255, 'circle', False, 60)
    particle_system.add_generator(particle_generator)
    particle_generator.start()
    running = True
    temp = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        particle_system.generators[0].edit(400+temp)

        # particle_system.add_particle(400, 300, random.uniform(-1, 1), 0, 0, 0.1, 0, 2, 60, 100, 10, 255, 0, 0, 255, 'circle')
        # particle_system.add_particle(2, 300, 0, random.uniform(-1, 1), 0.1, 0, 0, 2, 60, 100, 10, 0, 255, 0, 255, 'square')
        # particle_system.add_particle(500, 10, random.uniform(-1, 1), random.uniform(-1, 1), 0, 0.1, 0, 2, 60, 100, 10, 0, 0, 255, 255, 'triangle')
        # particle_system.add_particle(400, 300, 0, 0, 0.1, 0, 0, 2, 60, 100, 10, 255, 255, 0, 255, 'star')

        screen.fill((0, 0, 0))
        delta_time = clock.tick(120) / 1000.0
        particle_system.update(delta_time=delta_time)
        particle_system.draw(screen)
        pygame.display.flip()

        temp+=1

        #print fps
        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    test_particle_system_window()