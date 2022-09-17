import pygame.font

class Scoreboard:
    """Classe pour afficher les informations de score."""
    
    def __init__(self, ai_game):
        """Initialise les attributs du suivi de score"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Paramètres de police des informations de score.
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prépare l'image de score initiale.
        self.prep_score()
        
    def prep_score(self):
        """Transforme le score en image restituée à l'écran"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Affiche le score en haut à droite de l'écran.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Dessine le score à l'écran"""
        self.screen.blit(self.score_image, self.score_rect)    