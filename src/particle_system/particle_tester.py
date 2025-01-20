import pygame
import pygame_gui
import random
from src.particle_system.particle_system import ParticleSystem

class ParticleTester:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Particle System GUI")
        self.clock = pygame.time.Clock()
        self.running = True

        self.particle_system = ParticleSystem()
        self.manager = pygame_gui.UIManager((1280, 720))

        self.create_ui_elements()

    def create_ui_elements(self):
        labels = ["X", "Y", "VX", "VY", "DVX", "DVY", "Angle", "DAngle", "Speed", "Lifespan", "Size", "Red", "Green", "Blue", "Alpha", "Shape"]
        defaults = [400, 300, random.uniform(-1, 1), random.uniform(-1, 1), 0, 0, 0, 0.1, 2, 60, 10, 255, 0, 0, 255, 'circle']
        y = 10
        self.input_boxes = []
        for label, default in zip(labels, defaults):
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, y), (100, 30)), text=label, manager=self.manager)
            self.input_boxes.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((120, y), (200, 30)), manager=self.manager))
            self.input_boxes[-1].set_text(str(default))
            y += 40

        self.add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, y), (200, 30)), text="Add Particle", manager=self.manager)

    def add_particle(self):
        values = [box.get_text() for box in self.input_boxes]
        x, y, vx, vy, dvx, dvy, angle, dangle, speed, lifespan, size, red, green, blue, alpha, shape = values
        self.particle_system.add_particle(float(x), float(y), float(vx), float(vy), float(dvx), float(dvy), float(angle), float(dangle), float(speed), int(lifespan), int(size), int(red), int(green), int(blue), int(alpha), shape)

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.add_button:
                        self.add_particle()
                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.fill((30, 30, 30))
            self.manager.draw_ui(self.screen)

            delta_time = self.clock.tick(120) / 1000.0
            self.particle_system.update(delta_time=delta_time)
            self.particle_system.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    gui = ParticleTester()
    gui.run()