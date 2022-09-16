class Settings:
    """Classe pour stocker les paramètres d'Alien Invasion."""
    
    def __init__(self):
        """Initialiser les paramètres du jeu."""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (60, 60, 60)
        
        # Paramètre de la fusée
        self.ship_speed = 8.5
        
        # Paramètre des balles
        self.bullet_speed = 10.0
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (236, 236, 236)
        self.bullet_allowed = 5
        
        # Paramètres des aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 correspond à la droite ; 
        # -1 à la gauche
        self.fleet_direction = 1 