import sqlite3
from sqlite3 import Error

# 连接SQLite数据库
def create_connection(db_file):
    """创建与SQLite数据库的连接"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row # 使查询结果通过数组的方式访问，row["name"]
        return conn
    except Error as e:
        print(f"连接数据库时出错: {e}")

    return conn

def create_table(conn, create_table_sql):
    """根据SQL语句创建表"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        return True
    except Error as e:
        print(f"创建表时出错: {e}")
        return False

