import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Classe globale pour gérer les ressources et le comportement du jeu."""
    
    def __init__(self):
        """Initialiser le jeu et créer ses resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        
    def run_game(self):
        """Commencer la boucle principale du jeu."""
        while True:
            # Surveiller les évements de clavier et de la souris.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redessiner l'écran à chaque exécution de la boucle.
            self.screen.fill(self.settings.bg_color)
                    
            # Afficher l'écran le plus récemment dessiné.
            pygame.display.flip()
            
if __name__ == '__main__':
    # Créer une instance du jeu et lancer le jeu.
    ai = AlienInvasion()
    ai.run_game()