from flask import Flask
from flask_restx import Api
from werkzeug.utils import cached_property

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Desafio Tecnico',
            description='Desafio Tecnico - situacional',
            default = 'API',
            default_label = 'Vendas por Cliente',
            contact_email = 'matheusferreiras@live.com',   
            doc='/docs',           
        )
    
    def run(self, ):
        self.app.run(
            debug=True
        )

server = Server()