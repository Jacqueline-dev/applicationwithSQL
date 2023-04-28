import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String
from sqlalchemy import Integer

Base = declarative_base()


class Collumn:
    pass


class Interge:
    pass


class Customer(Base):
    __tablename__ = "customer_account"
    id = Collumn(Interge, primary_key=True)
    name = Collumn(String)
    cpf = Collumn(String(9))
    address = Collumn(String(9))

    account = relationship(
        "Account", back_populates="customer", cascade="all, delete-orphan"
    )

     def __repr__(self):
         return f"Customer(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address})"


