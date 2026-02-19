"""
Docstring for Day-12.__Doc__

• SQLAlchemy ORM
• Relationships
• Alembic	migrations
• Connection pooling
"""

"""
sqlalchemy orm:
    - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
    sqlmy core = work with connect, is not an ORM. It is a SQL Abstraction Toolkit.
    sqlmy orm = works with session
    - object relational mapper

"""

"""
relationships:
    - it is method from the sqal.orm module to bind 
    - used with foreingn key 
    - posts = relationship("Post", back_populates="user")
    - user = relationship("User", back_populates="posts")
    - one to one
    - one to many
    - many to many

"""

"""
alembic migrations:
    migration:
            - database migration is way to incrementally modify your database schema. For example, adding new tables, altering existing tables, etc...
            - schema evaluation 
    - alembic is a database migration tool for SQLAlchemy
    - The alembic_version Table
    

"""
