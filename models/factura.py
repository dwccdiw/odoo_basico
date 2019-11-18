from odoo import models, fields, api

class factura (models.Model):
    _name = "odoo_basico.factura" #IMPORTANTE é o nome da táboa
    _description = " factura"

    name = fields.Char (required=True,size=12,string="Número de factura") #IMPORTANTE o campo ten que chamarse name
    data_factura = fields.Date (string="Data Factura",default=lambda self: fields.Date.today ())
    _sql_constraints = [('factura unica', 'unique(name)', 'Non se pode repetir o número de factura'),
                        ('pedido unico', 'unique(cabeceira_id)', 'Non se pode volve a facturar o pedido')]
    cabeceira_id = fields.Many2one ('odoo_basico.cabeceira')


