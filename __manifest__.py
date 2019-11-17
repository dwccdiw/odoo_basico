# -*- coding: utf-8 -*-
{
    'name': 'odoo_basico',
    'summary': 'Exemplos dos tipos de datos a utilizar',
    'description': """Exemplos dos tipos de datos a utilizar, 
                       as relacións, vistas, menus ... """,
    'author': 'IES Teis. Antonio Crespo',
    'website': 'http://www.iesteis.es',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Educación',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'views/factura.xml',
        'views/mezcla_lineas.xml',
        'views/cabeceira.xml',
        'views/linea.xml',
        'views/informacion.xml',
        'views/relacion.xml',
        'views/templates.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}