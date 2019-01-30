import tornado.httpserver
import tornado.ioloop
import tornado.web
from applications import NewApp
import config
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(NewApp())
    #http_server.bind(config.options['port'])
    http_server.listen(options.port)
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()
