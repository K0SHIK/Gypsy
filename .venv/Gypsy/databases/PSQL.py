import psycopg2
import logging

from config_data.config import Config


logger = logging.getLogger(__name__)


# Креды для подключения к базе
def connect_to_database(config: Config):
    return psycopg2.connect(
        dbname=config.db.database,
        host=config.db.db_host,
        user=config.db.db_user,
        password=config.db.db_password
    )
# Проверка пользователя по ID
def check_user(tg_id, config: Config):
    logger.info('Проверка пользователя с id_tg %s', tg_id)
    try:
        conn = connect_to_database(config=config)
        cursor = conn.cursor()
        sql = """
            SELECT 
                name
            FROM taro
            WHERE tg_id = %s
        """
        cursor.execute(sql, (tg_id,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return None
    except psycopg2.Error as e:
        logger.error('Ошибка подключения к базе данных: %s', e)
        return None
    except Exception as e:
        logger.error('Неожиданная ошибка: %s', e)
        return None



# При первом заходи добовляем ного пользователя в базу
# def add_new_user():
#     try:
#         conn = connect_to_database()
#         cursor = conn.cursor()

