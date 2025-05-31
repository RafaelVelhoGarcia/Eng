from typing import Set
from .card import Card
from .tool import Tool
from .tool_type import ToolType

class RepairCard(Card):
    def __init__(self, card_id: int, tools: Set[ToolType]):
        super().__init__(card_id)
        self._tools = tools
    
    def get_repair_tools(self) -> Set[Tool]:
        return {Tool(tool_type) for tool_type in self._tools}