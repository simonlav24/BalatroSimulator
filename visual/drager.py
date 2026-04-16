

from visual.view_registry import ViewRegistry

class Drager:
    def __init__(self, view_reg: ViewRegistry):
        self.view_reg = view_reg
    
    def handle_event(self, event) -> None:
        ...