from pydantic import BaseModel


class AdviceRequest(BaseModel):
    query: str


class AdviceResponse(BaseModel):
    advice: str
