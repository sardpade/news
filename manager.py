# session 存储flask数据用的
from flask import Flask,session
# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
#CSRFProtect只做验证工作
from flask_wtf.csrf import CSRFProtect
# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
from flask_session import Session
# 导入管理类，接管app
from flask_migrate import Manager
from config import config_dict


# 1.创建app对象
app = Flask(__name__)

# 2.配置信息注册到APP中
# config_dict相当于接口，调用"development"就等于调用--->>>DevelopmenConfig这个类
config_class = config_dict["development"]
app.config.from_object(config_class)

# 3.创建数据库对象
db = SQLAlchemy(app)

# 4.创建redis数据对象
redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_NUM, decode_responses=True)

# 5.开启flask后端csrf保护机制，仅仅开启后端csrf验证，
# 抽取cookie里面的csrf_token和ajax请求头里面的csrf_token进行验证
# TODO: 设置csrf_token值到cookie中需要自己补充
csrf = CSRFProtect(app)

# 6.# 大写开头的Session ,是借助第三方session类去调整flask中session的存储位置
# 没有返回值，就这样设置就可以了
Session(app)

# 7.创建manage管理类
managr = Manager(app)


@app.route("/")
def demo():
    # 在调整设置之前session数据存储到flask后端服务器的，i借助cookie将session_id给前度你
    session["name"] = "test"
    # print(session.get("name"))
    return "程序是树，bug是花，没有花哪来的果"

if __name__ == '__main__':
    # 已经在右上角绿色三角形左边设置了runserver。
    # 用命令运行的话 python manager.py runserver -h -p -d
    managr.run()