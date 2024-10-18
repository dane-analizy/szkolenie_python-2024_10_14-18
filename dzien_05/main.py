# Login: postgres
# Password: Password!

# SQLAlchemy -> pakiet do obsługi baz danych

# https://dbeaver.io/
# utworzenie tabelki:
"""
create table players (
        player_id serial primary key,
        first_name text not null,
        last_name text not null,
        height numeric not null,
        weight numeric not null
);
"""

# dodanie przykładowych rekordów do tabeli:
"""
insert into players (first_name,last_name,height,weight)  
values ('Jan', 'Kowalski', 1.84, 85);  
  
insert into players (first_name,last_name,height,weight)  
values ('Marian', 'Nowak', 1.90, 50);  
  
insert into players (first_name,last_name,height,weight)  
values ('Zdzisław', 'Dyrman', 1.73 ,74);  
  
insert into players (first_name,last_name,height,weight)  
values ('Zenon', 'Brzęczyk', 1.64, 95);  
  
insert into players (first_name,last_name,height,weight)  
values ('Chuck','Norris', 1.82, 78);  
  
insert into players (first_name,last_name,height,weight)  
values ('Krzysztof','Jarzyna', 1.68, 70);
"""


# SQLAlchemy -> pakiet do obsługi baz danych

# pip install sqlalchemy
# python -m pip install sqlalchemy
# py -m pip install sqlalchemy

# - pakiet do łączenia się z PostgreSQL
# 	- pip install psycopg2
# - pakiet do łączenia się z Oracle
# 	-`pip install cx_oracle
# - pakiet do łączenia się z MS SQL
# 	- pip install pymssql

from sqlalchemy import create_engine

conn_str = "postgresql+psycopg2://login:haslo@serwer:port/baza""
engine = create_engine(conn_str)
