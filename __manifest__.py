# -*- coding: utf-8 -*-
{
    'name': "funema",

    'summary': "Desarrollo personalizado para Funema",

    'description': """

    """,

    'author': "SISPAV",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/stock_quant_views.xml',
        'views/stock_warehouse_views.xml',        
    ],
}

