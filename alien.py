import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe pour représenter un alien"""
    
    def __init__(self, ai_game):
        """Initialiser l'alien et définir sa position initial."""
        super().__init__()
        self.screen = ai_game.screen
        
        # Charger l'image et définir son attribut rect.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        # Placer chaque nouvel alien près de l'angle supérieur gauche de l'écran.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Stocker la position horizontale exacte de l'alien.
        self.x = float(self.rect.x)
        