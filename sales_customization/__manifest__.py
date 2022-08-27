# -*- coding: utf-8 -*-
{
    'name': 'Sales Customization',
    'version': '1.6',
    'summary': '',
    'category': 'Sales',
    'author': 'Wael',
    'sequence': '-100',
    'description': """
Custom Modules.
======================================

The event module allows you to efficiently organize events and all related tasks: planning, registration tracking,
attendances, etc.

Key Features
------------
* Manage your Events and Registrations
* Use emails to automatically confirm and send acknowledgments for any event registration
""",
    'depends': ['sale_management'],
    'data': [
        'views/sales_orders_inheritance.xml',
        'reports/sale_report_inherit.xml',




    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {

    },
}
