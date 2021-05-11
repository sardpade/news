from flask import Flask
# 导入数据库扩展，并在配置中加载配置
from flask_sqlalchemy import SQLAlchemy



class Config(object):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://root：mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATION = True

# 1.创建app对象
app = Flask(__name__)
# 2.配置信息注册到APP中
app.config.from_object(Config)
# 3.创建数据库对象
db = SQLAlchemy(app)





@app.route("/")
def demo():

    return "程序是树，bug是花，没有花哪来的果"

if __name__ == '__main__':
    app.run(debug=True)