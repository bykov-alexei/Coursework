from config import config
import pymysql

def connect():
    connection = pymysql.connections.Connection(**config['database'])
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    return connection, cursor
