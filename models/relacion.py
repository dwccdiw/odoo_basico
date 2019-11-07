# -*- coding: utf-8 -*-

from odoo import models, fields


class relacion (models.Model):
    _name = "odoo_basico.relacion" #IMPORTANTE é o nome da táboa
    _description = "Exemplos de relacións"

    name = fields.Char(required=True, size=20,string="Título")  # IMPORTANTE o campo ten que chamarse name para visualizalo

    moeda_id = fields.Many2one ('res.currency')
    orzamento = fields.Monetary ("Orzamento", 'moeda_id')


    informacion_ids = fields.Many2many('odoo_basico.informacion', relation='odoo_basico_relacion_informacion',
                                     column1='relacion_id',column2='informacion_id',
                                     ondelete='set null',string="Informacións" )



