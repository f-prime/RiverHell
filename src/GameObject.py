from abc import ABC, abstractmethod

class GameObject(ABC):
    """
    This is just an abstract game object. Other game objects
    inheret this class and implement update. This also allows
    us to use a type other than "Any" in the Game class.
    
    Other than this, inheritance should not be used.
    """

    @abstractmethod
    def update(self, game: "Game") -> None:
        ...
