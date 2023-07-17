from flask_restx import fields, Api, Resource
from src.server.instance import server

clientes = server.api.model('Clientes', {
    'sigla': fields.String(description="Sigla do Cliente"),
    'quantidadeVendas': fields.String(description="Quantidade de Vendas do Cliente"),
    })

vendas = server.api.model('Vendas', {
    'id': fields.Integer(description="O ID do Registro"),
    'idProduto': fields.Integer(description="O ID do Produro"),
    'produto': fields.String(description="Nome do Produto"),
    'clientes': fields.Nested(clientes)
})