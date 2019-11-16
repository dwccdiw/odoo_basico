from odoo import models, fields,api

class linea (models.Model):
    _name = "odoo_basico.linea" #IMPORTANTE é o nome da táboa
    _description = "Línea factura"

    descripcion_da_liña = fields.Char (required=True,string="Descripción da liña")
    factura_id = fields.Many2one('odoo_basico.factura', ondelete='cascade', required=True)
    name_da_factura = fields.Char (compute="_nome",size=12,store=False)

    @api.depends ('factura_id.name')  # cambios nunha táboa relacionada
    def _nome(self):
        for rexistro in self:
            for outrorexistro in rexistro.factura_id:
                rexistro.name_da_factura = outrorexistro.name

    #  @api.depends('partner_id.street')
    #
    # def _get_street(self):
    #
    #       for record in self:
    #
    #                for line in record.partner_id:
    #
    #                    record.street = line.street