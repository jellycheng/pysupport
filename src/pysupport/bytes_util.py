import binascii,codecs

def bytes_to_hex(data: bytes) -> str:
    if len(data) == 0:
        return ""
    return binascii.hexlify(data).decode('utf-8')

def bytes2hex(data: bytes) -> str:
    if len(data) == 0:
        return ""
    return codecs.encode(data, 'hex').decode('utf-8')
