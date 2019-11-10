from odoo import models, fields

class un_a_un (models.Model):
    _name = "odoo_basico.un_a_un" #IMPORTANTE é o nome da táboa
    _description = "Factura un a un"

    name = fields.Char (required=True, string="Relación un a un con factura") #IMPORTANTE o campo ten que chamarse name
   # factura_id = fields.Many2one('odoo_basico.factura', required=True)
    _sql_constraints = [('relacion un a un unica', 'unique(name)', 'Non se pode repetir o campo name')]
