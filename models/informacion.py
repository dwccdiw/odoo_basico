# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning #Ao usar warning temos que importar a libreria
from odoo.exceptions import ValidationError #Ao usar constrains temos que importar a libreria ValidationError
import pytz
import locale
# from datetime import datetime
# from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

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
    hora_usuario = fields.Char (compute="_hora_usuario", string="Hora Usuario", size=15, store=True)
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")
    sexo = fields.Selection([('Home', 'Home'), ('Muller', 'Muller'), ('Outros', 'Outros')], string='Sexo')
    sexo_traducido = fields.Selection([('Hombre', 'Home'), ('Mujer', 'Muller'), ('Otros', 'Outros')], string='Sexo')

    def actualiza_hora(self,obxeto_rexistro):
        obxeto_rexistro.hora_usuario = self.convirte_data_hora_de_utc_a_timezone_do_usuario (obxeto_rexistro.data_hora).strftime ("%H:%M:%S")


    def actualiza_hora_boton(self):
        self.actualiza_hora (self)# leva self como parametro por que actualiza_hora ten 2 parametros
        # porque usamos tamén actualiza_hora dende outro modelo e lle pasamos como parametro o rexistro

    @api.depends ('data_hora')
    def _hora_usuario(self):
        self.actualiza_hora_boton ()

    def _actualiza_alto(self, rexistro):
        rexistro.alto_en_cms = 11
        rexistro.sexo_traducido = "Mujer"

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






    # data_hora_utc_string = hora_utc_object.strftime ('%Y-%m-%d %H:%M:%S')  # data hora en formato string
    # data_hora_utc_object = datetime.strptime (data_hora_utc_string, DEFAULT_SERVER_DATETIME_FORMAT)  # data hora en formato object
    # return pytz.UTC.localize (data_hora_utc_object).astimezone (usuario_timezone) # hora co horario do usuario en formato object



    def boton3(self):  # é necesario engadir no xml da vista no header o botón
        for rexistro in self:
            raise Warning ('Contexto: %s ' %  rexistro.env.context) # A env.context é un diccionario  https://www.w3schools.com/python/python_dictionaries.asp
        return True

    # Sempre se pasa como primeiro parametro self.
    # Por iso definimos dos parámetros e ao chamar a función pasamos un
    def convirte_data_hora_de_utc_a_timezone_do_usuario(self,data_hora_utc_object):# recibe a data hora en formato object
        usuario_timezone = pytz.timezone (self.env.user.tz or 'UTC')  # obter a zona horaria do usuario
        return pytz.UTC.localize (data_hora_utc_object).astimezone(usuario_timezone)  # hora co horario do usuario en formato object

    # operar con datas fields.Date.to_string (datetime.now () + timedelta (days))

    def boton4(self):  # é necesario engadir no xml da vista no header o botón
        data_hora_usuario_object = self.convirte_data_hora_de_utc_a_timezone_do_usuario(fields.Datetime.now())
        for rexistro in self:
            data_hora_do_campo_data_hora = self.convirte_data_hora_de_utc_a_timezone_do_usuario(rexistro.data_hora)
            raise Warning ('Datetime.now() devolve a hora UTC %s cambiamola coa configuración horaria do usuario %s cambiamos tamén a do campo data_hora %s'
                       % (fields.Datetime.now().strftime ('%Y-%m-%d %H:%M'),data_hora_usuario_object,data_hora_do_campo_data_hora))
        return True

    def boton5(self):
        # from odoo import SUPERUSER_ID
        # user_admin = self.env['res.user'].browse(SUPERUSER_ID)
        my_user = self.env.user
        mail_from = my_user.partner_id.email
        mail_to = 'antoniocfrv@gmail.com'
        mail_vals = {
                    'subject': 'Notificacion de ... ',
                    'author_id': my_user.id,
                    'email_from': mail_from,
                    'email_to': mail_to,
                    'message_type':'email',
                    'body_html': 'En la Fecha  se encontraron las'
        }
        mail_id = self.env['mail.mail'].create(mail_vals)
        mail_id.send()
        return True
#https://miblogtecnico.wordpress.com/2018/07/25/acciones-planificadas-en-odoo/


    @api.depends('data')# permite cambios nunha táboa relacionada e os cambios almacenanse na BD a diferencia de onchange.
    # Para os campos compute
    def _mes_date(self):
        for rexistro in self:
           if 'lang' in  rexistro.env.context:
               locale_usuario = rexistro.env.context['lang'] + '.utf8'
           else:
               locale_usuario = 'fr_FR.utf8'
           locale.setlocale(locale.LC_TIME, locale_usuario)
           rexistro.mes_date = rexistro.data.strftime ("%B")
           #rexistro.boton5()

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
