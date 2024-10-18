# Login: postgres
# Password: Password!

# SQLAlchemy -> pakiet do obsługi baz danych


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
