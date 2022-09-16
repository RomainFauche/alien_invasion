class GameStats:
    """Suivre les statistiques d'alien invasion."""
    
    def __init__(self, ai_game):
        """Initialiser les statistique"""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialiser les statisique qui peuvent changer pendant le jeu."""
        self.ships_left = self.settings.ship_limit