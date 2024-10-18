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

# from sqlalchemy import create_engine

# conn_str = "postgresql+psycopg2://login:haslo@serwer:port/baza"
# conn_str = "postgresql+psycopg2://postgres:Password!@localhost:5432/postgres"

# engine = create_engine(conn_str)


#### ZADANIE 38

# Napisz funkcję load_config() która jako parametr
# przyjmie nazwę pliku YAML z konfiguracją i wczyta tą konfigurację.
# Na wyjściu funkcja ma zwrócić słownik z konfiguracją.


import yaml
from sqlalchemy import create_engine, text


def load_config(nazwa_pliku):
    slownik_konfig = {}
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as file:
            slownik_konfig = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")

    # sprawdzić czy potrzebne klucze w słowniku istnieją
        
    return slownik_konfig

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"

config = load_config(CONFIG_FILE)

conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
# print(conn_str)
engine = create_engine(conn_str)
# print(engine)

conn = engine.connect()
# print(conn)

sql_query = "SELECT * FROM players;"
res = conn.execute(text(sql_query))

for r in res:
    print(r)

conn.close()
