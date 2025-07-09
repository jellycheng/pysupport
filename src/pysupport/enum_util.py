from enum import Enum,IntEnum

class AccountStatusEnum(Enum):
    """
    账号状态 0-正常,1-无效
    """
    NORMAL = 0
    INVALID = 1

class IsDeleteEnum(IntEnum):
    """
    是否删除 0-正常,1-删除
    """
    IS_DELETE0 = 0
    IS_DELETE1 = 1

class StatusEnum(IntEnum):
    """
    启停状态 1-启用,2-停用
    """
    StatusEnable = 1
    StatusDisable = 2

class AccountPlatfromEnum(Enum):
    """
    平台账号代号
    """
    XHS = "xhs"  # 小红书
    WEIBO = "wb"  # 微博
    KUAISHOU = "ks"  # 快手
    DOUYIN = "douyin"  # 抖音
    BILIBILI = "bilibili"  # 哔哩哔哩
    TIEBA = "tieba"  # 百度贴吧
    ZHIHU = "zhihu"  # 知乎
    TAOBAO = "taobao"  # 淘宝
    JD = "jd"  # 京东
    PINDUODUO = "pinduoduo"  # 拼多多
    TOUTIAO = "toutiao"  # 头条
    WECHAT = "wechat"  # 微信
    QQ = "qq"  # QQ
    ALIPAY = "alipay"  # 支付宝
    WECHATPAY = "wechatpay"  # 微信支付
    DOUYINPAY = "douyinpay"  # 抖音支付
