import hashlib

def md5(s: str) -> str:
    """
    生成md5并以大写 16 进制字符串（不带 0x 前缀）返回。
    """
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.digest().hex().upper()
