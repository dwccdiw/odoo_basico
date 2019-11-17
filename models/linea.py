from odoo import models, fields, api

class linea (models.Model):
    _name = "odoo_basico.linea" #IMPORTANTE é o nome da táboa
    _description = "Línea factura"

    descripcion_da_liña = fields.Char (required=True,string="Descripción da liña")
    cabeceira_id = fields.Many2one('odoo_basico.cabeceira', ondelete='cascade', required=True)
    name_da_cabeceira = fields.Char (compute="_nome",size=12,store=False)

    @api.depends ('cabeceira_id.name')  # cambios nunha táboa relacionada
    def _nome(self):
        for rexistro in self:
            for outrorexistro in rexistro.cabeceira_id:
                rexistro.name_da_cabeceira = outrorexistro.name
