from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs" 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')
    likes = relationship("Like", back_populates="blog", cascade="all, delete-orphan")

    @property
    def liked_by(self):
        return [like.user for like in self.likes]