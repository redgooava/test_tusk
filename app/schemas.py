from pydantic import BaseModel


class AppendRequest(BaseModel):
    links: list[str]


class AppendResponse(BaseModel):
    links: dict[str, str]
    links_num: int


class FindRequest(BaseModel):
    links_list: list[int]


class FindResponse(BaseModel):
    pass
