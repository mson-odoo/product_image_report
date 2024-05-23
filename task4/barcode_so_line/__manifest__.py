# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SO line using Barcode',
    'version': '1.0',
    'depends': ['barcodes', 'sale_management'],
    'data': [
        'data/product_barcode_sequence.xml',
        'report/sale_order_report_templates.xml',
        'report/invoice_report_template.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3'
}
