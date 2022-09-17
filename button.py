import pygame.font

class Button:
    
    def __init__(self, ai_game, msg):
        """Initialise les attributs du bouton."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Définir les dimensions et les propriétés du bouton.
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Crée l'objet rect du bouton et le centrer.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Message du crée une fois pour toutes.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Transforme msg en une image et centre le texte dans le bouton"""
        self.msg_image = self.font.render(msg, True, 
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Déssine le bouton vide, puisdessine le message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect) 