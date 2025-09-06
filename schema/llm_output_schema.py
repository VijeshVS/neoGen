from pydantic import BaseModel, Field

class File(BaseModel):
    name: str = Field(description="Name of the file")
    path: str = Field(description="The path of the file")

class Plan(BaseModel):
    name: str = Field(description="Name of the application to be built")
    description: str = Field(description="A one liner description of the application to be built")
    techstack: str = Field(description="The tech stack to be used for the app, e.g. react,flask,django etc")
    features: str = Field(description="List of features that is needed in the application e.g user authentication")
    files: list[File] = Field(description="List of files that should be created")

class Step(BaseModel):
    step_detail: str = Field(
        description="A detailed instruction describing a specific step to be performed."
    )

class ImplementationDetails(BaseModel):
    filePath: str = Field(
        description="The relative file path for which the implementation steps are provided."
    )
    steps: list[Step] = Field(
        description="An ordered list of steps required to implement changes in the file."
    )

class ImplementationTask(BaseModel):
    implementations: list[ImplementationDetails] = Field(
        description="A collection of implementation instructions for all files in the project."
    )
