import binascii,codecs
import base64

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
