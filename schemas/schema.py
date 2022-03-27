from pydantic import BaseModel

    
class BlogSchema(BaseModel):
    title: str
    slug: str
    description: str
    is_active: bool

    class Config:
        orm_mode=True

