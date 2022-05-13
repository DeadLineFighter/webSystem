from flask import Flask
from requests import options
from model.plotlyFunction import *
from website.views import views
from website.auth import auth

template_dir = os.path.dirname(os.path.abspath(__file__))+"//template"

server = Flask(__name__, template_folder=template_dir)

server.register_blueprint(views, url_prefix='/')
server.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    server.run(debug=False)