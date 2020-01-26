# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning #Ao usar warning temos que importar a libreria
from odoo.exceptions import ValidationError #Ao usar constrains temos que importar a libreria ValidationError
import pytz
from datetime import datetime
import locale
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class informacion (models.Model):
    _name = "odoo_basico.informacion" #IMPORTANTE é o nome da táboa
    _description = "Exemplos de atributos"
    _order = "data_hora desc"
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome')]

    name = fields.Char(required=True,size=20,string="Título")#IMPORTANTE o campo ten que chamarse name para visualizalo
    descripcion = fields.Text(string="A Descripción")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    alto_en_cms = fields.Integer(string="Alto en centímetros")
    longo_en_cms = fields.Integer (string="Longo en centímetros")
    ancho_en_cms = fields.Integer (string="Ancho en centímetros")
    volume = fields.Float (compute="_volume", store=True,default=0)
    volume_entre_100 = fields.Float(compute="_volume_entre_100", store=False)
    peso = fields.Float(digits=(6, 2), string="Peso en Kg.s", default=2.7)
    densidade = fields.Float (compute="_densidade", store=True)
    data = fields.Date (string="Data",default=lambda self: fields.Date.today ())  # w3schools lambda function
    data_hora = fields.Datetime(string="Data e Hora", default=lambda self: fields.Datetime.now()) #w3schools lambda function
    mes_date = fields.Char(compute="_mes_date",size=15,store=True)
    mes_datetime = fields.Char(compute="_mes_datetime",size=15,store=True)
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")
    sexo = fields.Selection([('Home', 'Home'), ('Muller', 'Muller'), ('Outros', 'Outros')], string='Sexo')
    sexo_traducido = fields.Selection([('Hombre', 'Home'), ('Mujer', 'Muller'), ('Otros', 'Outros')], string='Sexo')



       #@api.multi é a opción por defecto non temos que declarala
    def boton1(self):  # é necesario engadir no xml da vista no header o botón
        self.ensure_one ()
        for informacion in self:
            if informacion.alto_en_cms < 10 or informacion.alto_en_cms > 20:
                raise Warning ( #Ao usar warning temos que importar a libreria
                    'O alto de %s non está entre 10 e 20' % informacion.name)
            else:
                raise Warning (
                    'Altura de %s correcta' % informacion.name)
        return True


    def boton2(self):  # é necesario engadir no xml da vista no header o botón
        for rexistro in self:
            rexistro.autorizado = not rexistro.autorizado
        return True

    def boton3(self):  # é necesario engadir no xml da vista no header o botón
        user_tz = pytz.timezone (self.env.user.tz or 'UTC')
        agora = pytz.UTC.localize (datetime.strptime (
            fields.Datetime.now ().strftime ('%Y-%m-%d %H:%M:%S'), DEFAULT_SERVER_DATETIME_FORMAT)).astimezone (user_tz)
        for rexistro in self:
            campo_data_hora = pytz.UTC.localize (datetime.strptime (
                rexistro.data_hora.strftime ('%Y-%m-%d %H:%M:%S'), DEFAULT_SERVER_DATETIME_FORMAT)).astimezone (user_tz)
            raise Warning ('Datetime.now()= %s cambiada coa configuración horaria do usuario %s e a do campo data hora %s'
                       % (fields.Datetime.now ().strftime ('%Y-%m-%d %H:%M'),agora,campo_data_hora.strftime ('%Y-%m-%d %H:%M')))
        return True

    @api.depends('data')# permite cambios nunha táboa relacionada e os cambios almacenanse na BD a diferencia de onchange.
    # Para os campos compute
    def _mes_date(self):
        for rexistro in self:
           # locale.setlocale(locale.LC_TIME, self.env.context['lang'] + '.utf8')
           # locale.setlocale (locale.LC_TIME, 'es_ES.utf8')
           rexistro.mes_date = rexistro.data.strftime ("%B")

    @api.onchange('data_hora')#Se lanza o evento cando temos cambios a nivel de form, NON se gardan na BD.
    def _mes_datetime(self):
        for rexistro in self:
            rexistro.mes_datetime = rexistro.data_hora.strftime("%B")

    @api.depends ('alto_en_cms','longo_en_cms','ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)

    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume_entre_100(self):
        for rexistro in self:
            rexistro.volume_entre_100 = (float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms))/100

    @api.depends ('volume', 'peso')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = 100 * float (rexistro.peso) / float (rexistro.volume)
            else:
                rexistro.densidade = 0



    @api.constrains('peso') #Ao usar constrains temos que importar a libreria ValidationError
    def _constrain_peso(self):
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError (
                    'O peso de %s ten que ser entre 1 e 4 ' % rexistro.name)
