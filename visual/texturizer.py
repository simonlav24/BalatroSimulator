
import re
from enum import Enum
from typing import Any

import pygame
from pygame import Surface, SRCALPHA

from core.utils import Vector2, Rect
from core.data_registry import DataRegistry
from domain.board import Board
from domain.card import CardData
from domain.definitions import Enhancement, Seal
from domain.jokers import *
from visual.view_registry import ViewRegistry
from visual.renderer import create_card_surf
from visual.definitions import Colors
import visual.definitions as fonts

class CardTexturizer:
    def __init__(self, data_reg: DataRegistry, view_reg: ViewRegistry):
        self.data_reg = data_reg
        self.view_reg = view_reg

    def retexture_enhancement(self, id: int, enhancement: Enhancement) -> None:
        card_data: CardData = self.data_reg[id].data
        card_view = self.view_reg[id]
        card_view.surf = create_card_surf(card_data.rank, card_data.suit, enhancement, card_data.seal, card_data.edition)

TITLE_MARGIN = 4
DESC_MARGIN = 6
DESC_SIZE = Vector2(178, 200)
SPACE_LEN = 6
LINE_MARGIN = 3

class TokenHandle(Enum):
    NONE = 0
    CONTINUE = 1
    LINE_BREAK = 2

class DescriptionMaker:
    def __init__(self, board: Board):
        self.color = [Colors.DARK_GRAY]
        self.pos = Vector2()
        self.board = board
    
    def calculate_text(self, text: str, text_area_width: int) -> list[dict[str, Any]]:
        text_list = []
        tokens = self._tokenize_description(text)
        pos = Vector2(0, 0)
        sentence: list[Surface] = []
        sentence_len = 0
        for token in tokens:
            handle_key = self._handle_state_token(token)
            if handle_key == TokenHandle.CONTINUE:
                continue
            elif handle_key == TokenHandle.LINE_BREAK:
                self._flush_sentence(sentence, surf)
                sentence_len = 0
                continue
            # render and add to surf
            text = fonts.fonts.joker_description.render(token, False, self.color[-1])
            if sentence_len + SPACE_LEN + text.get_width() > surf.get_width() - 2 * DESC_MARGIN:
                # blit sentence
                self._flush_sentence(sentence, surf)
                sentence_len = 0
            else:
                sentence_len += SPACE_LEN + text.get_width()
            sentence.append(text)
        self._flush_sentence(sentence, surf)
        return text_list


    def _tokenize_description(self, text: str) -> list[str]:
        pattern = r'<[^>]+>|\b\w+\b'
        return re.findall(pattern, text)

    def _handle_state_token(self, token: str) -> TokenHandle:
        handled = TokenHandle.CONTINUE
        if token == '<red>':
            self.color.append(Colors.RED)
        elif token == '<yellow>':
            self.color.append(Colors.YELLOW)
        elif token == '<gray>':
            self.color.append(Colors.LIGHT_GRAY)
        elif token == '<orange>':
            self.color.append(Colors.YELLOW)
        elif token == '<cls>':
            self.color.pop(-1)
        elif token == '<br>':
            return TokenHandle.LINE_BREAK
        elif token.startswith('<'):
            print(f'unrecognized token {token}')
        else:
            handled = TokenHandle.NONE
        return handled

    def _flush_sentence(self, sentence: list[Surface], surf: Surface) -> None:
        if len(sentence) == 0:
            return
        sentence_len = sum(i.get_width() for i in sentence) + (len(sentence) - 1) * SPACE_LEN
        self.pos.x = surf.get_width() / 2 - sentence_len / 2
        for item in sentence:
            surf.blit(item, self.pos)
            self.pos.x += item.get_width() + SPACE_LEN
        self.pos.y += sentence[0].get_height() + LINE_MARGIN
        sentence.clear()

    def create_joker_description(self, joker: Joker) -> list[str]:
        description_str = joker.get_description(self.board)
        tokens = self._tokenize_description(description_str)
        surf = Surface(DESC_SIZE, SRCALPHA)
        pygame.draw.rect(surf, Colors.DARK_GRAY, surf.get_rect(), 0, 4)
        pygame.draw.rect(surf, Colors.LIGHT_GRAY, surf.get_rect(), 2, 4)
        name = fonts.fonts.joker_title.render(joker.data.name, False, Colors.WHITE)
        
        surf.blit(name, Vector2(surf.get_width() / 2 - name.get_width() / 2, TITLE_MARGIN))
        # pygame.draw.rect(surf, (255, 0, 0), (Vector2(surf.get_width() / 2 - name.get_width() / 2, TITLE_MARGIN), name.get_size()), 1)
        self.pos.y = 2 * TITLE_MARGIN + name.get_height()
        pygame.draw.rect(surf, Colors.WHITE, ((DESC_MARGIN, self.pos.y), DESC_SIZE - (DESC_MARGIN * 2, 100)), 0, 4)
        self.pos.y += DESC_MARGIN

        sentence: list[Surface] = []
        sentence_len = 0
        for token in tokens:
            handle_key = self._handle_state_token(token)
            if handle_key == TokenHandle.CONTINUE:
                continue
            elif handle_key == TokenHandle.LINE_BREAK:
                self._flush_sentence(sentence, surf)
                sentence_len = 0
                continue
            # render and add to surf
            text = fonts.fonts.joker_description.render(token, False, self.color[-1])
            if sentence_len + SPACE_LEN + text.get_width() > surf.get_width() - 2 * DESC_MARGIN:
                # blit sentence
                self._flush_sentence(sentence, surf)
                sentence_len = 0
            else:
                sentence_len += SPACE_LEN + text.get_width()
            sentence.append(text)
        self._flush_sentence(sentence, surf)
        return surf



