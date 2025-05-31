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

    # Properties for all directions with getters and setters
    @property
    def north(self) -> bool:
        """Get the north path status"""
        return self._north

    @north.setter
    def north(self, value: bool) -> None:
        """Set the north path status"""
        self._north = value

    @property
    def south(self) -> bool:
        """Get the south path status"""
        return self._south

    @south.setter
    def south(self, value: bool) -> None:
        """Set the south path status"""
        self._south = value

    @property
    def east(self) -> bool:
        """Get the east path status"""
        return self._east

    @east.setter
    def east(self, value: bool) -> None:
        """Set the east path status"""
        self._east = value

    @property
    def west(self) -> bool:
        """Get the west path status"""
        return self._west

    @west.setter
    def west(self, value: bool) -> None:
        """Set the west path status"""
        self._west = value

    # Other properties
    @property
    def is_destroyable(self) -> bool:
        """Check if the card is destroyable"""
        return self._is_destroyable

    @property
    def is_continuous(self) -> bool:
        """Check if the path is continuous"""
        return self._is_continuous

    @is_continuous.setter
    def is_continuous(self, value: bool) -> None:
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