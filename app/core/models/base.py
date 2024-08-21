from sqlalchemy import CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class UserPhrase(Base):
    __tablename__ = "user_phrase"

    phrase: Mapped[str]
    positive_score: Mapped[float] = mapped_column(
        CheckConstraint("positive_score BETWEEN 0 AND 1")
    )
    neutral_score: Mapped[float] = mapped_column(
        CheckConstraint("neutral_score BETWEEN 0 AND 1")
    )
    negative_score: Mapped[float] = mapped_column(
        CheckConstraint("negative_score BETWEEN 0 AND 1")
    )
