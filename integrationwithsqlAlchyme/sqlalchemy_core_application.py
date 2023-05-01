from pydoc import text

from sqlalchemy import (create_engine, MetaData, Integer, Table, Column, String)

engine = create_engine('sql:///:memory')

metadata_obj = MetaData()
customer = Table(
    'customer',
    metadata_obj,
    Column('customer_id', Integer, primary_key=True),
    Column('customer_name', String(9), nullable=False),
    Column('customer_cpf', String(9), nullable=False),
    Column('email_address', String(9))


)

class Foreignkey:
    pass

customer_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('customer_id', Integer, Foreignkey('customer.customer_id', nullable=False)),
    Column('pref_name', String(9), nullable=False),
    Column('pref_value', String(100)),
)

print("\nInfo of table customer")
print(customer_prefs.primary_key)
print(customer_prefs.constraints)

print(metadata_obj.tables)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)

metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

sql_insert = text("insert into user values(3, 'maria', 'email@gmail.com', 'mai')")
engine.execute(sql_insert)

print("\nInfo of table financial_info")
print(financial_info.primary_key)
print(financial_info.constraints)

print('\nExecute statement sql')
sql = text('select * from user')
result = engine.execute(sql)
for row in result:
    print(row)
