# from flask import Flask
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     print("GET /")
#     return "Welcome, this is my Flask app deployed on Zeabur"

# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')

# -*- coding: utf-8 -*-

from os import getenv
from mypandora_cloud.server import ChatBot

_port = getenv('PORT')
_proxy = getenv('PANDORA_PROXY')
_debug = getenv('PANDORA_DEBUG', 'false').lower() == 'true'
_sentry = getenv('PANDORA_SENTRY', 'false').lower() == 'true'
_listen = getenv('PANDORA_SERVER_LISTEN', 'true').lower() == 'true'
_server = getenv('PANDORA_SERVER', '0.0.0.0:{}'.format(_port) if _port else '0.0.0.0')
# _server = '127.0.0.1'
app = ChatBot(proxy=_proxy, debug=_debug, sentry=_sentry, login_local=True).run(_server, listen=_listen)
