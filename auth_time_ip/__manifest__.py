# -*- coding: utf-8 -*-
{
    'name': "Time &IP Authentation",
    'summary': """
        User Time Authentation and IP Authentation""",
    'license': 'GPL-3',
    'description': """
        Users cannot access the system in a specified time range
    """,
    'author': "Yoromang Jatta <y.jatta41@gmail.com>",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/ss_1.jpeg',
    ],
    }
