from sqlalchemy.orm import Session
from schemas.schema import BlogSchema
from models.blog_models import Blog


def get_blog(db:Session, blog_id:int):
    return db.query(blog_models.Blog).filter(blog_models.Blog.id == blog_id).first()

def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(blog_models.Blog).offset(skip).limit(limit).all()



class BlogCrud:
    def __init__(self, db:Session) -> None:
        self.db_session = db

    async def create_blog(self, blog) -> dict[str, any]:
        db_blog = Blog(
            title = blog.title,
            slug = blog.slug,
            description = blog.description,
            is_active = blog.is_active
        )
        self.db_session.add(db_blog)
        await self.db_session.commit()
        return db_blog

    def get_blogs(self) -> list[Blog]:
        response = self.db_session.query(Blog).all()
        return response

    def get_blog(self, blog_id:int):
        response = self.db_session.query(Blog).get(blog_id)
        return response