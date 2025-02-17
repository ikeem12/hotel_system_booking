from .extensions import MySQL


def get_db_conection():
    return MySQL().get_connection()