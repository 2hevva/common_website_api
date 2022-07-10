import pymysql

biliApiInfoRecord_database_config = {
    'host': 'YOUR SERVER',
    'port': 3306,
    'user': 'root',
    'password': 'YOUR PASSWORD',
    'database': 'YOUR DATABASE',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor
}


def bili_api_info_record(sql):
    try:
        connection = pymysql.connect(**biliApiInfoRecord_database_config)
        with connection.cursor() as cursor:
            count = cursor.execute(sql)
            connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()
