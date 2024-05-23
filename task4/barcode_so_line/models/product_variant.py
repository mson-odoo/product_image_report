# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class ProductVariant(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self,vals):
        res = super().create(vals);
        if not vals.get('barcode'):
            res['barcode'] = self.env['ir.sequence'].next_by_code('product.barcode.sequence')
        return res
