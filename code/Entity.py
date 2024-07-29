from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left = position[0], top=position[1])
        self.speed = 0

    @abstractmethod  #para o python n reclamar, pois quem vai implementar é os filhos
    def move(self,):
        pass