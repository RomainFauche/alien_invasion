import sys

import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    """Classe globale pour gérer les ressources et le comportement du jeu."""
    
    def __init__(self):
        """Initialiser le jeu et créer ses resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        
    def run_game(self):
        """Commencer la boucle principale du jeu."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Surveiller les évements de clavier et de la souris.
            
    def  _check_events(self):
        """Répondre aux événements de touche enfoncée et de la souris""" 
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()   
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:  
                    self._check_keyup_events(event)  
                   
    def _check_keydown_events(self, event):
        """Répondre aux événements de touche enfoncée."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """Répondre au événement de touche relacher"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False                   
                                                               
    def _update_screen(self):                            
        """Mettre à jour les images à l'écran et passer au nouvel écran"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
                    
        # Afficher l'écran le plus récemment dessiné.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Créer une instance du jeu et lancer le jeu.
    ai = AlienInvasion()
    ai.run_game()