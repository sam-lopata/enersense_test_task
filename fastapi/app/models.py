from typing import Optional, List
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from pydantic import ConfigDict, BaseModel, Field

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class SessionModel(BaseModel):
    """
    Container for a single session.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    timestamp: int = Field(...)
    topic: str = Field(...)
    payload: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class SessionCollection(BaseModel):
    """
    A container holding a list of `SessionModel` instances.
    """

    sessions: List[SessionModel]
