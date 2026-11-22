#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pygame

from code.Menu import Menu

if TYPE_CHECKING:
    from Background import Background
    from Level import Level
    from Player import Player


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 450))
        self.current_level: Optional[Level] = None
        self.player: Optional[Player] = None
        self.background: Optional[Background] = None

        self.game_status: str = "menu"
        self.current_player_name: str = ""
        self.score: int = 0
        self.history: list = []



    def start_game(self) -> None:
        pass

    def next_level(self) -> None:
        pass

    def check_game_over(self) -> bool:
        return False

    def restart_game(self) -> None:
        pass

    def record_result(self) -> None:
        pass

    def run(self) -> None:
        pygame.display.set_caption("Color Runner")

        menu = Menu(self.window)
        menu.run()

