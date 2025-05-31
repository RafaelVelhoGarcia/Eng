from card import Card

class GoalCard(Card):
    def __init__(self, card_id: int, is_gold: bool):
        super().__init__(card_id)
        self._is_gold = is_gold
        self._is_revealed = False
    
    def reveal(self) -> None:
        self._is_revealed = True
    
    def is_revealed(self) -> bool:
        return self._is_revealed
    
    def is_gold(self) -> bool:
        return self._is_gold