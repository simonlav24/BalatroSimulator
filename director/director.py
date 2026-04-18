

from domain.board import Board
from domain.card import CardData, Card
from domain.joker import Joker
from domain.factory import Factory

from core.event_bus import EventBus
from core.data_registry import DataRegistry

from visual.view_registry import ViewRegistry
from visual.card_view import CardView, create_card_surf, create_joker_surf
from visual.renderer import Renderer
from visual.input_system import InputSystem
from visual.animation_system import AnimationSystem
from visual.board_view import BoardView

from director.board_player import BoardPlayer
from director.card_factory import CardFactory


class Director:
    def __init__(self):
        self.event_bus = EventBus()
        self.board = Board()
        self.data_registry = DataRegistry()
        self.view_registry = ViewRegistry()
        self.factory = Factory(self.event_bus, self.data_registry)

        self.renderer = Renderer(self.board, self.view_registry)
        self.board_view = BoardView(self.view_registry, self.data_registry)

        self.input_system = InputSystem(self.board_view, self.event_bus)
        self.animation_system = AnimationSystem(self.view_registry)
        self.board_player = BoardPlayer(self.board, self.board_view, self.event_bus, self.animation_system)
    
    def get_card_factory(self) -> CardFactory:
        return CardFactory(self.data_registry, self.event_bus, self.view_registry)

    def get_player(self) -> BoardPlayer:
        return self.board_player

    def step(self) -> None:
        # handle game events
        for event in self.event_bus.get_game_queue():
            self.handle_event(event)

        self.board_view.step()
        self.animation_system.step()

    def handle_event(self, event) -> None:
        self.board_player.handle_event(event)

    



