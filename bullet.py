import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe pour gérer les balles tirées par la fusée"""
    
    def __init__(self, ai_game):
        """Créer un objet balle à l'emplacement de la fusée"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Créer un rect de balle en (0, 0) puis définir sa position correcte.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Stoker la position de la balle sous la forme d'une valeur décimal.
        self.y = float(self.rect.y)
    
    def update(self):
        """Faire monter la balle à l'écran."""
        # Mettre à jour la position décimale de la balle.
        self.y -= self.settings.bullet_speed
        # Mettre à jour la position de rect.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Dessiner la balle à l'écran."""
        pygame.draw.rect(self.screen, self.color, self.rect)