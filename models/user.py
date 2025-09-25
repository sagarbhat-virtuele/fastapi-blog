from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    blogs = relationship('Blog', back_populates='creator')
    profile = relationship("Profile", back_populates="user", uselist=False)  
    likes = relationship("Like", back_populates="user", cascade="all, delete-orphan")

    @property
    def liked_blogs(self):
        return [like.blog for like in self.likes]