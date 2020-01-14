from odoo import models, fields, api

class cabeceira (models.Model):
    _name = "odoo_basico.cabeceira" #IMPORTANTE é o nome da táboa
    _description = "Cabeceira do pedido "
    _sql_constraints = [('pedido unico', 'unique(name)', 'Non se pode repetir o número de pedido'),
                        ('relación un a un unica', 'unique(factura_id)',
                         'Non se pode repetir o campo da relación un a un')]
    # Ao non poder repetir o campo factura_id garantizamos unha relación 1 a 1 entre as táboas


    name = fields.Char (required=True,size=12,string="Número de pedido") #IMPORTANTE o campo ten que chamarse name
    linea_ids = fields.One2many('odoo_basico.linea','cabeceira_id')# Os campos One2many Non se almacena na BD


    factura_id = fields.Many2one ('odoo_basico.factura', compute='_relacion', inverse = '_inverse',store=True) # para a relación 1 a 1
    factura_ids = fields.One2many ('odoo_basico.factura', 'cabeceira_id')# Os campos One2many Non se almacena na BD
     # A través de One2many obtemos o relación con factura e a través de depends actualizamos factura_id
    lineas = fields.Integer(compute="_conta",default= 0)

    @api.depends ('factura_ids')
    def _relacion(self):
        for rexistro in self:
            if len (rexistro.factura_ids) > 0:
               rexistro.factura_id = rexistro.factura_ids[0]

    def _inverse(self):
        for rexistro in self:
            if len (rexistro.factura_ids) > 0:
            # delete previous reference
                fra = rexistro.env['odoo_basico.factura'].browse (rexistro.factura_ids[0].id)
                fra.cabeceira_id = False
        # set new reference
            rexistro.factura_id.cabeceira_id = rexistro

    def _conta(self):
        for rexistro in self:
             rexistro.lineas = self.env['res.users'].search_count([('id', '>', 0)])


    #self.search_count ([('is_company', '=', True)])

    # @api.one
    # @api.depends ('factura_ids')
    # def _relacion(self):
    #     if len (self.factura_ids) > 0:
    #         self.factura_id = self.factura_ids[0]
    #
    # @api.one
    # def _inverse(self):
    #     if len (self.factura_ids) > 0:
    #         # delete previous reference
    #         fra = self.env['odoo_basico.factura'].browse (self.factura_ids[0].id)
    #         fra.cabeceira_id = False
    #     # set new reference
    #     self.factura_id.cabeceira_id = self

