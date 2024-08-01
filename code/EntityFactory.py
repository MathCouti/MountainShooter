import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:  # factory não tem __init__ (construtor)
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':  # BACKGROUND DO LEVEL 1
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':  # BACKGROUND DO LEVEL 2
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':  # BACKGROUND DO LEVEL 3
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
