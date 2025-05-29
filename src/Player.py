#from card import Card

class Player:
    def __init__(self):
        self._cards: list[tuple] = []
        """# @AssociationMultiplicity 0..3
        # @AssociationKind Aggregation"""
        self._won_game: bool = False
        self._your_turn: bool = False
        self._player_id: str = None

    def initialize(self, player_id: str = ""):
        self.reset()
        self.player_id = player_id

    def reset(self):
        self._cards = []
        self._won_game = False
        self._your_turn = False

    def switch_turn(self):
        self._your_turn = not self._your_turn

    def get_player_id(self) -> str:
        return self._player_id

    def get_turn(self) -> bool:
        return self._your_turn

    def get_player_wins(self) -> list:
        return self._hand_wins

    def assign_game_win(self):
        self._won_game = True

    def get_cards(self) -> list[tuple]:
        return self._cards

    def receive_cards(self, cards: list):
        self._cards = list(
            map(lambda card: (Card.from_dict(card), self._player_id), cards)
        )
    
    def remove_card(self, card: tuple):
        self._cards.remove(card)
