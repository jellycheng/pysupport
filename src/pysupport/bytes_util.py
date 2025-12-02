import binascii,codecs
import base64
from . import str_util

# hex 转 bytes
def hex_to_bytes(src: str) -> bytes:
    src = str_util.trimAll(src)
    if str_util.isEmpty(src):
        return b""
    try:
        return binascii.unhexlify(src)
    except binascii.Error:
        # 输入不是合法 hex，返回空 bytes
        return b""

def bytes_to_hex(data: bytes) -> str:
    if len(data) == 0:
        return ""
    return binascii.hexlify(data).decode('utf-8')

def bytes2hex(data: bytes) -> str:
    if len(data) == 0:
        return ""
    return codecs.encode(data, 'hex').decode('utf-8')

def bytes2base64(data: bytes)->str:
    base64Str = base64.b64encode(data).decode('utf-8')
    return base64Str

# 从文件读取 bytes 数据并转换为 base64
def file2base64(file_path):
    with open(file_path, 'rb') as file:
        fileBytes = file.read()
        return base64.b64encode(fileBytes).decode('utf-8')

# hex 字符串 转 字符串, print(bytes_util.hex2string("e4bda0e5a5bd")) 打印 你好
def hex2string(hex_str: str) -> str:
    try:
        return binascii.unhexlify(hex_str).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError):
        return ""

# 字符串 转 hex 字符串（不带 0x，全部小写）
def string2hex(s: str) -> str:
    return binascii.hexlify(s.encode("utf-8")).decode("ascii")

def string2hex_v2(s: str) -> str:
    s = str_util.trimAll(s)
    return string2hex(s)

# 判断是否为合法 hex 字符串
def isHexString(s: str) -> bool:
    return all(c in "0123456789abcdefABCDEF" for c in s)

