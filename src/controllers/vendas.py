from flask import Flask
from flask_restx import Api, Resource
from src.server.instance import server
from src.server.models.vendas import *
from src.server.db import vendas_db
from src.server.models.clientes import *
from src.server.db import clientes_db
from src.server.models.produtos import *
from src.server.db import produtos_db

app, api = server.app, server.api

@api.route('/clientes')
class ClientesList(Resource):
    @api.marshal_with(clientes)
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self, ):
        '''Listagem de Clientes'''
        return clientes_db
    
@api.route('/produtos')
class ProdutosList(Resource):
    @api.marshal_with(produtos)
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self, ):
        '''Listagem de Produtos'''
        return produtos_db
    
@api.route('/vendas')
class VendaList(Resource):
    @api.marshal_with(vendas)
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self, ):
        '''Listagem de Vendas por Cliente'''
        return vendas_db

    
    