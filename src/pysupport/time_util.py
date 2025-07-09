import time

def get_now_timestamp() -> int:
    """
    获取当前的时间戳(10位,精确到秒)： 1752049203
    :return:
    """
    return int(time.time())


def get_current_timestamp() -> int:
    """
    获取当前的时间戳(13位,精确到毫秒)： 1752049203168
    :return:
    """
    return int(time.time() * 1000)


def get_current_time(time_format: str = "%Y-%m-%d %X") -> str:
    """
    获取当前的时间：'2025-07-09 16:20:38'
    Args:
        time_format: 时间格式
    :return:
    """
    return time.strftime(time_format, time.localtime())


def get_current_date() -> str:
    """
    获取当前的日期：'2025-07-09'
    :return:
    """
    return time.strftime('%Y-%m-%d', time.localtime())



if __name__ == '__main__':
    print(get_current_date())
    print(get_current_time())

