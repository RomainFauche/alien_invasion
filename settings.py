class Settings:
    """Classe pour stocker les paramètres d'Alien Invasion."""
    
    def __init__(self):
        """Initialiser les paramètres du jeu."""
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (139, 186, 192)
        
        # Paramètre de la fusée
        self.ship_speed = 1.5
        
        # Paramètre des balles
        self.bullet_speed = 1.0
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (207, 164, 13)