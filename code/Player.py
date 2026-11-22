#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Color

from Entity import Entity


class Player(Entity):

    def __init__(self):
        self.color: Color = None
        self.lives: int = None
        self.state: str = None

    def jump(self) -> None:
        pass

    def crouch(self) -> None:
        pass

    def change_color(self) -> None:
        pass

    def lose_life(self) -> None:
        pass

    def reset_for_level(self) -> None:
        pass
