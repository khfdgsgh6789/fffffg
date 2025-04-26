import pygame
pygame.init()
window = pygame.display.set_mode((750, 750))
window.fill((158, 213, 0))
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = color
        self.rect = pygame.Rect(x, y, width, height)
        
    def set_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        
    def draw(self):
        window.blit(self.image, (self.x, self.y))

platform_x = 200
platform_y = 300

# ВАЖЛИВО: ці зображення мають бути в одній папці з .py файлом
ball = Picture("ball.png", 160, 200, 50, 50)
platform = Picture("platform.png", platform_x, platform_y, 100, 30)

# створення ворогів
start_x = 5
start_y = 5
monsters = []
for i in range(4):
    y = start_y + (55 * i)
    x = start_x + (25 * i)
    for j in range(4):
        enemy = Picture("enemy.png", x, y, 50, 50)
        monsters.append(enemy)
        x += 55

game = True
while game:
    window.fill((158, 213, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    clock.tick(40)
    pygame.display.update()

pygame.quit()