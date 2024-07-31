from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):  # __ é método privado que só funciona nessa classe
        if isinstance(ent, Enemy):  # verifica se a entidade é inimigo
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # lista de entidades
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # lista de entidades
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
