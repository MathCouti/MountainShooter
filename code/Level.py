import random

import pygame
import sys
from cgitb import text

import pygame.display
from pygame import Surface, KEYDOWN, K_ESCAPE

from code import Entity
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAM, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode : str, player_score : list[int], TIME : TIMEOUT_LEVEL,
                 list_enemys : list[str]):
        self.window = window
        self.timeout = TIME  # 20 segundos
        self.name = name
        self.list_enemys = list_enemys
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # extend para mais de 1
        player = EntityFactory.get_entity('Player1')  # append para 1 entidade
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')  # append para 1 entidade
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100MS

    def run(self, player_score : list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela antes de redesenhar

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAM, (10, 45))

            for event in pygame.event.get():   #CHECAGENS DE EVENTOS
                if event.type == pygame.QUIT: # evento de fechar
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == EVENT_ENEMY: # evento de spawn inimigo
                    choise = random.choice(self.list_enemys)
                    self.entity_list.append(EntityFactory.get_entity(choise))
                if event.type == EVENT_TIMEOUT:  # evento de time
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False     # evento de morte de player
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Verifies
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
