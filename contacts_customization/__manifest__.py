# -*- coding: utf-8 -*-
{
    'name': 'Contacts Customization',
    'version': '1.6',
    'summary': '',
    'category': 'Contacts',
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
    'depends': ['base_setup',
                'mail',
                'resource',
                'web', 'contacts'],
    'data': [
        'views/dob_inheritance.xml',
        'data/cron_birthday_wish.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {

    },
}
