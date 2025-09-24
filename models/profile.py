# models/profile.py
from core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)          
    profession = Column(String, nullable=True)             

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)  
    user = relationship("User", back_populates="profile")
