#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Player(Entity):

    def __init__(self):
        self.color: Color = None
        self.lives: int = None
        self.state: str = None

    def jump(self) -> void:
        pass

    def crouch(self) -> void:
        pass

    def change_color(self) -> void:
        pass

    def lose_life(self) -> void:
        pass

    def reset_for_level(self) -> void:
        pass
