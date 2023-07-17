from flask_restx import fields, Api, Resource
from src.server.instance import server

produtos = server.api.model('Produtos', {
    'id': fields.Integer(description="O ID do Registro"),
    'name': fields.String(description="Nome do Produto"),
})