from odoo import models, fields, api
from odoo.exceptions import Warning

class accion_planificada(models.Model):
    #_name = 'account.invoice'
    _inherit ='account.invoice'

    @api.model
    def listado_facturas(self, id=None):
        informacion_ids = self.env['odoo_basico.informacion'].search([('autorizado','=',False)])
        # from odoo.exceptions import Warning
        # raise Warning ('Cantos %s ' % len(informacion_ids))
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion']._actualiza_alto(rexistro)
        date_act = fields.Datetime.now ()
        facturas_ids = self.search ([('state', '=', 'open')])
        if facturas_ids:
            #listado = [(x.number,x.partner_id.display_name, x.amount_total) for x in facturas_ids]
            listado = ""
            for rexistro in facturas_ids:
                listado = listado + "<br/>" + str(rexistro.number)+ "-> "+str(rexistro.partner_id.display_name)+ "-> "+str(rexistro.amount_total)
            # from odoo import SUPERUSER_ID
            # user_admin = self.env['res.users'].browse (SUPERUSER_ID)
            # mail_to = user_admin.partner_id.email
            my_user = self.env.user
            mail_from = my_user.partner_id.email
           # mail_to = 'antoniocfrv@gmail.com'
            mail_to = 'antoniocrespo@edu.xunta.es'
            mail_vals = {
                'subject': 'Listado de Facturas a dia de hoxe %s' % date_act,
                'author_id': my_user.id,
                'email_from': mail_from,
                'email_to': mail_to,
                'reply_to': mail_from,
                'message_type': 'email',
                'body_html': 'Neste momento %s existen as seguintes facturas %s' % (date_act, str (listado)),
            }
            mail_id = self.env['mail.mail'].create (mail_vals)
            mail_id.send ()

