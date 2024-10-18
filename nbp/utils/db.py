from sqlalchemy import create_engine, text


def get_connection_string(config):
    return f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"


def get_engine(conn_str):
    return create_engine(conn_str)


def connect_db(config):
    conn_str = get_connection_string(config)
    eng = get_engine(conn_str)
    return eng


def get_db_data(engine, sql_query):
    res_list = []
    try:
        conn = engine.connect()
        res = conn.execute(text(sql_query))
        res_list = list(res)
        conn.close()
    except Exception as e:
        print(f"Błąd: {e}")
