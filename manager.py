# session 存储flask数据用的
from flask import Flask,session

# 导入管理类，接管app
from flask_migrate import Manager
from info import create_app

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
    # print(session.get("name"))
    return "程序是树，bug是花，没有花哪来的果"

if __name__ == '__main__':
    # 已经在右上角绿色三角形左边设置了runserver。
    # 用命令运行的话 python manager.py runserver -h -p -d
    managr.run()