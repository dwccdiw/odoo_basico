from odoo import models, fields

class factura (models.Model):
    _name = "odoo_basico.factura" #IMPORTANTE é o nome da táboa
    _description = "Cabecera factura"

    name = fields.Char (required=True,size=12,string="Número de factura") #IMPORTANTE o campo ten que chamarse name
    linea_ids = fields.One2many('odoo_basico.linea','factura_id')# Os campos One2many Non se almacena na BD
    _sql_constraints = [('factura unica', 'unique(name)', 'Non se pode repetir o número de factura'),
                        ('relación un a un unica', 'unique(un_a_un_id)', 'Non se pode repetir o campo da relación un a un')]
# Ao non poder repetir o campo un_a_un_id garantizamos unha relación 1 a 1 entre as táboas
    un_a_un_id = fields.Many2one('odoo_basico.un_a_un', required=True)

