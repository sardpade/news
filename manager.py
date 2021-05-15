from flask import Flask
# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
#CSRFProtect只做验证工作
from flask_wtf.csrf import CSRFProtect

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








# 1.创建app对象
app = Flask(__name__)
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

@app.route("/")
def demo():

    return "程序是树，bug是花，没有花哪来的果"

if __name__ == '__main__':
    app.run(debug=True)