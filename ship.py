import pygame

class Ship:
    """Classe pour gérer la fusée."""
    
    def __ini__(self, ai_game):
        """Initialise la fusée et définis sa position initile"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Charger l'image de fusée et obtenir son rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Placer chaque nouvelle fusée au centre et en bas de l'écran.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Dessine la fusée à son emplacement actuel"""    
        self.screen.blit(self.image, self.rect)