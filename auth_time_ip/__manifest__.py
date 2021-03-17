# -*- coding: utf-8 -*-
{
    'name': "Time and IP Authentation",

    'summary': """
        User Time and IP Authentation""",
    'license': 'GPL-3',
    'description': """
        Users cannot access the system in a specified time range
    """,

    'author': "Yoromang Jatta <y.jatta41@gmail.com>",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/ss_1.jpeg',
    ],
    }
