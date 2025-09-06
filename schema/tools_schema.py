from typing import Optional
from pydantic import BaseModel, Field

class ToolInput(BaseModel):
    path: Optional[str] = Field(
        default=None,
        description="Path of the file required by the tool (read_file or write_file)."
    )
    content: Optional[str] = Field(
        default=None,
        description="Content to write into a file when using write_file."
    )
    directory: Optional[str] = Field(
        default=None,
        description="Directory path to list files when using list_files."
    )
    cmd: Optional[str] = Field(
        default=None,
        description="Linux command to execute when using execute_command."
    )