from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    select,
    insert,
)

from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()

users_core = Table(
    "users_core",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
)


class UserORM(Base):
    __tablename__ = "users_orm"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


def create_tables():
    metadata.create_all(engine)
    Base.metadata.create_all(engine)


def core_example():
    with engine.connect() as conn:
        # Insert
        stmt = insert(users_core).values(name="Alice")
        conn.execute(stmt)
        conn.commit()

        # Select
        stmt = select(users_core)
        result = conn.execute(stmt)
        for row in result:
            print("CORE:", row)


def orm_example():
    session = SessionLocal()

    # Insert
    user = UserORM(name="Bob")
    session.add(user)
    session.commit()

    # Query
    users = session.query(UserORM).all()
    for user in users:
        print("ORM:", user.id, user.name)

    session.close()


if __name__ == "__main__":
    create_tables()
    core_example()
    orm_example()
