from flask import Flask
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+"\\model")
template_dir = os.path.dirname(os.path.abspath(__file__))+"\\template"
static_dir = os.path.dirname(os.path.abspath(__file__))+"\\template"

from website.views import views
from website.auth import auth

server = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

server.register_blueprint(views, url_prefix='/')
server.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    server.run(debug=False)