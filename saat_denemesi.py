"""import pygame
import random
import sys
# Pygame başlat
pygame.init()

# Renk tanımlamaları
BLUE = (135, 206, 235)  # Gökyüzü rengi

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Clock")
for i in range(13):
    pygame.image.load(f"{i}clock.png")
zero_clock=pygame.image.load('0clock.png')
def sittin_scale_image(image, width_ratio, height_ratio):
    new_width = int(zero_clock.get_width() * width_ratio)
    new_height = int(zero_clock.get_height() * height_ratio)
    return pygame.transform.scale(image, (new_width, new_height))
class Clock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        screen.blit(zero_clock, (self.x - zero_clock.get_width() // 2, self.y - zero_clock.get_height()))



ducks = [Clock(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(10)]

# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fare pozisyonu
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Ekranı temizle
    screen.fill(BLUE)

    # Ördekleri çiz
    for duck in ducks:
        # Eğer fare ördeğin üzerindeyse, ayağa kalk
        if (duck.x - 30 < mouse_x < duck.x + 30) and (duck.y - 30 < mouse_y < duck.y + 30):
            duck.is_standing = True
        else:
            duck.is_standing = False
        duck.draw()

    # Ekranı güncelle
    pygame.display.flip()"""
import pygame
import os

# Pygame'i başlat
pygame.init()

# Ekran boyutu
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Saatin merkezi
clock_center = (screen_width // 2, screen_height // 2)

# 12 adet saatin resmini yükle
clock_images = []
for i in range(0, 13):
    image = pygame.image.load(os.path.join(f"{i}clock.png"))
    clock_images.append(pygame.transform.scale(image, (150, 150)))  # İstediğin boyuta göre ayarla

# Saatin alanı
clock_rect = clock_images[0].get_rect(center=clock_center)

# Döngü ile resimleri değiştirme ayarları
image_index = 0
rotating = False

# FPS kontrolü
clock = pygame.time.Clock()

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fare pozisyonunu al
    mouse_pos = pygame.mouse.get_pos()

    # İmleç saatin üzerine geldiğinde döndürme işlemini başlat
    if clock_rect.collidepoint(mouse_pos):
        rotating = True
    else:
        rotating = False

    # Ekranı temizle
    screen.fill((255, 255, 255))  # Beyaz arkaplan

    # Resimleri döndür
    if rotating:
        image_index = (image_index + 1) % 12

    # Şu anki saatin resmini ekrana çiz
    screen.blit(clock_images[image_index], clock_rect)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı (örn: 10 resim/sn)
    clock.tick(10)
pygame.quit()
"""
aduket
import pygame
import os

# Pygame'i başlat
pygame.init()

# Ekran boyutu
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Saatin merkezi
clock_center = (screen_width // 2, screen_height // 2)

# 12 adet saatin resmini yükle
clock_images = []
for i in range(0, 2):
    image = pygame.image.load(os.path.join(f"aduket{i}.png"))
    clock_images.append(pygame.transform.scale(image, (150, 150)))  # İstediğin boyuta göre ayarla

# Saatin alanı
clock_rect = clock_images[0].get_rect(center=clock_center)

# Döngü ile resimleri değiştirme ayarları
image_index = 0
rotating = False

# FPS kontrolü
clock = pygame.time.Clock()

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fare pozisyonunu al
    mouse_pos = pygame.mouse.get_pos()

    # İmleç saatin üzerine geldiğinde döndürme işlemini başlat
    if clock_rect.collidepoint(mouse_pos):
        rotating = True
    else:
        rotating = False

    # Ekranı temizle
    screen.fill((255, 255, 255))  # Beyaz arkaplan

    # Resimleri döndür
    if rotating:
        image_index = (image_index + 1) % 2

    # Şu anki saatin resmini ekrana çiz
    screen.blit(clock_images[image_index], clock_rect)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı (örn: 10 resim/sn)
    clock.tick(10)
pygame.quit()
"""
