from typing import Optional, Literal
from pydantic import BaseModel, Field
from .tools_schema import ToolInput

class OutputModel(BaseModel):
    step: Literal["START","PLAN","TOOL","OBSERVE","OUTPUT"]
    content: str
    tool_name: Optional[str] = Field(default=None, description="Name of the tool to be invoked")
    tool_input: Optional[ToolInput] = Field(
        default=None,
        description="Input arguments required by the selected tool"
    )