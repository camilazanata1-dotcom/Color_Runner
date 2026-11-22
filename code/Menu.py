#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Menu:

    def __init__(self, window):
        self.window = window
        self.player_name: str | None = None
        self.surf = pygame.image.load('./asset/Menu.png')
        self.surf = pygame.transform.scale(self.surf, (800, 450))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self) -> None:
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        running = True

        while running:
            self.window.blit(source=self.surf, dest=self.rect)
            self.display()
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.mixer.music.stop()
        pygame.quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: pygame.font.Font = pygame.font.SysFont(name="Algerian", size=text_size)

        shadow_surf = text_font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 3, text_center_pos[1] + 3))

        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)

    def display(self) -> None:
        self.menu_text(40, "COLOR RUNNER", (255, 255, 255), (400, 100))

        self.menu_text(30, "PLAY", (255, 140, 0), (400, 215))
        self.menu_text(25, "INSTRUCTIONS", (255, 255, 255), (400, 275))
        self.menu_text(25, "HISTORY", (255, 255, 255), (400, 335))
        self.menu_text(25, "EXIT", (255, 255, 255), (400, 395))

    def show_instructions(self) -> None:
        pass

    def show_history(self) -> None:
        pass

    def handle_selection(self) -> None:
        pass

    def get_player_name(self) -> str:
        pass
