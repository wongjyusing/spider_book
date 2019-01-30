import os
import ui_modules
BASE_DIR = os.path.dirname(__file__)

options = {
    'port':8888,
}


settings = {
    'template_path':os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'xsrf_cookies':True,
    'debug':True,
    #'ui_modules':ui_modules,
    "xsrf_cookies": True,
    # "cookie_secret":'xxxxx'

    }
