import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("IotVers Game")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player = Player()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullet_group.add(bullet)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    elif keys[pygame.K_RIGHT]:
        player.rect.x += 5
    bullet_group.update()
    bullet_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.flip()
pygame.quit()