from _pydecimal import Decimal
from sqlite3 import Binary
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (Column, String, Integer, ForeignKey, LargeBinary)



Base = declarative_base()



class Customer(Base):
    __tablename__ = "customer_account"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    cpf = Column(String(9))
    address = Column(String(9))

    account = relationship(
        "Account", back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self):
         return f"Customer(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address})"



class Account(Base):
    __tablename__ = "account"
    id = Column(LargeBinary, primary_key=True)
    account_type = Column(String)
    agency = Column(String)
    number = Column(Integer)
    id_customer = Column(Integer, ForeignKey("user_customer.id"), unique=True)
    balance = Column(Decimal)

    user = relationship(
        "customer", back_populates="account"
    )

    def __repr__(self):
        return f"Account(id={self.id}, account_type={self.account_type}, agency={self.agency}, number={self.number}, id_customer={self.id_customer})"


print(Customer.__tablename__)
print(Account.__tablename__)
