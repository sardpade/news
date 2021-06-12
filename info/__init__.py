# info这个文件夹是拿来写业务逻辑的

# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from redis import StrictRedis
#CSRFProtect只做验证工作
from flask_wtf.csrf import CSRFProtect
# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
from flask_session import Session
from config import config_dict


def create_app(config_name):
    """工厂方法，create_app根据传入不同的配置信息，创建不同的app返回"""

    # 1.创建app对象
    app = Flask(__name__)

    # 2.配置信息注册到APP中
    # config_dict相当于接口在config.py里面
    config_class = config_dict[config_name]
    app.config.from_object(config_class)

    # 3.创建数据库对象
    db = SQLAlchemy(app)

    # 4.创建redis数据对象
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT,
                              db=config_class.REDIS_NUM, decode_responses=True)

    # 5.开启flask后端csrf保护机制，仅仅开启后端csrf验证，
    # 抽取cookie里面的csrf_token和ajax请求头里面的csrf_token进行验证
    # TODO: 设置csrf_token值到cookie中需要自己补充
    csrf = CSRFProtect(app)

    # 6.# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
    # 没有返回值，就这样设置就可以了
    Session(app)
    return app











