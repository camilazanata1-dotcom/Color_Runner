#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Obstacle(Entity):

    def __init__(self):
        self.color: Color = None
        self.passed: bool = None
        self.collided: bool = None

    def move(self) -> void:
        pass
