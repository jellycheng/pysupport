import sqlite3
from sqlite3 import Error
from typing import List, Tuple, Optional, Any, Dict

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

def close_conn(conn: sqlite3.Connection) -> None:
    """关闭数据库连接"""
    if conn:
        try:
            conn.close()
        except sqlite3.Error as e:
            raise Exception(f"关闭连接失败: {str(e)}")

def create_table(conn, create_table_sql):
    """根据SQL语句创建表"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        return True
    except Error as e:
        print(f"创建表时出错: {e}")
        return False

def insert(conn: sqlite3.Connection, sql: str, params: Optional[Tuple[Any, ...]] = None) -> int:
    """
    插入一条记录
    :param conn: 数据库连接
    :param sql: 插入SQL（如 "INSERT INTO t (col) VALUES (?)"）
    :param params: SQL参数（元组，如 (value,)）
    :return: 插入记录的自增ID
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        conn.commit()
        return cursor.lastrowid  # 返回自增主键
    except sqlite3.Error as e:
        conn.rollback()
        raise Exception(f"插入失败: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def batch_insert(conn: sqlite3.Connection, sql: str, params_list: List[Tuple[Any, ...]]) -> int:
    """
    批量插入数据
    :param params_list: 参数列表（如 [(v1,), (v2,)]）
    :return: 插入的总条数
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, params_list)  # 批量执行
        conn.commit()
        return len(params_list)
    except sqlite3.Error as e:
        conn.rollback()
        raise Exception(f"批量插入失败: {str(e)}")
    finally:
        if cursor:
            cursor.close()

def update(conn: sqlite3.Connection, sql: str, params: Optional[Tuple[Any, ...]] = None) -> int:
    """
    执行更新操作
    :return: 影响的行数
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        conn.commit()
        return cursor.rowcount  # 影响行数
    except sqlite3.Error as e:
        conn.rollback()
        raise Exception(f"更新失败: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def delete(conn: sqlite3.Connection, sql: str, params: Optional[Tuple[Any, ...]] = None) -> int:
    """
    执行删除操作
    :return: 影响的行数
    """
    return update(conn, sql, params)


def query_all(conn: sqlite3.Connection, sql: str, params: Optional[Tuple[Any, ...]] = None) -> List[Dict[str, Any]]:
    """
    执行查询操作，多条记录
    :return: 结果列表（每个元素为字典，键为列名）
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        # 转换为字典列表（支持按列名访问）
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        raise Exception(f"查询失败: {str(e)}")
    finally:
        if cursor:
            cursor.close()

def query_one(conn: sqlite3.Connection, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Dict[str, Any]]:
    """
    查询并返回单条记录
    :param conn: 数据库连接对象
    :param sql: 查询SQL语句（如 "SELECT * FROM 表 WHERE id = ?"）
    :param params: SQL参数（元组格式，如 (1,)，可选）
    :return: 单条记录字典（键为列名），无结果则返回 None
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        row = cursor.fetchone()
        # 转换为字典（若有结果）
        return dict(row) if row else None
    except sqlite3.Error as e:
        raise Exception(f"单条查询失败: {str(e)}")
    finally:
        if cursor:
            cursor.close()
