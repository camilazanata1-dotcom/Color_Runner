#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import annotations

import pygame
from typing import TYPE_CHECKING, Optional

from code.Menu import Menu

if TYPE_CHECKING:
    from Background import Background
    from Level import Level
    from Player import Player


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))
        self.current_level: Optional[Level] = None
        self.player: Optional[Player] = None
        self.background: Optional[Background] = None

        self.game_status: str = "menu"
        self.current_player_name: str = ""
        self.score: int = 0
        self.history: list = []

        self.window = None

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
        clock = pygame.time.Clock()
        running = True

        while running:
            menu = Menu(self.window)
            menu.run()
            pass


        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            running = False
        #    pygame.display.flip()
        #    clock.tick(60)

        #pygame.quit()
