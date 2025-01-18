import pygame

class Particle:
    def __init__(self, x, y, vx, vy, dvx, dvy, angle, dangle, speed, lifespan, size, red, green, blue, alpha, shape, gradient=False):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dvx = dvx
        self.dvy = dvy
        self.angle = angle
        self.dangle = dangle
        self.speed = speed
        self.lifespan = lifespan
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        self.shape = shape
        self.gradient = gradient

    def apply_force(self, fx, fy):
        self.vx += fx
        self.vy += fy

    def update(self, x, y):
        self.apply_force(self.dvx, self.dvy)
        self.x += self.vx * self.speed
        self.x += x
        self.y += self.vy * self.speed
        self.y += y
        self.angle += self.dangle
        if self.alpha > 0 and self.lifespan > 0:
            self.alpha -= self.alpha // (1 / 2 * self.lifespan)
            self.lifespan -= 2

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()
        if 0 <= self.x <= screen_width and 0 <= self.y <= screen_height:
            surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            if self.gradient:
                for i in range(self.size, 0, -1):
                    color = (self.red, self.green, self.blue, self.alpha - int(self.alpha * (i / self.size)))
                    if self.shape == 'circle':
                        pygame.draw.circle(surface, color, (self.size, self.size), i)
                    elif self.shape == 'square':
                        pygame.draw.rect(surface, color, pygame.Rect(self.size - i, self.size - i, i * 2, i * 2))
                    elif self.shape == 'triangle':
                        pygame.draw.polygon(surface, color,
                                            [(self.size, self.size - i), (self.size - i, self.size + i),
                                             (self.size + i, self.size + i)])
                    elif self.shape == 'star':
                        self.draw_star(surface, color, self.size, i)
            else:
                color = (self.red, self.green, self.blue, self.alpha)
                if self.shape == 'circle':
                    pygame.draw.circle(surface, color, (self.size, self.size), self.size)
                elif self.shape == 'square':
                    pygame.draw.rect(surface, color, pygame.Rect(0, 0, self.size * 2, self.size * 2))
                elif self.shape == 'triangle':
                    pygame.draw.polygon(surface, color,
                                        [(self.size, 0), (0, self.size * 2), (self.size * 2, self.size * 2)])
                elif self.shape == 'star':
                    self.draw_star(surface, color, self.size, self.size)

            # Rotate the surface based on the angle
            rotated_surface = pygame.transform.rotate(surface, self.angle)
            new_rect = rotated_surface.get_rect(center=(self.x, self.y))
            screen.blit(rotated_surface, new_rect.topleft)

    def draw_star(self, surface, color, size, i):
        points = [
            (size, size - i),
            (size + i * 0.2, size - i * 0.2),
            (size + i, size - i * 0.2),
            (size + i * 0.4, size + i * 0.2),
            (size + i * 0.6, size + i),
            (size, size + i * 0.4),
            (size - i * 0.6, size + i),
            (size - i * 0.4, size + i * 0.2),
            (size - i, size - i * 0.2),
            (size - i * 0.2, size - i * 0.2)
        ]
        pygame.draw.polygon(surface, color, points)