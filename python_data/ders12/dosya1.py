import pygame
from datetime import datetime as dt

pygame.init()
pencere = pygame.display.set_mode((1024, 768))
tarih = dt.today().date()

pygame.display.set_caption(f"Tarih: {tarih.day}-{tarih.month}-{tarih.year}")

karakter = pygame.image.load("./assets/super-mario.png")
karakter_bilgi = karakter.get_rect()
karakter_bilgi.topleft = (120, 120)

pygame.draw.rect(pencere, (200, 200, 200), (100, 100, 800, 600), 5, border_radius=20)

def fontislemi():
    sistemfontu = pygame.font.SysFont("Arial", 24, bold=True, italic=True)
    font = sistemfontu.render("pygame modülü", True, (255, 0, 0), (255, 255, 0))
    font_koor = font.get_rect()
    font_koor.topleft = (400, 300)

kontrol True
while kontrol: 
    pencere.fill("dodgerblue")
    pygame.draw.rect(pencere, (200, 200, 200), (100, 100, 800, 600), 5, border_radius=20)
    