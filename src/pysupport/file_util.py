import os

def file_get_contents(f: str)->str:
    """获取文件内容"""
    if os.path.isfile(f)==False:
      return ""

    with open(f, "r") as file:
      data = file.read()
      return data

def file_put_contents(f: str, data: str)->bool:
    """写文件内容"""
    os.makedirs(os.path.dirname(f), exist_ok=True)
    with open(f, "a+") as file:
      i = file.write(data + os.linesep)
      return i>0

