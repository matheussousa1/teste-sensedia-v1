from flask_restx import fields, Api, Resource
from src.server.instance import server

clientes = server.api.model('Clientes', {
    'id': fields.Integer(description="O ID do Registro"),
    'name': fields.String(description="Nome do Cliente"),
})