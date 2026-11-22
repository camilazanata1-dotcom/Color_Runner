#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Background import Background
    from Obstacle import Obstacle
    from Player import Player


class Level:

    def __init__(self):
        self.player: Player = None
        self.background: Background = None
        self.obstacles: list<Obstacle> = None
        self.speed: int = None
        self.status: str = None
        self.obstacles_passed: int = None
        self.obstacles_to_complete: int = None

    def create_obstacles(self) -> void:
        pass

    def check_collision(self) -> int:
        pass

    def check_level_complete(self) -> bool:
        pass

    def clear_obstacles(self) -> void:
        pass

    def check_obstacles_passed(self) -> void:
        pass
