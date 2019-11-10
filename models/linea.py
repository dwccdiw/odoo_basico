from odoo import models, fields

class linea (models.Model):
    _name = "odoo_basico.linea" #IMPORTANTE é o nome da táboa
    _description = "Línea factura"

    descripcion_da_liña = fields.Char (required=True,string="Descripción da liña")
    factura_id = fields.Many2one('odoo_basico.factura', ondelete='cascade', required=True)