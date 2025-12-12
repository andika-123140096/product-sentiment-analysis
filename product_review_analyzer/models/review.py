from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    review_text = Column(Text, nullable=False)
    sentiment = Column(Text)
    key_points = Column(Text)
    created_at = Column(DateTime, default=None)
