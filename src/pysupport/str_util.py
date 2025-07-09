from random import Random

def get_random_str(random_len: int = 6) -> str:
    """
    获取随机字符串
    :param random_len:
    :return:
    """
    random_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    _random = Random()
    for i in range(random_len):
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
    _random = Random()
    for i in range(random_len):
        random_str += chars[_random.randint(0, length)]
    return random_str
