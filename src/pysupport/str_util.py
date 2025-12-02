import random,re

def get_random_str(random_len: int = 6) -> str:
    """
    获取随机字符串
    :param random_len:
    :return:
    """
    random_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    _random = random.Random()
    for _ in range(random_len):
        random_str += chars[_random.randint(0, length)]
    return random_str

def get_random_strV2(random_len: int = 6) -> str:
    """
    获取随机字符串,去掉了不容易识别的字符
    :param random_len:
    :return:
    """
    random_str = ''
    chars = 'AaBbCcDdEeFfGgHhKkMmNnPpQqRrSsTtUuVvWwXxYyZz23456789'
    length = len(chars) - 1
    _random = random.Random()
    for _ in range(random_len):
        random_str += chars[_random.randint(0, length)]
    return random_str

def get_random_strV3(l: int=6, base_str:str="") -> str:
    """
    生成的随机字符串
    """

    base_str = base_str or "AaBbCcDdEeFfGgHhKkMmNnPpQqRrSsTtUuVvWwXxYyZz23456789"
    return "".join(random.choice(base_str) for _ in range(l))

def getPlaceholders4List(listData: list) -> str:
    """
    获取占位符,返回如 ?,?,?
    :return:
    """
    placeholders = ','.join(['?' for _ in listData])
    return placeholders

def split_dict_cookie(cookie_dict: dict) -> str:
    return "; ".join(f"{key}={value}" for key, value in cookie_dict.items())

# 判断字符串是否为空
def isEmpty(s: str) -> bool:
    return len(s) == 0

# 去掉所有空格（含 \r、\n、空格）
def trimAll(src: str) -> str:
    if isEmpty(src):
        return ""
    return re.sub(r"[\r\n ]+", "", src)

