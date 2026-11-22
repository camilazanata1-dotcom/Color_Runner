#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Background import Background
    from Level import Level
    from Player import Player


class Game:

    def __init__(self):
        self.current_level: Level = None
        self.player: Player = None
        self.background: Background = None
        self.game_status: str = None
        self.current_player_name: str = None
        self.score: int = None
        self.history: list = None

    def start_game(self) -> void:
        pass

    def next_level(self) -> void:
        pass

    def check_game_over(self) -> bool:
        pass

    def restart_game(self) -> void:
        pass

    def record_result(self) -> void:
        pass
