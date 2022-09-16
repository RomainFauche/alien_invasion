import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        # Créer une instance pour stocker les statistiques du jeu.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_game(self):
        """Commencer la boucle principale du jeu."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()            
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
        elif event.key == pygame.K_SPACE:
                    self._fire_bullet() 
                        
    def _check_keyup_events(self, event):
        """Répondre au événement de touche relacher"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
            
    def _fire_bullet(self):
        """Créer une balle et l'ajouter dans le groupe de balles."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 
            
    def _update_bullets(self):
        """Mettre à jour la position des balles et supprimer les anciennes balles."""
        # Mettre à jour les position des balles.
        self.bullets.update()       
            
        # Supprimer les balles qui ont disparu.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 
                
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Répondre au collision balle-alien."""                
        # Rechercher les balles qui ont touché des aliens.
        # Si oui, suprimer la balle et l'alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
            ) 
        if not self.aliens:
        #détruire les balles exisantes et créer une autre armée.
            self.bullets.empty()
            self._create_fleet()
                
    def _update_aliens(self):
        """Vérifier si l'armée a atteint un bord , puis mettre à jour les positions de tous le aliens."""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Rechercher les collisions entre un alien et le joueur.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
             
    def _ship_hit(self):
        """Répondre à la percussion de la fusée par un alien."""
        # Décrémenter ships_left.
        self.stats.ships_left -= 1
        
        # Supprimer les bales et les aliens restants.
        self.aliens.empty()
        self.bullets.empty()
        
        # Créer une autre armée et centrer le joueur.
        self._create_fleet()
        self.ship.center_ship()
        
        # Faire une pause.
        sleep(0.8)
                
    def _create_fleet(self):
        """Créer l'armée d'aliens."""
        # Créer un alien et calculer leur nombre par ligne.
        # L'espace entre chaque alien est égal à la largeur d'un alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Déterminer le nombre de lignes d'aliens possible à l'écran.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Créer la première ligne d'aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):        
        """Créer un alien et le placer sur la ligne."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)     
    
    def _check_fleet_edges(self):
        """Répondre correctement si des aliens ont atteint un bord."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Faire descendre l'armée d'un cran et inverser son sens de déplacement."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
                                                                                 
    def _update_screen(self):                            
        """Mettre à jour les images à l'écran et passer au nouvel écran"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
                    
        # Afficher l'écran le plus récemment dessiné.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Créer une instance du jeu et lancer le jeu.
    ai = AlienInvasion()
    ai.run_game()