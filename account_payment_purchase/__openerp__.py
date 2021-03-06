# -*- coding: utf-8 -*-
# Copyright 2016 Akretion (<http://www.akretion.com>).
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Payment Purchase',
    'version': '9.0.1.0.0',
    'category': 'Banking addons',
    'license': 'AGPL-3',
    'summary': "Adds Bank Account and Payment Mode on Purchase Orders",
    'author': "Akretion, "
              "Tecnativa, "
              "Odoo Community Association (OCA)",
    'website': 'http://www.akretion.com',
    'depends': [
        'purchase',
        'account_payment_partner'
    ],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
