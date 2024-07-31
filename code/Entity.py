from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() #esse convert_alpha, ele trata o png de forma optimizada
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod  # para o python n reclamar, pois quem vai implementar é os filhos
    def move(self, ):
        pass
