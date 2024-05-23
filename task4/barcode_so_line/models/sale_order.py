# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, Command


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'barcodes.barcode_events_mixin']

    def on_barcode_scanned(self, barcode):
        if barcode:
            product = self.env['product.product'].search([('barcode', '=', barcode)])
            if product:
                self.update({'order_line': [Command.create({'product_id': product.id})]})
