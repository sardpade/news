# info这个文件夹是拿来写业务逻辑的

# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from redis import StrictRedis
#CSRFProtect只做验证工作
from flask_wtf.csrf import CSRFProtect
# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
from flask_session import Session
import logging
from logging.handlers import RotatingFileHandler
from config import config_dict

print('import all success')

def create_log(config_name):
    """创建日志的配置信息"""

    # # 设置日志的记录等级
    # config_dict[config_name].LOG_LEVEL 获取配置类中对象日志级别
    level = config_dict[config_name].LOG_LEVEL
    logging.basicConfig(level=config_dict[config_name].LOG_LEVEL)# 调试debug级

    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    # file_log_handler = RotatingFileHandler("/home/python/Desktop/news/logs/log", maxBytes=1024 * 1024 * 100, backupCount= 10 )
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)

    # 创建日志记录的格式Formatter 日志等级 输入日志信息的文件名，行数（第几行产生），日志信息
    #INFO产生日志文件夹，文件名py： 第几行产生，产生的信息
    formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
    # formatter = logging.Formatter("%(levelnama)s %(filename)s:%(lineno)d %(message)s")

    # 为刚创建的日志记录器设置日志记录格式
    # file_log_handler.setFormatter(formatter)
    file_log_handler.setFormatter(formatter)

    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)



def create_app(config_name):
    """工厂方法，create_app根据传入不同的配置信息，创建不同的app返回"""

    print('before run create_log')
    # 补充日志功能
    create_log(config_name)
    print('after run create_log')

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











