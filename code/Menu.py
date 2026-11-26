#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 140, 0)
COLOR_YELLOW = (255, 220, 0)
COLOR_BLACK = (0,0,0)

MENU_OPTIONS = ["PLAY", "INSTRUCTIONS", "HISTORY", "EXIT"]
WIN_WIDTH = 800

class Menu:

    def __init__(self, window):
        self.selected_action = None
        self.running = True
        self.window = window
        self.player_name: str | None = None
        self.surf = pygame.image.load('./asset/Menu.png')
        self.surf = pygame.transform.scale(self.surf, (800, 450))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0

    def run(self) -> None:
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        while self.running:
            self.display()
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(MENU_OPTIONS)

                    if event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTIONS)

                    if event.key == pygame.K_RETURN:
                        self.handle_selection()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_selection()

        pygame.mixer.music.stop()

    def menu_text(self, text_size: int, text: str, text_color: tuple,
                  text_center_pos: tuple, shadow: bool = True, text_pos=None) -> None:

        text_font: pygame.font.Font = pygame.font.SysFont(name="Algerian", size=text_size)

        if shadow:
            shadow_surf = text_font.render(text, True, (0, 0, 0))
            shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 3, text_center_pos[1] + 3))
            self.window.blit(shadow_surf, shadow_rect)

        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)

    def menu_text_left(self, text_size: int, text: str, text_color: tuple,
                       text_pos: tuple) -> None:

        text_font = pygame.font.SysFont(name="Arial", size=text_size)

        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(topleft=text_pos)

        self.window.blit(text_surf, text_rect)

    def display(self) -> None:
        self.window.blit(source=self.surf, dest=self.rect)

        self.menu_text(40, "COLOR RUNNER", COLOR_WHITE, (400, 100))

        mouse_pos = pygame.mouse.get_pos()

        for i in range(len(MENU_OPTIONS)):
            text = MENU_OPTIONS[i]
            text_pos = (400, 215 + 60 * i)

            font = pygame.font.SysFont(name="Algerian", size=25)
            text_rect = font.render(text, True, COLOR_WHITE).get_rect(center=text_pos)

            if text_rect.collidepoint(mouse_pos):
                self.menu_option = i

            if i == self.menu_option:
                text_size = 32
                text_color = COLOR_ORANGE
            else:
                text_size = 25
                text_color = COLOR_WHITE

            self.menu_text(text_size, text, text_color, text_pos)

    def show_instructions(self) -> None:

        instructions = True

        while instructions:
            self.window.blit(self.surf, self.rect)
            panel = pygame.Surface((500, 260), pygame.SRCALPHA)
            panel.fill((255, 255, 255, 210))

            self.window.blit(panel, (150, 125))

            self.menu_text(28, "INSTRUÇÕES", COLOR_ORANGE, (400, 100))

            self.menu_text_left(18, "CONTROLES", COLOR_ORANGE, (180, 140))

            self.menu_text_left(18, "↑ - PULAR", COLOR_BLACK, (180, 180))

            self.menu_text_left(18, "↓ - AGACHAR", COLOR_BLACK, (180, 215))

            self.menu_text_left(18, "ESPAÇO - TROCAR DE COR", COLOR_BLACK, (180, 250))

            self.menu_text_left(18, "Corra, colete os diamantes da MESMA cor do personagem e acumule", COLOR_ORANGE, (180, 280))

            self.menu_text_left(18, "pontos para alcançar a maior pontuação possível!",COLOR_ORANGE, (180, 300))

            self.menu_text_left(18, "No nível 2, use a troca de cores para combinar com os obstáculos", COLOR_BLACK, (180, 325))

            self.menu_text_left(18, "e facilitar sua passagem!", COLOR_BLACK, (180, 350))

            self.menu_text(18, "Pressione ESC para voltar", COLOR_ORANGE, (400, 420))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    instructions = False
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        instructions = False

    def show_history(self) -> None:
        pass

    def handle_selection(self) -> None:

        selected_option = MENU_OPTIONS[self.menu_option]

        if selected_option == "PLAY":
            self.selected_action = "play"
            self.running = False

        elif selected_option == "INSTRUCTIONS":
            self.show_instructions()

        elif selected_option == "HISTORY":
            self.show_history()

        elif selected_option == "EXIT":
            self.selected_action = "exit"
            self.running = False

    def get_player_name(self) -> str:
        pass
