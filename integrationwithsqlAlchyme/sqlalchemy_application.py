from sqlite3 import Binary

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


class Unique:
    pass


class Foreignkey:
    pass


class Account(Base):
    __tablename__ = "account"
    id = Collumn(Binary, primary_key=True)
    account_type = Collumn(String)
    agency = Collumn(String)
    number = Collumn(Interge)
    id_customer = Collumn(Interge, Foreignkey("user_customer.id"), unique=True)

    user = relationship(
        "customer", back_populates="account"
    )

    def __repr__(self):
        return f"Account(id={self.id}, account_type={self.account_type}, agency={self.agency}, number={self.number}, id_customer={self.id_customer})"


print(Customer.__tablename__)
print((Account.__tablename__)