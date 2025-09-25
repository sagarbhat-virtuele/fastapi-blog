# models/like.py
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from core.database import Base
from sqlalchemy.orm import relationship

class Like(Base):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    blog_id = Column(Integer, ForeignKey("blogs.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="likes")
    blog = relationship("Blog", back_populates="likes")
    
    __table_args__ = (
        UniqueConstraint("user_id", "blog_id", name="unique_user_blog_like"),
    )
