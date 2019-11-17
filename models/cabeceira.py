from odoo import models, fields

class cabeceira (models.Model):
    _name = "odoo_basico.cabeceira" #IMPORTANTE é o nome da táboa
    _description = "Cabeceira do pedido "

    name = fields.Char (required=True,size=12,string="Número de pedido") #IMPORTANTE o campo ten que chamarse name
    linea_ids = fields.One2many('odoo_basico.linea','cabeceira_id')# Os campos One2many Non se almacena na BD
    _sql_constraints = [('pedido unico', 'unique(name)', 'Non se pode repetir o número de pedido'),
                        ('relación un a un unica', 'unique(factura_id)', 'Non se pode repetir o campo da relación un a un')]
# Ao non poder repetir o campo factura_id garantizamos unha relación 1 a 1 entre as táboas
    factura_id = fields.Many2one('odoo_basico.factura')

