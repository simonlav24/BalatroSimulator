

from domain.board import Board
from domain.factory import Factory

from core.event_bus import EventBus
from core.data_registry import DataRegistry

from visual.view_registry import ViewRegistry
from visual.renderer import Renderer
from visual.input_system import InputSystem
from visual.animation_system import AnimationSystem
from visual.effect_system import EffectSystem
from visual.board_view import BoardView
from visual.texturizer import CardTexturizer
from visual.ui_layer_round import UILayerRound

from director.board_player import BoardPlayer
from director.card_factory import CardFactory


class Director:
    def __init__(self):
        self.event_bus = EventBus()
        self.board = Board()
        self.data_registry = DataRegistry()
        self.view_registry = ViewRegistry()
        self.factory = Factory(self.event_bus, self.data_registry)

        self.board_view = BoardView(self.view_registry, self.data_registry)

        self.texturizer = CardTexturizer(self.data_registry, self.view_registry)
        self.effect_system = EffectSystem()
        self.animation_system = AnimationSystem(self.view_registry, self.board_view, self.effect_system, self.texturizer)
        self.input_system = InputSystem(self.board_view, self.event_bus)
    
        self.board_player = BoardPlayer(self.board, self.board_view, self.event_bus, self.animation_system, self.data_registry, self.view_registry)

        self.renderer = Renderer(self.board_view, self.view_registry, self.input_system)
        self.renderer.register_system(self.effect_system)
        self.ui_layer = None
        
    def get_card_factory(self) -> CardFactory:
        return CardFactory(self.data_registry, self.event_bus, self.view_registry)

    def get_player(self) -> BoardPlayer:
        return self.board_player
    
    def step(self) -> None:
        for event in self.event_bus.get_game_events():
            self.board_player.handle_game_event(event)
            if self.ui_layer:
                self.ui_layer.handle_game_event(event)
        self.event_bus.step()

        self.input_system.step()
        self.board_view.step()
        self.animation_system.step()
        self.effect_system.step()

    def initialize_round_ui(self):
        ui = UILayerRound(self.input_system, self.event_bus)
        self.ui_layer = ui
        self.renderer.ui_layer = self.ui_layer



