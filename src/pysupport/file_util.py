import os

def file_get_contents(f: str)->str:
    """获取文件内容"""
    if os.path.isfile(f)==False:
      return ""

    with open(f, "r", encoding="utf-8") as file:
      data = file.read()
      return data

def file_put_contents(f: str, data: str)->bool:
    """写文件内容"""
    try:
      os.makedirs(os.path.dirname(f), exist_ok=True)
    except Exception as e:
      pass
    with open(f, "a+", encoding="utf-8") as file:
      i = file.write(data)
      return i>0

def fileBinContents(f: str)->bytes:
  """获取文件内容"""
  if os.path.isfile(f)==False:
    return b""
  with open(f, "rb") as file:
    data = file.read()
    return data

