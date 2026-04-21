
import inspect
import domain.jokers as jokers


def get_all_joker_classes():
    return [
        cls for _, cls in inspect.getmembers(jokers, inspect.isclass)
        if cls.__module__ == jokers.__name__
    ]