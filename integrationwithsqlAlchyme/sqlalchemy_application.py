from _pydecimal import Decimal
from sqlite3 import Binary
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session, session
from sqlalchemy import (Column, String, Integer, ForeignKey, LargeBinary, create_engine, inspect)

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer_account"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    cpf = Column(String(9))
    email_address = Column(String(9))

    account = relationship(
        "Account", back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, cpf={self.cpf}, email_address={self.address})"


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
        return f"Account(id={self.id}, account_type={self.account_type}, agency={self.agency}, number={self.number}, id_customer={self.id_customer}, balance={self.balance})"


print(Customer.__tablename__)
print(Account.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("customer_account"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.defaut_schema_name)

with Session(engine) as sessions:
    jacque = Customer (
        name = 'Jacqueline',
        cpf = 123456789,
        email_address = [Customer(email_address='jacque@gmail.com')],
        account_type = 'conta corrente',
        number = '001',
        id_customer = 1,
        balance = 1550.1

    )



    ana = Customer (
         name = 'Ana',
         cpf = 987653421,
         email_address = [Customer(email_address='ana@outlook.com')],
         account_type = 'conta corrente',
         number = '002',
         id_customer = 2,
         balance = 1550.1

     )



    session.add_all([jacque, ana])

    session.commit()