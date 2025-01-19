import pygame

class Particle:
    def __init__(self, x: float, y: float, vx: float, vy: float, dvx: float, dvy: float, angle: float, dangle: float, speed: float, lifespan: int, size: int, red: int, green: int, blue: int, alpha: int, shape: str, gradient: bool = False) -> None:
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

    def apply_force(self, fx: float, fy: float) -> None:
        self.vx += fx
        self.vy += fy

    def update(self, x: float, y: float, delta_time: float = None) -> None:
        if delta_time is None:
            delta_time = 1.0
        self.apply_force(self.dvx * delta_time, self.dvy * delta_time)
        self.x += self.vx * self.speed * delta_time
        self.x += x * delta_time
        self.y += self.vy * self.speed * delta_time
        self.y += y * delta_time
        self.angle += self.dangle * delta_time
        if self.alpha > 0 and self.lifespan > 0:
            self.alpha -= self.alpha // (1 / 60 * self.lifespan) * delta_time
            self.lifespan -= 60 * delta_time

    def draw(self, screen: pygame.Surface) -> None:
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

    def draw_star(self, surface: pygame.Surface, color: tuple, size: int, i: int) -> None:
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