
from odoo import models, fields, api


class contexto (models.Model):
    _name = "odoo_basico.contexto"

    ver_contexto = fields.Char(string='Ver o Contexto', compute='_get_context')

    @api.depends ('ver_contexto')
    def _get_context(self):
        for rexistro in self:
            rexistro.ver_contexto = dict(rexistro.env.context)