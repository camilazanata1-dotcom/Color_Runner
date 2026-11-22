#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Background import Background
    from Obstacle import Obstacle
    from Player import Player


class EntityFactory:

    def create_player(self) -> Player:
        pass

    def create_obstacle(self) -> Obstacle:
        pass

    def create_background(self) -> Background:
        pass
