from pydantic import BaseModel

class Query_Request(BaseModel):
    query: str