# session 存储flask数据用的
from flask import Flask,session,current_app

# 导入管理类，接管app
# from flask_migrate import Manager
from flask_script import Manager
print('before import create_app')
from info import create_app
print('after import create_app')
import logging
# 从单一职责来看，manger.py只做一个程序入口
# 调用工厂方法，传入不同配置，获取不同app对象
#调用调用config.py里面的"development"就等于调用--->>>DevelopmenConfig这个类，开发者环境模式
app = create_app("development")
# 7.创建manage管理类
managr = Manager(app)


@app.route("/")
def demo():
    # 在调整设置之前session数据存储到flask后端服务器的，i借助cookie将session_id给前度你
    session["name"] = "test"

    logging.debug("debug 日志信息")
    logging.info("info 日志信息")
    logging.warning("warning 日志信息")
    logging.error("error 日志信息")
    logging.critical("critical 日志信息")

    # flask 里面封装了current_app这个日志的方法，以后就这样导入模块调用就行了
    current_app.logger.debug("flask封装的logger日志")

    return "程序是树，bug是花，没有花哪来的果"
if __name__ == '__main__':
    # 已经在右上角绿色三角形左边设置了runserver。
    # 用命令运行的话 python manager.py runserver -h -p -d
    print(app.url_map)
    managr.run()