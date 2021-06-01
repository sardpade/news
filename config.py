# 创建项目管理类
class Config(object):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://root：mysql@127.0.0.1:3306/new"
    # 开启数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # 使用第七个数据库
    REDIS_NUM = 7
    # seeion 配置
    SECRET_KEY = "SLKDJASLKDJKLASLJKDALS"

    # 以下是 from flask_session import Session 的配置信息
    # 调整sesion存储到redis配置信息
    # 设置存储session的数据库类型
    SESSIOM_TYPE = "redis"
    # 创建数据库实力对象配置。到时候真正存储数据是到这条数据库，因为使用大写Session改变位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NUM)
    # SIGER 签名的意思，在python意思就是需要加密
    SESSION_USE_SIGNER = True
    # SESSION设置有过期时长
    SESSION_PERMANENT = False
    # 设置过期时长 默认值：timedelta（days=31）
    PERMANENT_SESSION_LIFETIME = 86400 * 2

    """SESSIOM_TYPE, SESSION_RREDIS
     SESSION_USE_SIGNER, SESSION_PERMANENT
     PERMANENT_SESSION_LIFETIME  这五个值在Session(app)里面，按住ctrl点击进入Session里面看
     ，文档地址：http://pythonhosted.org/Flask-Session/这个地址有解释"""

