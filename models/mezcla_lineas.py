from odoo import models, fields

class mezcla_lineas (models.Model):
    _name = "odoo_basico.mezcla_lineas" #IMPORTANTE é o nome da táboa
    _description = "Mezcla lineas de facturas"

    name = fields.Char (required=True, string="Mezcla") #IMPORTANTE o campo ten que chamarse name
    linea_ids = fields.Many2many('odoo_basico.linea', relation='odoo_basico_many2many_mezcla_lineas',
                                     column1='mezcla',column2='linea_id',
                                     ondelete='set null',string="Mezclador de lineas" )# Para definir nos os nomes da táboa relación e dos campos
# neste suposto dende mezcla_lineas so podemos seleccionar lineas creadas dende unha factura,
# Non podemos dalas de alta porque non as estamos relacionando con unha cabeceira
#   (o campo cabeceira_id de linea.py,non está incluido na vista linea.xml)
# Se o incluisemos,cando chamasemos a linea.xml dende cabeceira teríamos un bucle

# para ocultar a posibilidade de crear as liñas dende a vista de mezcla_lineas, no xml poñemos options="{'no_create': True}"