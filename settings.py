class Settings:
    """Classe pour stocker les paramètres d'Alien Invasion."""
    
    def __init__(self):
        """Initialiser les paramètres statique du jeu."""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (60, 60, 60)
        
        # Paramètre de la fusée        
        self.ship_limit = 3
        
        # Paramètre des balles        
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (236, 236, 236)
        self.bullet_allowed = 5
        
        # Paramètres d'un alien        
        self.fleet_drop_speed = 10
        
        # Rythme d'accélération du jeu
        self.speedup_scale = 1.1
        # Rapidité d'augmentation de la en points des aliens
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialise les paramètres qui changent pendant la partie."""
        self.ship_speed = 8.5
        self.bullet_speed = 10.0
        self.alien_speed = 1.5
        
        # fleet_direction = 1 correspond à la droite ; -1 à la gauche
        self.fleet_direction = 1 
        
        # Score
        self.alien_points = 50
        
    def increase_speed(self):
        """Augmente les paramètre de vitesse et la valeur en points des aliens"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)