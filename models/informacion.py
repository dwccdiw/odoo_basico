# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class odoo_basico(models.Model):
#     _name = 'odoo_basico.odoo_basico'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class informacion (models.Model):
    _name = "odoo_basico.informacion" #IMPORTANTE é o nome da táboa
    _description = "Exemplos de atributos"

    name = fields.Char(required=True,size=20,string="Título")#IMPORTANTE o campo ten que chamarse name para visualizalo
    descripcion = fields.Text(string="A Descripción")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    alto_en_cms = fields.Integer(string="Alto en centímetros")
    longo_en_cms = fields.Integer (string="Longo en centímetros")
    ancho_en_cms = fields.Integer (string="Ancho en centímetros")
    volume = fields.Float (compute="_volume", store=True)
    peso = fields.Float(digits=(6, 2), string="Peso en Kg.s", default=2.7)
    data_sesion = fields.Datetime(string="Data da Sesión", default=lambda self: fields.Datetime.now()) #w3schools lambda function
    foto = fields.Binary(string='Foto')

   # sexo = fields.Selection(['Home', 'Muller', 'Outros'], string='Sexo')
    sexo_traducido = fields.Selection([('male', 'Home'), ('female', 'Muller'), ('others', 'Outros')], string='Sexo')


    # nacionalidade = fields.Many2one ('res.country', string='Nacionalidade')
    # moeda_id = fields.Many2one ('res.currency')
    # custo_por_hora = fields.Monetary ("Custo por hora", 'moeda_id')
    @api.depends ('alto_en_cms','longo_en_cms','ancho_en_cms')
    def _volume(self):
        self.volume = float(self.alto_en_cms) * float(self.longo_en_cms) * float(self.ancho_en_cms)