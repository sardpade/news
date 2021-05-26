# session 存储flask数据用的
from flask import Flask,session
# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
#CSRFProtect只做验证工作
from flask_wtf.csrf import CSRFProtect
# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
from flask_session import Session



# 1.创建app对象
app = Flask(__name__)

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
    SESSION_TYPE = "redis"
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



# 2.配置信息注册到APP中
app.config.from_object(Config)
# 3.创建数据库对象
db = SQLAlchemy(app)
# 4.创建redis数据对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_NUM, decode_responses=True)
# 5.开启flask后端csrf保护机制，仅仅开启后端csrf验证，
# 抽取cookie里面的csrf_token和ajax请求头里面的csrf_token进行验证
# TODO: 设置csrf_token值到cookie中需要自己补充
csrf = CSRFProtect(app)
# 6.# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
# 没有返回值，就这样设置就可以了
Session(app)






@app.route("/")
def demo():
    # 在调整设置之前session数据存储到flask后端服务器的，i借助cookie将session_id给前度你
    session["name"] = "test"
    # print(session.get("name"))
    return "程序是树，bug是花，没有花哪来的果"

if __name__ == '__main__':

    app.run(port=5001)
