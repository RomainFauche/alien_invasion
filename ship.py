import pygame
class Ship:
    """Classe pour gérer la fusée."""
    
    def __init__(self, ai_game):
        """Initialise la fusée et définis sa position initile"""
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Charger l'image de fusée et obtenir son rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        
        # Placer chaque nouvelle fusée au centre et en bas de l'écran.
        self.rect.midbottom = self.screen_rect.midbottom

        #Stoker une valeur décimale correspondant à la positon horizontale de la fusée
        self.x = float(self.rect.x)
        # Drapeau de déplacement
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Mettre à jour la position de la fusée en fonction du drapeau de déplacement"""
        # Mettre à jour la valeur x de la fusée, pas le rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Mettre à jour l'objet rect en fonction de self .x.
        self.rect.x = self.x
        
    def blitme(self):
        """Dessine la fusée à son emplacement actuel"""    
        self.screen.blit(self.image, self.rect)