from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


# class Category(Base):
#     __tablename__ = "category"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)		
#     created_by = Column(String(20))
#     date_created = Column(String(15))



class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    # category = relationship("Category", back_populates="blogs")
