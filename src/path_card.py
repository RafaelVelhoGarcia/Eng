from card import Card

class PathCard(Card):
    def __init__(self, 
                 card_id: int, 
                 is_destroyable: bool, 
                 north: bool, 
                 south: bool, 
                 east: bool, 
                 west: bool, 
                 is_continuous: bool):
        super().__init__(card_id)
        self._is_destroyable = is_destroyable
        self._north = north
        self._south = south
        self._east = east
        self._west = west
        self._is_continuous = is_continuous

    def to_dict(self) -> dict:
        """Convert the PathCard to a dictionary for serialization"""
        return {
            '_card_id': self._card_id,
            '_is_destroyable': self._is_destroyable,
            '_north': self._north,
            '_south': self._south,
            '_east': self._east,
            '_west': self._west,
            '_is_continuous': self._is_continuous
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a PathCard from a dictionary"""
        return cls(
            card_id=data['_card_id'],
            is_destroyable=data['_is_destroyable'],
            north=data['_north'],
            south=data['_south'],
            east=data['_east'],
            west=data['_west'],
            is_continuous=data['_is_continuous']
        )

    # Standard getter and setter methods
    def get_north(self) -> bool:
        """Get the north path status"""
        return self._north

    def set_north(self, value: bool) -> None:
        """Set the north path status"""
        self._north = value

    def get_south(self) -> bool:
        """Get the south path status"""
        return self._south

    def set_south(self, value: bool) -> None:
        """Set the south path status"""
        self._south = value

    def get_east(self) -> bool:
        """Get the east path status"""
        return self._east

    def set_east(self, value: bool) -> None:
        """Set the east path status"""
        self._east = value

    def get_west(self) -> bool:
        """Get the west path status"""
        return self._west

    def set_west(self, value: bool) -> None:
        """Set the west path status"""
        self._west = value

    # Other getters and setters
    def get_is_destroyable(self) -> bool:
        """Check if the card is destroyable"""
        return self._is_destroyable

    def get_is_continuous(self) -> bool:
        """Check if the path is continuous"""
        return self._is_continuous

    def set_is_continuous(self, value: bool) -> None:
        """Set if the path is continuous"""
        self._is_continuous = value

    def rotate(self) -> None:
        """Rotate the card 90 degrees clockwise"""
        # Store the current north value before rotation
        previous_north = self._north
        # Rotate each direction
        self._north = self._west
        self._west = self._south
        self._south = self._east
        self._east = previous_north

    def to_string(self):
        return f"Card(id={self._card_id})"