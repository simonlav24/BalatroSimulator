


from core.id_gen import SingletonMeta
from director.director import Director

class DebugHelper(metaclass=SingletonMeta):

    def set_director(self, director: Director) -> None:
        self.director = director
    
    def print_hand_cards(self) -> None:
        data_reg = self.director.data_registry

        print(f'domain:')
        for card in self.director.board.hand_cards:
            print(f"{card}, ", end='')
        print(f'\nview:')
        for card_view in self.director.board_view.hand_row.cards:
            card_data = data_reg[card_view.id]
            print(f"{card_data}, ", end='')
        print('\n-----------------------------------------------')

