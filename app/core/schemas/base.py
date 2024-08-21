from typing import Annotated
from pydantic import BaseModel, Field


class UserPhraseCreate(BaseModel):
    phrase: str
    positive_score: Annotated[float, Field(ge=0, le=1)]
    neutral_score: Annotated[float, Field(ge=0, le=1)]
    negative_score: Annotated[float, Field(ge=0, le=1)]
