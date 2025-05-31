from typing import Optional
from .tool_type import ToolType

class Tool:
    def __init__(self, tool_type: ToolType):
        self.tool_type = tool_type
    
    def get_tool(self) -> 'Tool':
        return self