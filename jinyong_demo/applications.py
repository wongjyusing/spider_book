from tornado.web import Application
from config import settings,options
from urls import urlpatterns
import ui_modules
# import psycopg2
import sqlite3 as db
class NewApp(Application):
    def __init__(self):
        handlers = urlpatterns
        # 这里可填写连接数据库代码，并生成游标


        self.conn = db.connect('demo.db')
        
        self.db = self.conn.cursor()
        print('服务器程序启动成功')

        print('按下 Ctrl + C 退出服务器程序')
        Application.__init__(self, handlers,**settings)
